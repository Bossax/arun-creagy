#!/usr/bin/env bun
// @ts-nocheck
// recap-rich.ts - Windows-safe full context recap (project-local)

import { $ } from "bun";
import { existsSync, readdirSync, realpathSync, statSync } from "fs";
import { join } from "path";

const safeText = async (cmd: any) => {
  try {
    return (await cmd.text()).trim();
  } catch {
    return "";
  }
};

const ROOT = process.env.ROOT || (await safeText($`git rev-parse --show-toplevel`)) || process.cwd();
const isGit = (await safeText($`git -C ${ROOT} rev-parse --is-inside-work-tree`)) === "true";
if (isGit) await $`git -C ${ROOT} config core.quotePath false`.quiet().catch(() => {});

const now = new Date();
const date = now.toLocaleDateString("en-GB", { day: "2-digit", month: "short", year: "numeric" });
const time = now.toTimeString().slice(0, 5);
const month = now.toISOString().slice(0, 7);

// Session detection (Windows-safe)
let sessionLine = "";
try {
  // Match global script logic but avoid unix utilities (ls/head)
  const encodedPwd = ROOT.replace(/^\//, "-").replace(/[\\/.]/g, "-");
  const home = process.env.USERPROFILE || process.env.HOME || "";
  const projectDir = home ? join(home, ".claude", "projects", encodedPwd) : "";
  if (projectDir && existsSync(projectDir)) {
    const jsonls = readdirSync(projectDir)
      .filter((f) => f.endsWith(".jsonl"))
      .map((f) => join(projectDir, f))
      .sort((a, b) => statSync(b).mtimeMs - statSync(a).mtimeMs);

    if (jsonls.length) {
      const sessionId = jsonls[0].split(/[\\/]/).pop()!.replace(/\.jsonl$/, "");
      const shortId = sessionId.slice(0, 8);
      let startStr = "";
      try {
        // Read only first line
        const f = Bun.file(jsonls[0]);
        const stream = f.stream();
        const reader = stream.getReader();
        const { value } = await reader.read();
        await reader.cancel();
        const chunk = new TextDecoder().decode(value || new Uint8Array());
        const firstLine = (chunk.split("\n")[0] || "").trim();
        const ts = JSON.parse(firstLine).timestamp;
        if (ts) {
          const start = new Date(ts);
          const elapsed = Math.round((Date.now() - start.getTime()) / 60000);
          const h = Math.floor(elapsed / 60);
          const m = elapsed % 60;
          startStr = h > 0 ? `${h}h ${String(m).padStart(2, "0")}m` : `${m}m`;
        }
      } catch {}
      const repoName = ROOT.split(/[\\/]/).pop() || "";
      sessionLine = `${shortId} | ${repoName}${startStr ? ` | ${startStr}` : ""}`;
    }
  }
} catch {}

console.log("# RECAP (Rich)");
if (sessionLine) console.log(`dY"� Session: ${sessionLine}`);
console.log(`\n${time} | ${date}\n\n---\n`);

// Resolve ψ / I^ symlink
// Global skill uses I^, but this repo uses ψ. Prefer I^ if present, else ψ.
const iCaretPath = join(ROOT, "I^");
const psiPath = join(ROOT, "ψ");
const psi = existsSync(iCaretPath)
  ? realpathSync(iCaretPath)
  : (existsSync(psiPath) ? realpathSync(psiPath) : psiPath);

// INCUBATED_BY detection
const incubatedByPath = join(ROOT, ".claude", "INCUBATED_BY");
if (existsSync(incubatedByPath)) {
  const breadcrumb = await Bun.file(incubatedByPath).text();
  console.log("## �s��,? INCUBATED REPO");
  console.log(breadcrumb.trim());
  console.log("");
}

// Focus
console.log("## FOCUS");
const focusFile = join(psi, "inbox", "focus-agent-main.md");
if (existsSync(focusFile)) {
  const content = await Bun.file(focusFile).text();
  const state = content.match(/^STATE:(.*)$/m)?.[1]?.trim() || "none";
  const task = content.match(/^TASK:(.*)$/m)?.[1]?.trim() || "No active focus";
  console.log(`\`${state}\` ${task}`);
} else {
  console.log("No focus file");
}

// Schedule
console.log("\n## UPCOMING");
const scheduleFile = join(psi, "inbox", "schedule.md");
if (existsSync(scheduleFile)) {
  const lines = (await Bun.file(scheduleFile).text()).split("\n");
  const rows = lines
    .filter((l) => l.startsWith("| ") && !l.includes("---") && !l.includes("Date"))
    .slice(0, 5);
  console.log(rows.join("\n") || "No events");
} else {
  console.log("No schedule file");
}

// Git
console.log("\n## GIT");
if (isGit) {
  console.log(await safeText($`git -C ${ROOT} status -sb`));
  console.log("**Last 3 commits:**");
  console.log(await safeText($`git -C ${ROOT} log --oneline -3`));
} else {
  console.log("Not a git repository");
}

// Tracks
console.log("## TRACKS");
const tracksDir = join(psi, "inbox", "tracks");
if (existsSync(tracksDir)) {
  const tracks = readdirSync(tracksDir)
    .filter((f) => f.endsWith(".md") && !f.includes("INDEX") && !f.includes("CLAUDE"))
    .slice(0, 6);
  for (const t of tracks) {
    const content = await Bun.file(join(tracksDir, t)).text();
    const id = t.match(/^(\d+)/)?.[1] || "-";
    const name = content.split("\n")[0]?.replace(/^# Track[^:]*: /, "") || t;
    console.log(`- ${id}: ${name}`);
  }
}

// Latest retro
console.log("\n---\n\n## LAST SESSION");
const retroDir = join(psi, "memory", "retrospectives", month);
if (existsSync(retroDir)) {
  const days = readdirSync(retroDir)
    .filter((d) => !d.startsWith("."))
    .sort()
    .reverse();
  for (const day of days) {
    const dayDir = join(retroDir, day);
    if (!existsSync(dayDir)) continue;
    const files = readdirSync(dayDir).filter((f) => f.endsWith(".md") && !f.includes("CLAUDE"));
    if (files.length) {
      const retro = await Bun.file(join(dayDir, files[0])).text();
      console.log(`**From**: ${files[0]}\n`);
      const summary = retro.match(/## Session Summary\n([\s\S]*?)(?=\n## |$)/)?.[1]?.trim();
      if (summary) console.log(`**Summary**:\n${summary.split("\n").slice(0, 8).join("\n")}`);
      break;
    }
  }
}

// Handoff
const handoffDir = join(psi, "inbox", "handoff");
if (existsSync(handoffDir)) {
  const handoffs = readdirSync(handoffDir)
    .filter((f) => f.endsWith(".md") && !f.includes("CLAUDE"))
    .sort()
    .reverse();
  if (handoffs.length) {
    const content = await Bun.file(join(handoffDir, handoffs[0])).text();
    console.log(`\n**Handoff**: ${handoffs[0]}`);
    console.log(content.split("\n").slice(2, 20).join("\n"));
  }
}

// Context
console.log("\n---\n\n## CONTEXT\n");
if (isGit) {
  const status = await safeText($`git -C ${ROOT} status --porcelain`);
  const modified = status
    .split("\n")
    .filter((l) => l.startsWith(" M"))
    .map((l) => l.slice(3));
  const untracked = status
    .split("\n")
    .filter((l) => l.startsWith("??"))
    .map((l) => l.slice(3));

  if (modified.length) console.log("**Modified**:\n" + modified.map((f) => `  ${f}`).join("\n"));
  if (untracked.length) console.log("\n**Untracked**:\n" + untracked.map((f) => `  ${f}`).join("\n"));
} else {
  console.log("Not a git repository — skipping file status");
}

