# Technical Specification: Pillar 5 - Governance Gates (G1–G5) Semantics (DQ + Metadata + Endorsement)

## 0. Purpose (DAMA-aligned, Phase-1 realistic)

Pillar 5 defines the **standard semantics** of the 5 governance gates (G1–G5).

It is intentionally written as a **TOR-first / Phase-1 governance standard** that can be executed manually (checklists + templates) and later automated in Project B.

- Pillar 4 and Pillar 7 store governance attributes (e.g., `Feasibility_Posture`, `Reference_Status`) at row/entity level.
- Pillar 5 defines **what those fields mean** and what constitutes acceptable values.
- Pillar 6 defines **who decides** (decision rights) and **how decisions are executed** (cadence + escalation + decision log).

## 1. Technical Requirements

### 1.1 Artifact format

*   **Artifact Format**: Governance Gate Definitions + Audit Checklist.
*   **File Type**: Markdown (.md) as the normative spec + optional structured annex (JSON/CSV) for future automation.

### 1.2 Mandatory gate semantics (normative)

*   **G1 — Classification + publishing rail**
    * **Fields**: `Data_Classification` (Open / G2G-GDX / Internal), `Publication_Rail`.
    * **Rule**: every asset must declare which rail it can travel on and why.
*   **G2 — Container metadata minima (catalog-level)**
    * **Fields (minimum)**: `Asset_Name`, `Description`, `Steward`, `Source`, `Spatial_Unit`, `Update_Cadence`, `Classification`, `Limitations_Statement`.
    * **Note**: entity/attribute schema design is mandated by Pillar 1; G2 is the *container metadata* standard.
*   **G3 — Endorsement / analytical authority (fitness-for-use)**
    * **Fields**: `Endorsement_Status` (Draft / Recommended / Superseded), `Authority_Role`.
    * **Rule**: endorsement means “recommended for a stated purpose/scale with caveats”, not “proven correct”.
*   **G4 — Canonical boundary / denominator + crosswalk governance**
    * **Fields**: `Canonical_Boundary_ID` (Admin / Hydrological / Other-defined).
    * **Rule**: if multiple denominators exist, crosswalk ownership must be declared (Pillar 6 workflow).
*   **G5 — Revision & maturity for event/impact data (post-event reality)**
    * **Fields**: `Observation_Timestamp`, `Validation_Flag`.
    * **Rule**: `Validation_Flag` expresses maturity status (e.g., Preliminary/Verified/Revised/Superseded). Exact labels are approved via Pillar 6.

### 1.3 Shared flag definitions used by other pillars

*   **`Feasibility_Posture`** (used in Pillar 4)
    * `Validated`: confirmed by a named source owner or authoritative documentation.
    * `Assumed`: inferred from public materials; not confirmed by the source owner.
    * `Unknown`: not enough evidence; requires follow-up.
*   **Metadata completeness posture**
    * Missing values should be recorded as `Unknown` with a limitations note; do not fabricate placeholders.

## 2. Verification Criteria

*   **National alignment (where applicable)**: G1/G2 semantics should be compatible with DGA rails and catalog harvesting practices, but this project does not certify compliance for every dataset.
*   **Honesty over completeness**: a record is non-compliant if it hides uncertainty (e.g., fake cadence, fake steward). Use `Unknown` + limitations statements instead.
*   **Denominator disclosure**: if `Canonical_Boundary_ID` is not Admin, the asset must explicitly declare the denominator and any required crosswalk.
*   **User transparency**: every asset/product must surface the limitations statement (G2) and maturity label (G5) in human-readable form.

## 3. Implementation Constraints

*   **Phase-1 posture (no overclaim)**: in this CRDB phase, gates can be executed procedurally (checklists + review). Full automation is a Project B responsibility.
*   **Non-negotiable for future implementation**: Project B must implement these gates as enforceable workflow controls, but Pillar 5 does not assume the existence of a running validation engine today.
*   **Audit trail requirement (future enforcement)**: the implementation must preserve decision/audit history; bypassing gates becomes a contract non-compliance issue in Project B.
