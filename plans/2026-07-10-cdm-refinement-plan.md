# Plan: Common Data Model (CDM) Schema Audit and Refinement

**Date**: 2026-07-10  
**Context**: Bossax/arun_creagy  
**Primary Objective**: Refine the DCCE Common Data Model (CDM) schema catalogs to ensure the database can govern the underlying Data Assets required to power downstream Climate Data Products and Services (including the BTR reporting pipeline, public portal services, and policy/engineering tools).

---

## 1. Plan Scope & Inputs

The audit will utilize the following source documents as inputs:

1.  **Baseline CDM Schema**:
    *   [`Entities-v2.csv`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Entities-v2.csv) (Table definitions and metadata terms).
    *   [`Relationships-v3.csv`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Relationships-v3.csv) (Primary/foreign keys and cardinalities).
2.  **Target Services & Use Cases (Data Product Requirements)**:
    *   [`2026-07-06_btr-me-reporting-pipeline-use-case.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/2026-07-06_btr-me-reporting-pipeline-use-case.md) (Automated transparency reporting pipeline specs).
    *   [`บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/%E0%B8%9A%E0%B8%97%E0%B8%AA%E0%B8%A3%E0%B8%B8%E0%B8%9B%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%95%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%9A%E0%B8%A3%E0%B8%B8%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B8%AA%E0%B8%B2%E0%B8%A3%E0%B8%AA%E0%B8%99%E0%B9%80%E0%B8%97%E0%B8%A8%E0%B8%94%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%A0%E0%B8%B9%E0%B8%A1%E0%B8%B4%E0%B8%AD%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A8_v6.md) (The 8 core Climate Services).
    *   [`2026-06-15_NCAIF-Service-Enrichment-Roadmap.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/2026-06-15_NCAIF-Service-Enrichment-Roadmap.md) (Sequential rollout and Service 4 L&D pilot requirements).
3.  **Target Database File**:
    *   [`a_btr_dissection.db`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/A-BTR_requirement_analysis/a_btr_dissection.db) (SQLite container).

---

## 2. Step-by-Step Execution Protocol

### Step 1: Use Case & Service Mapping (Data Asset Discovery)
*   **Action**: Scan the BTR M&E pipeline specs and the 8 core Climate Services (with focus on the Service 4 "Alpha Wedge" L&D pilot) to compile a list of necessary quantitative *Data Assets* (e.g. historical emergency relief payments, STAC metadata, localized damage functions, TPMAP social deprivation variables, and GGA technology readiness levels).
*   **Boundary Gate**: Filter out qualitative organizational information (like committee structures or textual lists of policy barriers) which, according to the system design in [`dcce_proposed_architecture_design.md`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/dcce_proposed_architecture_design.md), belong in the CMS Layer (Knowledge Assets) rather than the database schema.

### Step 2: Database Schema Gap Audit
*   **Action**: Audit the current `Entities-v2.csv` and `Relationships-v3.csv` catalogs against the compiled list of Data Assets.
*   **Verification Objective**: Check if the database has:
    1.  The tables and columns necessary to store the required data variables.
    2.  The primary, foreign, and associative keys (e.g., attribution and mapping tables) required to join these entities for reporting.
*   **Document Output**: Compile the findings in a new file `cdm_refinement_audit_report.md` detailing the identified table/relationship gaps.

### Step 3: Schema Refactoring & DB Synchronization
*   **Action**: Develop and run a Python script (`run_cdm_refinement.py`) to automate:
    1.  Updating the CSV files (`Entities-v2.csv` and `Relationships-v3.csv`) on disk with the refined/new entities and relationships.
    2.  Creating and updating the corresponding CDM tables inside the SQLite database `a_btr_dissection.db` to synchronize the physical database schema.

### Step 4: Verification & Stress Testing
*   **Action**: Write and run test SQL queries against the newly updated tables in `a_btr_dissection.db`.
*   **Testing Use Cases**:
    1.  *Service 4 L&D Pilot*: Query government advance relief payments (`เงินทดรองราชการ`) and GPP variables to verify the re-normalized macroeconomic damage calculation pipeline.
    2.  *Service 2 Spatial Risk*: Query administrative units joined to vulnerability variables (gender and TPMAP poverty indicators).
    3.  *Adaptation Finance*: Query domestic tagged budgets and international funds received.
*   **Final Output**: Save the verified Entity-Attribute-Relationship design inside strategy reports for approval.
