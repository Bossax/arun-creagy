---
name: rrr
description: Create session retrospective with AI diary and lessons learned. Use when user says "rrr", "retrospective", "wrap up session", "session summary", or at end of work session.
---

# /rrr

> "Reflect to grow, document to remember."

## Oracle Root Detection (REQUIRED — bash)

**Every skill that writes to ψ/ MUST detect the oracle root first.**

```bash
ORACLE_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
if [ -z "$ORACLE_ROOT" ]; then
  ORACLE_ROOT="$(pwd)"
fi
PSI="$ORACLE_ROOT/ψ"
if [ ! -d "$PSI" ]; then
  echo "⚠️ No ψ/ found at $ORACLE_ROOT — writing there anyway."
  mkdir -p "$PSI"
fi
```

---

## /rrr (Default — background dig + parallel write)

### 1. Gather git context

```bash
date "+%H:%M %Z (%A %d %B %Y)"
git log --oneline -10
git diff --stat HEAD~5
```

Detect session ID:

```bash
ENCODED_PWD="$(pwd | sed 's/[:/\\]/-/g')"
PROJECT_BASE=$(ls -td "$HOME/.claude/projects"/*"$ENCODED_PWD"* 2>/dev/null | head -1)
LATEST_JSONL=$(ls -t "$PROJECT_BASE"/*.jsonl 2>/dev/null | head -1)
if [ -n "$LATEST_JSONL" ]; then
  SESSION_ID=$(basename "$LATEST_JSONL" .jsonl)
  echo "SESSION: ${SESSION_ID:0:8}"
fi
```

### 1.5. Extract timestamps

> [!important]
> **Token Optimization:** We use a static Python script for timestamp extraction to avoid context inheritance and parsing errors.

Run the predefined miner script to extract session timestamps:

```bash
python "$ORACLE_ROOT/.agents/skills/rrr/scripts/miner.py"
```

### 2. Write Retrospective (main agent)

**Path**: `$PSI/memory/retrospectives/YYYY-MM/DD/HH.MM_slug.md`

### 3. Write Lesson Learned (Knowledge Ingestion)

**Mechanism**: You MUST use the `oracle_learn` MCP tool to ingest the lesson (if available in this session — verify with a tool search before assuming it's connected; if it isn't, write the lesson file directly and note the sync as skipped).
- **Pattern**: The core technical or philosophical learning.
- **Concepts**: Relevant tags (e.g., [ontology, causality]).
- **Project**: The current project ghq path.

> [!important]
> Prefer `oracle_learn` over a plain file write when the MCP tool is connected, so the pattern is indexed in the Oracle brain and available for hybrid search. If the tool isn't connected this session, write `$PSI/memory/learnings/` directly — don't block the retro on it.

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
