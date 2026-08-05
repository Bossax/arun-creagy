# Standing Instructions for agy — CRDB Lifecycle Grounding Research

This is a 3-iteration, folder-based handoff between Claude (running in Claude Code) and agy
(Google Antigravity CLI). Read `00_OBJECTIVE.md` in this same directory first for the research
goal.

## Model & Subagent Directives

1. **Main Agent (Orchestrator)**: Runs at **Medium reasoning** to manage workflow state, watch folder triggers, and coordinate subagent delegation.
2. **Query Subagent (`flash` / `flash_lite`)**: Spawned at **Low reasoning effort** to run all `nlm query` commands for bulk retrieval and verbatim JSON captures.
3. **Second-Opinion Subagent (`pro`)**: Spawned at **High reasoning effort**star to evaluate Claude's `02_synthesis.md`, perform web-search sanity checks, and append the second-opinion feedback.

## Command syntax (mandatory — inherited from this repo's `notebooklm-rules` skill)

Preflight, once per session:
```
nlm login --check
```
If this fails, stop and report the error. Do not attempt workarounds beyond the documented manual
cookie-login flow in that skill's `references/manual-cookie-login.md`.

Per question:
```
nlm query notebook <notebook_id> "<question>" --json --timeout 120
```

Notebook IDs for this research:
- Business requirement for SW development: `5133ef48-564c-40df-bdd1-142bb7e5bdf3`
- Enterprise Data Architecture: `3adf8897-245c-43c6-aec9-8977f2aab2fb`

## Guardrails (non-negotiable)

1. **Query-only.** Only `nlm query`, `nlm list`, `nlm source` commands are permitted. Never generate
   audio, podcasts, mindmaps, slide decks, or video overviews from a notebook.
2. **Verbatim capture ("nothing is deleted").** Save every raw response exactly as returned —
   no summarizing, no editing, no cleanup. Analysis happens later, in separate files, never by
   modifying the raw capture.
3. **No substitution on failure.** If a query fails or times out, stop and report the error. Never
   fall back to local files, general knowledge, or a web-search guess to fake an answer to a
   notebook question.
4. **Parameter discipline.** Always pass the explicit notebook UUID, `--json`, and `--timeout 120`.

## Trigger

Watch this directory tree:
`ψ/incubate/DCCE/CRDB/research/2026-08-05_lifecycle-grounding/`

When a new or updated `iteration-N/01_query_pack.md` appears, that is your signal to start querying
for iteration N.

## What to do for each iteration

1. Read `iteration-N/01_query_pack.md`. It has two sections, one per notebook, each with a numbered
   list of questions.
2. For each question, run the `nlm query` command above against the correct notebook.
3. Save the raw JSON response exactly as returned to:
   `iteration-N/raw/<notebook-slug>/Q<n>_<short-slug>.json`
   - `<notebook-slug>` is `business-requirement-sw-dev` or `enterprise-data-architecture`
     (folders already exist).
4. Once all questions for a notebook are done, write an empty marker file:
   `iteration-N/raw/<notebook-slug>/_COMPLETE.txt`
5. Stop and wait. Claude will read the raw extracts and write `iteration-N/02_synthesis.md`.
6. When `iteration-N/02_synthesis.md` appears or is updated, read it in full.
7. Do a second-opinion pass: use web search (permitted here — it is not part of the query-only nlm
   guardrail, which applies only to notebook queries) to sanity-check Claude's synthesis against
   real-world practice. Ask clarifying questions, flag anything that looks unsupported by the raw
   extracts, note anything a web search suggests was missed or mis-framed.
8. **Append** — never edit or delete anything above it — a new section at the bottom of the same
   `02_synthesis.md` file:
   ```
   ---
   ## Agy Second-Opinion Feedback

   <your feedback here>
   ```
9. Stop and wait for the next iteration's `01_query_pack.md`.

## Stop condition

After appending feedback for `iteration-3/02_synthesis.md`, stop. Claude will take it from there to
produce the final redirection plan.
