# Data Lineage: CRI Phase 1 Impact System

This document provides a human-readable map of the transformation logic used to build the CRI Phase 1 analytical tables, bridging the gap between raw Bronze files, Silver/Gold medallion layers, and Stage 1 exported app assets.

---

## 1. DDPM Village Stream (Disaster Impact)
*   **Raw Source**: `0_bronze/ddpm/*.csv` (11 yearly files: 2557–2567).
*   **Processing Script**: [`script/ELT/consolidate_ddpm_master_silver.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/ELT/consolidate_ddpm_master_silver.py)
*   **Gold Transformation**: [`script/ELT/build_gold_ddpm_tambon_impact_climate_2560_2567.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/ELT/build_gold_ddpm_tambon_impact_climate_2560_2567.py)
    *   **Logic**:
        *   **Dynamic Parsing & Header Stripping**: Years 2565–2567 use dual headers (EN/TH); script filters out sub-header row 0 (`Disaster Date != 'วันที่เกิดภัย'`).
        *   **Numeric Comma Sanitization**: Uses `parse_clean_numeric()` to strip thousand-separator commas (`"1,422"`) and empty whitespace cells (`" "`), recovering **1,100,814 households nationwide** in 2567 that were previously lost to `NaN` coercion.
        *   **Standardization**: Subdistrict codes are cleaned and padded to 6 digits (`subdistrict_code`), and province codes are padded to 2 digits.
        *   **Consolidation**: Merges ~210,000 village-level observations into `1_silver/ddpm/master_village_disaster_stat_2557_2567.csv` and builds Gold fact table `2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv`.

---

## 2. DDPM Financial Stream
*   **Raw Source**: `0_bronze/ddpm/สถิติข้อมูลการใช้จ่ายเงินทดรองราชการ ปี 2546 - ปัจจุบัน.xlsx`
*   **Processing Script**: `clean_financial_relief_data_ddpm.ipynb`
    *   **Logic**:
        *   **Multi-Sheet Extraction**: Iteratively slices sheets (Indices 4–18 for Hazards, 28–42 for Sectors).
        *   **Layout Adaptation**: Handles structural changes between older and newer sheet formats.
        *   **Aggregation**: Consolidates 1,872 provincial records for both Hazard and Sector-based relief.

---

## 3. DOPA Spatial Spine
- **URL**: https://drive.google.com/drive/folders/1zi3Z0l7wvsGN1p5YIWVVL3LFs3WnS7VQ
*   **Raw Source**: `0_bronze/dopa/thailanda-administrative-boundary/*.shp`
*   **Processing Scripts**:
    *   Tambon + Province enrichment (legacy combined): [`script/ELT/prep_dopa_boundaries.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/ELT/prep_dopa_boundaries.py)
    *   Province-only enrichment (preferred for province-only workflows): [`script/ELT/prep_dopa_province_boundaries.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/ELT/prep_dopa_province_boundaries.py)
    *   **Logic**:
        *   **Geometry Normalization**: Ensures CRS is set to WGS84 (EPSG:4326).
        *   **Forensic Alignment**: Applies 11 targeted nomenclature patches to resolve legacy attribute errors in the Bronze GIS file (e.g., renames, district shifts).
        *   **Enrichment**: Attaches canonical 6-digit `subdistrict_code` and 2-digit `province_code` from the **Gold** `dim_location_master.csv`.
    *   **Outputs**: 
        *   `1_silver/dopa/tambon_boundaries_enriched.shp`
        *   `1_silver/dopa/province_boundaries_enriched.shp`

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
            *   **Spelling Consistency**: Enforces official spelling from CCAATT master (e.g., "เทพารักษ์" with 'ก').
            *   **Noise Reduction**: Purges 176 invalid village records caused by sliding rows or typos.
    *   **Output**: `2_gold/dopa/dim_location_master.csv` (The National Administrative Spine).

---

## 5. Workbook-Derived Bronze CSV Extraction Layer (2026-06-12 Bundle)

*   **Purpose**: Convert four manually curated Excel workbooks into source-near `.raw.csv` intake files and extraction manifests before analytical normalization.
*   **Raw Source Folder**: `0_bronze/2026-06-12_cri_proj_data/`
*   **Source Workbooks**:
    *   `CRI Data - Heatwave.xlsx`
    *   `CRI Data - GPP.xlsx`
    *   `CRI Data - Government_Advanced_Payment.xlsx`
    *   `CRI Data - Population.xlsx`
*   **Bronze Extraction Scripts**:
    *   Shared definitions: [`script/extract_cri_definition_sheets.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/extract_cri_definition_sheets.py)
    *   Heatwave table: [`script/extract_heatwave_table.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/extract_heatwave_table.py)
    *   GPP tables: [`script/extract_gpp_tables.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/extract_gpp_tables.py)
    *   Government Advance Payment hazard sheets: [`script/extract_govt_adv_payment_hazard_sheets.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/extract_govt_adv_payment_hazard_sheets.py)
    *   Population tables: [`script/extract_population_tables.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/extract_population_tables.py)
*   **Outputs**:
    *   `0_bronze/2026-06-12_cri_proj_data/heatwave_extracts/heatwave.raw.csv`
    *   `0_bronze/2026-06-12_cri_proj_data/gpp_extracts/gpp-67.raw.csv` & `gpp-60-67.raw.csv`
    *   `0_bronze/2026-06-12_cri_proj_data/govt_adv_payment_extracts/govt_adv_payment-*.raw.csv`
    *   `0_bronze/2026-06-12_cri_proj_data/population_extracts/pop67.raw.csv` & `pop60-67.raw.csv`

---

## 6. Heatwave Casualties & Impact Stream (Bronze $\rightarrow$ Silver)

*   **Primary Agency Data Owner**: **Department of Health (DOH / กรมอนามัย, Ministry of Public Health)**
*   **Bronze Inputs**: `0_bronze/2026-06-12_cri_proj_data/heatwave_extracts/heatwave.raw.csv`
*   **Normalization Script**: [`script/normalize_heatwave_to_silver.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/normalize_heatwave_to_silver.py)
*   **Logic**:
    *   Parses pipe-delimited multi-level headers (`2561 - 2567 | Deaths`, `Injured_2`) into canonical long facts.
    *   Models heatwave casualties as `HEAT_DEATHS` and `HEAT_INJURED` under health sector.
    *   Computes standalone **Heatwave Casualty Score (`heat_score.json`)** via equal 50%-50% MinMax weighting ($0.5 \times s_{\text{deaths}} + 0.5 \times s_{\text{injured}}$).
*   **Outputs**:
    *   [`1_silver/heatwave/silver_heatwave_impact_long.csv`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/heatwave/silver_heatwave_impact_long.csv)

---

## 7. NESDC GPP Workbook Stream (Bronze $\rightarrow$ Silver)

*   **Primary Agency Data Owner**: **NESDC (สภาพัฒน์ / Office of the National Economic and Social Development Council)**
*   **Bronze Inputs**: `gpp_extracts/gpp-67.raw.csv` & `gpp-60-67.raw.csv`
*   **Normalization Script**: [`script/normalize_gpp_to_silver.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/normalize_gpp_to_silver.py)
*   **Logic**:
    *   Parses pipe-delimited headers (`2567 | 2024p`), mapping `2024p` preliminary GPP estimates to `2567`.
    *   Applies explicit $\times 1,000,000$ unit scaling (raw GPP published in **Million THB** $\rightarrow$ **THB**).
*   **Outputs**:
    *   [`1_silver/gpp/silver_gpp_annual_long.csv`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/gpp/silver_gpp_annual_long.csv)

---

## 8. Government Advance Payment Stream (Bronze $\rightarrow$ Silver)

*   **Primary Agency Data Owner**: **Ministry of Finance (กค. / Comptroller General's Department & DDPM)**
*   **Bronze Inputs**: `govt_adv_payment_extracts/govt_adv_payment-*.raw.csv`
*   **Normalization Script**: [`script/normalize_govt_adv_payment_to_silver.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/normalize_govt_adv_payment_to_silver.py)
*   **Logic**:
    *   Strips trailing whitespace in province names (`"กรุงเทพมหานคร "`) before DOPA master joins.
    *   Melts year columns into annual long rows and divides 7-year cumulative relief by 7.0 for annual averages.
*   **Outputs**:
    *   [`1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv)

---

## 9. Population Stream (Bronze $\rightarrow$ Silver)

*   **Primary Agency Data Owner**: **DOPA (กรมการปกครอง / Ministry of Interior)**
*   **Status**: **Completed Production Stream**
*   **Bronze Inputs**: `population_extracts/pop67.raw.csv` & `pop60-67.raw.csv`
*   **Normalization Script**: [`script/normalize_population_to_silver.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/normalize_population_to_silver.py)
*   **Logic**:
    *   Strips hidden UTF-8 BOM byte prefix (`\ufeff6712`) from column 0.
    *   Filters out national summary row 0 (`df["รหัสจังหวัด"] > 0`) to prevent double-counting 65.95M country total.
    *   **DOPA Multi-Registration Office Aggregation**: Resolves 1,368 split subdistrict records caused by dual District (`อำเภอ`) and Local Municipal (`ท้องถิ่น...`) registration offices by performing `groupby(["year_be", "province_code", "subdistrict_code"]).agg({"population_total": "sum", "household_total": "sum"})`, ensuring complete population totals without dropping municipal residents.
    *   Applies demographic ratio bounds ($0.5 \le R_{\text{subdistrict}} \le 10.0$) on population-per-household ratios.
*   **Outputs**:
    *   [`1_silver/population/silver_population_annual.csv`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/population/silver_population_annual.csv)
    *   [`1_silver/population/silver_household_annual.csv`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/population/silver_household_annual.csv)

---

## 10. Wildfire Ingestion Stream (Bronze $\rightarrow$ Gold)

*   **Raw Source**: `0_bronze/2026-07-16-cri-proj-data/Wildfire_hh_data.csv`
*   **Processing Script**: [`script/ELT/build_gold_wildfire_ddpm_fact.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/ELT/build_gold_wildfire_ddpm_fact.py)
*   **Outputs**:
    *   `2_gold/ddpm/fact_ddpm_tambon_impact_climate_wildfire_2560_2567.csv`

---

## 11. DDPM Provincial Impact (Gold Fact Tables | 2560–2567)

*   **Purpose**: Aggregated provincial-level impact scores and fiscal gap analysis.
*   **Inputs**: `2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv`
*   **Outputs**: `2_gold/ddpm/fact_ddpm_province_impact_climate_2560_2567.csv`

---

## 12. CRI Application Data Exporter Engine (v4.3 Release Upgrade)

*   **Purpose**: Package and export analytical layers into the JSON/GeoJSON data contracts consumed by the CRI Web Application.
*   **Processing Script**: [`script/export_cri_app_assets.py`](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/export_cri_app_assets.py) *(Formerly `tmp_stage1_export.py` / `build_stage1_export.py`)*
*   **v4.3 Upgrades**:
    1. **Legacy Window Deprecation**: `period_2560_2567` (2560–2567) is officially purged; outputs strictly cover `period_2561_2567` (canonical 7-year baseline) and `period_2567` (single-year).
    2. **Unified Schema Compliance**: All exported JSON records contain `raw_value`, `normalized_score`, `display_value`, `value`, `rank_desc`, and `unit_metadata`.
    3. **Standalone Heatwave Casualty Score**: Exports `heat_score.json` ($50\%\text{ Deaths} + 50\%\text{ Injured}$) under `period_2561_2567/all/` and `period_2567/all/`.
*   **Outputs**: 
    *   `output/cri_impact_app_v3/data/period_2561_2567/*.json`
    *   `output/cri_impact_app_v3/data/period_2567/*.json`
    *   `output/cri_impact_app_v3/data/spatial/*.geojson`

---

## 13. Summary Matrix of Raw Intake Anomalies vs Active ELT Code Handling

| Assumption / Anomaly | Target Raw Intake File | Empirical Reality in Raw Data | Active Sanitization Code Applied in ELT |
|:---|:---|:---|:---|
| **DDPM Comma Strings** | `ddpm/2567...csv` | Numbers $\ge 1,000$ formatted as `"1,422"` string | `parse_clean_numeric()` comma & whitespace stripping |
| **DDPM Sub-Headers** | `ddpm/2565-2567...csv` | Row 0 contains Thai column sub-headers | Header filtering `df[df["Disaster Date"] != "วันที่เกิดภัย"]` |
| **DOPA National Total** | `pop67.raw.csv` | Row 0 contains `รหัสจังหวัด = 0` (65.95M total) | Filter `df[df["รหัสจังหวัด"] > 0]` |
| **DOPA UTF-8 BOM** | `pop67.raw.csv` | Column 0 contains `\ufeff6712` byte prefix | BOM stripping `str.replace("\ufeff", "")` |
| **GPP Year Header** | `gpp-67.raw.csv` | Header string contains `2567 \| 2024p` | Header splitting on `\|` & mapping `2024p` $\rightarrow$ `2567` |
| **MOF Trailing Spaces** | `govt_adv_payment-*.raw.csv` | Province names contain trailing spaces (`"กรุงเทพมหานคร "`) | Whitespace stripping `.str.strip()` |
| **DOH Multi-Headers** | `heatwave.raw.csv` | Headers merged with pipes (`2561 - 2567 \| Deaths`) | Pipe-delimited string parsing into canonical metric codes |

---

## 14. Forensic Patch Registry (GIS Alignment)

The following 11 targeted patches were applied in `prep_dopa_boundaries.py` to bridge legacy GIS attributes (Bronze) and the Gold Spine:

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
