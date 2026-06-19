# Technical Design Note: Climate Risk Index (CRI) Hazard Disaggregation Architecture

**Date**: 2026-06-19
**Author**: Antigravity (Oracle Coding Assistant)
**Status**: Approved and Fully Implemented
**Project**: DCCE Climate Risk Index (CRI) Phase 1 Data System

---

## 1. Executive Summary

This design note establishes the data architecture, processing logics, and pipeline adjustments required to disaggregate the **Climate Risk Index (CRI) Phase 1 Score**, its sub-metrics, and the **Tambon-level Human Impact** by individual climate hazard types. 

The system will support **six (6) options** in total:
*   Five (5) individual climate hazards: **Flood (อุทกภัย)**, **Windstorm (วาตภัย)**, **Cold Spell (ภัยหนาว)**, **Landslide (ดินโคลนถล่ม)**, and **Drought (ภัยแล้ง)**.
*   One (1) consolidated option: **All Climate Hazards (รวมทุกภัยพิบัติ)**.

The proposed architecture introduces structured sub-directories in the Stage 1 JSON export payload, allowing the Streamlit frontend to load lightweight, pre-computed spatial and metric assets dynamically depending on the selected hazard and time period.

---

## 2. System Data Flow

The following diagram outlines the disaggregated data pipeline from raw source files in the Silver and Gold layers through the Stage 1 Export script to the frontend Streamlit application:

``` mermaid
graph TD
    %% Source Layers
    subgraph Gold Layer (DDPM Human Impact)
        G_Cons["fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv"]
    end

    subgraph Silver Layer (Financial Relief & Denominators)
        S_Loss["silver_govt_adv_payment_annual_long.csv"]
        S_Pop["silver_population_annual.csv"]
        S_HH["silver_household_annual.csv"]
        S_GPP["silver_gpp_annual_long.csv"]
    end

    %% Processing Script
    subgraph Stage 1 Export Processor (tmp_stage1_export.py)
        P_Filter["1. Hazard Filter & Aggregator"]
        P_Calc["2. Metric & Rate Calculator"]
        P_Norm["3. Hazard-Specific MinMax Normalizer"]
        P_CRI["4. Weighted CRI Scoring Engine"]
    end

    %% Export Outputs
    subgraph Stage 1 Export Outputs (build_exports/stage1/)
        OUT_All["period_2560_2567/all/"]
        OUT_Flood["period_2560_2567/flood/"]
        OUT_Other["period_2560_2567/[other_hazards]/"]
    end

    %% Streamlit App
    subgraph Streamlit App (cri_impact_app_v3)
        UI_Ctrl["UI Hazard & Period Selectors"]
        UI_Map["Map Renderer (PyDeck)"]
        UI_Rank["Ranking Tables"]
    end

    %% Connections
    G_Cons --> P_Filter
    S_Loss --> P_Filter
    S_Pop --> P_Calc
    S_HH --> P_Calc
    S_GPP --> P_Calc

    P_Filter --> P_Calc --> P_Norm --> P_CRI
    P_CRI --> OUT_All
    P_CRI --> OUT_Flood
    P_CRI --> OUT_Other

    OUT_All -.->|"data.load_metric()"| UI_Ctrl
    OUT_Flood -.->|"data.load_metric()"| UI_Ctrl
    UI_Ctrl --> UI_Map
    UI_Ctrl --> UI_Rank
```

---

## 3. Input Data Audit & Schema Mapping

To process the hazard dimension, the pipeline consumes the following specific inputs:

### A. Gold Layer: Human Impact (DDPM)
*   **Consolidated File (All Hazards)**: [fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv)
*   **Disaggregated Files (Hazard-Specific)**: The gold directory contains individual yearly files pre-split by hazard type:
    *   Flood: [fact_ddpm_tambon_impact_climate_yearly_flood_2560_2567.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_flood_2560_2567.csv)
    *   Drought: [fact_ddpm_tambon_impact_climate_yearly_drought_2560_2567.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_drought_2560_2567.csv)
    *   Windstorm: [fact_ddpm_tambon_impact_climate_yearly_windstorm_2560_2567.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_windstorm_2560_2567.csv)
    *   Cold Spell: [fact_ddpm_tambon_impact_climate_yearly_cold_spell_2560_2567.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_cold_spell_2560_2567.csv)
    *   Landslide: [fact_ddpm_tambon_impact_climate_yearly_landslide_2560_2567.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_landslide_2560_2567.csv)
*   **Key Fields**:
    *   `province_code` / `subdistrict_code`: Stable join keys.
    *   `year_be`: Thai Buddhist Era year (2560–2567).
    *   `deaths_sum` / `affected_households_sum`: Metric fields to aggregate.

### B. Silver Layer: Government Advance Payments (Relief Payouts)
*   **Target File**: [silver_govt_adv_payment_annual_long.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv)
*   **Key Fields**:
    *   `canonical_hazard_code`: Matches the codes in the Gold layer.
    *   `province_code` & `year_be`: Match keys.
    *   `value`: Numerical relief payout amount (in THB).

### C. Silver Layer: from 
These files contain standard socio-economic parameters and are **not** disaggregated by hazard:
*   **Population**: [silver_population_annual.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/population/silver_population_annual.csv) (for `population_total`).
*   **Households**: [silver_household_annual.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/population/silver_household_annual.csv) (for `household_total`).
*   **GPP**: [silver_gpp_annual_long.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/gpp/silver_gpp_annual_long.csv) where `metric_code == "GPP_CURRENT_MARKET_PRICE"` (in Million THB).

---

## 4. Processing Logics & Mathematical Formulations

For each selected hazard $H$ (where $H \in \{\text{FLOOD}, \text{WINDSTORM}, \text{COLD\_SPELL}, \text{LANDSLIDE}, \text{DROUGHT}, \text{ALL}\}$):

### Step 1: Human Impact Aggregation
The gold yearly CSV files contain tambon-level (subdistrict) records. These must be aggregated differently for Province-level metrics (CRI Score) and Tambon-level metrics (Human Impact View):

#### A. Province-Level Human Impact Aggregation (for CRI Index & Sub-metrics)
1. **Select & Load Source File**:
   * If $H = \text{ALL}$, load the consolidated yearly file [fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv).
   * If $H \ne \text{ALL}$, load the corresponding hazard-specific file (e.g. `fact_ddpm_tambon_impact_climate_yearly_[H_lowercase]_2560_2567.csv`).
2. **Annual Province Sums**:
   For each Province $P$, Year $Y$ (where $Y \in [2560..2567]$), and Hazard $H$, sum the tambon impacts:
   $$\text{Deaths}(P, Y, H) = \sum_{s \in \text{Tambons}(P)} \text{deaths\_sum}(s, Y, H)$$
   $$\text{Affected HH}(P, Y, H) = \sum_{s \in \text{Tambons}(P)} \text{affected\_households\_sum}(s, Y, H)$$
3. **Temporal Processing**:
   * **For the 2560–2567 Average Period**: Group by `province_code` and average the annual sums over the 8-year window:
     $$\overline{\text{Deaths}}(P, H) = \frac{\sum_{Y=2560}^{2567} \text{Deaths}(P, Y, H)}{8.0}$$
     $$\overline{\text{Affected HH}}(P, H) = \frac{\sum_{Y=2560}^{2567} \text{Affected HH}(P, Y, H)}{8.0}$$
   * **For the 2567 Single Year Period**: Filter for $Y = 2567$ and group by `province_code`:
     $$\text{Deaths}_{2567}(P, H) = \text{Deaths}(P, 2567, H)$$
     $$\text{Affected HH}_{2567}(P, H) = \text{Affected HH}(P, 2567, H)$$

#### B. Tambon-Level Human Impact Aggregation (for Human Impact Page Maps & Tables)
1. **Select & Load Source File**: Same source file selection logic as above based on hazard $H$.
2. **Annual Tambon Sums**:
   For each Subdistrict $S$ (tambon), Year $Y$, and Hazard $H$, sum the records (to handle any duplicate keys, though keys should be unique):
   $$\text{Tambon Deaths}(S, Y, H) = \sum \text{deaths\_sum}(S, Y, H)$$
   $$\text{Tambon Affected HH}(S, Y, H) = \sum \text{affected\_households\_sum}(S, Y, H)$$
3. **Temporal Processing**:
   * **For the 2560–2567 Average Period**: Group by `subdistrict_code` and average the annual sums over the 8-year window:
     $$\overline{\text{Tambon Deaths}}(S, H) = \frac{\sum_{Y=2560}^{2567} \text{Tambon Deaths}(S, Y, H)}{8.0}$$
     $$\overline{\text{Tambon Affected HH}}(S, H) = \frac{\sum_{Y=2560}^{2567} \text{Tambon Affected HH}(S, Y, H)}{8.0}$$
   * **For the 2567 Single Year Period**: Filter for $Y = 2567$ and group by `subdistrict_code`:
     $$\text{Tambon Deaths}_{2567}(S, H) = \text{Tambon Deaths}(S, 2567, H)$$
     $$\text{Tambon Affected HH}_{2567}(S, H) = \text{Tambon Affected HH}(S, 2567, H)$$

---

### Step 2: Economic Relief Aggregation (Province Level)
1. Filter [silver_govt_adv_payment_annual_long.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv) by the target hazard $H$. If $H = \text{ALL}$, sum values across all hazard codes.
2. Group by `province_code` and `year_be` to get annual totals:
   $$\text{Relief}(P, Y, H) = \sum \text{value}(P, Y, H)$$
3. Apply temporal processing:
   * **For the 2560–2567 Average Period**:
     $$\overline{\text{Relief}}(P, H) = \frac{\sum_{Y=2560}^{2567} \text{Relief}(P, Y, H)}{8.0}$$
   * **For the 2567 Single Year Period**:
     $$\text{Relief}_{2567}(P, H) = \text{Relief}(P, 2567, H)$$

---

### Step 3: Denominator Processing
Denominators (population, households, GPP) are at the province level and are **not** filtered by hazard. They are averaged or selected for the target periods:
* **For the 2560–2567 Average Period**:
  $$\overline{\text{Population}}(P) = \frac{\sum_{Y=2560}^{2567} \text{Population}(P, Y)}{8.0}$$
  $$\overline{\text{Households}}(P) = \frac{\sum_{Y=2560}^{2567} \text{Households}(P, Y)}{8.0}$$
  $$\overline{\text{GPP\_THB}}(P) = \frac{\sum_{Y=2560}^{2567} \text{GPP\_Million\_THB}(P, Y)}{8.0} \times 1,000,000$$
* **For the 2567 Single Year Period**:
  $$\text{Population}_{2567}(P) = \text{Population}(P, 2567)$$
  $$\text{Households}_{2567}(P) = \text{Households}(P, 2567)$$
  $$\text{GPP\_THB}_{2567}(P) = \text{GPP\_Million\_THB}(P, 2567) \times 1,000,000$$

### Step 4: Metric & Rate Calculations
For each province, calculate the exposure rates and economic ratios:
1.  **Death Rate (per 100,000 people)**:
    $$\text{Death Rate}(P, H) = \frac{\overline{\text{Deaths}}(P, H)}{\overline{\text{Population}}(P)} \times 100,000$$
2.  **Affected Household Rate (per 100 households)**:
    $$\text{Affected Rate}(P, H) = \frac{\overline{\text{Affected HH}}(P, H)}{\overline{\text{Households}}(P)} \times 100$$
3.  **Relief Payout per Unit GPP (%)**:
    $$\text{Relief/GPP}(P, H) = \frac{\overline{\text{Relief}}(P, H)}{\overline{\text{GPP\_THB}}(P)} \times 100.0$$
    Where $\overline{\text{GPP\_THB}}(P) = \overline{\text{GPP\_Million\_THB}}(P) \times 1,000,000$.

### Step 5: MinMax Normalization (Hazard-Specific)
To ensure the indicators occupy a consistent $[0, 1]$ range for indexing, apply MinMax normalization **within** each hazard category:
$$S\_X(P, H) = \frac{X(P, H) - \min_{p} X(p, H)}{\max_{p} X(p, H) - \min_{p} X(p, H)}$$
Where $X \in \{\text{Deaths\_Abs}, \text{Death\_Rate}, \text{Affected\_HH\_Abs}, \text{Affected\_Rate}, \text{Relief\_Abs}, \text{Relief/GPP}\}$.

> [!NOTE]
> **Why Hazard-Specific Normalization?**
> Climate hazards differ drastically in order of magnitude (e.g., Flood relief payments can be 100x larger than Landslide relief). Normalizing *within* each hazard isolates the spatial distribution of risk for that specific hazard type and avoids minor hazards being entirely drowned out by floods.

### Step 6: CRI Phase 1 Score Calculation
The final CRI score for a province $P$ under hazard $H$ is computed using the Phase 1 weight distribution:
$$\begin{aligned}
\text{CRI Score}(P, H) = 
& \quad S\_\text{Deaths\_Abs}(P, H) \times 0.075 \\
& + S\_\text{Death\_Rate}(P, H) \times 0.225 \\
& + S\_\text{Affected\_HH\_Abs}(P, H) \times 0.05 \\
& + S\_\text{Affected\_Rate}(P, H) \times 0.15 \\
& + S\_\text{Relief\_Abs}(P, H) \times 0.125 \\
& + S\_\text{Relief/GPP}(P, H) \times 0.375
\end{aligned}$$

---

## 5. Export Pipeline Adjustments (Stage 1 Export)

We will modify [tmp_stage1_export.py](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/tmp_stage1_export.py) to export a nested folder structure. For every time period and hazard key, the exporter will output the complete set of 7 province-level JSON files and 2 tambon-level JSON files.

### Export Directory Layout
```
build_exports/
└── stage1/
    ├── manifest.json
    ├── spatial/
    │   ├── province_boundaries.geojson
    │   ├── manifest.json
    │   └── tambon/
    │       └── [province_code].geojson
    ├── period_2560_2567/
    │   ├── all/
    │   │   ├── deaths_abs.json
    │   │   ├── deaths_rate.json
    │   │   ├── affected_hh_abs.json
    │   │   ├── affected_rate.json
    │   │   ├── loss_abs.json
    │   │   ├── loss_per_gpp.json
    │   │   ├── cri_score.json
    │   │   ├── tambon_deaths.json
    │   │   └── tambon_affected_households.json
    │   ├── flood/
    │   │   ├── [All 7 province metrics JSON files]
    │   │   ├── tambon_deaths.json
    │   │   └── tambon_affected_households.json
    │   └── [drought|windstorm|cold_spell|landslide]/
    │       ├── [All 7 province metrics JSON files]
    │       ├── tambon_deaths.json
    │       └── tambon_affected_households.json
    └── period_2567/
        ├── all/
        │   ├── [All 7 province metrics JSON files]
        │   ├── tambon_deaths.json
        │   └── tambon_affected_households.json
        ├── flood/
        │   ├── [All 7 province metrics JSON files]
        │   ├── tambon_deaths.json
        │   └── tambon_affected_households.json
        └── [drought|windstorm|cold_spell|landslide]/
            ├── [All 7 province metrics JSON files]
            ├── tambon_deaths.json
            └── tambon_affected_households.json
```

### Manifest Schema Extension
The root `manifest.json` will be updated to document the supported hazards and route paths:
```json
{
  "version": "2026-06-19-disaggregated-stage1",
  "generated_at": "2026-06-19T06:35:00Z",
  "periods": [
    {"period_key": "period_2560_2567", "period_label": "2560–2567 average"},
    {"period_key": "period_2567", "period_label": "2567 only"}
  ],
  "hazards": [
    {"hazard_key": "all", "hazard_label": "All Climate Hazards (รวมทุกภัย)"},
    {"hazard_key": "flood", "hazard_label": "Flood (อุทกภัย)"},
    {"hazard_key": "windstorm", "hazard_label": "Windstorm (วาตภัย)"},
    {"hazard_key": "cold_spell", "hazard_label": "Cold Spell (ภัยหนาว)"},
    {"hazard_key": "landslide", "hazard_label": "Landslide (ดินโคลนถล่ม)"},
    {"hazard_key": "drought", "hazard_label": "Drought (ภัยแล้ง)"}
  ]
}
```

---

## 6. Frontend Integration Plan

### A. Runtime Data Access Refactoring
In [runtime/data.py](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/runtime/data.py), update the metric loading utility to support a hazard key parameter:

```python
def load_metric(metric_key: str, period_key: str, hazard_key: str = "all") -> dict:
    """Loads a pre-calculated metric JSON, resolved by time period and hazard dimension."""
    # Build path matching the structure: build_exports/stage1/period_key/hazard_key/metric_key.json
    file_path = BASE_DATA_DIR / period_key / hazard_key / f"{metric_key}.json"
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
```

### B. User Interface (Streamlit)
*   Add a **Hazard Selector** (Selectbox) in the sidebar of `pages/cri.py` and `pages/tambon.py` alongside the existing Time Period control.
*   Populate option labels using the hazard dictionary (English + Thai translation).
*   Bind the selected hazard key to all data loads on the page.

---

## 7. QA & Verification Protocol

Before sealing the disaggregated assets, the export pipeline must pass these baseline QA rules:
1.  **Conservation of Sums**: Verify that for any province $P$ and year $Y$:
    $$\sum_{H \in \{\text{individual hazards}\}} \text{Metric}(P, Y, H) = \text{Metric}(P, Y, \text{ALL})$$
2.  **No Negative Rates**: Assert that normalized scores, death rates, and relief/GPP values are strictly $\ge 0$.
3.  **Boundary Handling**: Handle edge cases where a province has zero events for a specific hazard over the 8-year range (prevent division-by-zero errors in MinMax scaling by returning a default normalized score of `0.0`).
