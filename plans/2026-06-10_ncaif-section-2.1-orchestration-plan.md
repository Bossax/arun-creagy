# Orchestration Plan: NCAIF Section 2.1 Forensic Expansion

**Date**: 2026-06-10  
**Context**: High-level multi-agent coordination for the forensic audit and policy report writing.  
**Goal**: Transform 260 datasets into a 600-800 word evidence-based Section 2.1.

---

## 🏗️ Phase A: Forensic Data Audit (The Auditor Agent)
*   **Agent**: `generalist` (Sub-agent)
*   **Directive**: Execute Phase 1 and 2 of `plans/2026-06-10_ncaif-section-2.1-forensic-audit-plan.md`.
*   **Requirements**:
    *   Write Python scripts to process `ψ/incubate/DCCE/CRDB/output/03_DataInventory_DQ/data_catalog_v3.csv`.
    *   Output 5-7 distinct CSV artifacts to `ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/data_audit/`.
    *   Write `HANDOFF_AUDIT.md` to the same folder when complete.
*   **Status**: [✅] DONE

---

## ⚖️ Phase B: Quality Assessment (The Reviewer Agent)
*   **Agent**: `generalist` (Sub-agent)
*   **Directive**: Audit the CSV artifacts and handoff from Phase A.
*   **Criteria**:
    *   Categorical Integrity: Did H/E/V get mapped correctly?
    *   Traceability: Can the raw numbers be traced back to the source catalog?
    *   Completeness: Are all 5 planned audits present?
*   **Status**: [✅] DONE

---

## ✍️ Phase C: Narrative Generation (The Stylist Agents)
*   **Methodology**: `writing-th` skill + `ψ/memory/style/STYLE_PACK_NCAIF-Institutional.md`.
*   **Workspace**: `ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/pillar_analysis/`

| Step | Focus | Agent Target | Status |
| :--- | :--- | :--- | :--- |
| **C.1** | The Quantitative Landscape (HEV Distribution) | `generalist` | [✅] DONE |
| **C.2** | Dimensional Imbalance (The Missing E/V Gaps) | `generalist` | [✅] DONE |
| **C.3** | Spatial Failure (Provincial vs. Tactical) | `generalist` | [✅] DONE |
| **C.4** | Institutional Bottleneck (The Access Trap) | `generalist` | [✅] DONE |

---

## 🏛️ Phase D: Final Narrative Synthesis (The Main Agent)
*   **Directive**: Read intermediate artifacts from Phase C and the audit CSVs.
*   **Final Output**: Create a new file `Section_2.1_Forensic_Expansion_v3.4.md`.
*   **Key Metrics for Success**:
    *   [✅] Clear distinction between Hazard abundance vs. Exposure scarcity.
    *   [✅] Proof of agency-specific info patterns (5-6 key agencies).
    *   [✅] Zero English parentheticals (Style Pack compliance).
    *   [✅] 600-800 words of forensic evidence.

---
**Status**: [✅] COMPLETED
