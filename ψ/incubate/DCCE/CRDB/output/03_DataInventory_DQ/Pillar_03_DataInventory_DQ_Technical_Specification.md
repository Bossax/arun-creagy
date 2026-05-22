# Technical Specification: Pillar 3 — Baseline Data Inventory & Information Product Inventory (TOR §5.3.4–5.3.5)

## 0. Purpose (DAMA-aligned, Phase-1 realistic)

Pillar 3 exists to satisfy the TOR’s explicit requirement to deliver:

- an **Information Product Inventory** (TOR §5.3.4)
- a **Baseline Data Inventory** (TOR §5.3.5)

**Data quality is secondary**: in this phase, DQ exists primarily as **labels + caveats** applied to inventory rows (so downstream implementers can prioritize verification and avoid false certainty), not as a full measurement program.

It is intentionally written as a **TOR-first / Phase-1 governance standard** that can be executed manually (checklists + templates) and later automated in Project B.

- Pillar 1 and Pillar 8 store governance attributes (e.g., `Feasibility_Posture`, `Reference_Status`) at row/entity level.
- Pillar 3 standardizes **how uncertainty, provenance, and minimum metadata** are expressed in inventory rows.
- Pillar 7 defines **who decides** (decision rights) and **how decisions are executed** (cadence + escalation + decision log).

## 1. Data Structural Requirements

### 1.1 Mandatory artifact set (acceptance gate)

1. **Information Product Inventory** (products/services)
2. **Baseline Data Inventory** (raw datasets)

Supporting artifacts (optional):

- Gap analysis tables/matrices that derive from these inventories
- Evidence notes that justify row entries

### 1.1 Artifact format

*   **Artifact Format**: Inventory minimum standard + governance label definitions (for consistent inventory entries).
*   **File Type**: Markdown (.md) as the normative spec + inventories in spreadsheet/CSV form.

### 1.2 Mandatory gate semantics (normative)

*   **G1 — Classification + publishing rail**
    * **Fields**: `Data_Classification` (Open / G2G-GDX / Internal), `Publication_Rail`.
    * **Rule**: every asset must declare which rail it can travel on and why.
*   **G2 — Inventory metadata minima (catalog-level)**
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

*   **`Feasibility_Posture`** (used in Pillar 1)
    * `Validated`: confirmed by a named source owner or authoritative documentation.
    * `Assumed`: inferred from public materials; not confirmed by the source owner.
    * `Unknown`: not enough evidence; requires follow-up.
*   **Metadata completeness posture**
    * Missing values should be recorded as `Unknown` with a limitations note; do not fabricate placeholders.

## 2. Verification Criteria

*   **Inventory completeness (bounded)**: inventories must cover the high-priority items evidenced through interviews/workshops and DCCE baseline materials; missing items are allowed but must be explicitly marked as gaps (not silently omitted).
*   **National alignment (where applicable)**: labels/fields should be compatible with DGA rails and catalog harvesting practices, but this project does not certify compliance for every dataset.
*   **Honesty over completeness**: a record is non-compliant if it hides uncertainty (e.g., fake cadence, fake steward). Use `Unknown` + limitations statements instead.
*   **Denominator disclosure**: if `Canonical_Boundary_ID` is not Admin, the asset must explicitly declare the denominator and any required crosswalk.
*   **User transparency**: every asset/product must surface the limitations statement (G2) and maturity label (G5) in human-readable form.

## 3. Implementation Constraints

*   **Phase-1 posture (no overclaim)**: in this CRDB phase, inventory labels can be executed procedurally (checklists + review). Full automation is a Project B responsibility.
*   **Non-negotiable for future implementation**: Project B must implement these gates as enforceable workflow controls, but Pillar 5 does not assume the existence of a running validation engine today.
*   **Audit trail requirement (future enforcement)**: the implementation must preserve decision/audit history; bypassing gates becomes a contract non-compliance issue in Project B.
