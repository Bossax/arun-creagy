# CRDB Execution Architecture Index (Canonical)

## Purpose

Canonical navigation entrypoint for CRDB execution artifacts, reflecting the **new 9-item DCCE deliverable folder structure** (physically restructured 2026-08-06, WP0 of the final sprint).

Supersedes: [`CRDB-Workstreams-Index.md`](../archive/CRDB-Workstreams-Index.md) (via the prior version of this file, D-022)

**Last updated:** 2026-08-06. Folders were physically moved via `git mv` to match the 9-item DCCE list (Item 1 = new Business Objective / Platform Rationale). Per Boss's call, most cross-references elsewhere in the project (Deliverable Map rows, other ledgers, older research notes) still point to the **old pillar paths** and have not been updated yet — that full relink pass is deferred to WP10 (Final Packaging). This index and the Deliverable Map's top note are the only two updated immediately.

## 1) Item folders (new canonical structure)

| Folder | Item | Was (old pillar path) |
|---|---|---|
| `00_Strategy_Reports/` | (not a DCCE item — internal strategy/decision trail) | unchanged |
| `01_Business_Objective_Platform_Rationale/` | Item 1 (new) | new — empty, pending WP1 |
| `02_Data_Inventory/` | Item 2 | was `03_DataInventory_DQ/` |
| `03_Data_Product_Inventory/` | Item 3 (new) | new — empty, pending WP3 |
| `04_Sitemap/` | Item 4 | was `01_Sitemap_InterfaceMapping/` |
| `05_Data_Management_Framework/Glossary/` | Item 5 (sub) | was `04_Glossary/` |
| `05_Data_Management_Framework/CDM_EARCatalog/` | Item 5 (sub) | was `05_CDM_EARCatalog/` |
| `05_Data_Management_Framework/Governance_RACI/` | Item 5 (sub) | was `07_Governance_RACI/` |
| `05_Data_Management_Framework/RefData_Matrix/` | Item 5 (sub) | was `08_RefData_Matrix/` |
| `06_Use_Case_Demand_Analysis/` | Item 6 | was `02_UseCases_FunctionalSpecs/`; now also contains `A-BTR_requirement_analysis/` as a subfolder (was at output root) |
| `07_Gap_Analysis/` | Item 7 (new) | new — empty, pending WP7 |
| `08_Recommendations/` | Item 8 (new) | new — empty, pending WP8 |
| `09_LDM_LossDamage_DataModel/` | Item 9 | was `06_LDM_LossDamage_DataModel/` |


Canonical content within each (unchanged from before the move, just relocated):
- Item 2: `data_catalog_v3.csv` (D-037, 260 datasets)
- Item 4: `NCAIF_Detailed_Sitemap_v8.md` (D-050)
- Item 5/CDM_EARCatalog: `Pillar_05_CDM_EARCatalog_Deliverable.md` (D-036, narrative) + `Domains-v3.csv`, `Entities-v3.csv`, `Relationships-v4.csv` (D-051, data). `Conceptual Data Model for climate risk and adaptation data system.md` (D-010) is superseded — see marker in that file.
- Item 5/RefData_Matrix: spec only — see `DECISION-2026-08-06-Reference-Data-Deferred-to-TOR70.md`
- Item 6: `บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md` (D-043, 8 services) + `A-BTR_requirement_analysis/`
- Item 9: most mature pillar; currently has no Deliverable Map entry — pending WP9

## 2) Submission staging

- `final_report/` — assembled deliverable, organized by TOR clause number (5.2, 5.3, 5.4, 5.5 + appendices). This is the DCCE-facing package shape.
- `2026-05-18_TOR-Review/` — TOR70 briefing deck + architecture analysis (D-053–D-055), feeds Item 8 (Recommendations).

## 3) Archive (not touched further this sprint)

- `archive/interim-report/` — superseded by `final_report/` (moved 2026-08-06)
- `archive/Interview summary notes/` — frozen since 2026-03-23 (moved 2026-08-06)
- `00_Drafts_Archive/` — scratch/superseded drafts bucket (left at root, already archive-named)
- `consultation_workshop/mvp/code/` — contains a Python venv, gitignored (`venv/`, `venv_clean/`), not tracked in git; left in place per Boss's call

## 4) PM ledgers

- Deliverables: [`CRDB-Deliverable-Map.md`](../CRDB-Deliverable-Map.md)
- Triggers: [`CRDB-Trigger-Log.md`](../CRDB-Trigger-Log.md)
- Changes: [`CRDB-Change-Log.md`](../CRDB-Change-Log.md)
- Evidence: [`CRDB-Evidence-Registry.md`](../CRDB-Evidence-Registry.md)

**Note:** the 4 ledgers above still reference the *old* pillar paths in their row-level links (e.g. `output/05_CDM_EARCatalog/...`). Use this index's table to translate old path → new path until WP10's relink pass runs.

## 5) Current sprint plan

- [`plans/2026-08-06-crdb-final-sprint-implementation-plan.md`](../../../../../plans/2026-08-06-crdb-final-sprint-implementation-plan.md) — 12 work packages (WP0–WP11) covering the remaining two weeks
