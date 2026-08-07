# Position Paper: Scope the Final 7 Days Around the Two Named Use Cases, Defer the Rest to TOR70

**Author stance:** Agile/Incremental Delivery Lead
**Date:** 2026-08-07
**Re:** CRDB final-sprint deliverable pack, days 8–14

## The call

Spend the remaining ~7 days making A-BTR reporting and disaster-loss-statistics analysis *fully handoff-grade*, and close everything else — the other 7 services, the other 250 catalog rows, the recommended-but-not-critical gaps — with a one-line deferral note into WP8. Do not attempt full standards-alignment across the whole catalog. That is not an achievable scope in 7 days, and pretending otherwise produces a document that is uniformly 60%-done instead of two pillars that are 100%-done.

## The deliverable pack, named

- **WP2 (Data Inventory):** finish the 9-field deep-capture for the 10 already-identified critical assets. No change — this is in-flight and already correctly scoped.
- **WP3 (Data Product Inventory):** business metadata, 5-role governance, compliance classification for the same 10 assets only. Already scoped correctly; hold the line at 10.
- **WP6 (Use Case & Demand Analysis):** the full Functional Spec + Assumption Log for A-BTR and disaster-loss-statistics gets built to fixed-price-handoff depth, and specifically absorbs the two CRITICAL gaps the NotebookLM audit flagged:
  - **Source-to-Target Mapping**, field-level, built ONLY for the catalog rows feeding these two use cases (a subset of the 10 WP2/WP3 assets, likely 4–8 rows). The remaining ~250 rows in `data_catalog_v3.csv` get a single annotated line: "STM deferred to TOR70 Phase 1 discovery — see WP8."
  - **Data-specific Acceptance Criteria** (row-count reconciliation, null-handling rules, format checks, Definition of Done) written ONLY for these two use cases' data flows. The other 7 services get the same one-line deferral.
  - The NFR/latency matrix (recommended-tier gap) gets built for these two use cases as a natural extension of the Functional Spec — it's cheap once you're already in the weeds on these two, and it materially strengthens exactly the deliverables DCCE will act on first.
- **WP5 (Data Management Framework):** Assumption Log / Client Dependency Register gets built as a standalone cross-cutting document (the third CRITICAL gap), but scoped to bound DCCE-vs-TOR70 obligations at the *platform and governance* level — not attempting a service-by-service assumption log for all 9 services. This is where the WP1 finding about stalled DCCE ratifications (adoption metric, phase-2 trigger, governance sign-off, DBA org assignment) gets formally logged as client-side dependencies blocking downstream work. Glossary update and RACI matrix proceed as scoped; Reference Data stays deferred-and-logged, per existing precedent.
- **WP7 (Gap Analysis):** DATER dims 1–6 scored against Item 1 rationale as planned; no expansion.
- **WP8 (Recommendations):** becomes the collector for every deferral in this plan — STM for 250 rows, acceptance criteria for 7 services, the formal RACI (kept in prose, not built as a separate matrix artifact), and the DAMA-6 quality thresholds (kept conceptual, not annotated row-by-row). Each deferral gets named explicitly as a TOR70 Phase 1 task with a suggested owner and rough effort, not left as a vague gap.
- **WP9, WP10, WP11:** proceed as scoped; WP10's TBD-owner-and-deadline check now includes verifying every deferral item in WP8 has an owner (TOR70) and a phase (Phase 1).

## The risk being accepted, named plainly

I am knowingly accepting that TOR70 will begin its fixed-price build with an incomplete field-level transformation map and incomplete acceptance criteria for 7 of 9 services, and with 250 of 260 catalog rows unprofiled beyond high-level schema. That is real technical risk: it increases the odds of misinterpretation, rework, or a change-order conversation on those 7 services during build. I accept it because (a) those 7 services are not what DCCE is building first — A-BTR and disaster-loss-statistics are the named build-next targets, so risk capital should concentrate where the money moves first; (b) DCCE itself has demonstrated, in WP1, that it cannot currently ratify decisions at the pace CRDB produces them — the adoption metric, phase-2 trigger, governance sign-off, and DBA assignment are all sitting in DCCE's queue, unresolved. A CRDB that hands over nine services' worth of pristine STM and acceptance criteria into an organization that hasn't yet ratified its own governance committee is optimizing the wrong constraint. The bottleneck is DCCE's review capacity, not CRDB's documentation depth.

## Rebutting the standards-architect objection

The expected counter is that any gap in STM, acceptance criteria, or the assumption log invites TOR70 to renegotiate scope or price mid-build, citing ambiguity — and that a requirements handoff exists precisely to foreclose that move. This is a real mechanism, not a strawman, and I won't wave it off. My answer is that the Assumption Log / Client Dependency Register is exactly the instrument designed to neutralize it: it doesn't need to describe every field to be renegotiation-proof, it needs to explicitly state that STM and acceptance criteria are complete for use cases A-BTR and disaster-loss-statistics and *are deliberately scoped out for the remaining 7 services, to be delivered by TOR70 in Phase 1 discovery as a named, budgeted task*. A vendor cannot successfully claim "the spec was unclear" about something the spec explicitly says is out of scope with a named owner and phase. The renegotiation risk comes from silent gaps, not disclosed ones. CRDB already ran this exact play with Data Contracts and Reference Data this sprint — cut, named, assigned to TOR70 — and nobody is calling that scope a landmine. Applying the identical pattern to the 7 non-priority services and 250 catalog rows is consistency, not corner-cutting.

## Terminology: "data platform" vs "data system"

Not worth a dedicated pass. It's a five-minute find-and-replace during WP10's terminology cross-check, not a workstream. Bundle it into the WP10 consistency sweep that's already scoped to happen; do not spend a discrete day or a discrete meeting on it. Spending deliberation time on this while three CRITICAL gaps sit open on the two priority use cases would be exactly the kind of misallocation this paper argues against.
