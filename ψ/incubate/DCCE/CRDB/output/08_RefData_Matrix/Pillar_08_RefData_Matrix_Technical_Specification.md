# Technical Specification: Pillar 8 - Reference Data Dependency Matrix

## 0. Scope decision (time-bound, TOR-supporting)

**Decision:** This project will not have time to fully **validate / verify / testify** the canonical reference datasets (admin units, hazard codes, agency codes, etc.) across the entire future data system before the July 6 submission.

Therefore, Pillar 8 is specified as a **dependency matrix + authority/source map** that supports TOR inventories (by making them joinable and interpretable), rather than a delivered, fully reconciled master data package.

**Governance separation note (DAMA-aligned):**
- Pillar 8 defines the *reference data dependency artifact* (what reference sets exist, who is the authority, what depends on what).
- The **definitions** of shared governance attributes (classification, metadata minima, endorsement labels, revision/maturity labels) are standardized in **Pillar 3 (Data Inventory & DQ Framework)**.
- The **decision rights and workflow** for resolving contested authorities, issuing new versions, and approving crosswalks are standardized in **Pillar 7 (Governance: RACI & workflow)**.

This keeps Pillar 8 auditable and joinable without duplicating governance semantics across pillars.

TOR context: baseline data inventory requires consistent categories + limitations and would otherwise silently diverge by coding systems ([`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:169)).

## 1. Data Structural Requirements
*   **Artifact Format**: Reference Data Matrix.
*   **File Type**: Structured Excel (.xlsx) or Comma-Separated Values (.csv).
*   **Mandatory Schema**:
    *   **`Reference_Entity_ID`**: Unique identifier for the master data set (e.g., `REF_ADMIN_V4`, `REF_HAZARD_TYPES`).
    *   **`Entity_Name`**: The canonical name of the reference entity (e.g., Administrative Unit, Agency Code, River Basin).
    *   **`Attribute_Set`**: Mandatory columns required for the lookup (e.g., `Unit_Code`, `Name_TH`, `Name_EN`, `Parent_Code`).
    *   **`Authority_Source`**: The official agency providing the master list (e.g., DGA for agency codes, NSO for administrative units).
    *   **`Update_Frequency`**: Cadence for refreshing the master list.
    *   **`Reference_Status`**: One of `Agreed` / `Contested` / `Unknown`.
        - Definitions and escalation workflow are specified in Pillar 7; Pillar 8 stores the selected value per entity.
    *   **`Versioning_Expectation`**: Brief text describing whether stable codes/IDs are expected and whether effective dating exists (or `Unknown`).
    *   **`Crosswalk_Required`**: `Yes`/`No`/`Unknown` (e.g., Admin ↔ Hydrological; legacy codes ↔ current codes).
    *   **Logical Scope**: The matrix must include all entities that act as "Master Data" or "Lookups" for the TOR-facing inventories and the Pillar 1/3 conceptual/logical models, specifically:
    1.  **Administrative Boundaries** (Province, District, Sub-district).
    2.  **Hydrological Units** (Major Basins, Sub-basins).
    3.  **Agency/Department Codes** (Standardized Government Registry).
    4.  **Parameter Units & Thresholds** (Standardized Measurement Units).

## 2. Quality Assurance & Verification Criteria
*   **Standards posture (honest)**:
    * where a national standard exists, record it as the preferred authority source;
    * where it is unknown/contested, record as `Unknown/Contested` rather than asserting compliance.
*   **Contestability explicitness**: Every reference entity must set `Reference_Status` (Agreed/Contested/Unknown). Do not hide contestability only in prose.
*   **Hierarchy posture**: The matrix must document the intended parent-child hierarchy fields, but does not need to prove cross-system consistency in this project.
*   **Referential linking (inventory-level)**: List which inventories / CDM/LDM entities depend on each reference set (so downstream implementers can prioritize reconciliation work).
*   **DCCE sovereignty (only when necessary)**: Only assert DCCE as canonical owner if (a) no national standard exists and (b) the term/list is required for TOR deliverables.

## 3. Implementation Constraints
*   **Handoff constraint for the 25M THB implementation (Project B)**:
    * The implementation contractor must seed the platform using authoritative reference sets as identified here.
    * This CRDB project does not implement seeding or an MDM interface; it delivers the dependency specification and authority map.
*   **Single-source intent**: The matrix states the intent that future systems should avoid duplicated/siloed lookups; enforcement is an implementation responsibility.

*   **Governance dependency**:
    * Pillar 8 does not redefine governance semantics.
    * Any changes to allowed values/definitions of `Reference_Status` must be made in Pillar 7 and then applied here.
