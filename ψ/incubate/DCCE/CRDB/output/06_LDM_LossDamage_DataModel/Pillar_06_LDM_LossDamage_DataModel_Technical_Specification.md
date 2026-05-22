# Technical Specification: Pillar 3 - Logical Data Model (LDM) & MVD Logic Rules

## 0. TOR-first grounding (contract reality)

This Pillar is driven by the TOR’s explicit obligations to:

- design a (Draft) **Minimum Viable Dataset (MVD)** and a **Loss & Damage Reporting Form** ([`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:190))
- **test** the (Draft) MVD by collecting data from **≥ 3 past events** ([`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:192))

MVP-2 “ingestion + quarantine gateway” is **supporting context only** and may change; the TOR deliverable contract remains the priority.

## 1. Data Structural Requirements
*   **Artifact Format**: Logical Data Model (LDM) specification for Loss & Damage + MVD field standard + reporting-form template.
*   **Primary File Types** (TOR-compatible):
    *   Structured Excel (.xlsx) / CSV templates for MVD and reporting form.
    *   Optional: a lightweight validation suite (Python or equivalent) for checking schema compliance and revision/audit rules.
*   **Mandatory Component Schema**:
    *   **Event header + observation tables ("Disaster Card")**: Must define the logical structure for:
        *   `DISASTER_RECORD` (event header / registry)
        *   `LOSS_DAMAGE_RECORD` (impact/loss observations)
        *   key identifiers and linkage fields, including `Event_ID` (or equivalent), hazard type, location/spatial unit, dates, and reporting agency.
    *   **Reporting form template (TOR 5.3.6)**: A standardized form layout whose fields correspond 1:1 to the MVD field standard.
    *   **Revision + validation fields (auditability)**: Must define status fields for:
        *   `Validation_State` (e.g., Quarantined, Verified, Revised)
        *   `Data_Provenance` (source agency/system + extract method)
        *   `Revision_ID` / `Revision_Timestamp` / `Supersedes_Revision_ID` (or equivalent)
        *   `Timeliness_Label` (freshness / “as-of” labeling)
        *   optional categorical confidence / data-quality tiering (not statistical intervals unless evidence exists).
    *   **Optional extensions (not required unless explicitly mandated)**:
        *   economic-loss estimation models (direct/indirect), normalization, or attribution weighting logic.
*   **Logic Domains**: The model must provide explicit rules for:
    1.  **Disaster Data Ingestion**: Intake validation for DDPM-derived datasets.
    2.  **Loss & Damage (MVD)**: Mandatory field-set for Sendai Framework reporting (Targets A-D).
    3.  **Revision Control**: Logic for handling lagged data updates and "Relief Payout" vs. "Estimated True Loss" separation.

## 2. Quality Assurance & Verification Criteria
*   **TOR MVD coverage**: 100% of the TOR-defined MVD + reporting-form fields must be represented in the MVD standard + templates.
*   **3-event pilot evidence (TOR 5.3.7)**: A test pack must exist demonstrating collection and representation of the MVD across **≥ 3 past events**, including revision handling and validation state changes.
*   **Relational Integrity**: All loss records must demonstrate a mandatory logical link to a `HAZARDOUS_EVENT` or a `CLIMATE_DRIVER` via the `ATTRIBUTION_LINK` pattern.
*   **Operational readiness (minimum)**: The specification must define which fields are required at first ingestion vs fields that may be completed later (revision workflow), and how “official” vs “quarantined” status is determined.

## 3. Implementation Constraints
*   **Schema sovereignty**: The MVD field standard + reporting form field set are the baseline. The contractor is prohibited from redefining or substituting the required field set without explicit DCCE approval.
*   **Temporal Consistency**: The system must support the storage of historical revisions. Overwriting original impact observations with revised data without maintaining an audit trail is prohibited.
*   **System Boundary**: The contractor must implement the "Quarantine Gateway" logic, ensuring that unverified disaster data is logically separated from "Official Source of Truth" reporting until verification criteria are met.

### 3.1 Explicit non-requirement (to prevent scope creep)

- This Pillar does **not** automatically mandate a full loss-estimation methodology engine (direct/indirect loss models, normalization models, attribution weighting algorithms). If such computation is required, it must be introduced as an explicit, separately agreed scope item with named evidence sources and acceptance tests.
