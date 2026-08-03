---
name: trace
description: The Lens — unified forensic discovery across git history, repos, docs, and Oracle. Maps technical ancestry and generates T-E-D-A hypotheses. Use when user asks "trace", "find project", "where is [project]", "search history". Supports --oracle (fast), --smart (default), --deep (wave execution).
---

# /trace — Unified Discovery System (The Forensic Lens)

> "Discover reality. Map the ancestry. Hypothesize the why."

## Usage

```
/trace [query]                    # Current repo (default --smart)
/trace [query] --oracle           # Oracle only (fastest)
/trace [query] --smart            # Oracle first, fallback to deep
/trace [query] --deep             # Forensic wave execution (thorough)
```

---

## Oracle Root Detection

**Every skill that writes to ψ/ MUST detect the oracle root first.**

Resolve the repository root with the host's normal Git capability, falling back to
the working directory, then set `PSI` to `<root>/ψ`. Do not assume a shell or a
provider-owned workspace layout. Before a mode that writes a trace artifact,
discover `oracle_search` and `oracle_trace`; Oracle is required and the skill must
stop before writing if either capability is unavailable.

---

## 🛡️ The Workflow (The Forensic Lens)

### Mode 1: --oracle (Oracle Only)
**Fastest. Just Oracle MCP.**
Query Oracle knowledge base:
```
oracle_search("[query]", limit=15)
```
Display results and done.

### Mode 2: --smart (Default)
**Oracle first → auto-escalate if results < 3**
- Query Oracle first: `oracle_search("[query]", limit=10)`
- If Oracle results >= 3 → Display and done.
- If Oracle results < 3 → Auto-escalate to `--deep` mode.

### Mode 3: --deep (Wave Execution + Session Mining)
**Multiple waves of parallel search + session mining. Each wave has fresh context.**

#### Wave 1 — Fast surface search + session mining
- **Agent A (Current Repo Files)**: Search for file names, paths, code, or configs matching the query.
- **Agent B (Oracle Memory)**: Search ψ/memory/ for learnings, retrospectives, and previous trace logs matching the query.
- **Session History**: Query the shared adapter for the explicitly selected host:
  ```text
  python .agents/skills/_shared/scripts/session_history.py --host auto --limit 50
  ```
  Search normalized session data for mentions of the query. If unavailable, record
  the returned reason and continue without provider-log fallback.

Check if Wave 1 results are sufficient (answer clear and >= 3 results). If insufficient, proceed to Wave 2.

#### Wave 2 — Deep search
- **Agent C (Git History)**: Search git commits: `git log --all --oneline --grep="[query]"`
- **Agent D (Cross-Repo)**: Search other repos under the ghq root.
- **Agent E (GitHub Issues/PRs)**: Run `gh issue list --search "[query]"` and `gh pr list --search "[query]"` if remote exists.

---

## Step 3: Calculate Friction Score
Calculate `friction_score = S + C_offset` (clamped to `[0.0, 1.0]`).

**S — Source Score** (highest-tier source with relevant result):
- **1.0**: Oracle (Frictionless)
- **0.7**: Repo files (Present but not indexed)
- **0.5**: Git history (Buried)
- **0.3**: Cross-repo (Hidden)
- **0.0**: Not found (Invisible)

**C_offset — Completeness** (from goal-backward check in Step 4):
- **high**: +0.00
- **medium**: −0.10
- **low**: −0.20

Calculate `coverage` (dimensions searched): `oracle`, `files`, `git`, `cross-repo`, `github`, `session-history`.

---

## Step 4: Goal-Backward Check
Ask: *"Did this trace actually answer the original question?"*
- **Yes** → confidence: high
- **Partial** (found related but not exact) → confidence: medium (note what's missing)
- **No** → confidence: low (note what next step is needed)

---

## Step 5: Write Trace Log
Write findings to `ψ/memory/traces/YYYY-MM-DD/HHMM_[query-slug].md`.

**Markdown Log Template**:
```markdown
---
type: trace
traceId: [trace_id]
date: YYYY-MM-DD
query: "[query]"
target: "[TARGET_NAME]"
mode: [oracle|smart|deep]
timestamp: YYYY-MM-DD HH:MM
friction_score: [0.0–1.0]
coverage: [oracle, files, git, cross-repo, github, session-history]
confidence: [high|medium|low]
---

# Trace: [query]

**Target**: [TARGET_NAME]
**Mode**: [mode] | **Friction**: [friction_score] | **Confidence**: [confidence]
**Time**: [timestamp]

## Oracle Results
[list results or "None"]

## Files Found
[list files or "None"]

## Git History
[list commits or "None"]

## GitHub Issues/PRs
[list or "None"]

## Cross-Repo Matches
[list or "None"]

## Oracle Memory
[list or "None"]

## Session History
[normalized results or "Unavailable: reason"]

## Friction Analysis
**Score**: [0.0–1.0] — [interpretation]
**Coverage**: [dimensions searched]
**Goal check**: [Did this answer the question? What's missing?]

### Potential Ledger Yields (T-E-D-A Hypothesis)

- **[T] Potential Trigger**: [The conceptual "Why" discovered in the trace]
- **[E] Supporting Evidence**: [File Path A], [File Path B]
- **[D] Potential Decision**: [The strategy/posture this trace seems to validate]
- **[A] Target Asset**: [The file this trace was investigating]
```

> [!important]
> **Artifact vs. Motive Separation**: Files (PDFs, scripts, notebooks) are **Evidence (E)**. The insight or mandate derived from them is the **Trigger (T)**. Never log a file path as a Trigger.

---

## Step 6: Log to Oracle Database
Call `oracle_trace` (MCP) with the query, foundFiles, foundCommits, foundIssues, friction_score, and confidence. Record the returned `traceId` in the markdown file header.

---

## Step 7: Confirm Trace Log Path
Output the resolved absolute path to the trace file.

---

## 📜 Hard Rules

1. **Lens Only**: Do NOT use `replace` or `write_file` on project ledgers (e.g., `ψ/incubate/`).
2. **Nothing is Deleted**: Every trace generates a new file. Never overwrite old traces.
3. **Zero Trust**: Assume nothing about project history until you see a physical file or a session string.
4. **Handoff Prompt**: Upon completion, you MUST state: *"Trace complete. Findings logged to [Path]. If you wish to formalize these yields into the project ledgers, run `/seal`."*

---

**Philosophy**: Discover reality. Map the ancestry. Hypothesize the why. *"Trace to understand; Seal to commit."*
