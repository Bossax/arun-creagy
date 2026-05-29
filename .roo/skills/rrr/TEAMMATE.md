# RRR --deep --teammate Mode (3 Coordinated Team Agents) — Windows/ψ adaptation

This document preserves the original global structure, but rewrites command blocks for Windows PowerShell and uses `ψ/`.

**Team-based deep retro with coordinated agents.** Teammates reconstruct from artifacts (git log, file mtimes, ψ files) — they don't rely on conversation memory.

**Requires**: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in settings.json env.
**Fallback**: If agent teams unavailable, fall back to `--deep` with a warning.

## Step 0: Oracle Root + Gather context

```powershell
Get-Date -Format 'HH:mm zzz (dddd dd MMMM yyyy)'

$ORACLE_ROOT = (git rev-parse --show-toplevel 2>$null)
if ($ORACLE_ROOT -and (Test-Path (Join-Path $ORACLE_ROOT 'CLAUDE.md')) -and (Test-Path (Join-Path $ORACLE_ROOT 'ψ'))) {
  $ROOT = $ORACLE_ROOT
} else {
  $ROOT = (Get-Location).Path
}

$PSI = (Get-Item -LiteralPath (Join-Path $ROOT 'ψ')).FullName

git log --oneline -15
git diff --stat HEAD~5
git log --format="%h %ai %s" -10
```

## Step 1: Create team + tasks

```
TeamCreate("rrr-deep")

TaskCreate("Git + files + timeline analysis")
TaskCreate("Pattern and learning extraction")
TaskCreate("Oracle memory search — connections to past")
```

## Step 2: Spawn 3 teammates (all in one message, parallel)

**Agent: analyst** (model: sonnet)
```
You are the Analyst on team rrr-deep. Do Task #1.
REPO: [ROOT]
Run: git log --format='%h %ai %s' -15
     git diff --stat HEAD~5
     git show --stat HEAD HEAD~1 HEAD~2
     (Windows) Use PowerShell Get-ChildItem for directory inspection instead of ls.

Build a timeline table: Time | Phase | Activity | Evidence
When done: TaskUpdate(taskId='1', status='completed')
SendMessage(to='team-lead@rrr-deep', summary='Analysis complete', message='your findings')
Under 600 words.
```

**Agent: patterns** (model: sonnet)
```
You are the Pattern Extractor on team rrr-deep. Do Task #2.
REPO: [ROOT]
Read today's files in ψ/memory/learnings/ and ψ/memory/retrospectives/.
Extract: reusable patterns, mistakes, anti-patterns, transferable techniques.
When done: TaskUpdate(taskId='2', status='completed')
SendMessage(to='team-lead@rrr-deep', summary='Patterns extracted', message='your findings')
Under 500 words.
```

**Agent: oracle** (model: sonnet)
```
You are the Oracle Memory Searcher on team rrr-deep. Do Task #3.
REPO: [ROOT]
Search ψ/memory/ — learnings, retros, traces.
Find: recurring patterns, connections to past, growth trajectory.
When done: TaskUpdate(taskId='3', status='completed')
SendMessage(to='team-lead@rrr-deep', summary='Oracle connections found', message='your findings')
Under 500 words.
```

## Step 3: Wait for 3 reports

Messages arrive automatically via SendMessage.

## Step 4: Lead compiles final retro

Write to: `ψ/memory/retrospectives/DATE_PATH/TIME_rrr-deep-teammate.md`

**MANDATORY sections** (all required):

| Section | Source |
|---|---|
| Session Summary | Synthesized from all 3 agents |
| Timeline | From analyst (markdown table with exact timestamps) |
| Files Modified | From analyst (categorized by type) |
| AI Diary (150+ words) | Lead synthesizes all findings + lived experience |
| Honest Feedback (100+ words) | Lead + patterns agent friction points |
| Lessons Learned | From patterns + oracle |
| Next Steps | From oracle's unresolved threads |
| Team Meta-Analysis | What worked about the team approach |

## Step 5: Shutdown + cleanup

Same as global: send shutdown requests, delete team.

## Step 6: Save

**Do NOT `git add ψ/`** — vault files are shared state, not committed to repos.

