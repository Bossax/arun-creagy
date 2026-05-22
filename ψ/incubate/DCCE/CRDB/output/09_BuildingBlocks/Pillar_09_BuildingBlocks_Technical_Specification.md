# Technical Specification: Pillar 9 - NCAIF Building Blocks (TOR 5.2) + Budgeting/Strategy-Oriented Presentation (Catalog Secondary)

## 0. Grounding note (contract reality + project history)

This pillar exists to satisfy **TOR 5.2** (develop the National Climate Adaptation Information Framework + the data-management structure), not to prescribe a full platform implementation.

- TOR 5.2 requires a draft NCAIF structure covering major content classes and a draft data-management structure with sources, responsible agencies, and mechanisms: [`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:124)
- Project execution framing after the May 12–13 workshop emphasizes **production + ratification** and treats content outputs as governed assets (owned, versioned, linked): [`ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/2026-05-13_CRDB-Post-Workshop-Reorientation-Synthesis.md`](ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/2026-05-13_CRDB-Post-Workshop-Reorientation-Synthesis.md:32)

**Interpretation:** Pillar 8 is a **structured inventory of NCAIF building blocks** to support (a) a budgeting/strategy-oriented presentation as the primary interface, with (b) catalog/link-out as a secondary support layer.

## 1. Technical Requirements
*   **Artifact Format**: Building Block Inventory (NCAIF-first).
*   **File Type**: Structured Excel (.xlsx) or Comma-Separated Values (.csv).
*   **Mandatory Schema**:
    *   **`Block_ID`**: Unique identifier for the functional component (e.g., `BB-01`).
    *   **`Building_Block_Name`**: The descriptive name of the feature.
    *   **`Priority_Tier`**: Classification of priority for July 6 deliverables.
        * `Tier 1 (TOR-critical)` = required to credibly deliver TOR 5.2 outputs (framework + management structure)
        * `Tier 2 (Strongly supporting)` = materially improves usability/buy-in but can be reduced if time is constrained
        * `Tier 3 (Future expansion)` = beyond current TOR credibility needs
    *   **`NCAIF_Section`**: Explicit mapping to a draft NCAIF section (TOR 5.2.3 minimum categories):
        * Climate Data
        * Risk and Impact Assessment Data
        * Adaptation Guidelines and Examples
        * Adaptation Implementation Results
    *   **`Budget_Strategy_View`**: One of `Primary` / `Secondary` / `Not_Applicable`.
        * `Primary` blocks are those that directly support budgeting/strategy-oriented presentation (policy/decision-facing).
        * `Secondary` blocks are catalog/link-out support layers.
    *   **`Deliverable_Link`**: Which TOR deliverable(s) this block supports (e.g., TOR 5.2.3 draft framework, 5.2.5 revision cycle).
    *   **`Evidence_Anchor`**: Link to project evidence/history motivating the block (workshop outputs, synthesis notes, or prior artifacts).
    *   **`Dependency`**: List of other Pillars/blocks required (e.g., Pillar 1 CDM, Pillar 2 glossary, Pillar 5 gate semantics, Pillar 6 decision rights).

### 1.1 Minimum Tier-1 block set (grounded to TOR 5.2)

Tier 1 must include (at minimum):

1. **Budgeting/Strategy-oriented presentation spine** (Primary)
   - A structured set of “policy questions” / decision views mapped to NCAIF sections.
2. **Catalog/link-out layer (Secondary)**
   - Minimal “what exists + where it lives + how to request/access” listing aligned to the data-management structure requirement.
3. **Governance hooks (not full automation)**
   - Explicit inclusion of G1–G5 semantics references (Pillar 5) and decision workflow (Pillar 6) so content does not become stale.
4. **CDM/NCAIF translation rule**
   - Ensure every block maps to CDM subject areas and to NCAIF sections (prevents an unstructured portal-of-portals failure mode).

## 2. Verification Criteria
*   **TOR coverage**: Tier 1 blocks must collectively cover the four minimum NCAIF content categories required by TOR 5.2.3: [`ψ/incubate/DCCE/CRDB/inbox_source/CRDB - TOR.md`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:130).
*   **Budgeting/strategy primacy**: At least one Tier 1 block per NCAIF section must be marked `Budget_Strategy_View=Primary`.
*   **Catalog secondary constraint**: The catalog/link-out layer must be explicitly marked `Budget_Strategy_View=Secondary` to prevent scope drift into “catalog-only product”.
*   **Traceability to project history**: Every Tier 1 block must include an `Evidence_Anchor` (so the NCAIF is defensible as derived from consultation + synthesis, not invented).
*   **Governance anti-staleness**: Blocks that present “recommended baselines”, “official indicators”, or “implementation results” must declare which gate semantics apply (Pillar 5) and who owns updates (Pillar 6).

## 3. Implementation Constraints
*   **No overclaim**: This pillar does not require “fully operational” software modules in this CRDB phase. It specifies the building blocks as a **contractual baseline** and reporting structure for TOR 5.2.
*   **Semantic consistency**: All building blocks must use the semantics defined in Pillar 2 (glossary) and Pillar 1 (CDM) for labels and mappings.
*   **Governance dependency**: Any block that asserts an “official view” must be bound to Pillar 5 (gate semantics) and Pillar 6 (decision rights + cadence).
*   **Budget shield (still valid)**: If budget/time is constrained, preserve Tier 1 (TOR-critical) and reduce Tier 2/3.
