#agy
# Implementation Plan: CRDB Deliverables Simplification & 4-Pillar Consolidation

## Goal Description
The CRDB (Climate Risk Data Blueprint) project's current structure enforces a strict **9-Pillar physical directory taxonomy** (`output/01_...` through `09_...`) which was designed in May 2026 to ensure zero-discovery procurement. Over the course of the project, significant drift has occurred:
*   Three pillars (P3 Data Inventory, P8 Reference Data, P9 Building Blocks) have gone dormant.
*   Pillar 2 (Use Cases) pivoted to concrete *Service Dossiers* in Thai.
*   Pillar 5 (CDM) expanded to 41 entities but created a version mismatch with Pillar 4 (Glossary).
*   Pillar 6 (LDM) is highly mature but is missing from the `CRDB-Deliverable-Map.md` ledger.
*   Two versions of Pillar 5 CDM (D-036 and D-051) are both marked "Sealed" without supersession.

This plan consolidates the 9 physical pillars into **4 Simplified Core Deliverables (Pillars I-IV)**. This eliminates administrative overhead, integrates the LDM, reconciles CDM version control, and maps the output directly to the **3-layer decoupled architecture** proposed in the TOR70 analysis.

---

## User Review Required

> [!IMPORTANT]
> **Consolidation of Directory Names**:
> This plan will physically rename and move directory paths inside `ψ/incubate/DCCE/CRDB/output/` from the numeric `01_Sitemap_InterfaceMapping` - `09_BuildingBlocks` structure to the consolidated `01_Portal_Interface_and_Service_Dossiers` - `04_Data_Stewardship_and_Governance` structure. 
> 
> Any local shortcuts or references to the old 01-09 folders will need updating. Internal links inside the files will be updated as part of this task.

---

## Proposed Changes

### Component 1: Filesystem Restructuring (Directory Remapping)
We will physically move and group files under a new 4-directory structure in `ψ/incubate/DCCE/CRDB/output/`:

*   **`01_Portal_Interface_and_Service_Dossiers`** (Consolidates old P1, P2)
    *   `NCAIF_Detailed_Sitemap_v8.md`
    *   `บทสรุปความต้องการใช้งานบริการข้อมูลสารสนเทศด้านภูมิอากาศ_v6.md` (Service Dossiers)
    *   All corresponding spec sheets and UX evaluation reports.
*   **`02_Unified_Data_Schemas`** (Consolidates old P5, P6)
    *   `Entities-v3.csv` / `Relationships-v4.csv` / `Domains-v3.csv` (CDM v3)
    *   `Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md` and any Loss & Damage schema tables.
*   **`03_Semantic_Layer_and_Metadata_Standards`** (Consolidates old P3, P4, P8)
    *   `Glossary-v4.csv` and `Glossary-v4.md`
    *   `data_catalog_v3.csv` (Data Inventory)
    *   `Pillar_08_RefData_Matrix_Technical_Specification.md` (Reference Data codes)
*   **`04_Data_Stewardship_and_Governance`** (Consolidates old P7, P9)
    *   `คู่มือการใช้งานระบบธรรมาภิบาลข้อมูล...Data Governance User Manual.md`
    *   RACI Matrix sheets, SDLC guidelines, and the decommissioned stubs of P9.

---

### Component 2: Ledger Updates (T-E-D-A Compliance)
To ensure trace and audit consistency, we must update the CRDB project ledgers:

#### `[MODIFY]` `ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md`
1.  **Mark Supersession**: Reconcile CDM dual-seal by marking `D-036` (CDM v1, 17 entities) as **Superseded** and linking it forward to `D-051` (CDM v3, 41 entities).
2.  **Seal Pillar 6 (LDM)**: Register the Loss & Damage Data Model as a new deliverable ID (`D-057`) with status **Active (Canonical)**.
3.  **Remap Directory Paths**: Update the path references in the deliverable table to reflect the new 4-pillar folder names.
4.  **Register Consolidation Deliverable**: Append a new deliverable record (`D-058`) for the consolidated 4-pillar output package.

#### `[MODIFY]` `ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md`
*   Add a change log entry (`CH-036`) registering this structural reorganization, citing the motive to simplify deliverables and align with the TOR70 architecture.

#### `[MODIFY]` `ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md`
*   Add a trigger entry (`T-042`) recording Boss's directive to shift focus and simplify the deliverables.

#### `[MODIFY]` `ψ/incubate/DCCE/CRDB/CRDB-Evidence-Registry.md`
*   Add evidence entry (`E-070`) pointing to the git commit executing the directory and ledger remapping.

---

## Verification Plan

### Manual Verification
1.  **Directory Existence**: Confirm that the folders `01` through `04` contain the moved files and that the old `05` through `09` folders are retired/empty.
2.  **Broken Link Audit**: Perform a grep check on file references across `ψ/` to ensure no broken internal markdown links exist.
3.  **Ledger Integrity Check**: Verify that `CRDB-Deliverable-Map.md` accurately registers:
    *   CDM `D-036` $\rightarrow$ Superseded.
    *   LDM `D-057` $\rightarrow$ Sealed Active.
    *   Remapped paths for all re-allocated deliverables.

