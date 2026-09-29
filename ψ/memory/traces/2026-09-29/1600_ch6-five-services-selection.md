---
query: "why chapter 6 (5.3.9) selects 5 services + data catalog vs the 8 services in 3.3 and top-3 urgent; why services 3,5,6,8 excluded"
target: "Arun_Creagy"
mode: smart (Oracle, then targeted file search)
timestamp: 2026-09-29 16:00
---

# Trace: chapter 6 five-service selection

**Target**: Arun_Creagy
**Mode**: smart, escalated by hand to targeted grep (not the 5-agent deep mode)
**Time**: 2026-09-29 16:00

## Oracle Results
10 hits, none answered the question. Nearest: `ψ/memory/learnings/2026-06-25_crdb-5.3-evidence-first-service-drafting.md` (chain from interviews to workshop to prioritized services to gaps to recommendations). The Oracle index has no note on the 5-service choice.

## Files Found
- `ψ/incubate/DCCE/CRDB/output/2026-05-18_TOR-Review/2026-08-26_TOR70-Director-Toey-briefing-deck-content-TH.md` lines 104-158. **Origin of the 3+2.** Slide 5: existing 3 (spatial climate-risk database, hazard and exposure map, climate risk index CRI) are brought into the platform and governed; new 2 (A-BTR reporting, disaster loss statistics) are specified and built end to end. Speaker note: the 5 are a delivery strategy, not a replacement for CRDB's long-term service group; the remaining services stay in the later roadmap; the contractor rebuilds an existing product only if an approved requirement says it must change.
- `ψ/incubate/DCCE/CRDB/output/08_Recommendations/README.md` names the same 3+2 list (D-053) as the basis for the WP8 roadmap.
- Memory `project_crdb_wp6_use_case_selection.md`: the "3" are DCCE's existing tools; the "2" are the new products CRDB proposed and no one else owns. A-BTR and disaster-loss statistics are the two validated priority products.
- `crdb-full-report-3.3/draft.md` and slide deck slides 35-36: 8 services, top-3 urgent (catalog, loss and damage, spatial risk). No stated selection criteria beyond "assessed and prioritized with stakeholders".
- `2026-06-25_evidence-note_5.3.3_5.3.8_5.3.9.md` lists a demand-clustering document (in `02_UseCases_FunctionalSpecs`) that ranks demand clusters. Not opened.

## Git History
Not searched.

## Summary
The 5 services in chapter 6 come from the TOR70 briefing deck (Aug 2026), not from the 3.3 top-3. The reasoning on file: the 3 existing DCCE products already exist and only need to enter the platform under governance; the 2 new ones (A-BTR, disaster-loss statistics) are the new products with a clear owner need (reporting obligation, evidence for investment). It is framed as a delivery strategy, and the other services stay in the later roadmap.
Not found: any written reason for excluding services 3, 5, 6 and 8 individually, or a bridge between the 3.3 top-3 and the 3+2. Chapter 6 and 3.3 use two different cuts of the same 8.
Next: open demand clustering in `02_UseCases_FunctionalSpecs` for ranking evidence; ask Boss for the reasoning behind the 3+2 if not written down.
