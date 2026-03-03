---
query: "how did I create atomic notes in DMCR project?"
target: "Knowledge_System"
mode: smart
timestamp: 2026-02-26 23:54
---

# Trace: DMCR atomic notes pattern

## What “atomic notes” looked like (DMCR)

In the DMCR project, “atomic notes” were created as **compact, single-claim evidence statements** embedded inside `notes/` markdown files, written as numbered blocks like **“Atomic Note 1/2/3…”**, often followed by a short **Rule/Hint/Warning** interpretation.

Concrete example:

- [`src/01_Projects/2026-01_DMCR- marine-soundscape/notes/Spatial Replication & Acoustic Footprint.md:12`](src/01_Projects/2026-01_DMCR-%20marine-soundscape/notes/Spatial%20Replication%20%26%20Acoustic%20Footprint.md:12)
  - Contains multiple sections of **Atomic Note N:** (each a single claim) with citations like “(Lillis et al., 2018; Raick et al., 2021)” and optional takeaways labeled as **Rule/Hint/Warning**.

Additional atomic-note style inputs:

- Hydrophone placement vertical tradeoffs:
  - [`src/01_Projects/2026-01_DMCR- marine-soundscape/notes/Hydrophone Height & Water Column Placement.md:12`](src/01_Projects/2026-01_DMCR-%20marine-soundscape/notes/Hydrophone%20Height%20%26%20Water%20Column%20Placement.md:12)
- Proximity/masking framing:
  - [`src/01_Projects/2026-01_DMCR- marine-soundscape/notes/Proximity & Masking Risks.md:13`](src/01_Projects/2026-01_DMCR-%20marine-soundscape/notes/Proximity%20%26%20Masking%20Risks.md:13)
- Topography/substrate/boundary effects:
  - [`src/01_Projects/2026-01_DMCR- marine-soundscape/notes/Topography & Substrate Clues.md:12`](src/01_Projects/2026-01_DMCR-%20marine-soundscape/notes/Topography%20%26%20Substrate%20Clues.md:12)

## How those atomic notes were used (KO&I pattern)

The DMCR workflow made atomic notes useful by **connecting them into an evidence → synthesis → consumption chain**:

1) **Evidence inputs** = AI_output notes (containing atomic notes)
2) **Synthesis artifact** = consolidated factors / decision rules
3) **Consuming docs** = methodology + SOP

This chain is explicitly represented in the evidence index:

- [`src/01_Projects/2026-01_DMCR- marine-soundscape/output/DMCR_Hydrophone_Evidence_Index.md:15`](src/01_Projects/2026-01_DMCR-%20marine-soundscape/output/DMCR_Hydrophone_Evidence_Index.md:15)
  - “Evidence inputs (AI_output notes)” → links to note files
  - “Synthesis artifacts (KO&I outputs)” → links to synthesis
  - “Consuming documents” → links to methodology/SOP
  - “Guiding questions → sources → synthesis → consumption” mapping

The synthesis artifact that consumed these atomic notes:

- [`src/01_Projects/2026-01_DMCR- marine-soundscape/output/Deployment configuration factors.md:16`](src/01_Projects/2026-01_DMCR-%20marine-soundscape/output/Deployment%20configuration%20factors.md:16)

## Practical “atomic note” template inferred from DMCR files

Minimal template (matches the DMCR pattern):

1. **Atomic Note N: Short label** — one claim (1–3 sentences), include citation(s)
2. Optional: **Rule / Hint / Warning** — how to use the claim operationally

## Related workflow guidance

The broader repo workflow explains the KO&I chain (scan AI_output → synthesize → evidence index → align methodology):

- [`src/00_Meta/00_WORKFLOW.md:38`](src/00_Meta/00_WORKFLOW.md:38)
- [`src/00_Meta/Knowledge_Organization_and_Indexing_SOP.md:80`](src/00_Meta/Knowledge_Organization_and_Indexing_SOP.md:80)

## Summary

DMCR “atomic notes” were **embedded, numbered evidence statements inside AI_output notes**, then made actionable via:

- an **evidence index** mapping questions → evidence → synthesis → consuming documents
- a **synthesis artifact** that converted evidence into decision rules
