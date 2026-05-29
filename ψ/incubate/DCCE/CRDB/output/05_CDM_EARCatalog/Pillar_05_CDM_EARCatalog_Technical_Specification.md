# Technical Specification: Pillar 5 — Climate Data Model (CDM) & EAR Catalog

## 0. Grounding note (current CRDB reality)

This spec is **not a hypothetical CDM**. It is constrained by the project’s existing CDM artifact and evidence chain:

- **Sealed Deliverable (Canonical)**: [`ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Pillar_05_CDM_EARCatalog_Deliverable.md`](ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Pillar_05_CDM_EARCatalog_Deliverable.md)
- CDM anchor (current): [`ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md)
- Evidence bridge (why CDM exists + how to position it): [`ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md`](ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md)

The CDM’s “non-negotiables” (Version 2.2) include:

- Separation of **continuous climate drivers** (`CLIMATE_DRIVER`) vs **discrete hazardous events** (`HAZARDOUS_EVENT`).
- Adoption of **DDPM_ID** for local disaster tracking while maintaining **WMO_UUID** as a secondary attribute.
- An explicit bridge for “slow-onset” attribution via `ATTRIBUTION_LINK` to avoid inventions of fake events.
- A **strategy pattern** for vulnerability: `VULNERABILITY_FRAMEWORK` implemented either as `IMPACT_FUNCTION` (hard/curve) or `VULNERABILITY_DIMENSION` + `VULNERABILITY_STRUCTURE` + `VULNERABILITY_DETERMINANT` (soft/index).
- **Closed-Loop MEL**: Direct feedback from `INTERVENTION_RESULT` to `COMPOSITE_INDEX`.

## 1. Data Structural Requirements
*   **Artifact Format**: Entity-Attribute-Relationship (EAR) Catalog.
*   **File Type**: Structured Excel (.xlsx) or Comma-Separated Values (.csv).
*   **Mandatory Schema**:
    *   **Entity Catalog**: Must include `Entity_Name`, `Subject_Area_ID`, `Business_Definition`, and `Primary_Key_Type`.
    *   **Attribute Registry**: Must include `Entity_Name`, `Attribute_Name`, `Data_Nature` (Temporal, Spatial, or Static), and `Standard_Reference` (e.g., ISO 19115, CF Conventions).
    *   **Relationship Mapping**: Must include `Parent_Entity`, `Child_Entity`, `Cardinality` (1:N, M:N), and `Referential_Integrity_Rules`.
*   **Logical domains (v2.2)**:
    1. **Physical Climate (cause)**: `CLIMATE_SCENARIO`, `CLIMATE_DRIVER`, `HAZARDOUS_EVENT`.
    2. **Risk Analysis (calculation)**: `RISK_ANALYSIS`, `RISK_METRIC`, `COMPOSITE_INDEX`.
    3. **Vulnerability & Exposure (receptor)**: `SPATIAL_UNIT`, `EXPOSED_ASSET`, `VULNERABILITY_FRAMEWORK`, `VULNERABILITY_DIMENSION`, `VULNERABILITY_STRUCTURE`.
    4. **Adaptation Planning (action)**: `DECISION_CONTEXT`, `ADAPTATION_PORTFOLIO`, `ADAPTATION_OPTION`, `ADAPTATION_PROJECT`.
    5. **Monitoring & MEL (result)**: `INTERVENTION_RESULT`, `FUNDING_SOURCE`, `RISK_TOLERANCE_PROFILE`.

### 1.1 Minimum entity set (acceptance gate)

The EAR catalog is **not acceptable** unless it includes entities representing the following CDM commitments:

- `CLIMATE_DRIVER` vs `HAZARDOUS_EVENT` separation.
- `ATTRIBUTION_LINK` (slow-onset compatible loss linkage).
- `VULNERABILITY_FRAMEWORK` strategy split (curve vs dimension-based index).
- Neutral determinant library (`VULNERABILITY_DETERMINANT`) + role assignment (`VULNERABILITY_STRUCTURE`).
- **Feedback Linkage**: `INTERVENTION_RESULT` → `COMPOSITE_INDEX`.

## 2. Quality Assurance & Verification Criteria
*   **TOR traceability**: The EAR must be usable to satisfy the TOR-driven needs for data management structure, inventory categories, MVD, and gap analysis. 
*   **NCAIF traceability**: 100% of data products defined in the NCAIF Sitemap must map to ≥1 CDM entity.
*   **Standard Alignment**: `CLIMATE_DRIVER` attributes must conform to IPCC AR6 Climatic Impact-Driver (CID) classifications.
*   **System Interoperability**: `EXPOSED_ASSET` attributes must include mandatory fields for TGEIS (Activity Data) and GED4ALL integration.
*   **Determinant neutrality (hard requirement)**: Socio-economic indicators MUST be stored as neutral `VULNERABILITY_DETERMINANT` variables; their role (Sensitivity vs Adaptive Capacity etc.) MUST be expressed via mapping entities, not by duplicating variables.
*   **No “fake events” rule**: The model must not require inventing `HAZARDOUS_EVENT` rows to represent slow-onset drivers. 

## 3. Implementation Constraints
*   **Structural Integrity**: Core logical relationships (e.g., the separation of Vulnerability from Exposure) are immutable. The contractor is prohibited from denormalizing these into flat structures that prevent multi-dimensional analysis.
*   **Identification Standards**: All `HAZARDOUS_EVENT` entries must utilize **DDPM_ID** for primary local indexing, with **WMO-CHE UUIDs** for international interoperability.
*   **Technical Consultation**: The contractor may optimize physical storage (e.g., indexing, partitioning, data types) but must prove that the physical implementation maintains 100% fidelity to this logical baseline.

### 3.1 Explicit handoff constraint: logical sovereignty vs physical optimization

- The vendor may change **physical** implementation choices (relational vs document, indexing, partitioning, storage engines), but cannot change **logical commitments** listed in §0 and §1.1.
- Any proposal that collapses `CLIMATE_DRIVER` + `HAZARDOUS_EVENT` into a single concept, or removes the `INTERVENTION_RESULT` feedback loop, is a **scope change request** (not an implementation detail).
