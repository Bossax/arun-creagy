---
query: "CRDB Information Product Inventory (TOR 5.3.4) row-level data file — 99 products / 45 agencies"
target: "Arun_Creagy"
mode: smart → deep
timestamp: 2026-09-24 20:46
---

# Trace: CRDB Information Product Inventory (TOR 5.3.4) data file

**Target**: Arun_Creagy (+ OneDrive SharePoint sync)
**Mode**: smart → deep (the Oracle search returned nothing relevant)
**Time**: 2026-09-24 20:46

## Oracle Results
Nothing relevant. The top hits were unrelated CRI England and Soul-Brews learnings.

## Files Found
**The file lives OUTSIDE the repo, in the OneDrive-synced SharePoint library**: `C:\Users\sitth\OneDrive - The Creagy Company Limited\DCCE Climate Risk DataBase - Documents\`

- **Canonical final deliverable:** `04_Deliverable\D4 Final Report\260904_TOR5.3.4_Information Product Inventory.xlsx` (2026-09-04). The `all_datasets` sheet has **114 products**, P001 onward. The 14 columns are product_id, title, notes_th, notes, delivery_format, service_type, owner_org, developer, geo_coverage, use_case, sectors, data_source, source_type, url. Other sheets: introduction, data_dictionary (14), codelist (44), agencies (72).
- **Working versions** are in `03_Working_file\Data catalog\TOR5.3.4_Information Product Inventory\`. Product rows per version:

  | Version | Products | Note |
  |---|---|---|
  | 260416 v1 | 118 | |
  | v2 | 76 | |
  | v3 | 76 | |
  | v5 | 102 | |
  | **v7** | **99** | origin of the "99" figure |
  | v8.1 | 114 | 15 rows added via the `QA_new_rows` sheet |
  | v9.0 | 114 | |
  | v10 | 114 | |

- The same folder also has `Climate Information Product Inventory_V8.pdf`, `260831_DCCE_NCAIF_TOR5.3.4_Booklet_A5.docx` and `Data catalog\TOR5.3.4&5.3.5 Report.docx`.
- **In-repo candidates (not the answer):**
  - `inbox_source/data_product_and_service_2026-2.csv`: 76 filled rows, an earlier version (≈ v2/v3).
  - `data_product_and_service_2025.csv` (120 rows), which is a different schema.
  - `output/03_Data_Product_Inventory/`, which holds only a placeholder README.
  - `output/final_deliverable/2 รายงานสรุป…md`, which is 0 bytes.

## Git History
No product-inventory data file was ever committed, on any branch (757 commits checked).
- The 5.3.4 prose was created in `e0836b2` (2026-06-18, empty), filled in `dee129a` (2026-07-03), renamed in `3dffb4c`, and moved to `draft_final_report/5.3/` in `952afe7` (2026-08-11).
- The deleted `NCAIF_Service_Inventory_v*.csv` files (`9bdd0d4` → `fae56dc`) hold the 8 services, not products.

## GitHub Issues/PRs
None. The repo `Bossax/arun_creagy` has 4 issues, all about CRI, and no PRs.

## Cross-Repo Matches
None in ghq, the other OracleWorkspace repos, or the Desktop. The OneDrive hit is listed above. Downloads also holds `TOR5.3.4&5.3.5 Report.pdf` and `บัญชีรายการผลิตภัณฑ์ข้อมูลและสารสนเทศภูมิอากาศ.pdf`.

## Oracle Memory
- `ψ/memory/traces/2026-08-28/2248_crdb-product-inventory-breakdown.md`: an earlier trace that failed to find the itemized table.
- `ψ/memory/retrospectives/2026-08/21/00.55_wp6-service-alignment-and-inventory-audit.md`: records the 99-vs-76 gap as unresolved.
- `ψ/memory/retrospectives/2026-08/28/11.22_crdb-exec-summary-2.3-isolated-draft-and-review.md`: says the 99 should be treated as an aggregate until an item table exists.
- `output/final_deliverable/Executive Summary Report/แผนการเขียนบทที่ 2…md` L342: the 99 must be confirmed before it is cited.

## Summary
- **Resolved.** The row-level inventory exists only on OneDrive, never in git. That's why every in-repo search, including the 2026-08-28 trace, failed.
- **Count drift.** "99 products / 45 agencies" comes from **v7 (2026-07-09)**. v8.1 (2026-08-31) added 15 QA rows. The delivered inventory (260904) has **114 products** and 56 distinct owner organisations once multi-owner entries are split. Every report text that cites 99 is stale relative to the deliverable: draft 5.3.4, full-report 3.4 and the dissemination deck slide 39.
- **Field count.** The prose says 12 metadata fields; the deliverable has 14 (12 plus notes_th/notes).
- **Next.** §5.1 product matching uses the 260904 file (114 rows). Boss needs to decide whether 3.4 and 5.3.4 are updated to 114. Consider copying the deliverable into the repo (e.g. `output/03_Data_Product_Inventory/`) so future searches find it.
