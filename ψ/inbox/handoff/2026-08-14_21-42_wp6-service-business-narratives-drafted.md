# Handoff: WP6 service business narratives drafted, awaiting Boss review

**Date**: 2026-08-14 21:42
**Context**: Session moved from WP4 (sealed) into WP6. Boss course-corrected the approach twice — first away from an NFR-first attempt, then away from a project-internal writing voice — landing on a business-case document covering all 9 services. Boss's closing word: "I will come back with the review."

## What We Did

- **Started WP6 after confirming WP4/WP5 were fully sealed** (`2671039`, `acf8f72`, `089af83` — the prior handoff's "uncommitted work" caveat was already resolved).
- **Corrected an early mis-scope**: initially traced WP7 (Gap Analysis) as the next work package before Boss clarified the intent was WP6. WP7 remains unstarted, 0% — its own README is still just a placeholder.
- **Discovered three service→website dependencies WP4's DRD never made explicit** — traced live with Boss:
  1. **DEL-12** (disaster statistics product, REQ-001/011) and the DRD's blocked "Loss and Damage product line" (REQ-012/049/050/051) share the same `DDPM_2_1` source. DEL-12's "ready to build" status only covers presentation; the data-engineering half is what a disaster-loss-statistics spec would define.
  2. **A-BTR** is cited as the source for 8 "Ready to build" requirements (REQ-014, 017, 025, 043, 044, 045, 053, 057) via a one-time dissection snapshot — nothing accounts for BTR being a recurring UNFCCC cycle, so that content is frozen without the live pipeline.
  3. **D-043 Service 2** (high-resolution area risk) is the most structurally load-bearing service in the whole DRD — 9 "product surface" requirements + the entire Appendix B2 investigation + Briefs E-4/E-5/E-6 are all downstream of it — yet it was only slated for lightweight NFR treatment.
  These are captured in a **separate deferred-task handoff**: `ψ/inbox/handoff/2026-08-14_17-39_wp6-service-to-drd-requirement-reconciliation-deferred.md`. Boss's call: don't chase the full reconciliation now, finish WP6 first.
- **First WP6 attempt (NFR thresholds table) was rejected by Boss as too shallow** — built from abstract NFR categories rather than stakeholder demand, and mis-assigned Service 2's ownership to a single CDM domain when it's a cross-domain risk-analytic product owned by DCCE's risk data development subdivision. File kept on disk, not deleted: `2026-08-14-WP6-Business-NFR-Thresholds-Table.md`.
- **Found Boss's own pre-existing writing directive** for exactly this task: `inbox_note/service_package_in_5.3.3.md` — ground in the v6 doc first (why the service exists, which stakeholder use cases it serves, convincingly), then bring in the Enrichment Roadmap as *suggestion* not requirement, 3–4 paragraphs per service.
- **Ran 3 parallel research agents** which surfaced material not previously in play: DCCE's real org chart (`CDM_EARCatalog/DCCE Data Value Chain.md`), a full pre-existing Service 8 dossier (`Pillar_02_Service_08_Uncertainty_Governance_TH.md`), named-institution interview notes (Thai Bankers Association, FTI, กรมโยธาธิการและผังเมือง), and the existing DITTO-built M&E platform plus its internal critique (`inbox_source/DCCE-MandE-platform-2025*.md`).
- **Drafted `2026-08-14-WP6-Service-Business-Narratives.md`** — 9 sections (Services 1–8 + the BTR pipeline), 4 paragraphs each, no ownership attribution (Boss assigning that separately), stale `archive/2026-06-05_stale_pillar2/` lineage skipped entirely per Boss's call.
- **Verified format against BA standards** (trace → brave-search; Perplexity not needed): confirmed the document matches business-case/business-narrative shape (context → current state → problem → future state, persuasive narrative prose). Confirmed it is *not* user-story format ("As a / I want / so that" + Given/When/Then). Boss confirmed: **business case is enough, no user-story layer needed.**
- **Completeness pass against all stakeholder material gathered** — found and fixed 8 gaps: REQ-069's catalog caveat (S1), the money-only-not-capability pattern across the finance cluster (S3), the shared acceptance-test rubric (S4), the composite-index non-reuse warning (S5), the impact-chain diagram as insufficient adjacent content (S6), the base v6 use cases that had been dropped in favor of the richer dossier (S8), and two BTR items (the source material's own honest limitation, plus the 379-requirement→19-node sitemap mapping).
- **Full rewrite for voice** after Boss's final note: stripped every internal code (REQ/DEL/Brief/DOM IDs), internal artifact name (DRD, Enrichment Roadmap, D-043, WP labels), and evolutionary framing ("WP4 found...", "this session flagged..."). Technical shorthand plain-languaged throughout (STAC/ISO → "international metadata conventions", TPMAP → "existing national poverty data", CMIP6 → "global climate projections", PDPA → "a privacy review"). Final section retitled from "A-BTR" to "Thailand's Biennial Transparency Report Pipeline".

## Pending

- [ ] **Boss is reviewing the narratives document** — "I will come back with the review." Nothing further on WP6 should advance until that lands. Do NOT `/seal`.
- [ ] **Ownership attribution is Boss's own task** — deliberately absent from every section. Do not add it unprompted.
- [ ] **The NFR thresholds table is parked, not dead** — it was rejected for being derived from categories rather than demand. Once the narratives are settled, NFRs can be re-derived properly from them.
- [ ] **The service→requirement reconciliation pass is formally deferred** — see the 17:39 handoff. Not to be started until WP6 is further along.
- [ ] **WP7 (Gap Analysis) is 0% started** — placeholder README only. Its plan calls for DATER dimensions 1–6, scored data-platform vs. web-platform separately.
- [ ] **The presentation restart** (Phase 2 style discovery) is still outstanding across multiple sessions. Untouched again.

## Next Session

- [ ] Pick up wherever Boss's review lands — likely edits to the narratives' framing, service-level detail, or which findings belong in the closing paragraphs.
- [ ] If the review clears the document, the natural next steps within WP6 are the two full Functional Specs (disaster-loss-statistics and the BTR pipeline) plus re-deriving NFRs from the settled narratives — but confirm sequencing with Boss rather than assuming.
- [ ] Keep the Service 2 lesson in mind for anything downstream: a risk analytic product spans hazard + exposure/vulnerability + impact together, not one domain slice.

## Key Files

**Written this session:**
- `ψ/incubate/DCCE/CRDB/output/06_Use_Case_Demand_Analysis/2026-08-14-WP6-Service-Business-Narratives.md` — the deliverable awaiting review
- `ψ/incubate/DCCE/CRDB/output/06_Use_Case_Demand_Analysis/2026-08-14-WP6-Business-NFR-Thresholds-Table.md` — rejected first attempt, kept as record
- `ψ/inbox/handoff/2026-08-14_17-39_wp6-service-to-drd-requirement-reconciliation-deferred.md` — the deferred reconciliation task

**Load-bearing sources for any further WP6 work:**
- `output/06_Use_Case_Demand_Analysis/บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md` — the 8 service definitions
- `output/06_Use_Case_Demand_Analysis/2026-06-15_NCAIF-Service-Enrichment-Roadmap.md` — enriched dossiers + Service 4's methodology sketch
- `output/06_Use_Case_Demand_Analysis/Pillar_02_Service_08_Uncertainty_Governance_TH.md` — the standalone Service 8 dossier
- `inbox_note/service_package_in_5.3.3.md` — Boss's own writing directive for this document
- `inbox_note/Interview Note - Thailand Bank Association.md`, `archive/Interview questions/detail info/สภาอุตสาหกรรมแห่งประเทศไทย.md`, `archive/Interview questions/detail info/กรมโยธาธิการและผังเมือง.md` — named-stakeholder evidence
- `inbox_source/DCCE-MandE-platform-2025.md` + `-criticism-1.md` — the existing DITTO platform and its critique
- `output/05_Data_Management_Framework/CDM_EARCatalog/DCCE Data Value Chain.md` — DCCE's real org chart (for Boss's ownership pass)

**Plan file from this session**: `C:\Users\sitth\.claude\plans\wiggly-conjuring-raven.md`
