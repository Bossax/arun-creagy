# Handoff: WP6 service ↔ DRD requirement reconciliation (deferred)

**Date**: 2026-08-14 17:39
**Context**: While scoping WP6 (Use Case & Demand Analysis), Boss and I traced three cases where a D-043/A-BTR service turns out to be the structural basis for specific WP4 DRD (`2026-08-12-WP4-Developer-Ready-Design-Requirements-Specification.md`, D-068) requirements — a connection the DRD itself never made explicit, because WP4 was scoped and written from "what asset covers this page," not "which underlying service produces and maintains this page's data." Boss's direction: **do not chase this now** — finish WP6 first, then come back and systematically reconcile.

## What we found, this session

1. **DEL-12 ("Disaster statistics product," REQ-001/REQ-011) and the DRD's "Loss and Damage product line" (REQ-012/049/050/051)** both draw on the same `DDPM_2_1` source. REQ-001/011 are marked "Ready to build" in the DRD; REQ-012/049/050/051 are explicitly blocked: *"the loss-and-damage work package's own specification hasn't been written yet."* That work package is D-043 Service 4 = **disaster-loss-statistics**, one of WP6's two priority use cases. DEL-12's "ready" status only covers the front-end presentation; the underlying data-engineering pipeline is exactly what a disaster-loss-statistics Functional Spec would define.

2. **A-BTR** is cited as the source for 8 "Ready to build" DRD requirements (REQ-014, 017, 025, 043, 044, 045, 053, 057) via the A-BTR dissection database (a one-time extraction, not a live feed). The DRD doesn't flag these as blocked, because the snapshot exists today — but nothing in the DRD accounts for A-BTR reporting being a recurring UNFCCC cycle. Without the actual A-BTR reporting pipeline (WP6's other priority use case) built and running, this content is frozen to whatever cycle it was extracted from.

3. **D-043 Service 2 ("การวิเคราะห์ความเสี่ยงในระดับพื้นที่ที่มีความละเอียดสูง" / high-resolution area-level risk analysis)** — not one of WP6's two chosen priority use cases, only slated for lightweight NFR-table treatment — turns out to be the single most structurally load-bearing service in the DRD:
   - REQ-008, REQ-014, REQ-015, REQ-027, REQ-035 all cite the same province-level-only resolution ceiling as their blocker.
   - The entire **Appendix B2 investigation** (9 "Product surface" requirements: REQ-004, 005, 009, 010, 013, 015, 028, 041, 070) exists because the composite risk index can't be traced below province level.
   - Three **"Awaiting decision" briefs** are Service 2 broken into sub-workstreams: **E-4** (engineering design values / rainfall IDF curves), **E-5** (synthesizing 77 provincial plans into sub-provincial data), **E-6** (geospatial re-aggregation onto LAO/municipal boundaries).

## Why this matters (not yet acted on)

WP7's plan already calls for "split data-platform vs. web-platform gap scoring" (2026-08-07 addendum) — but doing that well requires exactly this kind of service-to-requirement tracing, done systematically across all of D-043's 8 services (plus A-BTR) against the DRD's 72 requirements, not just the 3 cases surfaced by conversation so far. Right now WP4's DRD accurately records symptoms (blocked/partial, cites a brief, awaiting decision) without naming which WP6-scoped service each symptom's root cause is.

## Deferred task, for a future session

**Do a full service-to-requirement traceability pass**: for each of D-043's 8 services + A-BTR, identify every DRD requirement (of the 72) that structurally depends on that service existing/being specified, not just the ones already surfaced by inline citation. Reconcile against:
- `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-08-12-WP4-Developer-Ready-Design-Requirements-Specification.md` (D-068) and its companion CSVs
- `ψ/incubate/DCCE/CRDB/output/06_Use_Case_Demand_Analysis/บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md` (D-043, the 8-service definitions)
- `ψ/incubate/DCCE/CRDB/output/06_Use_Case_Demand_Analysis/A-BTR_requirement_analysis/` (the A-BTR dissection database)

Likely output shape: a matrix (service × requirement) showing which DRD items are actually downstream of which WP6-scope service — probably feeds WP7 (gap analysis input) and/or WP8 (recommendations/sequencing), not a new standalone WP. Not scoped further than this yet — Boss wants WP6 finished first.

## Next Session

- [ ] Do NOT start this reconciliation pass until WP6 (A-BTR + disaster-loss-statistics Functional Specs, NFR table, layer tagging) is further along or done — Boss's explicit sequencing call this session.
- [ ] When picked back up: decide whether it's a WP6 sub-task, a WP7 input, or its own scoped step before WP8 — not decided yet.
- [ ] Re-derive the three cases above only if useful for grounding; they're fully written out here so they don't need to be re-traced from scratch.

## Key Files (reference only, nothing written yet for this task)

- `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-08-12-WP4-Developer-Ready-Design-Requirements-Specification.md` (D-068)
- `ψ/incubate/DCCE/CRDB/output/06_Use_Case_Demand_Analysis/บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md` (D-043)
- `ψ/incubate/DCCE/CRDB/output/06_Use_Case_Demand_Analysis/A-BTR_requirement_analysis/`
- `plans/2026-08-06-crdb-final-sprint-implementation-plan.md` (WP6/WP7 scope definitions)
