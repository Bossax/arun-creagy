# Technical Specification: Pillar 2 - Business Glossary

## 0. Purpose and grounding (TOR-supporting, not TOR-named)

The TOR does not explicitly name a “Business Glossary”, but it implicitly requires **semantic consistency** across:

- NCAIF domains + Draft Data Management Structure ([`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:130))
- Baseline Data Inventory categories (driver / hazard / exposure / sensitivity / adaptive capacity / impact / response / loss & damage) ([`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:169))
- MVD + reporting-form design (cross-agency comparability depends on stable definitions) ([`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:190))

Therefore Pillar 2 is treated as a **TOR-supporting execution rail**: a controlled semantic layer that prevents definitional drift across deliverables.

Primary seed sources that already exist in this repo:

- CDM entity vocabulary and business-rule distinctions (seed term list + `CDM_Entity_Link` mapping): [`ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md:56)
- Governance question framing for “glossary scope + definitions authority”: [`ψ/incubate/DCCE/CRDB/inbox_note/FGD2_plan_2026-02-26.md`](ψ/incubate/DCCE/CRDB/inbox_note/FGD2_plan_2026-02-26.md:127)

## 1. Data Structural Requirements
*   **Artifact Format**: Normalized Business Glossary.
*   **File Type**: Comma-Separated Values (.csv) or Structured Excel (.xlsx).
*   **Mandatory Schema**:
    *   **`Term_ID`**: A unique alphanumeric identifier for each term (e.g., `TERM_001`).
    *   **`Canonical_Name`**: The official technical name of the term in English and Thai.
    *   **`Business_Definition`**: A concise explanation of the term’s meaning **as used in CRDB/NCAIF/TOR delivery**.
    *   **`Semantic_Owner`**: The DCCE sub-division or external agency responsible for the term's authority.
    *   **`CDM_Entity_Link`**: Mapping to the corresponding entity in the Pillar 1 Climate Data Model.
    *   **`Usage_Tags`**: Metadata labels for classification (e.g., `Hazard`, `Vulnerability`, `NAP_Aligned`).
*   **Semantic Coverage**: The glossary must cover a minimum of 100 terms across the following categories:
    1.  **Climate Science Foundations** (Scenarios, Drivers, RCP/SSP).
    2.  **Disaster Risk Concepts** (Hazard, Exposure, Vulnerability, Risk).
    3.  **Impact & Outcome Metrics** (Loss, Damage, Sensitivity).
    4.  **Adaptation & Resilience** (Options, Actions, Transformative Capacity).

### 1.1 Recommended additional columns (execution guidance)

To reduce disputes and support phased approval, extend the schema with:

* **`Term_Status`**: `Draft` | `Proposed` | `Approved_Core` | `Approved_Extended` | `Deprecated`
* **`Definition_Tier1`**: Tier‑1 plain-language definition (policy/non-technical)
* **`Definition_Tier2`**: Tier‑2 technical definition (analyst/engineer)
* **`Source_Anchor`**: pointer to the evidence/authority used (e.g., IPCC/Sendai/Thaiwater/DCCE decision)
* **`Synonym_Of_Term_ID`**: if this row is a synonym/alias
* **`Conflict_Note`**: short note when definitions differ across agencies (until resolved)

## 2. Quality Assurance & Verification Criteria
*   **Approval Status (phased, to avoid rubber-stamping)**:
    * **Core set**: a bounded list of high-impact terms MUST be `Approved_Core` by the designated `Semantic_Owner` (director ratification optional if governance mandates it).
    * **Extended set**: additional terms may remain `Draft/Proposed` without blocking TOR delivery, but must carry `Source_Anchor` + owner pathway.
*   **Semantic Consistency (practical rule)**:
    * duplicates are discouraged;
    * **synonym mapping is mandatory** (`Synonym_Of_Term_ID`) instead of forcing immediate canonicalization.
    * if conflicts exist, preserve the conflict with provenance (`Conflict_Note`) until the steward resolves it.
*   **Cross-Pillar Alignment (meaning-first, not string-identity)**:
    * Every CDM/LDM *concept* used in Pillar 1/3 must map to a `Term_ID`.
    * Definitions may have Tier‑1 vs Tier‑2 views, but must share a single canonical meaning (`Term_ID`).
*   **Readability**: Definitions must be legible to Tier 1 audiences (Policy makers and non-technical staff) without sacrificing technical precision.

## 3. Implementation Constraints
*   **Universal Semantic Layer (USL) scope control**:
    * The glossary is mandatory for **core domain concepts** and **required metadata fields**.
    * Contractors may propose UI microcopy and alternative labels only if they map to the same `Term_ID` and do not change the canonical meaning.
*   **Tagging Mandate (minimum viable tagging)**:
    * Do not require “tag everything” up front.
    * Define a minimal publish gate tag set first (e.g., hazard type, sector, spatial unit, time period, methodology status) and phase in full tagging later.
*   **Update Protocol (change control)**:
    * Modifications to `Approved_Core` terms require a formal semantic revision request.
    * Draft/proposed terms may iterate with lighter governance, but must preserve history (append-only change log or revision notes).

---

## 4. Execution guidance: how to build Pillar 2 from existing assets

1. **Seed the term backlog from the CDM** (entities + key distinctions like event vs driver, exposure vs vulnerability): [`ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md:56)
2. **Add TOR category vocabulary as mandatory `Usage_Tags`** to enforce alignment with inventories and MVD: [`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:169)
3. **Define the core approved set** (small):
   - minimum: the TOR category terms + CDM’s core entities + the most misused policy terms (risk/hazard/vulnerability/impact/loss & damage).
4. **Assign `Semantic_Owner` using the FGD2 “authority” question set** (even if provisional): [`ψ/incubate/DCCE/CRDB/inbox_note/FGD2_plan_2026-02-26.md`](ψ/incubate/DCCE/CRDB/inbox_note/FGD2_plan_2026-02-26.md:127)
5. **Publish the glossary as a spreadsheet/CSV appendix** for Deliverable packaging (Design Report appendix + content tagging reference) and treat it as a living controlled artifact.
