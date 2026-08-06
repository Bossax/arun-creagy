# Decision: Reference Data Matrix Deferred to TOR70

**Date:** 2026-08-06
**Status:** Decided (housekeeping, WP0 of the final-sprint implementation plan)

## Decision

The Reference Data Matrix (Pillar 8 — shared/common lookups such as admin boundaries, province/district names, standard code lists) is **not built in this project round**, given the two weeks remaining in the sprint. Only the technical specification (`Pillar_08_RefData_Matrix_Technical_Specification.md`) exists; no actual reference-data content is populated.

This is an explicit deferral, not a silent drop: the Reference Data build is named as a task for TOR70 / the next phase in Item 9 (Recommendations) of the final sprint (per `99_FINAL_crdb-redirection-plan-v2.md`, Section 4 item 4 and Section 6 governance housekeeping).

## Why

- Boss confirmed no time remains in the current two-week window to populate this pillar.
- The original inception-era intent for Reference Data (shared cross-domain datasets like admin boundaries, province names) is acknowledged as genuinely useful, but low enough priority relative to the other 8 items that it doesn't survive the time cut.

## Consequence

- `08_RefData_Matrix/` stays at spec-only status through final packaging.
- Item 9 (Recommendations) must explicitly name this as a TOR70/next-phase task, not omit it.
- Ledger update (Deliverable Map / Change Log entries reflecting this decision) pending `/seal`.
