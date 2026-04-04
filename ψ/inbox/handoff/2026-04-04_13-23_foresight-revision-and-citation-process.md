# Handoff: Foresight Revision and Citation Process

**Date**: 2026-04-04 13:23
**Context**: Foresight 2590 report revision is now content-ready for the next editing pass, with benchmark criteria, citation-library refresh, and research-prompt scaffolding prepared.

## What We Did
- Updated [`plans/2026-04-04_foresight-report-v3-edited-vs-team-input-benchmark.md`](plans/2026-04-04_foresight-report-v3-edited-vs-team-input-benchmark.md) with section-by-section benchmark guidance, edit priorities, halal-economy strategic voice, and new **template-aligned revision benchmark criteria** based on [`ψ/lab/foresight-report-wrting/artifacts/source/Foresight report - output report reference.md`](ψ/lab/foresight-report-wrting/artifacts/source/Foresight report - output report reference.md).
- Created the cross-impact synthesis note [`ψ/lab/foresight-report-wrting/artifacts/2026-04-04_group3-cross-impact-synthesis-note.md`](ψ/lab/foresight-report-wrting/artifacts/2026-04-04_group3-cross-impact-synthesis-note.md) to support a later rewrite of `2.2.1`.
- Refreshed [`ψ/lab/foresight-report-wrting/citations/citation-library.md`](ψ/lab/foresight-report-wrting/citations/citation-library.md) to include newly added source artifacts, including:
  - [`ψ/lab/foresight-report-wrting/artifacts/source/Foresight report - output report reference.md`](ψ/lab/foresight-report-wrting/artifacts/source/Foresight report - output report reference.md)
  - [`ψ/lab/foresight-report-wrting/artifacts/source/Geopolitics & Regional Integration.md`](ψ/lab/foresight-report-wrting/artifacts/source/Geopolitics & Regional Integration.md)
  - [`ψ/lab/foresight-report-wrting/artifacts/source/Nationalism & Conservative Politics as Scenario Drivers.md`](ψ/lab/foresight-report-wrting/artifacts/source/Nationalism & Conservative Politics as Scenario Drivers.md)
  - [`ψ/lab/foresight-report-wrting/artifacts/source/AI and digital transformation.md`](ψ/lab/foresight-report-wrting/artifacts/source/AI and digital transformation.md)
- Audited the integrated draft comments wrapped in `%%` and converted the main unresolved research needs into external deep-research prompts for Gemini.
- Rescoped the Gemini prompt strategy so that macro-trends are handled in separate, citation-friendly clusters instead of one overloaded prompt.

## Pending
- [x] Run the external Gemini deep-research prompts for: %% done %%
  - structural drivers for `2.1.1`
  - nationalism & conservative politics
  - geopolitics & regional integration
  - AI and digital transformation
  - climate & global economic volatility
- [x] Register any new Gemini outputs back into [`ψ/lab/foresight-report-wrting/citations/citation-library.md`](ψ/lab/foresight-report-wrting/citations/citation-library.md) and related citation surfaces. %% done %%
- [ ] Rewrite [`ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3-edited.md`](ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3-edited.md), especially:
  - `2.1.1`
  - `2.1.2`
  - `2.2`
  - `2.2.1`
  - `3.2`
  - `3.3`
- [ ] Use the updated benchmark file as the control document for revision discipline.
- [ ] Decide later whether to keep Islamic social finance (zakat/waqf) as a supporting driver; if kept, it must be explained in `2.1.1`, not introduced loosely in later strategy sections.

## Next Session
- [ ] Start with the Gemini outputs and map each response to the exact section it should strengthen in the draft.
- [ ] Perform a **team-anchor preservation + section-function alignment** pass using [`plans/2026-04-04_foresight-report-v3-edited-vs-team-input-benchmark.md`](plans/2026-04-04_foresight-report-v3-edited-vs-team-input-benchmark.md).
- [ ] Rewrite `2.2.1` using the Group 3 synthesis note and workshop-grounded logic.
- [ ] Tighten Chapter 3 so the baseline future and scenario axes are explicitly supported by the new macro-trend evidence.

## Key Files
- Main draft: [`ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3-edited.md`](ψ/lab/foresight-report-wrting/2026-04-02_foresight-2590-integrated-rewrite-v3-edited.md)
- Revision benchmark: [`plans/2026-04-04_foresight-report-v3-edited-vs-team-input-benchmark.md`](plans/2026-04-04_foresight-report-v3-edited-vs-team-input-benchmark.md)
- Citation library: [`ψ/lab/foresight-report-wrting/citations/citation-library.md`](ψ/lab/foresight-report-wrting/citations/citation-library.md)
- Cross-impact note: [`ψ/lab/foresight-report-wrting/artifacts/2026-04-04_group3-cross-impact-synthesis-note.md`](ψ/lab/foresight-report-wrting/artifacts/2026-04-04_group3-cross-impact-synthesis-note.md)
- Section-content reference: [`ψ/lab/foresight-report-wrting/artifacts/source/Foresight report - output report reference.md`](ψ/lab/foresight-report-wrting/artifacts/source/Foresight report - output report reference.md)

## Git Note
- `git status --short` shows many pre-existing modified, deleted, and untracked files beyond this session.
- Any commit should be done carefully after reviewing scope, because the repo is **not** in a clean single-task state.
