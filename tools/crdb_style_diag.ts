// Bun-first script (avoid Node-only typings in this repo).
// Usage:
//   bun tools/crdb_style_diag.ts
//   bun tools/crdb_style_diag.ts path/to/file.md ...

type FileStats = {
  file: string;
  totalLines: number;
  nonEmptyLines: number;
  headingLines: number;
  headingL3Plus: number;
  bulletLines: number;
  tableLines: number;
  paragraphLikeLines: number;
  internalRepoLinkLines: number;
  hasExecSummarySection: boolean;
  hasEvidenceSection: boolean;
  hasAppendixSection: boolean;
  hasMissingDataSection: boolean;
  bulletRatio: number;
};

async function analyzeMarkdown(file: string): Promise<FileStats> {
  const raw = await Bun.file(file).text();
  const lines = raw.split(/\r?\n/);

  let nonEmptyLines = 0;
  let headingLines = 0;
  let headingL3Plus = 0;
  let bulletLines = 0;
  let tableLines = 0;
  let paragraphLikeLines = 0;
  let internalRepoLinkLines = 0;

  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed.length > 0) nonEmptyLines++;

    const isHeading = /^#{1,6}\s+/.test(trimmed);
    if (isHeading) {
      headingLines++;
      if (/^#{3,6}\s+/.test(trimmed)) headingL3Plus++;
      continue;
    }

    const isTable = /^\|/.test(trimmed);
    if (isTable) {
      tableLines++;
      continue;
    }

    const isBullet = /^(-|\*|\d+\.)\s+/.test(trimmed);
    if (isBullet) {
      bulletLines++;
      continue;
    }

    if (trimmed.length > 0) {
      paragraphLikeLines++;
    }

    if (/\]\(\s*ψ\//.test(line) || /\]\(\s*\.\.\//.test(line) || /ψ\//.test(line)) {
      internalRepoLinkLines++;
    }
  }

  const hasExecSummarySection = /###\s*สรุปสำหรับผู้บริหาร/.test(raw);
  const hasEvidenceSection = /###\s*ผลการดำเนินงานและหลักฐานอ้างอิง/.test(raw);
  const hasAppendixSection = /###\s*ประเด็นสำหรับภาคผนวก/.test(raw);
  const hasMissingDataSection = /###\s*ข้อมูลที่ต้องยืนยัน\/ยังขาด/.test(raw);

  const denom = bulletLines + paragraphLikeLines;
  const bulletRatio = denom === 0 ? 0 : bulletLines / denom;

  return {
    file,
    totalLines: lines.length,
    nonEmptyLines,
    headingLines,
    headingL3Plus,
    bulletLines,
    tableLines,
    paragraphLikeLines,
    internalRepoLinkLines,
    hasExecSummarySection,
    hasEvidenceSection,
    hasAppendixSection,
    hasMissingDataSection,
    bulletRatio,
  };
}

function fmtRatio(r: number): string {
  return `${Math.round(r * 100)}%`;
}

function pad(s: string, n: number): string {
  if (s.length >= n) return s;
  return s + " ".repeat(n - s.length);
}

async function main() {
  const defaultFiles = [
    "ψ/incubate/DCCE/CRDB/output/5.2.1-Interim-Report-v3-draft.md",
    "ψ/incubate/DCCE/CRDB/output/5.2.2-Interim-Report-v3-draft.md",
    "ψ/incubate/DCCE/CRDB/output/5.2.3-Interim-Report-v3-draft.md",
    "ψ/incubate/DCCE/CRDB/output/5.2.4-Interim-Report-v3-draft.md",
    "ψ/incubate/DCCE/CRDB/output/5.2.5-Interim-Report-v3-draft.md",
    "ψ/incubate/DCCE/CRDB/output/5.3.1-Interim-Report-v3-draft.md",
    "ψ/incubate/DCCE/CRDB/output/5.3.2-Interim-Report-v3-draft.md",
    "ψ/incubate/DCCE/CRDB/output/5.5.1-Interim-Report-v3-draft.md",
    "ψ/incubate/DCCE/CRDB/output/5.5.2-Interim-Report-v3-draft.md",
    "ψ/incubate/DCCE/CRDB/inbox_source/2026-03-23_interim-report-1st-submission.md",
  ];

  const args = Bun.argv.slice(2).filter((a) => a.trim().length > 0);
  const files = args.length > 0 ? args : defaultFiles;

  const missing: string[] = [];
  for (const f of files) {
    if (!(await Bun.file(f).exists())) missing.push(f);
  }
  if (missing.length) {
    console.error("Missing files:");
    for (const f of missing) console.error(`- ${f}`);
    Bun.exit(2);
  }

  const rows = await Promise.all(files.map(analyzeMarkdown));

  const header =
    pad("file", 64) +
    " | " +
    pad("bullets", 7) +
    " | " +
    pad("para", 5) +
    " | " +
    pad("H", 3) +
    " | " +
    pad("H3+", 4) +
    " | " +
    pad("repoLinks", 8) +
    " | " +
    pad("bullet%", 7) +
    " | flags";

  console.log(header);
  console.log("-".repeat(header.length));

  for (const r of rows) {
    const flags: string[] = [];
    if (r.hasExecSummarySection) flags.push("execSummary");
    if (r.hasEvidenceSection) flags.push("evidence");
    if (r.hasAppendixSection) flags.push("appendixSec");
    if (r.hasMissingDataSection) flags.push("missingDataSec");

    console.log(
      pad(r.file, 64) +
        " | " +
        pad(String(r.bulletLines), 7) +
        " | " +
        pad(String(r.paragraphLikeLines), 5) +
        " | " +
        pad(String(r.headingLines), 3) +
        " | " +
        pad(String(r.headingL3Plus), 4) +
        " | " +
        pad(String(r.internalRepoLinkLines), 8) +
        " | " +
        pad(fmtRatio(r.bulletRatio), 7) +
        " | " +
        flags.join(",")
    );
  }
}

await main();

