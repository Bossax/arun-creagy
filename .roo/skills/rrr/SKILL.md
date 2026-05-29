---
installer: local
name: rrr
description: '[local override] Windows/ψ adaptation of global /rrr docs (SKILL-only; preserves structure, rewrites command blocks).'
trigger: /rrr
argument-hint: "[--quick | --detail | --deep]"
---

# /rrr

> "Reflect to grow, document to remember."

```
/rrr                      # Retro + 1 background dig subagent (parallel, fast)
/rrr --quick              # No dig, no subagent — memory only (fastest)
/rrr --detail             # Full template + background dig
/rrr --deep               # 5 parallel subagents
/rrr --deep --teammate    # 3 coordinated team agents (requires AGENT_TEAMS)
```

**Default mode**: main agent starts writing the retro immediately from conversation memory.
One background subagent runs dig + .jsonl timestamp extraction in parallel.
When the subagent returns, main agent merges real timestamps into the Timeline section.
**No speed penalty** — dig runs while you write.

`--quick` skips dig entirely — memory only, zero subagents.

**Subagent rules**: default /rrr spawns exactly 1 background Agent (dig miner). `--deep` spawns 5. `--quick` spawns 0.
**NEVER use the Task tool.** Only `--deep` and `--deep --teammate` use TeamCreate.

---

## Oracle Root Detection (REQUIRED — run before any ψ/ write)

**Every skill that writes to ψ/ MUST detect the oracle root first.** Do not assume `pwd` is the oracle repo.

### PowerShell (Windows)

```powershell
# Step 1: Find git root
$ORACLE_ROOT = (git rev-parse --show-toplevel 2>$null)

# Step 2: Cross-check — oracle repo has CLAUDE.md + ψ/
if ($ORACLE_ROOT -and (Test-Path (Join-Path $ORACLE_ROOT 'CLAUDE.md')) -and (Test-Path (Join-Path $ORACLE_ROOT 'ψ'))) {
  $ROOT = $ORACLE_ROOT
} elseif ((Test-Path (Join-Path (Get-Location) 'CLAUDE.md')) -and (Test-Path (Join-Path (Get-Location) 'ψ'))) {
  $ROOT = (Get-Location).Path
} else {
  Write-Host "⚠️ Not in oracle repo (no CLAUDE.md + ψ at git root). Writing to current directory." -ForegroundColor Yellow
  $ROOT = (Get-Location).Path
}

# Step 3: Resolve ψ to a stable absolute path (handles the ψ character reliably)
$PSI = (Get-Item -LiteralPath (Join-Path $ROOT 'ψ')).FullName
```

**Why**: prevents retros writing to the wrong vault. All paths below use `$PSI/`.

---

## /rrr (Default — background dig + parallel write)

### 1. Gather git context (main agent)

```powershell
Get-Date -Format 'HH:mm zzz (dddd dd MMMM yyyy)'
git log --oneline -10
git diff --stat HEAD~5
```

Detect session ID (Windows-safe; no `sed/ls/head`):

```powershell
# Encode repo path for ~/.claude/projects/<encoded>
$ENCODED_PWD = '-' + ($ROOT -replace '[:\\/]+','-')
$PROJECT_DIR = Join-Path $HOME (Join-Path '.claude\projects' $ENCODED_PWD)

$LATEST_JSONL = Get-ChildItem -Path $PROJECT_DIR -Filter '*.jsonl' -ErrorAction SilentlyContinue |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 1

if ($LATEST_JSONL) {
  $SESSION_ID = [System.IO.Path]::GetFileNameWithoutExtension($LATEST_JSONL.Name)
  Write-Host ("SESSION: " + $SESSION_ID.Substring(0, [Math]::Min(8, $SESSION_ID.Length)))
}

If no `.jsonl` is found, continue without timestamps. (Some environments do not persist session logs.)
```

### 1.5. Spawn timestamp miner (background subagent)

Spawn ONE background Agent to extract real timestamps from the session .jsonl.

Important adaptation: **use PowerShell**, not `python3`, not Unix tools. Prompt should run a single PowerShell command that prints `YYYY-MM-DD HH:MM | <snippet>` for each user message.

```
Agent({
  name: "timestamp-miner",
  description: "Extract session timestamps for /rrr (PowerShell, Windows)",
  run_in_background: true,
  prompt: `Extract real user message timestamps from a Claude Code session file.
Read-only — do NOT write files.

Run this single command in PowerShell:

powershell.exe -NoProfile -Command "
$ROOT='[ORACLE_ROOT]'
$ENCODED_PWD='-' + ($ROOT -replace '[:\\/]+','-')
$PROJECT_DIR=Join-Path $HOME (Join-Path '.claude\\projects' $ENCODED_PWD)
$LATEST=Get-ChildItem -Path $PROJECT_DIR -Filter '*.jsonl' -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if(-not $LATEST){ exit 0 }
Write-Output ('SESSION_FILE: ' + $LATEST.FullName)
Get-Content $LATEST.FullName | ForEach-Object {
  try {
    $m = $_ | ConvertFrom-Json
    if($m.type -ne 'user'){ return }
    $ts = [string]$m.timestamp
    if(-not $ts){ return }
    $content = $m.message.content
    $text = ''
    if($content -is [string]){ $text = $content }
    elseif($content -is [System.Array]){
      $t = $content | Where-Object { $_.type -eq 'text' } | Select-Object -First 1
      if($t){ $text = [string]$t.text }
    }
    if(-not $text){ return }
    $snippet = ($text -replace '\\s+',' ') 
    if($snippet.Length -gt 80){ $snippet = $snippet.Substring(0,80) }
    # Keep ISO timestamp as-is; lead can format to GMT+7 table.
    Write-Output ($ts + ' | ' + $snippet)
  } catch {}
}
""

Return ALL output lines. The main agent will use them for the Timeline.`
})
```

### 2. Write Retrospective (main agent — start immediately, don't wait for dig)

**Path**: `$PSI/memory/retrospectives/YYYY-MM/DD/HH.MM_slug.md`

```powershell
$DATE_PATH = (Get-Date -Format 'yyyy-MM') + '\\' + (Get-Date -Format 'dd')
$RETRO_DIR = Join-Path $PSI (Join-Path 'memory\\retrospectives' $DATE_PATH)
New-Item -ItemType Directory -Force -Path $RETRO_DIR | Out-Null
```

**Start writing NOW from conversation memory.** Draft all sections. When the dig-miner subagent returns (background notification), merge its timestamp data into the Timeline section.

### Timeline format rules

1. **Use dig-miner timestamps when available** — real `HH:MM` from .jsonl extraction. If dig-miner hasn't returned yet or failed, write `[timestamps pending from dig-miner]` and fill in when it returns.
2. **Date once in header, time-only in rows** — same-day sessions.
3. **Never invent timestamps.** If dig-miner fails, say "timestamps unavailable" — don't guess.

Include in retrospective header:
```
dY"📡 Session: 74c32f34 | repo-name | Xh XXm
```

Write immediately, no prompts. Include:
- Session Summary
- Timeline
- Files Modified
- AI Diary (150+ words, first-person; must contain one line labeled `[🟧 AGENT DECISION]` naming a choice YOU made wrong)
- Honest Feedback (100+ words, 3 friction points)
- Lessons Learned (generalizable)
- Next Steps

### 3. Write Lesson Learned

**Path**: `$PSI/memory/learnings/YYYY-MM-DD_slug.md`

### 3.5. Append Session-Metrics Row (REQUIRED)

**Path**: `$PSI/memory/learnings/session-metrics.md`

If the file doesn't exist, create with the standard header, then append ONE row. (Keep the global format; do not skip.)

### 4. Oracle Sync

Write lesson learned markdown into `$PSI/memory/learnings/` (auto-memory picks it up).

### 4.5. Pattern Check (last 7 rows)

Read last 7 rows of `session-metrics.md`, count recurring themes in `friction` and `error`. If any theme appears ≥3 times, append a “Recurring Pattern Detected” section. Do not auto-open issues.

### 5. Save

**Do NOT `git add ψ/`** — vault files are shared state, not committed to repos.

### 6. Confirm (announce-mode — absolute paths required)

Use PowerShell to print absolute paths:

```powershell
$RETRO_FILE = '<fill absolute path>'
$LESSON_FILE = '<fill absolute path>'
$METRICS_FILE = Join-Path $PSI 'memory\\learnings\\session-metrics.md'
Write-Host ("dY" + '" Retrospective:  ' + $RETRO_FILE)
Write-Host ("dY" + "'" + ' Lesson learned: ' + $LESSON_FILE)
Write-Host ("dY" + '"S Metrics row:    ' + $METRICS_FILE)
```

---

## /rrr --detail

Same flow as default but use the full template (unchanged from global).

---

## /rrr --quick

Fast retro without dig — uses conversation memory only.

Use the same **PowerShell session detection** block above (no Unix tools).

---

## /rrr --deep

Read local [`DEEP.md`](DEEP.md:1).

---

## /rrr --deep --teammate

Read local [`TEAMMATE.md`](TEAMMATE.md:1).

