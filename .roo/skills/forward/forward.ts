#!/usr/bin/env bun
// @ts-nocheck

import { $ } from "bun";
import { existsSync, mkdirSync, realpathSync, readdirSync, readFileSync, statSync, writeFileSync, appendFileSync } from "fs";
import { basename, join, resolve } from "path";

type Paths = {
  root: string;
  psi: string;
  plansDir: string;
};

const safe = async (cmd: any) => {
  try {
    return (await cmd.text()).trim();
  } catch {
    return "";
  }
};

const nowStamp = () => {
  const d = new Date();
  const yyyy = d.getFullYear();
  const mm = String(d.getMonth() + 1).padStart(2, "0");
  const dd = String(d.getDate()).padStart(2, "0");
  const hh = String(d.getHours()).padStart(2, "0");
  const mi = String(d.getMinutes()).padStart(2, "0");
  return { date: `${yyyy}-${mm}-${dd}`, time: `${hh}-${mi}` };
};

const slugify = (s: string) =>
  (s || "session")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/(^-|-$)+/g, "")
    .slice(0, 80) || "session";

const parseArgs = (argv: string[]) => {
  const flags = new Set<string>();
  const rest: string[] = [];
  for (const a of argv) {
    if (a.startsWith("--")) flags.add(a);
    else rest.push(a);
  }
  const focus = rest.join(" ").trim();
  return {
    only: flags.has("--only"),
    planOnly: flags.has("--plan-only"),
    noOutbox: flags.has("--no-outbox"),
    issues: flags.has("--issues"),
    focus,
  };
};

const resolvePaths = async (): Promise<Paths> => {
  const root = (await safe($`git rev-parse --show-toplevel`)) || process.cwd();
  process.chdir(root);

  const psi = existsSync("ψ") ? realpathSync("ψ") : resolve(root, "ψ");
  const plansDir = join(root, "plans");
  return { root, psi, plansDir };
};

const detectSessionId = (root: string): string => {
  // Match our recap-rich approach: ~/.claude/projects/<encoded_pwd>/*.jsonl
  // Encode: replace path separators with '-', prefix '-' for drive root.
  // Example: C:\Users\me\Repo -> -C:-Users-me-Repo
  const cwdAbs = resolve(root);
  const encoded = "-" + cwdAbs.replace(/[:\\/]+/g, "-");
  const projectsDir = join("C:\\Users\\sitth\\.claude\\projects", encoded);
  try {
    const entries = readdirSync(projectsDir)
      .filter((n) => n.endsWith(".jsonl"))
      .map((n) => ({ n, m: statSync(join(projectsDir, n)).mtimeMs }))
      .sort((a, b) => b.m - a.m);
    const top = entries[0]?.n;
    if (!top) return "";
    return top.replace(/\.jsonl$/i, "");
  } catch {
    return "";
  }
};

const gitContext = async () => {
  await $`git config core.quotePath false`.quiet();
  const branch = await safe($`git branch --show-current`);
  const status = (await safe($`git status --porcelain`)) || "";
  const last3 = (await safe($`git log --oneline -3`)) || "";

  // Branches (for cleanup section)
  // Quote the format string so Bun's shell parser doesn't treat `(refname:short)` as syntax.
  const branchesRaw = (await safe($`git branch --format="%(refname:short)"`)) || "";
  const branches = branchesRaw
    .split(/\r?\n/)
    .map((s) => s.trim())
    .filter(Boolean);

  return { branch, status, last3, branches };
};

const extractCheckboxItems = (md: string): string[] => {
  const lines = md.split(/\r?\n/);
  const items: string[] = [];
  for (const l of lines) {
    const m = l.match(/^\s*-\s*\[ \]\s*(.+?)\s*$/);
    if (m) items.push(m[1]);
  }
  return items;
};

const ensureDir = (p: string) => {
  if (!existsSync(p)) mkdirSync(p, { recursive: true });
};

const writeHandoff = (psi: string, focus: string, sessionId: string, ctx: any) => {
  const { date, time } = nowStamp();
  const slug = slugify(focus);
  const dir = join(psi, "inbox", "handoff");
  ensureDir(dir);

  const file = join(dir, `${date}_${time}_${slug}.md`);
  const sessionLine = sessionId ? `📡 Session: ${sessionId.slice(0, 8)}` : "";

  const body = [
    `# Handoff: ${focus || "Next session"}`,
    "",
    `**Date**: ${date} ${time.replace("-", ":")}`,
    sessionLine ? `**Session**: ${sessionLine}` : "",
    "",
    "## What We Did",
    "- [fill: key accomplishments]",
    "",
    "## Pending",
    "- [ ] [fill: unfinished item]",
    "",
    "## Next Session",
    "- [ ] [fill: next concrete action]",
    "",
    "## Cleanup / Housekeeping",
    ctx?.status ? "```" + "\n" + ctx.status + "\n```" : "(none)",
    "",
    "## Key Files",
    "- [fill: important file paths]",
    "",
  ]
    .filter((l) => l !== "")
    .join("\n");

  writeFileSync(file, body, "utf8");
  return file;
};

const writePlan = (root: string, plansDir: string, focus: string, handoffPath: string, ctx: any) => {
  const { date } = nowStamp();
  const slug = slugify(focus);
  ensureDir(plansDir);

  const file = join(plansDir, `${date}_forward-${slug}-plan.md`);
  const relHandoff = handoffPath.replace(/\\/g, "/");

  const cleanupLines: string[] = [];
  if (ctx?.status) {
    cleanupLines.push("```", ctx.status, "```");
  }
  if (ctx?.branches?.length) {
    const nonMain = ctx.branches.filter((b: string) => b && b !== "main");
    if (nonMain.length) {
      cleanupLines.push("", "Stale/non-main branches (review):", ...nonMain.map((b: string) => `- ${b}`));
    }
  }

  const body = [
    `# Next-Session Plan — ${focus || "Forward"}`,
    "",
    `**Handoff Reference**: [\`${relHandoff}\`](${relHandoff})`,
    "",
    "## What We Accomplished This Session",
    "- [fill]",
    "",
    "## Pending Items Carried Forward",
    "- [ ] [fill]",
    "",
    "## Cleanup / Housekeeping",
    ...(cleanupLines.length ? cleanupLines : ["(none)"]),
    "",
    "## Next Session Goals and Scope",
    "1. [fill]",
    "",
    "## Next Session: Pick Your Path",
    "",
    "| Option | Command | What It Does |",
    "|--------|---------|--------------|",
    "| **Continue** | `/recap` | Pick up where we left off |",
    "| **Clean up first** | See cleanup list above, then `/recap` | Triage git state, then continue |",
    "| **Fresh start** | `/recap --quick` | Minimal context, start something new |",
    "",
    "### Cleanup Checklist",
    "- [ ] [fill]",
    "",
  ].join("\n");

  writeFileSync(file, body, "utf8");
  return file;
};

const writeOutboxPending = (psi: string, items: string[]) => {
  const { date } = nowStamp();
  const outboxDir = join(psi, "outbox");
  ensureDir(outboxDir);

  const file = join(outboxDir, `${date}_pending.md`);
  const header = `# Pending Items — ${date}\n\n## From: Arun_Creagy /forward\n\n`;

  if (!existsSync(file)) {
    writeFileSync(file, header, "utf8");
  } else {
    // Ensure the file ends with a newline before appending a new section.
    const existing = readFileSync(file, "utf8");
    if (!existing.endsWith("\n")) appendFileSync(file, "\n", "utf8");
    appendFileSync(file, `\n## From: Arun_Creagy /forward\n\n`, "utf8");
  }

  const lines = (items.length ? items : ["[fill: pending item]"]).map((t) => `- [ ] ${t}`);
  appendFileSync(file, lines.join("\n") + "\n", "utf8");
  return file;
};

const main = async () => {
  const args = parseArgs(process.argv.slice(2));
  const paths = await resolvePaths();
  const sessionId = detectSessionId(paths.root);
  const ctx = await gitContext();

  const focus = args.focus || "wrap up";

  let handoffPath = "";
  let planPath = "";
  let outboxPath = "";

  if (!args.planOnly) {
    handoffPath = writeHandoff(paths.psi, focus, sessionId, ctx);
  }

  if (!args.only && !args.planOnly) {
    planPath = writePlan(paths.root, paths.plansDir, focus, handoffPath, ctx);
  } else if (args.planOnly) {
    // Plan-only: create plan without handoff link.
    ensureDir(paths.plansDir);
    const fakeHandoff = "ψ/inbox/handoff/(skipped)";
    planPath = writePlan(paths.root, paths.plansDir, focus, fakeHandoff, ctx);
  }

  if (!args.noOutbox && !args.planOnly) {
    const handoffText = handoffPath ? readFileSync(handoffPath, "utf8") : "";
    const items = extractCheckboxItems(handoffText);
    outboxPath = writeOutboxPending(paths.psi, items);
  }

  console.log("# FORWARD");
  console.log("");
  if (handoffPath) console.log(`Handoff: ${handoffPath}`);
  if (planPath) console.log(`Plan:   ${planPath}`);
  if (outboxPath) console.log(`Outbox: ${outboxPath}`);
  console.log("");

  if (args.issues) {
    console.log("NOTE: --issues requested. This local implementation does not auto-create GitHub issues.");
    console.log("You must explicitly confirm issue creation before any `gh issue create` actions.");
  }
};

await main();

