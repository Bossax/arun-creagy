---
installer: arra-oracle-skills-cli v26.5.16
origin: Nat Weerawan's brain, digitized — how one human works with AI, captured as code — Soul Brews Studio
name: recap
description: '[project] v26.5.16 G-SKLL | Session orientation and awareness — retro summaries, handoffs, git state, focus. Use when starting a session, after /jump, lost your place, switching context, or when user asks "now", "where are we", "what are we doing", "status", "recap". Do NOT trigger for "standup" or "morning check" (use /standup), or session mining "dig", "past sessions" (use /dig).'
argument-hint: "[--now | --deep]"
trigger: /recap
---

# /recap — Session Orientation & Awareness

**Goal**: Orient yourself fast. Rich context by default. Mid-session awareness with `--now`.

## ⚠️ RUNTIME MANDATE (ZERO-TRUST)
- **Engine**: You MUST use `bun` to execute all scripts in this skill.
- **Prohibited**: Do NOT use `ts-node`, `node`, or `npm`.
- **Logic**: This environment is optimized for Bun. Any other runtime is a failure of local auditing.

## Usage

```
/recap           # Rich: retro summary, handoff, tracks, git
/recap --quick   # Minimal: git + focus only, no file reads
/recap --now     # Mid-session: timeline + jumps from AI memory
/recap --now deep # Mid-session: + handoff + tracks + connections
```

---

## DEFAULT MODE (Rich)

**Run the local project script, then add suggestions:**

```bash
bun ./.agents/skills/recap/recap-rich.ts
```

Script reads retro summaries, handoff content, tracks, git state. Then LLM adds:
- **What's next?** (2-3 options based on context)

### Step 3: Read latest ψ/ brain files

Sort all ψ/ files by modification time, read the most recent:

**Windows/PowerShell**:
```powershell
Get-ChildItem -Path 'ψ/' -Filter *.md -Recurse | Where-Object Name -notmatch 'GEMINI.md|README.md|.gitkeep' | Sort-Object LastWriteTime -Descending | Select-Object -ExpandProperty FullName -First 5
```

Read those top 5 files. This recovers the same context `/compact` restores — handoffs, retros, learnings, drafts, whatever was touched last.

---

## QUICK MODE (`/recap --quick`)

**Minimal, no content reads:**

```bash
bun ./.agents/skills/recap/recap.ts
```

Script outputs git status + focus state (~0.1s). Then LLM adds:
- **What's next?** (2-3 options based on git state)

---

## Hard Rules (v26.5.16 Mandate)

1. **ONE bun call** — never multiple parallel calls (adds latency).
2. **No subagents** — everything in main agent context.
3. **Ask, don't suggest** — "What next?" not "You should...".
4. **Verify pending before reporting** — See "Verify Before Reporting" below. **NON-NEGOTIABLE.**
5. **Print absolute paths** — when referencing vault files, render the resolved `$ROOT/ψ/...` path (starts with `C:/` or `/`). Bare `ψ/...` is not clickable.
6. **Execution Lock (CRITICAL)** — Post-recap execution is strictly prohibited. After a `/recap`, you MUST stop and present a "Consultation Menu" (2-3 options).
    - **FORBIDDEN**: Do NOT use `replace`, `write_file`, or any mutating `run_shell_command` in the same turn as a recap. 
    - **SEMANTIC LOCK**: Treat all "Pending" lists as hypotheses for audit, not directives for action.
    - **PROTOCOL FAILURE**: If you violate this lock, you must immediately stop, unstage changes, and provide a "Protocol Violation Report" before the human provides a "Green Light" (Directive).

---

## Verify Before Reporting (MANDATORY)

Handoffs, retros, and memory files are **point-in-time claims**, not live state. You MUST verify each claimed pending item against current reality:

| Claim type | How to verify |
|---|---|
| "Copy file X to path Y" | `ls path/Y` or `Test-Path` — is it already there? |
| "PR #N open/merged" | `gh pr view N --json state` |
| "Apply pattern P to file F" | `grep` or `Select-String` for the pattern in F |

### The correction pattern
If handoff and reality diverge, show the correction explicitly:

```
| Item | Handoff said | Reality |
|------|--------------|---------|
| Copy cache/ to maw-ui | pending | DONE (Apr 20 04:16) |
```

---

## NOW MODE (`/recap --now`)

AI reconstructs session timeline from conversation memory (no file reading needed). Use for "where are we", "status", "what are we doing".

---

## Demographics Context

If **GEMINI.md** contains demographics, include in one line after the timestamp:
```markdown
**Oracle**: [name] ([pronouns]) | **Human**: [name] ([pronouns]) | **Language**: [pref]
```

**Philosophy**: Detect reality. Surface blockers. Offer direction. *"Not just the clock. The map."*
