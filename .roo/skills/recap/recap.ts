#!/usr/bin/env bun
// @ts-nocheck
// Fast recap - no AI, just git status
// Usage: bun recap.ts

import { $ } from "bun";
import { existsSync, realpathSync, statSync } from "fs";
import { join } from "path";

const safe = async (cmd: any) => {
  try {
    return (await cmd.text()).trim();
  } catch {
    return "";
  }
};

// Get repo root
const root = (await safe($`git rev-parse --show-toplevel`)) || process.cwd();
process.chdir(root);

// Gather git data
const branch = (await safe($`git branch --show-current`));
let ahead = "0";
try {
  ahead = (await safe($`git rev-list --count @{u}..HEAD`)) || "0";
} catch {}
const lastCommit = (await safe($`git log --oneline -1`)).slice(8, 68);

// Resolve ψ symlink (used for focus + schedule)
const psi = existsSync("ψ") ? realpathSync("ψ") : "ψ";

// Focus state
let focusState = "none";
let focusTask = "No active focus";
const focusFile = join(psi, "inbox", "focus-agent-main.md");
if (existsSync(focusFile)) {
  const focusContent = await Bun.file(focusFile).text();
  const stateMatch = focusContent.match(/^STATE:\s*(.+)/m);
  const taskMatch = focusContent.match(/^TASK:\s*(.+)/m);
  if (stateMatch) focusState = stateMatch[1].trim();
  if (taskMatch) focusTask = taskMatch[1].trim().slice(0, 80);
}

// Schedule
let schedule = "No schedule";
const scheduleFile = join(psi, "inbox", "schedule.md");
if (existsSync(scheduleFile)) {
  const match = (await Bun.file(scheduleFile).text()).split("\n")
    .find(l => l.startsWith("| ") && !l.includes("---") && !l.includes("Date"));
  if (match) schedule = match.replace(/\|/g, "").trim().slice(0, 120);
}

// Latest retro and handoff
const monthDir = `ψ/memory/retrospectives/${new Date().toISOString().slice(0, 7)}`;
let latestRetro = "none";
let latestHandoff = "none";

const listLatest = async (pattern: string) => {
  // Windows-safe implementation (no bash/ls). Pattern is expected to be a glob.
  try {
    const files = Array.from(new Bun.Glob(pattern).scanSync({ dot: false })) as string[];
    const candidates = files
      .filter((f: string) => !f.includes("CLAUDE"))
      .sort((a: string, b: string) => {
        try {
          return statSync(b).mtimeMs - statSync(a).mtimeMs;
        } catch {
          return 0;
        }
      });
    const top = candidates[0];
    if (!top) return "none";
    return top.split(/[\\/]/).pop() || "none";
  } catch {
    return "none";
  }
};

latestRetro = await listLatest(`${monthDir}/*/*.md`);
latestHandoff = await listLatest("ψ/inbox/handoff/*.md");

// Git status
await $`git config core.quotePath false`.quiet();
const status = (await $`git status --porcelain`.text()).trim();
const lines = status ? status.split("\n") : [];

const modified = lines.filter(l => l.startsWith(" M"));
const untracked = lines.filter(l => l.startsWith("??"));

// Output
const now = new Date();
const time = now.toLocaleTimeString("en", { hour: "2-digit", minute: "2-digit", hour12: false });
const date = now.toLocaleDateString("en", { day: "2-digit", month: "short", year: "numeric" });

console.log("# RECAP");
console.log("");
console.log(`🕐 ${time} | ${date}`);
console.log("");
console.log("---");
console.log("");
console.log("## 🚧 FOCUS");
console.log(`\`${focusState}\` ${focusTask}`);
console.log("");
console.log("## 📅 TODAY");
console.log(schedule);
console.log("");
console.log(`## 📊 GIT: ${branch} (+${ahead} ahead)`);
console.log(`Last: ${lastCommit}`);
console.log("");

if (modified.length) {
  console.log(`**Modified** (${modified.length}):`);
  modified.forEach(l => console.log(`  ${l.slice(3)}`));
  console.log("");
}

if (untracked.length) {
  console.log(`**Untracked** (${untracked.length}):`);
  untracked.forEach(l => console.log(`  ${l.slice(3)}`));
  console.log("");
}

console.log("---");
console.log("");
console.log("## 📝 LAST SESSION");
console.log(`Retro: ${latestRetro}`);
console.log(`Handoff: ${latestHandoff}`);
