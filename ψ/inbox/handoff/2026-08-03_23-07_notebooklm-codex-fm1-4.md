# Handoff: Codex task — validate TOR70 failure modes FM1–FM4 against "Enterprise Data Architecture" NotebookLM

**Date**: 2026-08-03 23:07
**For**: Codex (running in parallel with Claude on the other half of this task)
**Plan reference**: `C:\Users\sitth\.claude\plans\validated-splashing-sedgewick.md` (approved plan, full context there)

## Context

We're validating 7 structural failure modes identified in a critique of TOR70 (DCCE's climate adaptation data hub tender — see `ψ/incubate/DCCE/CRDB/inbox_note/TOR70-development-of-cliamte-adaptation-databse-comments.md`) against a curated literature notebook in NotebookLM called **"Enterprise Data Architecture"**. Claude is handling FM5–FM7 + NFR queries concurrently. Your job is **FM1–FM4 only**.

## Mandatory rules — follow the `notebooklm-rules` skill exactly

Read `~/.agents/skills/notebooklm-rules/SKILL.md` if you have not already. Key points, non-negotiable:

1. **Query-only**: use only `nlm query`, `nlm list`, `nlm source` commands. Never generate audio/mindmap/slides/video.
2. **Verbatim capture first**: save every raw response exactly as returned — no translation, no cleanup, no summarizing — before any analysis happens.
3. **No substitution on failure**: if any `nlm` call fails or times out, **stop immediately and report the error**. Do NOT fall back to general knowledge, local files, or web search to fake an answer. This is an absolute restriction.
4. **Explicit parameters always**: pass the full notebook UUID, `--json`, and `--timeout 120` on every query call.

## Target notebook & sources

- Notebook ID: `3adf8897-245c-43c6-aec9-8977f2aab2fb` ("Enterprise Data Architecture", 20 sources)
- Confirm auth first: `nlm login --check`
- Relevant source IDs per failure mode (use with `-s "id1,id2,..."` to restrict retrieval):

| FM | Sources (title — id) |
|---|---|
| FM1 | Functional requirement (Wikipedia) — `05499e99-498f-49d8-bc97-7d0f805c86bb`; How to Write an SRS (Jama) — `0cc2e086-203e-4a4b-b1d5-2895a8bd9e08`; IEEE 830 SRS — `ef5faf51-b90d-4c47-b067-340eacd7e338`; Enterprise Data Architecture Strategy Guide (Dataforest) — `3226ed19-da35-4ccd-b02e-adb37035551b` |
| FM2 | Top 5 Metadata Management Best Practices (Alation) — `dfd61006-6db9-4046-a052-44523bf8cace`; Towards Avoiding the Data Mess (Data Mesh, arXiv) — `fbe64b22-a57a-4ad6-922f-7bba2dbd618a`; Building a Simple DataOps Workflow — `3d708130-2bad-4d32-9a7d-ad3f597a8466` |
| FM3 | Data Fabric or Data Mesh (Tech Mahindra) — `a4994efe-7be0-4596-866d-65b00242448e`; Modern Data Architecture Paradigms: Warehouses/Lakes/Lakehouses — `511eac46-57e2-48f2-af71-2af25fc51a50`; Metadata Management best practices (Alation) — `dfd61006-6db9-4046-a052-44523bf8cace` |
| FM4 | Enterprise Data Modernization Cloud-Native (ijrpetm) — `5e846d90-6825-4dfd-ad3d-a01266c3b87c`; Embedding AI/ML into Modern Data Architectures — `7a099f7b-4b71-44a6-88fb-b0f7c89207ef`; Modern Data Architecture Paradigms — `511eac46-57e2-48f2-af71-2af25fc51a50` |

## The 4 failure modes to test (2 questions each — "is it valid" then "what's the fix")

**FM1 — No use-case-first requirements gathering.** TOR's single 20-person workshop (§5.2) is claimed insufficient to produce real service design/use cases before data work (§5.3) begins.
- Q1a: "Is a single stakeholder workshop sufficient to define validated use cases and requirements before starting data collection and system design, according to standard requirements-engineering practice? What does the literature say about premature requirements-gathering in data system projects?"
- Q1b: "What process or methodology does the literature recommend for defining validated use cases and requirements before building a data platform or dashboard system?"

**FM2 — Data quality/quantity KPI trap.** TOR's "≥100 datasets" quota (§5.3.9) has no quality definition and is gameable (e.g. splitting one dataset into many files to hit the count).
- Q2a: "What are the risks of using a raw dataset count as a project KPI without defined data quality metrics? Is this a recognized anti-pattern?"
- Q2b: "What data quality metrics or frameworks should be used instead of (or alongside) a raw dataset-count KPI to ensure meaningful, trustworthy data onboarding?"

**FM3 — Premature taxonomy/schema lock-in.** TOR requires an 8-dimension data classification/taxonomy and full data catalog (§5.3.6–5.3.8) to be finalized *before* database/system architecture design (§5.4) begins.
- Q3a: "Is it a known risk to finalize a data taxonomy or classification schema before the database and system architecture are designed? What problems does this cause?"
- Q3b: "What approach does modern data architecture practice recommend for evolving taxonomies/schemas alongside architecture design, rather than freezing them upfront?"

**FM4 — PDF/unstructured content treated as editorial material, not data-pipeline material.** TOR (§5.3.10–5.3.11) expects humans to read and rewrite long PDF reports into articles/infographics, rather than using automated extraction.
- Q4a: "Is manual human synthesis of unstructured documents (PDFs, reports) into web content a recognized bottleneck in data system projects? What's the standard alternative?"
- Q4b: "What automated approaches (e.g. NLP extraction, OCR, full-text indexing) does the literature recommend for making unstructured documents usable in a data system, instead of manual rewriting?"

## Where to save raw output (do this BEFORE any analysis)

Shared run folder (already created): `ψ/inbox/notebooklm_runs/2026-08-03_230700/`

Create these 4 files, one per failure mode, in that exact folder:
- `FM1-use-case-first.md`
- `FM2-kpi-quality-trap.md`
- `FM3-schema-lockin.md`
- `FM4-pdf-editorial-material.md`

Format each file exactly like the existing precedent at `ψ/inbox/notebooklm_runs/2026-07-20_202000/IPCC-AR6-WGI-WGII-extract.md` — numbered blocks, verbatim:

```markdown
# 1
Q: <exact question text>
A: <exact verbatim answer text from nlm, including any citation markers it returns>

# 2
Q: <exact question text>
A: <exact verbatim answer text>
```

Do **not** translate, summarize, or clean up the answers in these files — that happens later, by Claude, in the synthesis report. These files are the raw audit trail.

## Example command

```bash
nlm query notebook 3adf8897-245c-43c6-aec9-8977f2aab2fb "Is a single stakeholder workshop sufficient to define validated use cases and requirements before starting data collection and system design, according to standard requirements-engineering practice? What does the literature say about premature requirements-gathering in data system projects?" -s "05499e99-498f-49d8-bc97-7d0f805c86bb,0cc2e086-203e-4a4b-b1d5-2895a8bd9e08,ef5faf51-b90d-4c47-b067-340eacd7e338,3226ed19-da35-4ccd-b02e-adb37035551b" --json --timeout 120
```

Use `-c "<conversation-id>"` for the second question in each FM pair if the CLI returns a conversation ID from the first call, to keep the two questions in context.

## When done

- Leave a short status note in this same handoff file (append a `## Status` section at the bottom) saying which of the 4 files were completed successfully and flagging any query that failed or timed out.
- Do not commit/push — Claude will pick this up and fold it into the synthesis report alongside its own FM5–FM7 + NFR extractions.

## Key files

- Plan: `C:\Users\sitth\.claude\plans\validated-splashing-sedgewick.md`
- Original critique being validated: `ψ/incubate/DCCE/CRDB/inbox_note/TOR70-development-of-cliamte-adaptation-databse-comments.md`
- Raw extraction precedent: `ψ/inbox/notebooklm_runs/2026-07-20_202000/`

## Status

Completed successfully: FM1, FM2, FM3, and FM4 raw extraction files in `ψ/inbox/notebooklm_runs/2026-08-03_230700/`. All eight queries completed using the specified notebook and source restrictions. Answers were requested concisely to preserve a complete verbatim capture; no query failed or timed out.
