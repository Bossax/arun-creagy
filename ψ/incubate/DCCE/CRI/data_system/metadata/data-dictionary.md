# CRI Data Dictionary (v4.3 Release Edition)

This document serves as the canonical reference for the metadata structures, Silver normalized facts, Gold analytical tables, and v4.3 exported application payloads used in the CRI Data System.

---

## 1. Categorical & Spatial Metadata (Dimensions)

### 1.1 Location Master (`dim_location_master.csv`)
**Role**: The "Gold Spine" of the project, establishing the national administrative hierarchy across 77 Provinces, 878 Districts, and 7,255 Subdistricts.

| Column Name | Data Type | Nullable | Role | Definition | Source Agency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `location_id` | string | No | PK | Official 6-digit DOPA Tambon code. | DOPA (กรมการปกครอง) |
| `subdistrict_code` | string | No | Unique | Official 6-digit DOPA Tambon code (padded). | DOPA (กรมการปกครอง) |
| `district_code` | string | No | - | Official 4-digit DOPA District code. | DOPA (กรมการปกครอง) |
| `province_code` | string | No | - | Official 2-digit DOPA Province code. | DOPA (กรมการปกครอง) |
| `province_name_th` | string | No | - | Standardized Thai province name. | DOPA (CCAATT Master) |
| `tambon_name_th` | string | No | - | Standardized Thai sub-district name. | DOPA (CCAATT Master) |

---

## 2. Silver Layer Normalized Fact Tables (Transformed from CRI Project Data)

### 2.1 Silver Population & Households (`1_silver/population/`)
**Source**: `0_bronze/2026-06-12_cri_proj_data/population_extracts/*.raw.csv` (DOPA)

| File Name | Granularity | Metric Columns | Key Transformation Logic |
| :--- | :--- | :--- | :--- |
| `silver_population_annual.csv` | Subdistrict $\times$ Year | `population_total`, `population_male`, `population_female` | Strips UTF-8 BOM bytes (`\ufeff6712`), filters `รหัสจังหวัด > 0` to exclude national summary totals. |
| `silver_household_annual.csv` | Subdistrict $\times$ Year | `household_total`, `pop_per_hh_ratio` | Sums split District (`อำเภอ`) and Local Municipal (`ท้องถิ่น...`) rows per subdistrict; computes subdistrict DOPA ratio $R = \text{Pop}/\text{HH}$; bounds valid range $0.5 \le R \le 10.0$. |

### 2.2 Silver Economic GPP (`1_silver/gpp/silver_gpp_annual_long.csv`)
**Source**: `0_bronze/2026-06-12_cri_proj_data/gpp_extracts/*.raw.csv` (NESDC / สภาพัฒน์)

| Column Name | Data Type | Role | Definition | Transformation Notes |
| :--- | :--- | :--- | :--- | :--- |
| `province_code` | string | FK | 2-digit DOPA province code. | Joined via DOPA master crosswalk. |
| `metric_code` | string | Dim | `GPP_CURRENT_MARKET_PRICE` | Evaluated at current market prices. |
| `year_be` | string | Dim | Buddhist Era Year (`2560`–`2567`). | Header `2024p` mapped to `2567`. |
| `value` | float | Metric | Gross Provincial Product in **THB**. | Scaled $\times 1,000,000$ from Million THB. |

### 2.3 Silver Government Financial Relief (`1_silver/govt_adv_payment/`)
**Source**: `0_bronze/2026-06-12_cri_proj_data/govt_adv_payment_extracts/*.raw.csv` (MOF / CGD & DDPM)

| File Name | Granularity | Metric Columns | Transformation Notes |
| :--- | :--- | :--- | :--- |
| `silver_govt_adv_payment_annual_long.csv` | Province $\times$ Hazard $\times$ Year | `value` (THB Relief Payment) | Unpivots year columns; strips trailing spaces in province strings (`.str.strip()`). |
| `silver_govt_adv_payment_period_total.csv` | Province $\times$ Hazard | `value` (7-Year Cumulative THB) | Represents total emergency advance fund spending (2561–2567). |

### 2.4 Silver Heatwave Casualties (`1_silver/heatwave/silver_heatwave_impact_long.csv`)
**Source**: `0_bronze/2026-06-12_cri_proj_data/heatwave_extracts/heatwave.raw.csv` (**Dept. of Health / DOH / กรมอนามัย**)

| Column Name | Data Type | Role | Definition | Transformation Notes |
| :--- | :--- | :--- | :--- | :--- |
| `province_code` | string | FK | 2-digit DOPA province code. | Joined via DOPA lookup. |
| `metric_code` | string | Dim | `HEAT_DEATHS`, `HEAT_INJURED` | Health sector casualties. |
| `time_scope` | string | Dim | `year_2567`, `range_2561_2567` | Single-year vs 7-year cumulative scope. |
| `value` | float | Metric | Count of deaths or injuries. | Extracted from pipe-delimited headers. |

---

## 3. Gold Fact Tables (Empirical Impact Layer)

### 3.1 DDPM Tambon Impact Facts (`2_gold/ddpm/`)
**Source**: `0_bronze/ddpm/25*.csv` (DDPM)

| File Name | Primary Metrics | Description |
| :--- | :--- | :--- |
| `fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv` | `affected_households_sum`, `deaths_sum`, `injured_sum` | Sub-district level annual disaster facts across Flood, Drought, Windstorm, Landslide, Cold Spell. |
| `fact_ddpm_tambon_impact_climate_wildfire_2560_2567.csv` | `affected_households_sum`, `deaths_sum` | **Wildfire Fact Table**: Sub-district level wildfire facts processed via `build_gold_wildfire_ddpm_fact.py` from `Wildfire_hh_data.csv`. |

---

## 4. Application Export Engine Payload Contract (v4.3 JSON Assets)
Location: `output/cri_impact_app_v3/data/period_2561_2567/` & `period_2567/`

All exported JSON payloads implement the v4.3 unified schema:

```json
{
  "province_code": "80",
  "province_name_th": "นครศรีธรรมราช",
  "province_name_en": "NAKHON SI THAMMARAT",
  "raw_value": 197934176.28,
  "normalized_score": 1.0,
  "rank_desc": 1,
  "display_value": "197,934,176.28 THB",
  "value": 197934176.28,
  "unit_metadata": {
    "primary_unit": "baht",
    "is_rate": false,
    "is_normalized_score": false
  }
}
```

### 4.1 Standalone Heatwave Casualty Metrics (`heat_score.json`)
* `heat_deaths.json`: Annual heat mortality count (DOH / กรมอนามัย).
* `heat_injured.json`: Annual heat illness/injury count (DOH / กรมอนามัย).
* `heat_score.json`: Standalone Heatwave Casualty Score ($0.5 \times s_{\text{heat\_deaths}} + 0.5 \times s_{\text{heat\_injured}}$).

---

## 5. Administrative Protocols
* **DOPA Spine Integrity**: All spatial joins MUST match 6-digit `subdistrict_code` or 2-digit `province_code`.
* **Canonical Baseline Window**: **2561–2567 (7-Year Average)** and **2567 (Single-Year)**. `period_2560_2567` is officially deprecated.
