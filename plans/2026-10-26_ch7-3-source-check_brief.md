# [DELIVERABLE BRIEF] 2026-10-26_ch7-3-source-check

**From**: arun  
**To**: samart  
**Date**: 2026-10-26 17:35 +07:00  
**Topic**: Section 7.3 source checks before draft  
**Reference Inbound Ticket**: `2026-10-26_ch7-3-source-check` (`ψ/inbox/2026-10-26_10-27_local-keth_local-keth-oracle-ticket-2026-10-26_ch7-3-source.md`)  
**Status**: Authoritative Resolution & Grounding Complete  

---

## Executive Summary

This deliverable provides authoritative source citations, technical reconciliations, and drafting guidance for the three source-check items raised prior to drafting Section 7.3 (*ข้อมูลเสนอแนะเชิงเทคนิค - Technical Recommendations*):

1. **The Count "147" A-BTR Metrics**: The count of 147 does **not** represent an official UNFCCC treaty-mandated indicator list. Rather, it represents the **147 structured quantitative metrics (`quantitative_value` records)** extracted by the CRDB project from draft BTR chapters (`260527_UNDP_BTR2_second_interim_report.md`) across Paris Agreement Article 13 adaptation reporting dimensions. In Section 7.3 prose, phrase these as *"ข้อมูลบ่งชี้และค่าชี้วัดเชิงปริมาณด้านการปรับตัว 147 ค่า (Project-extracted Quantitative Reporting Metrics)"* to avoid misleading readers that UNFCCC defines 147 rigid indicators.
2. **The 12 Mandatory Metadata Fields**: The discrepancy between Pillar 3's 8 container minima and the briefing deck's 12 mandatory attributes is an intentional architectural layer distinction. Pillar 3 Section 1.2 Gate G2 defined 8 baseline *container* fields, but when integrated with Gates G1 (access/classification), G3 (analytical authority/endorsement), G4 (canonical boundary/CDM link), and G5 (validation flag/quality maturity), it forms the **12 core mandatory technical headers** codified in `data_dictionary.csv`, `data_catalog_v4.csv`, and `plans/chapter6/english_outline.md`. Both are authoritative at their respective architectural layers.
3. **CDM Model Domains (ERD vs. Drafting Plan Line 111)**: The engineering Entity-Relationship Diagram (`cdm_mermaid_erd.md`) is the **authoritative architectural blueprint** containing the 8 formal technical domains (`DOM_EV`, `DOM_HAZ`, `DOM_022`, `DOM_023`, `DOM_024`, `DOM_030`, `DOM_040`, `DOM_050`). The labels in `plans/chapter7_3/drafting_plan.md` line 111 and `plans/chapter6/english_outline.md` line 89 represent high-level policy/narrative groupings. The actual ERD architecture governs the technical specification in Section 7.3.2.

---

## Detailed Findings & Authoritative Source Resolving

### 1. Count 147: A-BTR Quantitative Reporting Metrics Provenance

#### Authoritative Sources
- **Database & Report**: `ψ/incubate/DCCE/CRDB/output/06_Use_Case_Demand_Analysis/A-BTR_requirement_analysis/a_btr_dissection_database_report.md` (Table 3.1, Line 75; Data Dictionary Section 3.2, Lines 136–148).
- **Relational Table**: `ψ/incubate/DCCE/CRDB/output/A-BTR_requirement_analysis/quantitative_value.csv` (Exactly 147 rows).
- **SQLite Database**: `ψ/incubate/DCCE/CRDB/output/A-BTR_requirement_analysis/a_btr_dissection.db` (Table `quantitative_value`).
- **Source Document Parsed**: `ψ/incubate/DCCE/CRDB/output/A-BTR_requirement_analysis/260527_UNDP_BTR2_second_interim_report.md` (UNDP BTR2 2nd Interim Report).

#### Analysis & Clarification
- In the CRDB requirement analysis, the project decomposed the BTR draft report into 6 Task Groups (A–F), yielding:
  - 133 thematic areas (`theme`),
  - 379 atomic evidence baselines (`evidence_unit`),
  - 379 prescriptive reporting rules (`requirement_statement`),
  - **147 structured numeric metrics (`quantitative_value`)**.
- Each of these 147 rows captures specific climate indicators extracted from evidence units (e.g., `projected_mean_temperature_increase`, `rainfall_anomaly_percentage`, `extreme_flood_affected_provinces`, and economic damage figures) with exact fields: `metric_name`, `value_numeric`, `unit`, `comparison_operator`, `time_period`, `geography`, and `scenario_label`.
- **Conclusion**: These are **project-extracted reporting metrics / information requirements** for the national adaptation platform to service BTR reporting, **not** an official list of 147 fixed UNFCCC treaty indicators.

---

### 2. Final Approved List of 12 Mandatory Metadata Fields

#### Authoritative Sources
- **Normative Specification**: `ψ/incubate/DCCE/CRDB/output/02_Data_Inventory/Pillar_03_DataInventory_DQ_Technical_Specification.md` (Lines 36–53, Gates G1–G5).
- **Schema Data Dictionary**: `ψ/incubate/DCCE/CRDB/output/02_Data_Inventory/data_dictionary.csv` (All fields marked `required = TRUE`).
- **Active Production Catalog**: `ψ/incubate/DCCE/CRDB/output/02_Data_Inventory/data_catalog_v4.csv`.
- **Approved Chapter Outlines**: `plans/chapter6/english_outline.md` (Lines 75–87); `plans/chapter7_3/drafting_plan.md` (Line 114).

#### Reconciliation: 8 Gate G2 Minima vs. 12 Catalog Headers
Pillar 3 Section 1.2 explicitly separates container minima from the full multi-gate acceptance structure:
- **Pillar 3 Gate G2** defines the 8 *container catalog minima*: `Asset_Name`, `Description`, `Steward`, `Source`, `Spatial_Unit`, `Update_Cadence`, `Classification`, and `Limitations_Statement`.
- When an asset traverses all five quality gates (G1 through G5), the full operational dataset metadata requires 12 mandatory attributes aligned with ISO 19115 and DGA standards.

#### The Approved 12 Mandatory Attributes
| # | Standard Field Name (EN) | Thai Technical Label | Primary Data Standard | Gate Alignment | Active Column in `data_catalog_v4.csv` |
|---|---------------------------|----------------------|-----------------------|----------------|-----------------------------------------|
| 1 | `dataset_id` | รหัสชุดข้อมูล | DCCE / NonDGA | Container ID | `dataset_id` |
| 2 | `title` | ชื่อชุดข้อมูล | DGA / ISO 19115 | G2 (Asset_Name) | `title` |
| 3 | `owner_org` / `data_source` | หน่วยงานเจ้าของข้อมูล / แหล่งกำเนิด | DGA / ISO 19115 | G2 (Steward / Source) | `owner_org`, `data_source` |
| 4 | `maintainer` / `maintainer_email` | ผู้ดูแลชุดข้อมูลและช่องทางติดต่อ | DGA | G2 (Steward Contact) | `maintainer`, `maintainer_email` |
| 5 | `geo_coverage` | ขอบเขตพื้นที่ (Spatial Bounding) | DGA / ISO 19115 | G2 / G4 (Spatial_Unit) | `geo_coverage` |
| 6 | `spatial_resolution` | ความละเอียดเชิงพื้นที่ | DGA / ISO 19115 | G2 (Spatial_Unit) | `spatial_resolution` |
| 7 | `temporal_resolution` / `time_period` | ความละเอียดเชิงเวลาและช่วงเวลา | NonDGA / DGA | G2 / G5 (Time Period) | `time_period_start/end`, `temporal_resolution` |
| 8 | `update_frequency_interval` | รอบความถี่การปรับปรุง | DGA / ISO 19115 | G2 (Update_Cadence) | `update_frequency_interval` |
| 9 | `access_rights_dataset` / `license_id` | เงื่อนไขและสิทธิ์การเข้าถึง | DGA / NonDGA | G1 (Classification / Rail) | `access_rights_dataset`, `license_id` |
| 10| `data_format` | รูปแบบไฟล์และมาตรฐานการจัดเก็บ | DGA / W3C | Container Format | `data_format` |
| 11| `validation_flag` / `endorsement_status`| สถานะการรับรองและระดับคุณภาพ | DCCE / NonDGA | G3 (Endorsement) / G5 (Validation) | `endorsement_status`, `validation_flag` |
| 12| `cdm_domain` / `cdm_data_entity` | ความเชื่อมโยงมิติข้อมูล CDM | DCCE CDM | G4 (CDM Architecture) | `cdm_domain`, `cdm_data_entity` |

*(Note: API endpoint / URL distribution link is also mandated as part of the physical distribution metadata in `data_dictionary.csv` row `d-01` / `url`).*

---

### 3. CDM Model Domains: Architectural Normative Authority vs. Narrative Shorthand

#### Authoritative Sources
- **Normative Architectural Authority**: `ψ/incubate/DCCE/CRDB/output/05_Data_Management_Framework/CDM_EARCatalog/cdm_mermaid_erd.md` (Dated 2026-07-13, synchronized with Loss & Damage Model MVD).
- **Narrative Plan References**: `plans/chapter7_3/drafting_plan.md` (Line 111); `plans/chapter6/english_outline.md` (Line 89).

#### Domain Mapping & Resolution
The technical architecture defined in `cdm_mermaid_erd.md` **strictly governs** technical specifications and database schemas. The 8 formal CDM engineering domains and their mapping to the high-level drafting plan narrative are:

| Formal CDM ERD Domain Code | Architectural Domain Name (`cdm_mermaid_erd.md`) | Core Entities in Architecture | Policy/Narrative Shorthand (`drafting_plan.md` L111) |
|----------------------------|---------------------------------------------------|-------------------------------|-------------------------------------------------------|
| **`DOM_EV`** | **Essential Variables** | `METEOROLOGICAL_OBSERVATION`, `CLIMATE_DRIVER`, `ENVIRONMENTAL_DATA` | Greenhouse Gas & Climate Science |
| **`DOM_HAZ`** | **Hazards & Modeling** | `HAZARD_EVENT_CATALOG`, `CLIMATE_MODEL_RUN`, `HAZARD_SPATIAL_LAYER` | Hazard |
| **`DOM_022`** | **Vulnerability & Exposure** | `EXPOSED_ASSET`, `VULNERABILITY_INDEX`, `SPATIAL_UNIT` | Exposure / Vulnerability |
| **`DOM_023`** | **Risk** | `CLIMATE_RISK_ASSESSMENT`, `RISK_SCORE`, `ADAPTATION_DEFICIT` | Risk / Spatial Context |
| **`DOM_024`** | **Disaster Impact / Loss & Damage** | `IMPACT_EVENT`, `LOSS_DAMAGE_ASSESSMENT`, `DIRECT_DAMAGE`, `INDIRECT_LOSS` | Climate Impact |
| **`DOM_030`** | **Resilience** | `ADAPTATION_PROJECT`, `ADAPTIVE_CAPACITY_METRIC`, `NBS_MEASURE` | Adaptation Measure |
| **`DOM_040`** | **Planning & Governance** | `POLICY_INSTRUMENT`, `FINANCIAL_ALLOCATION`, `INSTITUTIONAL_FRAMEWORK` | Financial & Budget |
| **`DOM_050`** | **Monitoring, Evaluation & Learning (MEL)** | `MEL_INDICATOR`, `PROGRESS_TRACKING`, `EVALUATION_REPORT` | Spatial Context / Baseline |

#### Drafting Guidance for Samart
- In technical specification paragraphs (Section 7.3.2.1), use the **formal ERD 8 domains** from `cdm_mermaid_erd.md` (`Essential Variables`, `Hazard & Modeling`, `Vulnerability & Exposure`, `Risk`, `Disaster Impact / Loss & Damage`, `Resilience`, `Planning & Governance`, `Monitoring, Evaluation & Learning`).
- When introducing them in narrative policy context, note that these 8 technical domains operationalize the full spectrum of climate adaptation from scientific physical baseline to institutional budget execution and international reporting.

---

## Primary Citations & Evidentiary Grounding

1. `ψ/incubate/DCCE/CRDB/output/06_Use_Case_Demand_Analysis/A-BTR_requirement_analysis/a_btr_dissection_database_report.md`
2. `ψ/incubate/DCCE/CRDB/output/A-BTR_requirement_analysis/quantitative_value.csv`
3. `ψ/incubate/DCCE/CRDB/output/02_Data_Inventory/Pillar_03_DataInventory_DQ_Technical_Specification.md`
4. `ψ/incubate/DCCE/CRDB/output/02_Data_Inventory/data_dictionary.csv`
5. `ψ/incubate/DCCE/CRDB/output/02_Data_Inventory/data_catalog_v4.csv`
6. `ψ/incubate/DCCE/CRDB/output/05_Data_Management_Framework/CDM_EARCatalog/cdm_mermaid_erd.md`
7. `plans/chapter6/english_outline.md`
8. `plans/chapter7_3/drafting_plan.md`
