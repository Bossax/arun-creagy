# Data Lineage: CRI Phase 1 Impact System

This document provides a human-readable map of the transformation logic used to build the CRI Phase 1 analytical tables, bridging the gap between raw Bronze files and the Gold analytical layer.

---

## 1. DDPM Village Stream
*   **Raw Source**: `0_bronze/ddpm/*.csv` (11 yearly files: 2557–2567).
*   **Processing Script**: `consolidate_village_stats_ddpm.ipynb`
    *   **Logic**:
        *   **Dynamic Parsing**: Years 2565–2567 use dual headers (EN/TH); script skips the Thai header row.
        *   **Standardization**: Village codes are zero-padded to 8 digits.
        *   **Consolidation**: Merges ~210,000 village-level observations into a single master silver file.



## 2. DDPM Financial Stream
*   **Raw Source**: `0_bronze/ddpm/สถิติข้อมูลการใช้จ่ายเงินทดรองราชการ ปี 2546 - ปัจจุบัน.xlsx`
*   **Processing Script**: `clean_financial_relief_data_ddpm.ipynb`
    *   **Logic**:
        *   **Multi-Sheet Extraction**: Iteratively slices sheets (Indices 4–18 for Hazards, 28–42 for Sectors).
        *   **Layout Adaptation**: Handles structural changes between older and newer sheet formats.
        *   **Aggregation**: Consolidates 1,872 provincial records for both Hazard and Sector-based relief.

---

## 3. TEI Pilot Baseline
*   **Raw Source**: `0_bronze/tei_pilot/*.csv`
*   **Role**: Provides the 8-year average (2559–2566) for Population and GPP.


## 4. Integrity Standards (Metadata Layer)

*   **Gold Spine Integrity**: All Gold tables must pass a Foreign Key (FK) check against `dim_location_master.csv`. Unmatched records are discarded to prevent spatial noise.
*   **Hazard Canonicalization**: Mappings between raw disaster strings and canonical IDs are documented in `data_dictionary.xlsx` (Sheet: `bridge_hazard_canonical`) when available; the current in-repo canonical lookup table is `data/2_gold/dim_hazard_canonical.csv`.

## 5. Standardization & Exclusion Rules

To ensure spatial consistency across the CRI, the following rules are applied during the transformation from Silver to Gold:

### 5.1 Name Normalization
The following variants are normalized to "กรุงเทพมหานคร" (Province Code 10):
*   `กรุงเทพ` (From TEI Pilot)
*   `กทม.` (From DDPM Silver)
*   `กรุงเทพฯ` (From DDPM Silver)

### 5.2 Administrative Exclusions
*   **Non-Spatial Agencies**: Records associated with `หน่วยงานในสังกัด` (Affiliated Agencies) are **excluded** from the CRI pipeline.
*   **Reason**: These represent line-agency expenditures that cannot be spatially attributed to a specific province or village, and would introduce noise into the spatial risk index.
*   **Reference**: These rules are intended to be maintained in `metadata/standardization_mapping.csv`; current Stage 3 audit did not verify that file in this directory tree and treats it as an unresolved dependency.

-