# Technical Specification: Pillar 4 - Subject-Area Interface Map

## 0. Scope decision (time-bound, TOR-supporting)

**Decision:** This project will not have time to fully **validate / verify / testify** technical ingestion feasibility with all source agencies before the July 6 submission.

Therefore, this artifact is specified as a **TOR-supporting inventory scaffold** (a crosswalk) rather than a delivered ETL design.

**Governance separation note (DAMA-aligned):**
- Pillar 4 defines the *interface inventory artifact* (what sources exist, what they relate to, what is known/unknown).
- The **meaning** of governance flags/attributes (e.g., what counts as “Validated vs Assumed”, how metadata fields are defined) is standardized in **Pillar 5 (G1–G5)**.
- The **decision-rights + workflow** for changing mappings/flags (who approves changes, how versions are issued) is defined in **Pillar 6 (RACI)**.

This avoids duplicating governance semantics in every pillar while keeping Pillar 4 operationally auditable.

- TOR requires an Information Product Inventory + Baseline Data Inventory (5.3.4–5.3.5): [`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:167)
- This map exists to make those inventories **joinable** to CDM subject areas and to record integration posture + unknowns explicitly.

## 1. Data Structural Requirements
*   **Artifact Format**: Source-to-Subject Area Interface Map.
*   **File Type**: Structured Excel (.xlsx) or Comma-Separated Values (.csv).
*   **Mandatory Schema**:
    *   **`Source_System_ID`**: Unique identifier for the external data source (e.g., `ThaiWater`, `BTR_Portal`).
    *   **`Source_Agency`**: The government department or entity providing the data.
    *   **`Data_Class`**: The specific category of data (e.g., `Rainfall_Raster`, `Coastal_Erosion_Survey`).
    *   **`CDM_Subject_Area_Link`**: Explicit mapping to one of the four Pillar 1 CDM Subject Areas.
    *   **`Interface_Type`**: Integration posture (not a validated ETL design). Recommended values:
        * `Reference/Link` (catalog-only; no ingestion)
        * `Manual_File_Exchange` (CSV/Excel exchange possible but not validated)
        * `API` (API exists or is claimed; not validated in this project)
        * `Document_Only` (report/PDF; no structured data access)
    *   **`Refresh_Cadence`**: Observed/published cadence or `Unknown` (not a mandated SLA in this project).
    *   **`Feasibility_Posture`**: One of `Validated` / `Assumed` / `Unknown`.
        - Definitions are standardized in Pillar 5; Pillar 4 must store the selected value per row.
    *   **`Provenance_Anchor`**: Evidence pointer for the row (URL / inventory row ID / interview note / source document reference).
        - This is required even when feasibility is `Unknown`.
*   **Integration Scope**: The map should cover "High-Priority" external sources referenced in the inventories, but may be delivered in phases (v0/v1/v2) with explicit `Unknown` values where verification is not feasible.

## 2. Quality Assurance & Verification Criteria
*   **Logical Alignment**: Every mapped row must point to a CDM subject area link; where EAR-entity mapping is not yet resolved, record it as `TBD` rather than inventing a mapping.
*   **Feasibility posture (honest)**: Every row must set `Feasibility_Posture` (Validated/Assumed/Unknown). Do not encode this only in prose notes.
*   **Provenance visibility**: Every row must include a `Provenance_Anchor` sufficient to trace back to inventory evidence (owner/URL/source doc), even if ingestion feasibility is unknown.
*   **Cadence honesty**: `Refresh_Cadence` may be `Unknown`; do not fabricate cadences to satisfy completeness.

## 3. Implementation Constraints
*   **Handoff constraint for the 25M THB implementation (Project B)**:
    * The implementation contractor must treat this map as the baseline for building harvesters/ETL.
    * However, this CRDB project delivers the map as a **specification artifact**, not as implemented connectors.
*   **Mapping sovereignty**: Changes to the CDM subject-area mapping require a formal revision decision (to prevent silent drift).

*   **Governance dependency**:
    * Pillar 4 does not redefine governance semantics.
    * Any changes to the allowed values or definitions of `Feasibility_Posture` must be made in Pillar 5 and then applied here.
