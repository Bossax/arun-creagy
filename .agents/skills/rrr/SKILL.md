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

## Workflow: 2-Step Sequential Execution

The execution MUST be split into two discrete, sequential steps — NEVER skip the MCP call after writing the file:

### Step 1: Write Retrospective Artifact (Disk State)
1. **Gather git context**:
   ```bash
   date "+%H:%M %Z (%A %d %B %Y)"
   git log --oneline -10
   git diff --stat HEAD~5
   ```
2. **Write Retrospective Document**:
   - **Path**: `$PSI/memory/retrospectives/YYYY-MM/DD/HH.MM_slug.md`
   - Include Timeline, Files Modified, AI Diary with `[→ AGENT DECISION]`, and Lessons Learned.
3. **Verify on Disk**: Ensure file exists and is cleanly written before proceeding to Step 2.

### Step 2: Knowledge Ingestion (Mandatory MCP Call)
Immediately after Step 1, you MUST execute the `oracle_learn` MCP tool call. Do not end the turn without calling it:
- **Tool**: `oracle_learn` (or `call_mcp_tool` -> `oracle_learn`)
- **Pattern**: The core generalized technical or workflow heuristics distilled from the retrospective.
- **Concepts**: Relevant tags (e.g. `[rrr, <topic-tags>]`).
- **Project**: The current project name/ghq path.
- **Source**: `rrr on <retro_slug>`

> [!important]
> Writing the markdown file alone is only 50% of the skill. The turn is NOT complete until the `oracle_learn` MCP tool call has executed and confirmed ingestion into the Oracle Brain.

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
