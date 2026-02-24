#!/usr/bin/env bun
/**
 * Run a single Git Bash command reliably from this repo, even when the
 * tool-runner shell isn't Git Bash.
 *
 * Usage:
 *   bun tools/gitbash.ts "echo hi; bash tools/pulse.sh"
 */

import { spawnSync } from "node:child_process";

const DEBUG = process.env.GITBASH_DEBUG === "1";

const cmd = process.argv.slice(2).join(" ").trim();
if (!cmd) {
  console.error('Usage: bun tools/gitbash.ts "<bash command>"');
  process.exit(2);
}

// Prefer the explicit Git for Windows bash.exe you confirmed.
const candidates = [
  "C:/Program Files/Git/usr/bin/bash.exe",
  "C:/Program Files/Git/bin/bash.exe",
  "C:/Program Files (x86)/Git/usr/bin/bash.exe",
  "C:/Program Files (x86)/Git/bin/bash.exe",
];

const bashExe = candidates.find((p) => {
  try {
    return Bun.file(p).size >= 0;
  } catch {
    return false;
  }
});

if (!bashExe) {
  console.error("ERROR: Git Bash executable not found. Tried:");
  for (const c of candidates) console.error("- " + c);
  process.exit(1);
}

if (DEBUG) {
  // Use forward slashes in logs so they are shell-agnostic and easier to read.
  const normalizedExe = bashExe.replace(/\\/g, "/");
  console.error(`[GITBASH_DEBUG] exe=${normalizedExe}`);
  console.error(`[GITBASH_DEBUG] cmd=${cmd}`);
}

const res = spawnSync(bashExe, ["-lc", cmd], {
  stdio: "inherit",
  windowsHide: true,
});

process.exit(res.status ?? 1);

