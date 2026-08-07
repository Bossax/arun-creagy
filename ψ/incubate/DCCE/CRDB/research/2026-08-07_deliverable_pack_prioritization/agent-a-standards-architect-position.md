# Position Paper: Close the Handoff Gaps Now — Don't Ship Ambiguity to TOR70

**Persona:** DAMA-DMBOK / IIBA-BABOK-credentialed Enterprise Data Architect
**Date:** 2026-08-07 | **Context:** CRDB final sprint, ~7 days remaining before TOR70 handoff

## Stance

CRDB's job is not to write a report DCCE finds satisfying — it is to hand a fixed-price vendor a specification precise enough that TOR70 cannot later say "the spec didn't say" and reprice mid-build. Every hour spent polishing narrative material this week that isn't contractually load-bearing is an hour DCCE will pay for twice: once now, in analyst time, and again later, in a change-order negotiation with TOR70 holding the leverage. The three CRITICAL gaps — STM matrix, data-specific acceptance criteria, and the Assumption Log / Client Dependency Register — are the entire ballgame. They should consume the majority of the remaining 7 days, full stop.

## The Deliverable Pack

**WP2 (Data Inventory) — extend, don't just re-score.** Beyond the 9-field profile for the top-10 assets, each of those 10 gets a **field-level STM row-set**: Source Table/Field → Target CDM Entity/Attribute → Transformation Expression → Nullability Rule → Integration Frequency. This is Critical Gap #1, and WP2 is where the field inventory already lives — it's the natural host, not a new WP.

**WP3 (Data Product Inventory) — add a compliance-classification-to-acceptance-criteria bridge.** For each of the 10 assets, attach a short **Data-Specific Acceptance Criteria table**: row-count reconciliation formula, null-handling fallback rule, format verification (datetime, EPSG:4326, numeric precision). This is a compressed version of Gap #2, scoped to the asset level rather than the use-case level.

**WP5 (Data Management Framework) — the Governance RACI gets formalized as a table**, not prose, closing the "recommended" gap. Glossary and CDM conflict resolution proceed as planned; Reference Data stays deferred (already correctly scoped out).

**WP6(b) (Functional Specs, A-BTR + disaster-loss-statistics) — this is where Gap #2 fully lands.** Each use case gets: full Functional Spec (as already planned) **plus** its own Acceptance Criteria table (Definition of Done: unit test coverage, latency verification, metadata registry update) **plus** a use-case-scoped Assumption Log entry. Do not let WP6(b) ship as "Functional Spec + NFR enrichment only" — that's the single highest-leverage insertion point for developer-testable checks, because it's the artifact TOR70's engineers will open first.

**WP6(a) (NFR thresholds, 9 services) — keep, but bind to personas.** Turn the prose NFR statements into the persona-bound NFR/latency matrix (the other "recommended" gap). Low cost, high credibility payoff, same document.

**New standalone artifact: Assumption Log / Client Dependency Register (Gap #3).** This is not a WP6(b) footnote alone — it needs a project-level register that also captures platform-wide client obligations (AD, network, upstream agency API availability) that don't belong to any single use case. House it in WP10 as an explicit cross-cutting appendix, populated with entries fed from WP6(b) and WP2/WP3 as they surface dependencies.

**WP7 (Gap Analysis)** proceeds as scoped — dims 1–6 only, no expansion. It's already correctly bounded.

**WP9 (LDM)** — add the missing deliverable record and glossary link; this is quick and already flagged as needed. Keep it.

**WP10 (Final Packaging)** — becomes the seam where the Assumption Log lives, and where terminology gets enforced (see below).

## What Gets Cut or Compressed

To fund this, three things give: **WP11's executive deck drops from a full narrative deck to a 6-8 slide summary** — DCCE leadership needs the headline roadmap and budget ask, not a slide-by-slide replay of WP1–9. **WP4 (Sitemap)** stays check-only as scoped — no gold-plating an already-satisfied artifact. **WP8's Recommendations** stays a roadmap + budget note, explicitly punting Data Contracts and full Reference Data build to TOR70/next-phase — do not let anyone scope-creep WP8 into drafting those now; naming them as next-phase work *is* the deliverable.

## Rebutting the Pragmatic-Incrementalist Objection

The expected counter is: DCCE can't review this much technical density in 7 days, so building STM matrices and acceptance criteria nobody will ratify is wasted motion. This gets the audience backwards. The primary reader of the STM matrix and acceptance-criteria tables is not a DCCE reviewer — it's a TOR70 engineer during build, and a TOR70 contracts manager during a dispute. DCCE's role in these artifacts is sign-off on scope and boundaries (does the Assumption Log correctly place the AD/network burden on DCCE, yes or no?), not line-by-line technical validation of every transformation expression. That sign-off is a bounded, fast review — hours, not days — precisely because the artifacts are structured as tables, not prose. The incrementalist's error is treating "DCCE can't deeply review it" as equivalent to "DCCE doesn't need it to exist." A fixed-price vendor doesn't need the client to have pre-validated every cell; it needs the client to have committed to a spec it can be held to. Undocumented ambiguity, not unreviewed detail, is the actual risk being managed here.

## Terminology: Fix It, But It Rides With WP1, Not the Critical Path

"Data platform" vs. "data system" should be corrected — Item 1 is where it propagates from, and a rewritten Business Objective document accurately using "data platform" as it's re-touched during WP10 packaging costs near-zero incremental time (it's a find-and-standardize pass, not new drafting). But it is explicitly lower priority than the three critical gaps: if the 7 days run short, terminology cleanup is the item that slips to "best effort during final QA," not the STM matrix or the Assumption Log. Precision of vocabulary helps credibility; precision of contractual boundary prevents litigation. Spend the scarce days on the latter.
