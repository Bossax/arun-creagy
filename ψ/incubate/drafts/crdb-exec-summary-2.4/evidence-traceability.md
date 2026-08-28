# Evidence traceability — Executive Summary Section 2.4

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
| Baseline risk-component counts and shares are 72 Vulnerability (27.7%), 68 Exposure (26.2%), 49 Climate Driver (18.8%), 36 Hazard (13.8%), 11 Loss & Damage (4.2%), 10 Composite Index (3.8%), 5 Risk Metric (1.9%), 4 Response (1.5%), 3 Spatial Unit (1.2%), and 2 Disaster Record (0.8%) | `data_catalog_v4.csv`, column `cdm_sub_domain`; TOR 5.3.5, analysis section | Direct grouping totals 260; percentages use 260 as denominator and are rounded to one decimal. The largest four total 225 records or 86.5%. The figure must include all ten groups. |
| Access conditions are 214 Restricted, 43 Public, and 3 blank | `data_catalog_v4.csv`, column `access_rights_dataset`; TOR 5.3.5, analysis section | Direct grouping verified. The reported 83%/17% split is 214/257 and 43/257 among records with a stated access condition. Do not imply that the three blanks are public or restricted. |
| CSV occurs in 152 baseline records | `data_catalog_v4.csv`, column `data_format`; TOR 5.3.5, analysis section | Count records whose format contains CSV, including multi-format records. Only 129 records have CSV as the sole recorded format. Draft must say CSV appears in 152 records, not that 152 records contain only CSV. |
| Product inventory contains 99 products across 45 owners | TOR 5.3.4, lines 54–65 | This is a reported aggregate. No separate itemized product table was available for direct recounting. Per the approved contract, keep this recounting limitation in the sidecar rather than reader-facing prose. |
| Product geography is Thailand 62, global 31, regional 6 | TOR 5.3.4, line 56 | The counts total 99. Use the Thai audience-facing categories rather than database codes. |
| Product delivery formats are web 92, mobile application 5, and API 2 | TOR 5.3.4, line 56 | The counts total 99. API is retained as a technical acronym. |
| Fifty-eight products are cross-sectoral | TOR 5.3.4, line 61 | Use as a characteristic of the inventory, not as a gap-analysis conclusion. |
| The Information Product Inventory is positioned alongside the Baseline Data Inventory and the service/product study in the overall result structure | Dissemination slide deck, lines 97–104 | Use only for the role of the inventory in the study. Never cite slide numbers or internal locators in prose. |
| Product-type shares are Risk Assessment 32%, Observation Data 30%, Climate Systems 22%, Impact Analytics 18%, Decision Support Platforms 15%, and Sectoral Climate Services 13% | Dissemination slide deck, Slide 39 | The categories overlap, as shown by their total exceeding 100%. State that a product may belong to more than one category; use the percentages to compare prevalence, not as mutually exclusive shares. |
| Dashboards and GIS tools are the main content forms; climate-data access and risk assessment are the principal use cases | TOR 5.3.4, line 56 | Qualitative ranking only. The source provides no exact counts for these statements, so the draft must not invent them. |
| Slide 39 also states 39 core products from 13 organizations and 80% associated with six main agencies | Dissemination slide deck, Slide 39 | Excluded from reader-facing prose because the definition of the core subset and the denominator of the 80% statement are not sufficiently clear. |

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

- Sections 2.2 and 2.3 already explain evidence gathering and the eight services. Section 2.4 should contain only inventory results and characteristics.
- Domain imbalance may be described as an observed characteristic only. Gap analysis and recommendations belong to a later chapter.
- Product-type percentages from Slide 39 are overlapping classifications and must not be presented as mutually exclusive shares.
- Do not include the baseline sector breakdown; Boss clarified that the requested breakdown is by data domain.
- Internal file paths, slide numbers, database field names, and calculation commands must remain in this sidecar.
