---
name: rrr
description: Create session retrospective with AI diary and lessons learned. Use when user says "rrr", "retrospective", "wrap up session", "session summary", or at end of work session.
---

# /rrr

> "Reflect to grow, document to remember."

## Oracle Root Detection

**Every skill that writes to ψ/ MUST detect the oracle root first.**

Resolve the repository root with the host's normal Git capability, falling back to
the working directory, then set `PSI` to `<root>/ψ`. Do not assume a shell or a
provider-owned workspace layout.

---

## /rrr (Default — background dig + parallel write)

### 1. Gather git context

```bash
date "+%H:%M %Z (%A %d %B %Y)"
git log --oneline -10
git diff --stat HEAD~5
```

Obtain optional session identity and timestamps from the shared adapter:

```text
python .agents/skills/_shared/scripts/session_history.py --host auto --limit 10
```

The adapter returns normalized JSON for Antigravity or Codex only when the host is
explicitly selected (`ORACLE_SKILL_HOST`). If unavailable, use active conversation
and Git timestamps, state that fallback, and do not inspect another host's logs.

### 2. Write Retrospective (main agent)

**Path**: `$PSI/memory/retrospectives/YYYY-MM/DD/HH.MM_slug.md`

### 3. Write Lesson Learned (Knowledge Ingestion)

**Mechanism**: `oracle_learn` is required. Discover it before writing artifacts; if
it is unavailable, stop and report the missing Oracle capability.
- **Pattern**: The core technical or philosophical learning.
- **Concepts**: Relevant tags (e.g., [ontology, causality]).
- **Project**: The current project ghq path.

> [!important]
> Oracle ingestion keeps the learning indexed in the Oracle brain and available for
> hybrid search. Do not create an unsynchronized local fallback.

---

## Hard Rules

1. **Verify Before Reporting**: Retros are the final truth. Verify all "shipped" items against git/filesystem.
2. **Absolute Paths**: Render clickable Windows paths (e.g., `C:/...`) in the final announcement.
3. **No Rationalization**: Follow the Anti-Rationalization Guard rules (see `DEEP.md` for the multi-agent version; apply the same spirit solo).
4. **Agent Decision**: You MUST include exactly one `[→ AGENT DECISION]` naming a specific wrong choice you made.

---

## Demographics Context

Check **AGENTS.md** for demographics. Include in header:
```markdown
**Oracle**: [name] ([pronouns]) | **Human**: [name] ([pronouns])
```

**Philosophy**: Detect reality. Surface blockers. Offer direction. *"Reflect to grow, document to remember."*
