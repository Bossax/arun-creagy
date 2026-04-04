# Handoff: Foresight citation system and team-input anchoring

**Date**: 2026-04-04 07:22
**Context**: Foresight 2590 report grounding, citation workflow redesign, and anchoring check against team 5G inputs.

## What We Did
- Ran local `/recap` to understand current git state, recent retrospectives, and untracked foresight files.
- Read the latest retrospective and learning on citation friction:
  - Retro: [`ψ/memory/retrospectives/2026-04/04/05.49_foresight-grounding-audit-and-citation-system-friction.md`](ψ/memory/retrospectives/2026-04/04/05.49_foresight-grounding-audit-and-citation-system-friction.md)
  - Learning: [`ψ/memory/learnings/2026-04-04_foresight-grounding-audit-citation-system-friction.md`](ψ/memory/learnings/2026-04-04_foresight-grounding-audit-citation-system-friction.md)
- Agreed to prioritize **implementation efficiency** over the earlier heavy three-file citation architecture.
- Designed an iteration plan for efficient citation and evidence work:
  - [`plans/2026-04-04_foresight-citation-iteration-plan.md`](plans/2026-04-04_foresight-citation-iteration-plan.md)
  - Focus on: artifact-first workflow, simple citation library, evidence library, single Works Cited, and section-scoped grounding.
- Built a first-pass **Citation library** indexing all current foresight source artifacts:
  - [`ψ/lab/foresight-report-wrting/citations/citation-library.md`](ψ/lab/foresight-report-wrting/citations/citation-library.md)
  - One row per artifact under `ψ/lab/foresight-report-wrting/artifacts/source/` with `ART_ID`, `Title`, `Type`, `Path`, `Core_Tags`, and provisional `Baseline_Citation`.
- Switched grounding target from the v4 working set to the **integrated v3 edited draft** as the single source of truth:
  - [`ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3-edited.md`](ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3-edited.md)
- Added style-pack benchmarking step to the citation iteration plan so each grounded section is aligned with:
  - [`plans/foresight-report-writing-style-pack.md`](plans/foresight-report-writing-style-pack.md)
- Created a **team-input concept-note workflow** and plan:
  - Plan: [`plans/2026-04-04_team-input-concept-note-plan.md`](plans/2026-04-04_team-input-concept-note-plan.md)
  - Anchors concept note to three team-input files (5G notes, strategic presentation, and summary) and to the integrated draft’s outline.
- Drafted a **Concept Note for team-input anchoring**:
  - [`plans/2026-04-04_team-input-anchoring-concept-note.md`](plans/2026-04-04_team-input-anchoring-concept-note.md)
  - Section-by-section check of how the report’s outline is or is not anchored to the three team-input artifacts.

## Pending
- [ ] Harden the Citation library’s `Baseline_Citation` values with real bibliographic details once evidence backfilling progresses.
- [ ] Design and create the **Evidence library** file as per the iteration plan (e.g. `ψ/lab/foresight-report-wrting/citations/evidence-library.md`) and wire it into the section grounding workflow.
- [ ] Create and initialize a central **Works Cited** file (e.g. `ψ/lab/foresight-report-wrting/citations/works-cited.md`).
- [ ] Implement Iteration 1 of the citation plan for Chapter 2 segments (2.2–2.4) directly on `2026-04-02_foresight-2590-integrated-rewrite-v3-edited.md` using the efficient loop.
- [ ] Use the new concept note to systematically compare each major section of the report with team inputs and flag any sections where the report drifts away from the core narrative agreed in the 5G process.
- [ ] Decide and standardize the inline citation format and any artifact-trace suffixes (e.g. `(Author Year)` + `[#ART_ID-local]`) before large-scale grounding work begins.

## Next Session
- [ ] Instantiate the Evidence library and Works Cited files following [`plans/2026-04-04_foresight-citation-iteration-plan.md`](plans/2026-04-04_foresight-citation-iteration-plan.md) and wire them conceptually to `citation-library.md`.
- [ ] Start Iteration 1 by grounding one chosen Chapter 2 segment (likely the 2.2 signals section) end-to-end:
  - List claims from the integrated draft section.
  - Shortlist candidate artifacts from `artifacts/source` using `citation-library.md`.
  - Locate supporting evidence, append rows to the Evidence library, insert inline citations in the main draft, and update Works Cited.
  - Run style-pack benchmarking against [`plans/foresight-report-writing-style-pack.md`](plans/foresight-report-writing-style-pack.md).
- [ ] Use [`plans/2026-04-04_team-input-anchoring-concept-note.md`](plans/2026-04-04_team-input-anchoring-concept-note.md) as a lens while editing the integrated draft to keep the narrative anchored to the 5G team inputs, especially on:
  - Human security vs. military security
  - Children/orphans as core focus
  - Plural, life-relevant education
  - Creative economy and Malay-Muslim identity
  - Trust, safe spaces, and civil society’s role

## Key Files
- Citation iteration plan: [`plans/2026-04-04_foresight-citation-iteration-plan.md`](plans/2026-04-04_foresight-citation-iteration-plan.md)
- Citation library: [`ψ/lab/foresight-report-wrting/citations/citation-library.md`](ψ/lab/foresight-report-wrting/citations/citation-library.md)
- Writing style pack: [`plans/foresight-report-writing-style-pack.md`](plans/foresight-report-writing-style-pack.md)
- Main integrated draft: [`ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3-edited.md`](ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3-edited.md)
- Team-input concept plan: [`plans/2026-04-04_team-input-concept-note-plan.md`](plans/2026-04-04_team-input-concept-note-plan.md)
- Team-input anchoring concept note: [`plans/2026-04-04_team-input-anchoring-concept-note.md`](plans/2026-04-04_team-input-anchoring-concept-note.md)
