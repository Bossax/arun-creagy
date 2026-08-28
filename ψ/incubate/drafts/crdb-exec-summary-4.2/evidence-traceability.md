# Evidence traceability — 4.2 (Executive Summary)

| Claim in draft | Source |
|---|---|
| Reference Integrated Data and Web Platform SDLC (6 stages), synthesized from TOGAF/IBM/Australian National Archives/BrowserStack | `2026-05-18_TOR-Review/2026-08-26_TOR70-SDLC-storyline-for-DCCE-briefing.md` §"Reference development lifecycle for TOR70" |
| Stage 1 coverage 35% → 70% with CRDB adopted; Stage 2 coverage 40% → 80% with CRDB adopted | Same source, §"Coverage re-scored with CRDB adopted as baseline" table |
| Sitemap v9: 38 nodes, 6 top-level categories | `04_Sitemap/NCAIF_Detailed_Sitemap_v9.md` (headers `## 0.`–`## 5.`); `04_Sitemap/ncaif_sitemap_nodes.csv` (38 data rows; 6 hierarchy_level=1 rows) — corrects the master plan's earlier "4 categories" error, confirmed against both files |
| DRD v2: 75 requirements, 13 deliverables, 9 service briefs, 12 data specs | `04_Sitemap/2026-08-20-WP4-Developer-Ready-Design-Requirements-Specification-v2.md` |
| Storyboard v2 covers all nodes with UI components | `04_Sitemap/2026-08-20-WP4-Node-Content-Storyboard-and-Synthesis-Guide-v2.md` |
| CDM/DMF: 8 domains, 12-field metadata standard, 74-term glossary | `05_Data_Management_Framework/WP5-Data-Management-Framework-Report.md` |
| Content Writer closes 33 gap + 26 partial (59 total) requirements per Storyboard | Chapter-4 plan §4.1.1 (content gap analysis), cross-referenced to Storyboard v2 |
| Software Developer builds CMS validation, pipelines, UI per DRD v2 | Chapter-4 plan §4.2.4 |
| TOR70 sequencing risk: content/data curation (§5.3) locked before design (§5.4) that should govern it; pass-only review gates with no rework allowance | `2026-08-26_TOR70-SDLC-storyline-for-DCCE-briefing.md` §"Analysis" and §"Where TOR70 departs from standard practice" |
| Recommendation for ≥2 build iterations with mid-contract Beta/UAT milestone | `2026-08-26_TOR70-high-ambition-agile-delivery-note.md` |

## Notes for reviewer
- Per contract exclusions, the full 5-table DRD relational schema, the complete 38-page storyboard, and the TOR70-Analysis's own per-activity scoring methodology (1/0.5/0 per activity) are deliberately not detailed here.
- The 70%/80% coverage figures are the TOR70 Analysis document's own scoring against its stated reference-stage constituent activities (see that document's "How these figures were derived" note) — not an externally audited metric. Disclosed here for the reviewer's awareness; the writing contract explicitly approved using them as headline figures.
- This section corrects two errors carried in earlier chapter-4 plan drafts: (1) "DSDLC 7 phases, CRDB = phases 1–3" replaced with the Reference SDLC's 6 stages, CRDB = Stage 1–2; (2) Sitemap v9's category count corrected from 4 to 6. Both corrections were applied to the master plan file in this session before this draft was written.
