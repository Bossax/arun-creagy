# Standing Instructions for agy — CRDB Lifecycle Grounding Research

This is a folder-based handoff between Claude (running in Claude Code) and agy (Google Antigravity
CLI). Read `00_OBJECTIVE.md` and `SCOPE_LEDGER.md` in this same directory first for the research goal
and current scope — **`SCOPE_LEDGER.md` is required reading before every action below**, not
optional context.

Phase A (iterations 1-3) is closed. Phase B starts at iteration 4 and has **no fixed iteration
count** — it continues only as far as Boss approves between rounds. Do not assume it stops after any
particular iteration number; watch for `01_query_pack.md` files as they appear, however many there
turn out to be.

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

**Poll, don't wait for a nudge.** Check this directory tree every 60–120 seconds for a new or updated
`iteration-N/01_query_pack.md`. Use your own background polling loop (or a native filesystem watcher
if your runtime supports one) — do not wait for Claude or Boss to tell you a file has appeared. Keep
polling indefinitely between iterations; there is no fixed iteration count, so do not stop polling
just because some time has passed without a new file.

When a new or updated `iteration-N/01_query_pack.md` appears, that is your signal to start querying
for iteration N.

## What to do for each iteration

0. **Scope Sentinel check (new, mandatory, before anything else).** Read `SCOPE_LEDGER.md`. Compare
   every question in `iteration-N/01_query_pack.md` against its Settled Findings and Out of Scope
   sections. If any question re-opens a Settled Finding or touches an Out of Scope topic, **do not
   query it.** Instead, append to that same `01_query_pack.md` file:
   ```
   ---
   ## Agy Scope Flag

   <which question(s), which Settled Finding or Out-of-Scope item it conflicts with, and why>
   ```
   Then stop and wait for Claude to revise the pack. Only proceed to step 1 once every question in
   the pack is clear of scope conflicts (a flag on a subset of questions does not block querying the
   rest — flag the conflicting ones and proceed with the clean ones).
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
7. Do a second-opinion pass, now with two parts:
   - **Scope check against `SCOPE_LEDGER.md`**: does any conclusion in the synthesis restate a
     Settled Finding as if it were still open? Does it introduce a new tangent outside the Approved
     Research Areas for this iteration? Flag both explicitly if found.
   - **Real-world sanity check**: use web search (permitted here — it is not part of the query-only
     nlm guardrail, which applies only to notebook queries) to sanity-check the synthesis against
     real-world practice. Ask clarifying questions, flag anything unsupported by the raw extracts,
     note anything a web search suggests was missed or mis-framed.
8. **Append** — never edit or delete anything above it — a new section at the bottom of the same
   `02_synthesis.md` file:
   ```
   ---
   ## Agy Second-Opinion Feedback

   <scope-check findings first, then real-world sanity-check findings>
   ```
9. Stop and wait. Claude will finalize the synthesis and propose the next iteration's queries to
   Boss for approval — this may take some time, and there may or may not be a next iteration at all.
   Do not query further, and do not treat silence as a signal to act; just keep watching for the next
   `01_query_pack.md` (running its own Scope Sentinel check per step 0 when it appears).

## Stop condition

There is no fixed iteration count in Phase B. Keep watching for new `iteration-N/01_query_pack.md`
files indefinitely. Claude will tell you explicitly (via a note in `00_OBJECTIVE.md` or a new
`98_RESEARCH_CLOSED.md` marker file) when the research phase is over and the final redirection plan
is being produced instead.
