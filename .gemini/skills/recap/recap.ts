#!/usr/bin/env bun
// recap.ts - Local win32-hardened recap engine
// Usage: bun recap.ts

import { $ } from "bun";
import { existsSync, realpathSync, statSync } from "fs";
import { join, basename } from "path";

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
const branch = await safe($`git branch --show-current`);
let ahead = "0";
try {
  ahead = (await safe($`git rev-list --count @{u}..HEAD`)) || "0";
} catch {}
const lastCommit = (await safe($`git log --oneline -1`)).slice(8, 68);

// Resolve ψ symlink
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
  const content = await Bun.file(scheduleFile).text();
  const match = content.split("\n")
    .find(l => l.startsWith("| ") && !l.includes("---") && !l.includes("Date"));
  if (match) schedule = match.replace(/\|/g, "").trim().slice(0, 120);
}

// Native file sorter (win32-safe)
const getLatest = (pattern: string) => {
  try {
    const glob = new Bun.Glob(pattern);
    const files = Array.from(glob.scanSync({ dot: false })) as string[];
    const top = files
      .filter(f => !f.includes("GEMINI"))
      .sort((a, b) => statSync(b).mtimeMs - statSync(a).mtimeMs)[0];
    return top ? basename(top) : "none";
  } catch {
    return "none";
  }
};

const monthDir = `ψ/memory/retrospectives/${new Date().toISOString().slice(0, 7)}`;
const latestRetro = getLatest(`${monthDir}/*/*.md`);
const latestHandoff = getLatest("ψ/inbox/handoff/*.md");

// Git status
await $`git config core.quotePath false`.quiet();
const status = (await safe($`git status --porcelain`));
const lines = status ? status.split("\n") : [];
const modified = lines.filter(l => l.startsWith(" M"));
const untracked = lines.filter(l => l.startsWith("??"));

// Session detection (win32-native fallback)
let sessionLine = "";
try {
  const encodedPwd = root.replace(':', '').replace(/[\\/.]/g, '-');
  const projectDir = join(process.env.USERPROFILE || "", ".gemini", "tmp", "arun-creagy", "chats");
  const glob = new Bun.Glob(`session-*.jsonl`);
  const sessions = Array.from(glob.scanSync({ cwd: projectDir, absolute: true })) as string[];
  const latest = sessions.sort((a, b) => statSync(b).mtimeMs - statSync(a).mtimeMs)[0];

  if (latest) {
    const sessionId = basename(latest).replace('session-', '').replace('.jsonl', '');
    const firstLine = (await safe($`powershell.exe -NoProfile -Command "Get-Content -Path '${latest}' -TotalCount 1"`));
    let startStr = "";
    try {
      const ts = JSON.parse(firstLine).timestamp;
      if (ts) {
        const elapsed = Math.round((Date.now() - new Date(ts).getTime()) / 60000);
        const h = Math.floor(elapsed / 60);
        const m = elapsed % 60;
        startStr = h > 0 ? `${h}h ${String(m).padStart(2, '0')}m` : `${m}m`;
      }
    } catch {}
    sessionLine = `${sessionId.slice(0, 8)} | ${basename(root)}${startStr ? ` | ${startStr}` : ""}`;
  }
} catch {}

const now = new Date();
const time = now.toLocaleTimeString("en-GB", { hour: "2-digit", minute: "2-digit", hour12: false });
const date = now.toLocaleDateString("en-GB", { day: "2-digit", month: "short", year: "numeric" });

console.log("# RECAP (Project)");
console.log("");
if (sessionLine) console.log(`📡 Session: ${sessionLine}`);
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
