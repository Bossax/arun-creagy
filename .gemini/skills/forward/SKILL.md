---
installer: arra-oracle-skills-cli v26.5.16
origin: Nat Weerawan's brain, digitized — how one human works with AI, captured as code — Soul Brews Studio
name: forward
description: '[core] v26.5.16 G-SKLL | Create handoff + enter plan mode for next session. Use when user says "forward", "handoff", "wrap up", or before ending session.'
argument-hint: "[asap | --only]"
trigger: /forward
---

# /forward - Handoff to Next Session

Create context for next session, then enter plan mode to define next steps.

## Usage

```
/forward              # Create handoff, show plan, wait for approval
/forward asap         # Create handoff + commit immediately (no approval needed)
/forward --only       # Create handoff only, skip plan mode
```

## Steps

1. **Git status**: Check uncommitted work
2. **Detect session**: Current session ID for traceability
3. **Session summary**: What we did (from memory)
4. **Pending items**: What's left
5. **Next steps**: Specific actions

### Session Detection (Windows/PowerShell)

```powershell
$ENCODED_PWD = (Get-Location).Path.Replace(':', '').Replace('\', '-')
$PROJECT_DIR = "$env:USERPROFILE\.gemini\tmp\arun-creagy\chats"
$LATEST_JSONL = Get-ChildItem -Path "$PROJECT_DIR\*$ENCODED_PWD*\*.jsonl" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if ($LATEST_JSONL) {
  $SESSION_ID = $LATEST_JSONL.BaseName
  Write-Host "SESSION: $($SESSION_ID.Substring(0, 8))"
}
```

Include in handoff header if detected:
```markdown
📡 Session: 74c32f34 | repo-name | Xh XXm
```
Skip silently if detection fails.

## Output

Resolve vault path first:

**Windows/PowerShell**:
```powershell
$PSI = Resolve-Path 'ψ' -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Path
if (-not $PSI) { $PSI = Join-Path (Get-Location).Path 'ψ' }
```

Write to: `$PSI/inbox/handoff/YYYY-MM-DD_HH-MM_slug.md`

**IMPORTANT**: Always use the resolved absolute path (e.g., `C:/...`), never the `ψ/` symlink directly.
Do NOT `git add` vault files — they are shared state, not committed to repos.

```markdown
# Handoff: [Session Focus]

**Date**: YYYY-MM-DD HH:MM
**Context**: [%]

## What We Did
- [Accomplishment 1]
- [Accomplishment 2]

## Pending
- [ ] Item 1
- [ ] Item 2

## Hypotheses for Next Session (Audit Required)
- [ ] Hypothesis 1: [Specific action]
- [ ] Hypothesis 2: [Specific action]

## Key Files
- [Important file 1] (C:/path/to/file)
- [Important file 2] (C:/path/to/file)
```

### Confirm handoff write (Absolute Paths Required)

Always print the absolute Windows path so it is clickable in the terminal:
`echo "📤 Handoff: C:/Users/.../ψ/inbox/handoff/..."`

---

## Then: Create Issues from Pending Items

After writing the handoff file, extract actionable items and offer to create GitHub issues.      

### Step 3: Check for Duplicates (win32)

```powershell
# Check if issue exists
gh issue list --state open --search "ITEM_TITLE" --json title --jq '.[].title'
```

### Step 5: Create Issues (win32)

```powershell
$REMOTE = git remote get-url origin
$REPO = ($REMOTE -split '[:/]')[-2..-1] -join '/' -replace '\.git$', ''
gh issue create --repo "$REPO" --title "ITEM_TITLE" --body "From /forward handoff on $(Get-Date -Format 'yyyy-MM-dd')" 
```

---

## Then: MUST Show Plan Approval Box

1. **Call `EnterPlanMode`** tool
2. Write plan file with summary, pending, cleanup, and next steps.
3. **Always end plan with a choice table**:

```markdown
## Next Session: Pick Your Path

| Option | Command | What It Does |
|--------|---------|--------------|
| **Continue** | `/recap` | Pick up where we left off |
| **Clean up first** | See cleanup list below, then `/recap` | Merge PRs, delete branches, close issues, then continue |
| **Fresh start** | `/recap --quick` | Minimal context, start something new |
```

4. **Call `ExitPlanMode`** — user sees the built-in plan approval UI.

---

## Identity Context

If **GEMINI.md** contains demographics, include in handoff:

```markdown
## Context
**Oracle**: [name] ([pronouns]) | **Human**: [name] ([pronouns])
```

---

## ASAP Mode

If user says `/forward asap`:
- Write handoff file.
- **Immediately commit and push** (if requested/appropriate) — no approval needed.
- Skip plan mode.

**Philosophy**: Close the loop. Anchor the intent. *"The bridge is built before the light fades."*
