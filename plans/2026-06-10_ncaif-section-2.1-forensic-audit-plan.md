# Forensic Processing Plan: NCAIF Section 2.1 Expansion (v2.1)

**Date**: 2026-06-10  
**Context**: Rebuilding Section 2.1 of the NCAIF Policy Report with empirical evidence.  
**Methodology**: Traceable Forensic Audit (generating CSV artifacts for verification).

---

## 1. Goal
To expand Section 2.1 into a 600-800 word forensic analysis that proves the structural data gaps of the NCAIF. Every claim must be backed by a **Traceable CSV Artifact** generated from the 260-dataset inventory.

## 2. Audit Phases & Traceable Artifacts

### Phase 1: The Multi-Dimensional Pivot Audit (The "Silo" Proof)
*   **Audit 1.1: HEV-Integration Ratio**
    *   **Logic**: Map `Data_Entity` to H (Climate Driver), E (Exposed Asset), or V (Sensitivity/Adaptive Capacity).
    *   **Output**: `tmp/audit_1.1_hev_distribution.csv`
*   **Audit 1.2: Hazard Deep-Dive (H-Only)**
    *   **Logic**: Analyze `Related Hazards` specifically for datasets tagged as `CLIMATE_DRIVER` or `HAZARD_MAP`.
    *   **Output**: `tmp/audit_1.2_hazard_distribution.csv`
*   **Audit 1.3: Exposure Deep-Dive (E-Only)**
    *   **Logic**: Analyze `Sectors` and `Data_Entity` specifically for `EXPOSED_ASSET` to identify what assets (Infrastructure, Social, Agri) are actually mapped.
    *   **Output**: `tmp/audit_1.3_exposure_distribution.csv`
*   **Audit 1.4: Vulnerability Deep-Dive (V-Only)**
    *   **Logic**: Analyze `Sectors` specifically for `SENSITIVITY` and `ADAPTIVE_CAPACITY`.
    *   **Output**: `tmp/audit_1.4_vulnerability_distribution.csv`
*   **Audit 1.5: Spatial Granularity Audit**
    *   **Logic**: Classify `Spatial Resolution` into **Local/Tactical** (Mooban, Tambon, Grid < 1km) vs **Strategic** (Province, National).
    *   **Output**: `tmp/audit_1.5_spatial_granularity.csv`

### Phase 2: The Utility Bottleneck Mapping (The "Static Trap" Proof)
*   **Audit 2.1: Format-to-Access Matrix**
    *   **Logic**: Cross-tabulate `data_format` (CSV, NetCDF, GIS vs PDF, XLS) and `accessible_condition` (Restricted vs Open).
    *   **Output**: `tmp/audit_2.1_format_access_trap.csv`
*   **Audit 2.2: Temporal Readiness Audit**
    *   **Logic**: Group `update_frequency_unit` into **Operational** (Daily, Weekly) vs **Archival** (Annual, Static).
    *   **Output**: `tmp/audit_2.2_temporal_readiness.csv`

### Phase 3: Impact-Driven Synthesis (Writing)
*   **Narrative Flow**: 
    1.  **The Quantitative Landscape**: Lead with results from `audit_1.1`.
    2.  **The Dimensional Imbalance**: Use `audit_1.2`, `1.3`, and `1.4` to show that while we have hazards (H), we lack the sectoral exposure (E) and vulnerability (V) data to calculate risk.
    3.  **The Spatial Failure**: Use `audit_1.5` to prove the failure of Service 05 (Engineering).
    4.  **The Institutional Bottleneck**: Use `audit_2.1` and `audit_2.2` to prove the "Manual Coordination Trap."

---

## 3. Data Source
- `ψ/incubate/DCCE/CRDB/output/03_DataInventory_DQ/data_catalog_v3.csv` (260 Datasets).

## 4. Operational Guardrail
- **No Sunk Analysis**: All Python analysis MUST save to one of the `ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/data_audit/audit_*.csv` files before I write the report.
- **Traceability**: If the user asks "where does 82% come from?", I must point to the specific CSV artifact.

---
**Status: READY FOR EXECUTION**
