# Evidence traceability — Executive Summary Section 2.3

This file is an internal evidence sidecar. Paths, line locators, calculation notes, and source limitations recorded here must not be copied into audience-facing prose.

## Source restriction confirmed by Boss

Claims about the Information Product Inventory may use only:

1. `ψ/incubate/DCCE/CRDB/output/draft_final_report/5.3/5.3.4 จัดทำบัญชีรายการผลิตภัณฑ์ข้อมูลและสารสนเทศ (Information Product Inventory).md`
2. `ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/Slide-deck-CRDB-26th-final-dissemination-event.md`

No other source may support Information Product Inventory facts in this section.

## Claim-to-source map

| Claim used in draft | Source and locator | Verification and permitted interpretation |
|---|---|---|
| The two inventories represent different asset types | Chapter 2 writing plan, lines 210–234; Section 2.1 approved draft | Use only as a compact distinction. Do not repeat Section 2.1's full scoping logic. |
| Baseline inventory contains 260 records with 260 unique dataset IDs from 44 owners | `data_catalog_v4.csv`; direct `Import-Csv` count and grouping | Verified directly from the current CSV. SHA-256: `09F74A4D05EC24EA28EE208FD4C50B61DE11B5A310EE5D1DF19101A086962C84`. |
| All 260 baseline records are `Baseline-Draft` and `Unverified-Baseline` | `data_catalog_v4.csv`, columns `endorsement_status` and `validation_flag` | Direct grouping returns 260 records in each stated category. Describe this as a preliminary baseline, not an endorsed national registry. |
| Baseline risk-component counts are 72 Vulnerability, 68 Exposure, 49 Climate Driver, 36 Hazard, 11 Loss & Damage, 10 Composite Index, 5 Risk Metric, 4 Response, 3 Spatial Unit, and 2 Disaster Record | `data_catalog_v4.csv`, column `cdm_sub_domain`; TOR 5.3.5, analysis section | Direct grouping totals 260. Draft prose may foreground the largest and smallest categories; the figure must include all ten so the chart total remains 260. |
| Access conditions are 214 Restricted, 43 Public, and 3 blank | `data_catalog_v4.csv`, column `access_rights_dataset`; TOR 5.3.5, analysis section | Direct grouping verified. The reported 83%/17% split is 214/257 and 43/257 among records with a stated access condition. Do not imply that the three blanks are public or restricted. |
| CSV occurs in 152 baseline records | `data_catalog_v4.csv`, column `data_format`; TOR 5.3.5, analysis section | Count records whose format contains CSV, including multi-format records. Only 129 records have CSV as the sole recorded format. Draft must say CSV appears in 152 records, not that 152 records contain only CSV. |
| Product inventory contains 99 products across 45 owners | TOR 5.3.4, lines 54–65 | This is a reported aggregate. No separate itemized product table was available for direct recounting. State that limitation in reader-facing prose. |
| Product geography is Thailand 62, global 31, regional 6 | TOR 5.3.4, line 56 | The counts total 99. Use the Thai audience-facing categories rather than database codes. |
| Product delivery formats are web 92, mobile application 5, and API 2 | TOR 5.3.4, line 56 | The counts total 99. API is retained as a technical acronym. |
| Fifty-eight products are cross-sectoral | TOR 5.3.4, line 61 | Use as a characteristic of the inventory, not as a gap-analysis conclusion. |
| The Information Product Inventory is positioned alongside the Baseline Data Inventory and the service/product study in the overall result structure | Dissemination slide deck, lines 97–104 | Use only for the role of the inventory in the study. Never cite slide numbers or internal locators in prose. |
| More than 40 use cases were synthesized into eight information services | Dissemination slide deck, lines 1195–1256; Service Intelligence Report, lines 10–15 and service headings | This is a service-synthesis claim, not a product-inventory statistic. |
| Three services were presented as high priority: catalog, historical loss and damage, and high-resolution spatial risk analytics | Dissemination slide deck, lines 1261–1270 | Describe this as the high-priority group in the dissemination material. Do not say that all three were selected for detailed specification. |
| Later detailed-development selection focused on Historical Loss & Damage and the national reporting pipeline supporting Adaptation M&E | Service Business Narratives, lines 1–7 | Preserve the distinction between a high-priority shortlist and the narrower detailed-specification selection. |
| Climate Design Parameters was explicitly deferred because locally calibrated design parameters and curves were unavailable and cross-disciplinary partnership was required | Service Business Narratives, lines 92–107 | Do not imply that the service is ready to build or that existing climate projections alone solve the design-method problem. |

## Calculation record for baseline inventory

| Field | Result |
|---|---:|
| Data rows | 260 |
| Unique `dataset_id` | 260 |
| Unique nonblank `owner_org` | 44 |
| Restricted | 214 |
| Public | 43 |
| Access condition blank | 3 |
| Records whose format contains CSV | 152 |
| `Baseline-Draft` | 260 |
| `Unverified-Baseline` | 260 |

## Editorial cautions

- Section 2.2 already explains the survey and synthesis process. Section 2.3 should foreground results and characteristics rather than repeat the process.
- Domain imbalance may be described as an observed characteristic only. Gap analysis and recommendations belong to a later chapter.
- The eight services are proposed information-service concepts, not eight operating systems.
- The high-priority group and the later detailed-development selection are different classifications from different project artifacts.
- Internal file paths, slide numbers, database field names, and calculation commands must remain in this sidecar.

