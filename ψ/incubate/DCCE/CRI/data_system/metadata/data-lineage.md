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

## 3. DOPA Spatial Spine
- **URL**: https://drive.google.com/drive/folders/1zi3Z0l7wvsGN1p5YIWVVL3LFs3WnS7VQ
*   **Raw Source**: `0_bronze/dopa/thailanda-administrative-boundary/*.shp`
*   **Processing Scripts**:
    *   Tambon + Province enrichment (legacy combined): [`script/ELT/prep_dopa_boundaries.py`](ψ/incubate/DCCE/CRI/data_system/script/ELT/prep_dopa_boundaries.py:1)
    *   Province-only enrichment (preferred for province-only workflows): [`script/ELT/prep_dopa_province_boundaries.py`](ψ/incubate/DCCE/CRI/data_system/script/ELT/prep_dopa_province_boundaries.py:1)
    *   **Logic**:
        *   **Geometry Normalization**: Ensures CRS is set to WGS84 (EPSG:4326).
        *   **Forensic Alignment**: Applies 11 targeted nomenclature patches to resolve legacy attribute errors in the Bronze GIS file (e.g., renames, district shifts).
        *   **Enrichment**: Attaches canonical 6-digit `subdistrict_code` and 2-digit `province_code` from the **Gold** `dim_location_master`.
    *   **Outputs**: 
        *   `1_silver/dopa/tambon_boundaries_enriched.shp`
        *   `1_silver/dopa/province_boundaries_enriched.shp`

> Province-only note: `prep_dopa_province_boundaries.py` performs the province enrichment join against the Gold spine and writes `province_boundaries_enriched.shp` without reading or depending on tambon geometries.

---

## 4. Location Master (Gold Spine)
- **URL**: https://stat.bora.dopa.go.th/stat/statnew/statMenu/newStat/ccaa.php
*   **Raw Source**: `0_bronze/dopa/ccaatt.xlsx` (Master Hierarchy) + `0_bronze/dopa/code_village_dopa_2019.xls` (Village Names).
*   **Processing Script**: `etl_dopa_master.py`
    *   **Logic**:
        *   **Hierarchical Schema Validation**: Uses `ccaatt.xlsx` as the absolute sovereign schema for codes and names. Records with invalid parent codes are discarded.
        *   **Nomenclature Inheritance**: Parent names (Province/District/Subdistrict) are inherited strictly from the CCAATT master, overwriting all variants in the `code_village_dopa_2019.xls` list.
        *   **Hardening Tweaks**: 
            *   **Restoration of Official Names**: Corrects shortened names like "เมือง" back to the canonical "เมืองนครราชสีมา".
            *   **Spelling Consistency**: Enforces the official spelling from the CCAATT master (e.g., "เทพารักษ์" with 'ก').
            *   **Noise Reduction**: Purges 176 invalid village records caused by sliding rows or typos in the source list.
    *   **Output**: `2_gold/dopa/dim_location_master.csv` (The National Administrative Spine).

---

## 5. Workbook-Derived Bronze CSV Extraction Layer (2026-06-12 Bundle)

*   **Purpose**: Convert four manually curated Excel workbooks into source-near Bronze CSVs and extraction manifests before analytical normalization.
*   **Raw Source Folder**: `0_bronze/2026-06-12_cri_proj_data/`
*   **Source Workbooks**:
    *   `CRI Data - Heatwave.xlsx`
    *   `CRI Data - GPP.xlsx`
    *   `CRI Data - Government_Advanced_Payment.xlsx`
    *   `CRI Data - Population.xlsx`
*   **Exploration Script**: [`script/inspect_cri_workbooks.py`](ψ/incubate/DCCE/CRI/data_system/script/inspect_cri_workbooks.py:1)
    *   **Logic**:
        *   Inspects workbook sheet structures, candidate headers, and workbook-specific layout patterns.
        *   Confirms that extraction strategy must be sheet-family specific rather than generic workbook flattening.
*   **Bronze Extraction Scripts**:
    *   Shared definitions: [`script/extract_cri_definition_sheets.py`](ψ/incubate/DCCE/CRI/data_system/script/extract_cri_definition_sheets.py:1)
    *   Heatwave table: [`script/extract_heatwave_table.py`](ψ/incubate/DCCE/CRI/data_system/script/extract_heatwave_table.py:1)
    *   GPP tables: [`script/extract_gpp_tables.py`](ψ/incubate/DCCE/CRI/data_system/script/extract_gpp_tables.py:1)
    *   Government Advance Payment hazard sheets: [`script/extract_govt_adv_payment_hazard_sheets.py`](ψ/incubate/DCCE/CRI/data_system/script/extract_govt_adv_payment_hazard_sheets.py:1)
    *   Population tables: [`script/extract_population_tables.py`](ψ/incubate/DCCE/CRI/data_system/script/extract_population_tables.py:1)
*   **Bronze Policy**:
    *   Bronze preserves source-near layout and raw formulas where present.
    *   Derived values are not resolved in Bronze; they are deferred to Silver.
    *   Workbook-specific manifests document sheet structure, header interpretation, and extraction anomalies.
*   **Outputs**:
    *   `0_bronze/2026-06-12_cri_proj_data/definition_sheet_extracts/*`
    *   `0_bronze/2026-06-12_cri_proj_data/heatwave_extracts/*`
    *   `0_bronze/2026-06-12_cri_proj_data/gpp_extracts/*`
    *   `0_bronze/2026-06-12_cri_proj_data/govt_adv_payment_extracts/*`
    *   `0_bronze/2026-06-12_cri_proj_data/population_extracts/*`

---

## 6. Heatwave Workbook Stream (Bronze → Silver)

*   **Bronze Inputs**:
    *   `0_bronze/2026-06-12_cri_proj_data/heatwave_extracts/heatwave.raw.csv`
    *   `0_bronze/2026-06-12_cri_proj_data/heatwave_extracts/heatwave.manifest.json`
*   **Normalization Script**: [`script/normalize_heatwave_to_silver.py`](ψ/incubate/DCCE/CRI/data_system/script/normalize_heatwave_to_silver.py:1)
*   **Logic**:
    *   Splits workbook-derived wide columns into a long fact structure.
    *   Produces one row per `province_code + metric_name + time_scope`.
    *   Preserves source header text in lineage columns for traceability.
    *   Joins province identities against the Gold geography spine.
    *   Resolves canonical hazard against `dim_hazard_canonical.csv`. 
	    * I added a new row 'HEATWAVE' by hand
*   **Assumptions / Changes**:
    *   `2567` is treated as a single-year scope.
    *   `2561 - 2567` is treated as a multi-year aggregate scope.
    *   Heatwave metrics are modeled as `Deaths` and `Injured` under the health sector.
    *   Canonical hazard is required for analysis; source-specific hazard-type alignment may lag behind without blocking the Silver fact table.
*   **Outputs**:
    *   [`1_silver/heatwave/silver_heatwave_impact_long.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/heatwave/silver_heatwave_impact_long.csv)
    *   [`1_silver/heatwave/heatwave_normalization_report.json`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/heatwave/heatwave_normalization_report.json)

---

## 7. GPP Workbook Stream (Bronze → Silver)

*   **Bronze Inputs**:
    *   `0_bronze/2026-06-12_cri_proj_data/gpp_extracts/gpp-67.raw.csv`
    *   `0_bronze/2026-06-12_cri_proj_data/gpp_extracts/gpp-60-67.raw.csv`
    *   `0_bronze/2026-06-12_cri_proj_data/gpp_extracts/gpp.manifest.json`
*   **Normalization Script**: [`script/normalize_gpp_to_silver.py`](ψ/incubate/DCCE/CRI/data_system/script/normalize_gpp_to_silver.py:1)
*   **Logic**:
    *   Unfolds province/code blocks into row-level analytical facts.
    *   Extracts metric rows under each province block.
    *   Expands yearly wide columns into long annual rows.
    *   Prefers the standalone `2567` extract over the multi-year extract for year `2567`.
    *   Joins province labels to the Gold geography spine where possible.
*   **Assumptions / Changes**:
    *   Grain is one row per `area_code_or_area_label + metric_name + year`.
    *   `2024p` is treated as a provisional-status indicator rather than a distinct year.
    *   Minor yearly-sum vs `Total` mismatches are treated as floating-point validation noise until a tolerance policy is finalized.
*   **Outputs**:
    *   [`1_silver/gpp/silver_gpp_annual_long.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/gpp/silver_gpp_annual_long.csv)
    *   [`1_silver/gpp/gpp_normalization_report.json`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/gpp/gpp_normalization_report.json)

---

## 8. Government Advance Payment Workbook Stream (Bronze → Silver)

*   **Bronze Inputs**:
    *   `0_bronze/2026-06-12_cri_proj_data/govt_adv_payment_extracts/govt_adv_payment-อุทกภัย.raw.csv`
    *   `0_bronze/2026-06-12_cri_proj_data/govt_adv_payment_extracts/govt_adv_payment-ภัยแล้ง.raw.csv`
    *   `0_bronze/2026-06-12_cri_proj_data/govt_adv_payment_extracts/govt_adv_payment-วาตภัย.raw.csv`
    *   `0_bronze/2026-06-12_cri_proj_data/govt_adv_payment_extracts/govt_adv_payment.manifest.json`
*   **Province Lookup Bridge**:
    *   [`script/build_province_code_lookup.py`](ψ/incubate/DCCE/CRI/data_system/script/build_province_code_lookup.py:1)
    *   Output: [`1_silver/dopa/province_code_lookup.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/dopa/province_code_lookup.csv)
    *   Source: `archive_stage3_legacy/data/1_silver/stage3_dopa_province_boundary_code_crosswalk.csv`
*   **Normalization Script**: [`script/normalize_govt_adv_payment_to_silver.py`](ψ/incubate/DCCE/CRI/data_system/script/normalize_govt_adv_payment_to_silver.py:1)
*   **Logic**:
    *   Merges three hazard-specific workbook extracts into one hazard-aware analytical stream.
    *   Melts year columns `2560–2567` into annual long rows.
    *   Separates `2560 - 2567` into a period-total fact table.
    *   Maps Thai hazard names to canonical hazard identities using `dim_hazard_canonical.csv`.
    *   Joins `จังหวัด` strings via `province_code_lookup.csv` to obtain `province_code` and canonical province naming.
    *   Excludes non-province rows such as blank spacer rows, `วงเงินอำนาจอธิบดี`, `กทม.`, and `Total`.
*   **Assumptions / Changes**:
    *   Bronze formulas in total columns are preserved as raw source evidence.
    *   Silver period totals are derived from annual values and compared to Bronze period values when numeric.
    *   Province-level join uses the dedicated province lookup table because the active `dim_location_master.csv` snapshot is not directly province-oriented for this workflow.
*   **Outputs**:
    *   [`1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv)
    *   [`1_silver/govt_adv_payment/silver_govt_adv_payment_period_total.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/silver_govt_adv_payment_period_total.csv)
    *   [`1_silver/govt_adv_payment/govt_adv_payment_normalization_report.json`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/govt_adv_payment_normalization_report.json)

---

## 9. Population Workbook Stream (Bronze → Silver, in progress)

*   **Bronze Inputs**:
    *   `0_bronze/2026-06-12_cri_proj_data/population_extracts/pop67.raw.csv`
    *   `0_bronze/2026-06-12_cri_proj_data/population_extracts/pop60-67.raw.csv`
    *   `0_bronze/2026-06-12_cri_proj_data/population_extracts/population.manifest.json`
*   **Bronze Extraction Script**: [`script/extract_population_tables.py`](ψ/incubate/DCCE/CRI/data_system/script/extract_population_tables.py:1)
*   **Current State**:
    *   Bronze extraction is complete.
    *   Header flattening for `pop60-67` was corrected so `2567` remains its own year column.
    *   Bronze keeps duplicated/raw code fields source-near and preserves formulas for later Silver derivation.
*   **Planned Silver Logic**:
    *   `pop67` → monthly geography-level population fact table.
    *   `pop60-67` → annual long population fact table plus separate period-total handling.
    *   Formula-derived and resolved subdistrict code fields will be separated semantically in Silver.
*   **Planned Outputs**:
    *   `1_silver/population/...` (to be materialized after normalization implementation)

---

## 11. DDPM Provincial Impact (Gold Fact Tables | 2560–2567)

*   **Purpose**: Aggregated provincial-level impact scores and fiscal gap analysis.
*   **Inputs**: 
    *   **Tambon Gold Fact Table**: `2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv`
    *   **Financial Relief (Silver)**: `1_silver/ddpm/master_financial_relief_by_hazard.csv`
*   **Logic**:
    *   **Aggregation**: Sums tambon-level metrics (`affected_households_sum`, `deaths_sum`) to provincial level.
    *   **Normalization**: Applies **min-max scoring** (0.0 to 1.0) across all provinces for presentation-ready mapping.
    *   **Gap Analysis**: Joins impact sums with `วงเงินอนุมัติ` (Approved Relief). 
    *   **Gap Flag**: Sets `admin_gap_flag` to TRUE if `affected_households_sum > 0` AND `approved_relief == 0`, signaling potential under-reporting or fiscal-access barriers.
*   **Outputs**: `2_gold/ddpm/fact_ddpm_province_impact_climate_2560_2567.csv`

---

## 13. Stage 1 Export (Analytical Layer)

*   **Purpose**: Final transformation and packaging of all metrics into the JSON data contract used by the CRI Web App v3.
*   **Processing Script**: [`script/tmp_stage1_export.py`](ψ/incubate/DCCE/CRI/data_system/script/tmp_stage1_export.py:1)
*   **Inputs**:
    *   **Gold Tambon Impacts**: `2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv` (Cumulative sums).
    *   **Silver Population/Households**: `1_silver/population/silver_population_annual.csv` & `silver_household_annual.csv`.
    *   **Silver GPP/Loss**: `1_silver/gpp/...` & `1_silver/govt_adv_payment/...`.
    *   **Silver Heatwave**: `1_silver/heatwave/silver_heatwave_impact_long.csv`.
*   **Logic**:
    *   **Averaging (2560–2567)**: 
        *   It reads the cumulative sums from the Gold/Silver layers, aggregates them by `province_code`, and divides by **8.0** to calculate the annual average.
        *   **Heat Exception**: Heat metrics are divided by **7.0** to reflect the 2561–2567 data availability window.
    *   **Rate Calculation**:
        *   **Affected Rate**: Calculated as `(Annual Avg Affected Households / Annual Avg Total Households) * 100`.
        *   **Incidence Multiplier**: Because the numerator counts *events* and a single household can be affected by multiple disasters in a year, this rate is an **incidence frequency multiplier** (where >100% indicates multiple impacts per household per year).
    *   **Normalization**: Applies min-max normalization to generate the composite **CRI Score**.
*   **Outputs**: 
    *   `build_exports/stage1/period_2560_2567/*.json`
    *   `build_exports/stage1/period_2567/*.json`
    *   `build_exports/stage1/spatial/*.geojson`

---


---

## 9. Forensic Patch Registry (GIS Alignment)

The following 11 targeted patches were applied in `prep_dopa_boundaries.py` to bridge the gap between legacy GIS attributes (Bronze) and the modern Gold Spine:

| Province | GIS District | GIS Subdistrict | Resolution (Target DOPA Name/District) | Reason |
| :--- | :--- | :--- | :--- | :--- |
| **อุตรดิตถ์** | ท่าปลา | ท่าแฝก | **น้ำปาด**, ท่าแฝก (530407) | Subdistrict moved district in 2015. |
| **อุบลราชธานี** | สิรินธร | นิคมลำโดมน้อย | **นิคมสร้างตนเองลำโดมน้อย** (342905) | Full name required for Gold match. |
| **เชียงใหม่** | แม่วาง | ทุ่งปี้ | **ทุ่งปี๊** (502202) | Tone mark mismatch (๊ vs ี้). |
| **ชัยภูมิ** | เกษตรสมบูรณ์ | ซับสีทอง | **เมืองชัยภูมิ**, ซับสีทอง (360119) | District shift since GIS capture. |
| **หนองคาย** | เมืองหนองคาย | สองห้อง | **โพนสว่าง** (430111) | Renamed to avoid local duplication. |
| **เชียงใหม่** | อมก๋อย | สบโขง | **แม่หลอง** (501805) | Renamed to align with local geography. |
| **บึงกาฬ** | เมืองบึงกาฬ | หนองเข็ง | **โนนสว่าง** (380103) | Renamed to avoid local duplication. |
| **นครสวรรค์** | เมืองนครสวรรค์ | วัดไทร | **วัดไทรย์** (600113) | Gold Spine uses official spelling. |
| **แพร่** | เมืองแพร่ | วังหงษ์ | **วังหงส์** (540113) | Gold Spine uses official spelling. |
| **มหาสารคาม** | ยางสีสุราช | ขามเรียน | **สร้างแซ่ง** (441106) | Renamed in modern DOPA hierarchy. |
| **อุบลราชธานี** | วารินชำราบ | ห้วยขะยูง | **ห้วยขะยุง** (341524) | Corrected official spelling (ย vs ยู). |

---

## 10. Standardization & Exclusion Rules

To ensure spatial consistency across the CRI, the following rules are applied during the transformation from Silver to Gold:

### 8.1 Name Normalization
The following variants are normalized to "กรุงเทพมหานคร" (Province Code 10):
*   `กรุงเทพ` (From TEI Pilot)
*   `กทม.` (From DDPM Silver)
*   `กรุงเทพฯ` (From DDPM Silver)

### 8.2 Administrative Exclusions
*   **Non-Spatial Agencies**: Records associated with `หน่วยงานในสังกัด` (Affiliated Agencies) are **excluded** from the CRI pipeline.
*   **Reason**: These represent line-agency expenditures that cannot be spatially attributed to a specific province or village, and would introduce noise into the spatial risk index.
*   **Reference**: These rules are maintained in `metadata/standardization_mapping.csv`.
 from the CRI pipeline.
*   **Reason**: These represent line-agency expenditures that cannot be spatially attributed to a specific province or village, and would introduce noise into the spatial risk index.
*   **Reference**: These rules are maintained in `metadata/standardization_mapping.csv`.
