# Technical Specification: Pillar 5 — Climate Data Model (CDM) & EAR Catalog

## 0. Grounding note (current CRDB reality)

This spec is **not a hypothetical CDM**. It is constrained by the project’s existing CDM artifact and evidence chain:

- CDM anchor (current): [`ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md:10)
- Evidence bridge (why CDM exists + how to position it): [`ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md`](ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md:47)
- Evidence registry index: [`ψ/incubate/DCCE/CRDB/CRDB-Evidence-Registry.md`](ψ/incubate/DCCE/CRDB/CRDB-Evidence-Registry.md:35) (E-002)

The CDM’s “non-negotiables” already present in the anchor model include:

- Separation of **continuous climate drivers** (`CLIMATE_DRIVER`) vs **discrete hazardous events** (`HAZARDOUS_EVENT`).
- An explicit bridge for “slow-onset” attribution via `ATTRIBUTION_LINK` (to avoid inventing fake events just to satisfy FK constraints). %% can ATTRIBUTION_LINK be left out for now? since its use case is still unclear. What if we decide to add it later on, would it impact the system in overall?  %%
- A **strategy pattern** for vulnerability: `VULNERABILITY_DEFINITION` implemented either as `IMPACT_FUNCTION` (hard/curve) or `VULNERABILITY_FRAMEWORK` + `FRAMEWORK_MAPPING` + `VULNERABILITY_DETERMINANT` (soft/index).

## 1. Data Structural Requirements
*   **Artifact Format**: Entity-Attribute-Relationship (EAR) Catalog.
*   **File Type**: Structured Excel (.xlsx) or Comma-Separated Values (.csv).
*   **Mandatory Schema**:
    *   **Entity Catalog**: Must include `Entity_Name`, `Subject_Area_ID`, `Business_Definition`, and `Primary_Key_Type`.
    *   **Attribute Registry**: Must include `Entity_Name`, `Attribute_Name`, `Data_Nature` (Temporal, Spatial, or Static), and `Standard_Reference` (e.g., ISO 19115, CF Conventions).
    *   **Relationship Mapping**: Must include `Parent_Entity`, `Child_Entity`, `Cardinality` (1:N, M:N), and `Referential_Integrity_Rules`.
*   **Logical domains (must match the current CDM anchor)**:
    1. **Physical Climate (cause)**: `CLIMATE_SCENARIO`, `CLIMATE_DRIVER`, `HAZARDOUS_EVENT`.
    2. **Attribution (bridge)**: `ATTRIBUTION_LINK` (links `LOSS_DAMAGE_RECORD` → `HAZARDOUS_EVENT` *or* `CLIMATE_DRIVER`).
    3. **Assets & space (receptor)**: `SPATIAL_UNIT`, `EXPOSED_ASSET`.
    4. **Vulnerability (strategy)**: `VULNERABILITY_DEFINITION` with both pathways:
       - `IMPACT_FUNCTION` (curve-based)
       - `VULNERABILITY_FRAMEWORK` + `FRAMEWORK_MAPPING` + `VULNERABILITY_DETERMINANT` (index/indicator-based)
    5. **Outcomes (products)**: `RISK_ASSESSMENT` → `RISK_METRIC` and/or `COMPOSITE_INDEX`; plus `LOSS_DAMAGE_RECORD`.

### 1.1 Minimum entity set (acceptance gate)

The EAR catalog is **not acceptable** unless it includes entities representing the following CDM commitments:

- `CLIMATE_DRIVER` vs `HAZARDOUS_EVENT` separation
- `ATTRIBUTION_LINK` (slow-onset compatible loss linkage)
- `VULNERABILITY_DEFINITION` strategy split (curve vs framework)
- Neutral determinant library (`VULNERABILITY_DETERMINANT`) + role assignment (`FRAMEWORK_MAPPING`)

## 2. Quality Assurance & Verification Criteria
*   **TOR traceability**: The EAR must be usable to satisfy the TOR-driven needs explicitly mapped in the CDM anchor (data management structure, inventory categories, MVD, gap analysis). Evidence: [`ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md:10).
*   **NCAIF traceability**: 100% of data products defined in the NCAIF Sitemap must map to ≥1 CDM entity (the CDM is the hidden coherence layer, not the UI). Context: [`ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md`](ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/2026-03-12_crdb-section1-cdm-mvp-evidence-analysis.md:184).
*   **Standard Alignment**: `CLIMATE_DRIVER` attributes must conform to IPCC AR6 Climatic Impact-Driver (CID) classifications.
*   **System Interoperability**: `EXPOSED_ASSET` attributes must include mandatory fields for TGEIS (Activity Data) and GED4ALL integration.
*   **Determinant neutrality (hard requirement)**: Socio-economic indicators MUST be stored as neutral `VULNERABILITY_DETERMINANT` variables; their role (Sensitivity vs Adaptive Capacity etc.) MUST be expressed via `FRAMEWORK_MAPPING` (framework-specific), not by duplicating variables across role-specific tables. Evidence: [`ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md:142).
*   **No “fake events” rule**: The model must not require inventing `HAZARDOUS_EVENT` rows to represent slow-onset drivers. Slow-onset linkage must be representable via `ATTRIBUTION_LINK` → `CLIMATE_DRIVER` (+ time context if needed in the logical design). Evidence: [`ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md:210).

## 3. Implementation Constraints
*   **Structural Integrity**: Core logical relationships (e.g., the separation of Vulnerability from Exposure) are immutable. The contractor is prohibited from denormalizing these into flat structures that prevent multi-dimensional analysis.
*   **Identification Standards**: All `HAZARDOUS_EVENT` entries must utilize **WMO-CHE UUIDs** to ensure cross-agency data consistency.
*   **Technical Consultation**: The contractor may optimize physical storage (e.g., indexing, partitioning, data types) but must prove that the physical implementation maintains 100% fidelity to this logical baseline.

### 3.1 Explicit handoff constraint: logical sovereignty vs physical optimization

- The vendor may change **physical** implementation choices (relational vs document, indexing, partitioning, storage engines), but cannot change **logical commitments** listed in §0 and §1.1.
- Any proposal that collapses `CLIMATE_DRIVER` + `HAZARDOUS_EVENT` into a single concept, or removes `ATTRIBUTION_LINK`, is a **scope change request** (not an implementation detail).
