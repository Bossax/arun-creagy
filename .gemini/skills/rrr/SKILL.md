---
installer: arra-oracle-skills-cli v26.5.16
origin: Nat Weerawan's brain, digitized — how one human works with AI, captured as code — Soul Brews Studio
name: rrr
description: '[project] v26.5.16 G-SKLL | Create session retrospective with AI diary and lessons learned. Use when user says "rrr", "retrospective", "wrap up session", "session summary", or at end of work session.'
argument-hint: "[--quick | --detail | --deep]"
trigger: /rrr
---

# /rrr

> "Reflect to grow, document to remember."

## Oracle Root Detection (REQUIRED — win32/PowerShell)

**Every skill that writes to ψ/ MUST detect the oracle root first.**

```powershell
# Step 1: Find git root
$ORACLE_ROOT = git rev-parse --show-toplevel 2>$null

# Step 2: Cross-check — oracle repo has GEMINI.md + ψ/
if ($ORACLE_ROOT -and (Test-Path "$ORACLE_ROOT\GEMINI.md") -and (Test-Path "$ORACLE_ROOT\ψ")) {
    $PSI = Resolve-Path "$ORACLE_ROOT\ψ" | Select-Object -ExpandProperty Path
} elseif ((Test-Path "GEMINI.md") -and (Test-Path "ψ")) {
    $PSI = Resolve-Path "ψ" | Select-Object -ExpandProperty Path
    $ORACLE_ROOT = (Get-Location).Path
} else {
    Write-Warning "Not in oracle repo (no GEMINI.md + ψ/). Writing to current directory."
    $PSI = (Get-Location).Path
}
```

---

## /rrr (Default — background dig + parallel write)

### 1. Gather git context (win32)

```powershell
Get-Date -Format "HH:mm K (dddd dd MMMM yyyy)"
git log --oneline -10
git diff --stat HEAD~5
```

Detect session ID (win32-native):

```powershell
$ENCODED_PWD = (Get-Location).Path.Replace(':', '').Replace('\', '-')
$PROJECT_BASE = Get-ChildItem -Path "$env:USERPROFILE\.claude\projects\*$ENCODED_PWD*" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
$LATEST_JSONL = Get-ChildItem -Path "$PROJECT_BASE\*.jsonl" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if ($LATEST_JSONL) { $SESSION_ID = $LATEST_JSONL.BaseName; Write-Host "SESSION: $($SESSION_ID.Substring(0, 8))" }
```

### 1.5. Spawn timestamp miner (background subagent — win32 adapted)

Spawn ONE background Agent to extract real timestamps:

```
Agent({
  name: "timestamp-miner",
  description: "Extract session timestamps for /rrr (win32)",
  run_in_background: true,
  prompt: `Extract ISO timestamps from a session .jsonl file on Windows.
Read-only.

Command:
powershell.exe -NoProfile -Command "$ENCODED_PWD = '[ORACLE_ROOT]'.Replace(':', '').Replace('\\', '-'); $PROJECT_BASE = Get-ChildItem -Path \"$env:USERPROFILE\\.claude\\projects\\*$ENCODED_PWD*\" | Sort-Object LastWriteTime -Descending | Select-Object -First 1; $LATEST_JSONL = Get-ChildItem -Path \"$PROJECT_BASE\\*.jsonl\" | Sort-Object LastWriteTime -Descending | Select-Object -First 1; if ($LATEST_JSONL) { python3 -c \"import json, os; from datetime import datetime, timezone, timedelta; tz = timezone(timedelta(hours=7)); f_path = r'$($LATEST_JSONL.FullName)'; with open(f_path, encoding='utf-8') as f: [print(f'{datetime.fromisoformat(m['timestamp'].replace(\"Z\", \"+00:00\")).astimezone(tz).strftime(\"%Y-%m-%d %H:%M\")} | {m['message']['content'][:80]}') for m in (json.loads(l) for l in f) if m.get('type') == 'user' and 'message' in m]\" }"`
})
```

### 2. Write Retrospective (main agent)

**Path**: `$PSI/memory/retrospectives/YYYY-MM/DD/HH.MM_slug.md`

### 3. Write Lesson Learned

**Path**: `$PSI/memory/learnings/YYYY-MM-DD_slug.md`

### 3.5. Append Session-Metrics Row (REQUIRED)

**Path**: `$PSI/memory/learnings/session-metrics.md`

---

## Hard Rules (v26.5.16 Mandate)

1. **Verify Before Reporting**: Retros are the final truth. Verify all "shipped" items against git/filesystem.
2. **Absolute Paths**: Render clickable Windows paths (e.g., `C:/...`) in the final announcement.
3. **No Rationalization**: Follow the Anti-Rationalization Guard rules.
4. **Agent Decision**: You MUST include exactly one `[→ AGENT DECISION]` naming a specific wrong choice you made.

---

## Demographics Context

Check **GEMINI.md** for demographics. Include in header:
```markdown
**Oracle**: [name] ([pronouns]) | **Human**: [name] ([pronouns])
```

**Philosophy**: Detect reality. Surface blockers. Offer direction. *"Reflect to grow, document to remember."*
