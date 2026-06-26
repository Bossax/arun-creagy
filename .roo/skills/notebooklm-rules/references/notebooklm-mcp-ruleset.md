# NotebookLM MCP Ruleset

Canonical guardrails for using the low-latency API-based NotebookLM MCP in this repo.

This file condenses rules and patterns adapted for `notebooklm-mcp-cli` (API-based, low-latency) from:
- [`2026-04-08_notebooklm-source-fidelity-and-parameter-discipline.md`](ψ/memory/learnings/2026-04-08_notebooklm-source-fidelity-and-parameter-discipline.md)
- [`2026-04-08_notebooklm-extraction-vs-local-harmonisation.md`](ψ/memory/learnings/2026-04-08_notebooklm-extraction-vs-local-harmonisation.md)
- MCP infrastructure and auth/timeouts learnings in [`ψ/memory/learnings`](ψ/memory/learnings)
- Environment-specific issues recorded in [`NotebookLM-MCP-troubleshooting.md`](ψ/inbox/NotebookLM-MCP-troubleshooting.md)

Use this ruleset as the **first reference** before running any structured NotebookLM extraction.

---

## 1. Scope and boundaries

1. NotebookLM is used for **literature-grounded extraction and citation-bearing concept harvesting**.
2. Harmonisation, flattening, de-duplication, QC, and canonical register maintenance are performed **locally in the repo**, not in NotebookLM.
3. NotebookLM runs must produce **raw, row-oriented or atomic-note outputs** (e.g., JSON or Markdown lists) that can be saved verbatim and later transformed locally.

Implications:
- Do not ask NotebookLM to "merge", "harmonise", "deduplicate", "rewrite the dictionary", or "QC the register".
- Do ask NotebookLM to "extract", "list", "identify", or "quote" evidence with citations.

---

## 2. Parameter discipline

Every NotebookLM MCP call must make these parameters explicit:

1. `notebook_id`
   - Always specify which notebook is being used in the `notebook_query` tool.
   - Do not rely on implicit or default active notebooks.

2. `session_id`
   - Use a concrete session ID for sequential Q&A to maintain conversation thread context.
   - For fresh, independent queries, omit `session_id` to start a clean session and reduce token bloat.

3. `source_format`
   - Set to `none` for fast, snappy chat where citations are not needed.
   - Set to `footnotes` or `inline` when presenting answers to a human where source verification is required.
   - Set to `json` when downstream tools need to process citations programmatically.

4. Source-binding assumptions
   - For each batch, specify whether it is corpus-wide or tied to a specific packet of named sources.
   - Encode this assumption in the prompt itself.

*Note: Playwright browser options (headless, show, stealth, typing speed) are obsolete and no longer used in the API-based server.*

---

## 3. Source fidelity as a hard gate

When a batch depends on named sources ("source-bound" batches):

1. **Title resolution**
   - Run `notebook_get` to list the **actual notebook titles** of your documents.
   - Use the exact titles that NotebookLM sees, not local guesses.

2. **Small, exact-title source packets**
   - Group runs into packets of 1–3 exact titles.
   - Copy titles directly from the NotebookLM source list (no paraphrasing).

3. **Fail-fast behaviour**
   - In the prompt, instruct NotebookLM to **stop and report** when any named title is missing or ambiguous.
   - It must not substitute nearby uploaded literature without reporting.

4. **Gate for evidence validity**
   - Any batch that silently uses substitute sources fails the source-fidelity gate.
   - Such runs may be kept as methodological examples, but not as evidence for the intended packet.

The pipeline should treat this gate as **non-negotiable**. Convenience does not override source fidelity.

---

## 4. Prompt design

Design prompts so that NotebookLM stays in its strongest mode: structured extraction.

1. Single objective per prompt
   - Each prompt should target one theme (e.g., methodological capacities, framework indicators, governance clauses).
2. Extraction-only and targeted query language
   - Allowed: "extract", "list", "identify", "quote", "cite", "classify within X".
   - Forbidden: "harmonise", "deduplicate", "merge outputs", "QC the register", "rewrite".
3. Length and latency
   - Keep prompts concise. Shorter, crisply scoped prompts reduce latency and behavior drift.
   - The API-based server returns fully formed JSON/Text responses directly, bypassing DOM rendering wait times.

---

## 5. MCP health and auth

1. Health check before long sessions
   - Confirm status via CLI `nlm doctor` or profile status checks.
2. Timeouts
   - The API-based server operates under a 2–5s latency profile per query, well below the host's 60s hard timeout.
   - If a query times out, simplify the prompt scope or restrict the query to specific sources using names in the prompt text.
3. Auth expiration
   - When Google invalidates cookies (usually every 2-4 weeks), you will see `Authentication expired`.
   - Resolve by manually copying the cookie string from the browser Developer Tools (Network tab -> batchexecute headers) and running:
     `nlm login --manual --file <path_to_cookie_file>`

---

## 6. Tool Discipline & Context Management

With the migration to `notebooklm-mcp-cli` introducing **39 programmatic tools**, the agent must enforce strict context discipline to avoid overloading the token window and polluting decision paths.

1. **The Core RAG Focus (Default)**
   For 95% of tasks involving literature-grounded search and extraction, restrict tool calls strictly to:
   *   `notebook_list` (To find the target notebook)
   *   `notebook_get` (To inspect existing sources and verify structure)
   *   `notebook_query` (For citation-backed RAG queries)
   *   `source_add` (Only if the human asks to append new literature to a notebook)

2. **Absolute Feature Restrictions (Query-Only Policy)**
   The use of NotebookLM for generating podcasts, mindmaps, slide decks, video overviews, quizzes, or flashcards is **strictly prohibited** in this project workspace. The agent must never call these studio generation tools or attempt to download generated media. The active toolset is restricted exclusively to:
   *   `notebook_query` (For RAG questions and text extraction)
   *   `notebook_get` (To inspect sources)
   *   `notebook_list` (To find the notebook)
   *   `source_add` (If adding text/URLs/PDFs)

   All other tools (e.g. `studio_create`, `download_artifact`, `export_artifact`, `tag_*`, `pipeline`, etc.) are banned.

By enforcing this query-only boundary, the agent keeps its execution path predictable, avoids API rate limits, and saves significant token context.
