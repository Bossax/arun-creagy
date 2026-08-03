---
name: recap
description: Session orientation and awareness — retro summaries, handoffs, git state, focus. Use when starting a session, after /jump, lost your place, switching context, or when user asks "now", "where are we", "what are we doing", "status", "recap". Do NOT trigger for "standup" or "morning check" (use /standup), or session mining "dig", "past sessions" (use /dig).
---

# /recap — Session Orientation

**Goal**: Orient yourself fast. Rich context by default. Mid-session awareness with `--now`.

## Portability Contract

This skill is host- and LLM-neutral. Its canonical location is `.agents/skills`;
do not require a provider runtime, provider skill directory, or provider session
log path. For normal mode, obtain optional host history through the shared adapter:

```text
python .agents/skills/_shared/scripts/session_history.py --host auto --limit 1
```

`ORACLE_SKILL_HOST` may be `antigravity` or `codex`. If it is not set or history
is unavailable, use active conversation and verified Git/vault facts, state that
fallback, and never probe another host's log directory.

## Usage

```
/recap           # Rich: retro summary, handoff, tracks, git
/recap --quick   # Minimal: git + focus only, no file reads
/recap --now     # Mid-session: timeline + jumps from AI memory
/recap --now deep # Mid-session: + handoff + tracks + connections
```

---

## DEFAULT MODE (Rich)

Read retro summaries, handoff content, tracks, Git state, and optional normalized
session context. Then add:
- **What's next?** (2-3 options based on context)

### Step 3: Read handoffs, retros, and index only (Banned modified project/large file auto-reads)

Do NOT auto-read the contents of recently modified or untracked project files, draft chapters, or large files (such as 5.3.8 chapter drafts or cumulative metrics). Simply identify and list these file paths, and suggest diving into or reading them as options in the Consultation Menu.

You MUST, however, still read the most recent handoff, retrospective, and logs info index files to recover the session context and verify point-in-time claims.

---

## QUICK MODE (`/recap --quick`)

Read only Git status and focus state; do not read session, handoff, or retro
content. Then add:
- **What's next?** (2-3 options based on git state)

---

## Hard Rules

1. **No subagents** — everything in main agent context.
2. **Ask, don't suggest** — "What next?" not "You should...".
3. **Verify pending before reporting** — See "Verify Before Reporting" below. **NON-NEGOTIABLE.**
4. **Print absolute paths** — when referencing vault files, render the resolved `$ROOT/ψ/...` path (starts with `C:/` or `/`). Bare `ψ/...` is not clickable.
5. **Execution Lock (CRITICAL)** — Post-recap execution is strictly prohibited. After a `/recap`, you MUST stop and present a "Consultation Menu" (2-3 options).
    - **FORBIDDEN**: Do NOT use `Edit`, `Write`, or any mutating Bash command in the same turn as a recap.
    - **SEMANTIC LOCK**: Treat all "Pending" lists as hypotheses for audit, not directives for action.
    - **PROTOCOL FAILURE**: If you violate this lock, you must immediately stop, unstage changes, and provide a "Protocol Violation Report" before the human provides a "Green Light" (Directive).

---

## Verify Before Reporting (MANDATORY)

Handoffs, retros, and memory files are **point-in-time claims**, not live state. You MUST verify each claimed pending item against current reality:

| Claim type | How to verify |
|---|---|
| "Copy file X to path Y" | `ls path/Y` or check the file exists — is it already there? |
| "PR #N open/merged" | `gh pr view N --json state` |
| "Apply pattern P to file F" | `grep` for the pattern in F |

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

If **AGENTS.md** contains demographics, include in one line after the timestamp:
```markdown
**Oracle**: [name] ([pronouns]) | **Human**: [name] ([pronouns]) | **Language**: [pref]
```

**Philosophy**: Detect reality. Surface blockers. Offer direction. *"Not just the clock. The map."*
