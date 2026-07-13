# Comprehensive CDM Schema Refinement & Gap Audit Report (A-BTR Aligned)

**Date**: 2026-07-10  
**Context**: Bossax/arun_creagy  
**Target Schema**: `Entities-v2.csv`, `Relationships-v3.csv`
**Source of Truth**: UNFCCC A-BTR Requirements Database (`requirement_statement` table) & NCAIF Climate Service Roadmaps

---

## 1. Executive Summary
A direct analysis of the A-BTR requirement text reveals critical schema deficiencies in how the current Common Data Model (CDM) handles Non-Economic Loss (NEL), M&E indicator tracking, and Institutional governance.

This report outlines the **12 specific new entities** that must be added to the physical database to achieve 100% structural compliance with the A-BTR and the 8 NCAIF Climate Services.

---

## 2. Exhaustive List of Proposed New Entities

To fully support the A-BTR compliance queries, the following entities must be added to the `Entities-v2.csv` catalog:

### A. Loss, Damage & Relief (Unfolding `LOSS_DAMAGE_RECORD`)
*A-BTR Mandates: B-033 to B-106 (mandating distinct tracking of GDP loss, human health/fatalities, and ecological destruction like coral bleaching and forest fires).*

1.  **`ECONOMIC_LOSS_RECORD`**: Tracks monetized damages to physical assets, infrastructure, and agricultural/sectoral production losses (OpEx/CapEx).
2.  **`HUMAN_IMPACT_RECORD`**: Tracks demographic and health impacts, including fatalities, injuries, displaced persons, malnutrition rates, and heat-related illnesses.
3.  **`ENVIRONMENTAL_LOSS_RECORD`**: Tracks non-economic ecological damages, such as extent of coral bleaching, forest fire burn areas, and biodiversity loss.
4.  **`RELIEF_PAYMENT_RECORD`**: Tracks Government Advance Payments (`เงินทดรองราชการ`) for emergency disaster response (critical for macroeconomic normalization).

%% these conceptual entities can be synced with [[ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification|Pillar_06_LDM_LossDamage_DataModel_Technical_Specification]] %%

### B. Monitoring, Evaluation & Learning (MEL)
*A-BTR Mandates: C-025, C-043, C-044 (strictly criticizing the reliance on output metrics and mandating outcome-based resilience assessment).*

5.  **`ADAPTATION_OUTPUT`**: Replaces the generic `INTERVENTION_RESULT`. Tracks immediate, countable deliverables of an adaptation project (e.g., number of training workshops held, length of seawall built).
6.  **`ADAPTATION_OUTCOME`**: Tracks measurable changes in resilience, vulnerability reduction, and adaptive capacity (e.g., % reduction in expected annual loss, improvement in food security indices) linked to GGA/Belém targets.

%%
- is there 'Adaptation_project' table yet? what are adjacent entities to fully describe an adaptation project?
- Does the ADAPTATION_OUTPUT track at project level or aggregate? since A-BTR reports aggregate statistics, should the unit of analysis be project or country level? 
- Do we need a mapping table for GGA dimensional and thematic indicators? so that we can seal the logical framework of linking existing indicators produced by line agencies to GGA indicators. This allows for dynamic mapping rather than hard coding this logic somewhere else (check if I am correct, compare the the lesson from the M&E platform) 
- There is still unclear issues about what M&E platform can answer. Are those indicators reported by the focal point line agencies map-able to GGA indicators? or are those indicators focused on tracking NAP which is not fully aligned with GGD yet
%%

### C. Finance & Support Tracking
*A-BTR Mandates: C-036 to C-042 (mandating explicit tracking of embedded domestic budgets and international support).*

7.  **`BUDGET_TAG_RECORD`**: Tracks domestic government budget line items explicitly tagged for climate adaptation, linked to projects and ministries. %% this code is non-existent in the Bureau of Budget's system yet %%
8.  **`SUPPORT_TRACKING_RECORD`**: Tracks international support (Financial, Technology Transfer, and Capacity-Building) categorizing what is *needed* versus what is *received*.

### D. Institutional Governance & Data Stewardship
*A-BTR Mandates: A-011 to A-022, C-027, C-047 (mandating the identification of specific focal points, committees, and data owners).*

9.  **`INSTITUTIONAL_BODY`**: Registers government agencies, national committees, focal points, and working groups responsible for adaptation actions or data governance.
10. **`DATASET_CATALOG`**: A registry of official climate datasets used for adaptation planning, capturing metadata for STAC compliance and "Suitability for Use" uncertainty confidence levels (NCAIF Service 8). %% why is this a separate entity? what is it actually? a table of metadata? isnt this redundant? %%


### E. Baselines & Engineering (Climate Services Integration)
*A-BTR Mandates: A-004 to A-007 (socio-economic context), plus NCAIF Services 2 & 5.*

11. **`MACRO_ECONOMIC_STATISTIC`**: Stores baseline socio-economic metrics per spatial unit (GPP, GDP, poverty incidence, demographic counts) required to normalize absolute loss data into comparative risk indices.
12. **`ENGINEERING_DESIGN_PARAMETER`**: Stores derived, actionable scientific outputs like Intensity-Duration-Frequency (IDF) curves, design runoff, and peak flow coefficients for infrastructure planning. %% which domains does this entity belong to? %%

---

## 3. Required Relationship Updates

To bind these new entities into the CDM, the following primary/foreign key relationships must be added to `Relationships-v3.csv`:

*   **Loss & Damage Unfolding**:
    *   `DISASTER_RECORD` $\rightarrow$ `ECONOMIC_LOSS_RECORD` (1:N)
    *   `DISASTER_RECORD` $\rightarrow$ `HUMAN_IMPACT_RECORD` (1:N)
    *   `DISASTER_RECORD` $\rightarrow$ `ENVIRONMENTAL_LOSS_RECORD` (1:N)
    *   `DISASTER_RECORD` $\rightarrow$ `RELIEF_PAYMENT_RECORD` (1:N)
*   **M&E Logic**:
    *   `ADAPTATION_PROJECT` $\rightarrow$ `ADAPTATION_OUTPUT` (1:N)
    *   `ADAPTATION_PROJECT` $\rightarrow$ `ADAPTATION_OUTCOME` (1:N)
*   **Finance Tracking**:
    *   `ADAPTATION_PROJECT` $\rightarrow$ `BUDGET_TAG_RECORD` (1:N)
    *   `FUNDING_SOURCE` $\rightarrow$ `SUPPORT_TRACKING_RECORD` (1:N)
*   **Governance**:
    *   `INSTITUTIONAL_BODY` $\rightarrow$ `ADAPTATION_PROJECT` (1:N) *(Agency owns/implements project)*
    *   `INSTITUTIONAL_BODY` $\rightarrow$ `DATASET_CATALOG` (1:N) *(Agency is custodian of dataset)*
*   **Spatial Baselines**:
    *   `SPATIAL_UNIT` $\rightarrow$ `MACRO_ECONOMIC_STATISTIC` (1:N)
    *   `SPATIAL_UNIT` $\rightarrow$ `ENGINEERING_DESIGN_PARAMETER` (1:N)

---

## 4. Next Steps
Once this comprehensive entity list is approved, the Python automation script (`run_cdm_refinement.py`) will be executed to inject these 12 entities and 12 relationships into the CSV files and synchronize the SQLite `a_btr_dissection.db` database.
