#!/usr/bin/env bun
// recap-rich.ts - Local win32-hardened full context recap
// Usage: bun recap-rich.ts

import { $ } from "bun";
import { existsSync, readdirSync, realpathSync, statSync } from "fs";
import { join, basename } from "path";

const safe = async (cmd: any) => {
  try {
    return (await cmd.text()).trim();
  } catch {
    return "";
  }
};

const ROOT = (await safe($`git rev-parse --show-toplevel`)) || process.cwd();
const isGit = (await safe($`git -C ${ROOT} rev-parse --is-inside-work-tree`)) === "true";
if (isGit) await $`git -C ${ROOT} config core.quotePath false`.quiet();

// Session detection (win32-native fallback)
let sessionLine = "";
try {
  const encodedPwd = ROOT.replace(':', '').replace(/[\\/.]/g, '-');
  const projectDir = join(process.env.USERPROFILE || "", ".claude", "projects");
  const glob = new Bun.Glob(`*${encodedPwd}*/*.jsonl`);
  const sessions = Array.from(glob.scanSync({ cwd: projectDir, absolute: true })) as string[];
  const latest = sessions.sort((a, b) => statSync(b).mtimeMs - statSync(a).mtimeMs)[0];

  if (latest) {
    const sessionId = basename(latest, ".jsonl");
    const firstLine = (await safe($`powershell.exe -NoProfile -Command "Get-Content -Path '${latest}' -TotalCount 1"`));
    let startStr = "";
    try {
      const ts = JSON.parse(firstLine).timestamp;
      if (ts) {
        const elapsed = Math.round((Date.now() - ts) / 60000);
        const h = Math.floor(elapsed / 60);
        const m = elapsed % 60;
        startStr = h > 0 ? `${h}h ${String(m).padStart(2, '0')}m` : `${m}m`;
      }
    } catch {}
    sessionLine = `${sessionId.slice(0, 8)} | ${basename(ROOT)}${startStr ? ` | ${startStr}` : ""}`;
  }
} catch {}

const now = new Date();
const date = now.toLocaleDateString("en-GB", { day: "2-digit", month: "short", year: "numeric" });
const time = now.toLocaleTimeString("en-GB", { hour: "2-digit", minute: "2-digit", hour12: false });
const month = now.toISOString().slice(0, 7);

console.log("# RECAP (Project Rich)");
if (sessionLine) console.log(`📡 Session: ${sessionLine}`);
console.log(`\n${time} | ${date}\n\n---\n`);

const psiPath = join(ROOT, "ψ");
const psi = existsSync(psiPath) ? realpathSync(psiPath) : psiPath;

// INCUBATED_BY detection
const incubatedByPath = join(ROOT, ".claude", "INCUBATED_BY");
if (existsSync(incubatedByPath)) {
  const breadcrumb = await Bun.file(incubatedByPath).text();
  console.log("## ⚠️ INCUBATED REPO");
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
  const rows = lines.filter((l) => l.startsWith("| ") && !l.includes("---") && !l.includes("Date")).slice(0, 5);
  console.log(rows.join("\n") || "No events");
} else {
  console.log("No schedule file");
}

// Git
console.log("\n## GIT");
if (isGit) {
  console.log(await safe($`git -C ${ROOT} status -sb`));
  console.log("**Last 3 commits:**");
  console.log(await safe($`git -C ${ROOT} log --oneline -3`));
}

// Tracks
console.log("## TRACKS");
const tracksDir = join(ROOT, "ψ/inbox/tracks");
if (existsSync(tracksDir)) {
  const tracks = readdirSync(tracksDir)
    .filter((f) => f.endsWith(".md") && !f.includes("INDEX") && !f.includes("CLAUDE") && !f.includes("GEMINI"))
    .sort((a, b) => statSync(join(tracksDir, b)).mtimeMs - statSync(join(tracksDir, a)).mtimeMs)
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
const retroDir = join(ROOT, "ψ/memory/retrospectives");
if (existsSync(retroDir)) {
  const glob = new Bun.Glob("**/*.md");
  const retros = Array.from(glob.scanSync({ cwd: retroDir, absolute: true })) as string[];
  const latest = retros
    .filter(f => !f.includes("CLAUDE") && !f.includes("GEMINI"))
    .sort((a, b) => statSync(b).mtimeMs - statSync(a).mtimeMs)[0];

  if (latest) {
    const content = await Bun.file(latest).text();
    console.log(`**From**: ${basename(latest)}\n`);
    const summary = content.match(/## Session Summary\n([\s\S]*?)(?=\n## |$)/)?.[1]?.trim();
    if (summary) console.log(`**Summary**:\n${summary.split("\n").slice(0, 8).join("\n")}`);
  }
}

// Handoff
const handoffDir = join(ROOT, "ψ/inbox/handoff");
if (existsSync(handoffDir)) {
  const glob = new Bun.Glob("*.md");
  const handoffs = Array.from(glob.scanSync({ cwd: handoffDir, absolute: true })) as string[];
  const latest = handoffs
    .filter(f => !f.includes("CLAUDE") && !f.includes("GEMINI"))
    .sort((a, b) => statSync(b).mtimeMs - statSync(a).mtimeMs)[0];

  if (latest) {
    const content = await Bun.file(latest).text();
    console.log(`\n**Handoff**: ${basename(latest)}`);
    console.log(content.split("\n").slice(2, 20).join("\n"));
  }
}

// Context
console.log("\n---\n\n## CONTEXT\n");
if (isGit) {
  const status = await safe($`git -C ${ROOT} status --porcelain`);
  const modified = status.split("\n").filter((l) => l.startsWith(" M")).map((l) => l.slice(3));
  const untracked = status.split("\n").filter((l) => l.startsWith("??")).map((l) => l.slice(3));
  if (modified.length) console.log("**Modified**:\n" + modified.map((f) => `  ${f}`).join("\n"));
  if (untracked.length) console.log("\n**Untracked**:\n" + untracked.map((f) => `  ${f}`).join("\n"));
}
