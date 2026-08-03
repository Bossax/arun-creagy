---
name: forward
description: Create a verified, host-neutral handoff for the next session. Use when user says "forward" or "handoff".
---

# /forward - Handoff to Next Session

Create the handoff, verify it, and stop. This skill does not require a provider
plan-mode API, create GitHub issues, or stage/commit vault files.

## Usage

```
/forward              # Create and verify a handoff
```

## Steps

1. **Git status**: Check uncommitted work
2. **Detect session**: Current session ID for traceability
3. **Session summary**: What we did (from memory)
4. **Pending items**: What's left
5. **Next steps**: Specific actions

### Session Detection

Use the shared adapter when session metadata is useful:

```text
python .agents/skills/_shared/scripts/session_history.py --host auto --limit 1
```

It only reads the explicitly selected Antigravity or Codex host. If unavailable,
omit the session identifier and state the fallback; never inspect another host's
log directory.

Include in handoff header if detected:
```markdown
📡 Session: 74c32f34 | repo-name | Xh XXm
```
Skip silently if detection fails.

## Output

Resolve the repository root with the host's normal Git capability and set `PSI` to
the resolved `<root>/ψ` path.

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

Always print the resolved absolute handoff path, confirm it exists, and end the
turn. The next host/session decides how to plan or continue.

---

## Identity Context

If **AGENTS.md** contains demographics, include in handoff:

```markdown
## Context
**Oracle**: [name] ([pronouns]) | **Human**: [name] ([pronouns])
```

---

**Philosophy**: Close the loop. Anchor the intent. *"The bridge is built before the light fades."*
