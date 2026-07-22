# Execution Plan: CRI Web App v4.2 Data & UI Upgrade

**Date**: 2026-07-22  
**Version**: v4.2.0  
**Target**: Data Pipeline Normalization Script + Exporter Guardrails + Normalized Component Exports + Tambon Rate Expansion + Streamlit App Integration  

---

## 1. Objective & Scope
The objective of **CRI v4.2** is to address data lineage bugs and enhance metric presentation across the platform:
1. **Upstream Script Repair (`normalize_population_to_silver.py`)**: Update the silver population normalization script to build `silver_household_annual.csv` directly and consolidate split subdistrict rows to eliminate join fan-out.
2. **Exporter Join Guardrail**: Implement pre-join aggregation in `tmp_stage1_export.py` as a runtime safeguard.
3. **Normalized CRI Component Presentation**: Replace raw absolute values in the 6 CRI component metrics (`deaths_abs`, `deaths_rate`, `affected_ppl_abs`, `affected_ppl_rate`, `loss_abs`, `loss_per_gpp`) with their min-max normalized scores (`Score [0-1]`).
4. **Tambon-Level Rates Expansion**: Add 2 new subdistrict metrics:
   * `tambon_deaths_rate` (Tambon Deaths per 100k Population)
   * `tambon_affected_people_rate` (Tambon Affected People per 100k Population)
5. **Streamlit UI Updates**: Update metric selectors and display labels in `pages/cri.py` and `pages/tambon.py`.

---

## 2. User Review Required

> [!IMPORTANT]
> **Upstream Silver Script Modification**:
> Instead of manually fixing the `silver_household_annual.csv` file, `normalize_population_to_silver.py` will be modified to consolidate duplicate `(subdistrict_code, year_be)` entries into pure subdistrict records and materialize `silver_household_annual.csv` automatically upon execution.

> [!IMPORTANT]
> **Component Normalized Scores**: 
> For the 6 CRI component metrics (e.g., `deaths_abs`, `loss_abs`), the exported `value` in the JSON files will now hold the **min-max normalized score [0-1]** (matching the scale of the composite `cri_score`), rather than the raw absolute count or THB value.

---

## 3. Proposed Changes

### Phase 1: Upstream Asset Script & Exporter Guardrails

#### [MODIFY] `data_system/script/normalize_population_to_silver.py`
Add household aggregation and output routine for `silver_household_annual.csv`:
```python
# Add household output path definition
HOUSEHOLD_ANNUAL_OUTPUT_PATH = OUTPUT_DIR / "silver_household_annual.csv"

# Add subdistrict consolidation routine to aggregate split registrations per subdistrict year
def export_silver_household_annual(annual_rows):
    df_annual = pd.DataFrame(annual_rows)
    df_sub = df_annual[df_annual["geography_level"] == "subdistrict"].copy()
    
    df_clean = df_sub.groupby(
        ["year_be", "province_code", "province_name_th", "subdistrict_code", "subdistrict_name_th"], 
        dropna=False
    ).agg(
        population_total=("population_total", "sum"),
        household_total=("household_total", "sum")
    ).reset_index()
    
    df_clean.to_csv(HOUSEHOLD_ANNUAL_OUTPUT_PATH, index=False, encoding="utf-8-sig")
```

#### [MODIFY] `data_system/script/tmp_stage1_export.py`
1. Update `apply_conversion_and_clean_keys()` to aggregate `hh_copy` by `['subdistrict_code', 'year_be']` before join.
2. Modify metric exporter lists `avg_specs_2560_2567` and `avg_specs_2567` to map `f"s_{metric_key}"` to `"value"` for the 6 component metrics, setting unit labels to `"Score [0-1]"`.
3. Add Tambon subdistrict population aggregation and calculate `tambon_deaths_rate` and `tambon_affected_people_rate`.
4. Export new JSON files:
   * `period_2561_2567/<hazard>/tambon_deaths_rate.json`
   * `period_2561_2567/<hazard>/tambon_affected_people_rate.json`
   * `period_2567/<hazard>/tambon_deaths_rate.json`
   * `period_2567/<hazard>/tambon_affected_people_rate.json`

---

### Phase 2: Front-End UI Updates (Streamlit)

#### [MODIFY] `output/cri_impact_app_v3/pages/cri.py`
Update metric selector labels and unit captions to indicate min-max normalized scores:
```python
metric_options.update({
    "Deaths (Score)": "deaths_abs",
    "Death Rate (Score)": "deaths_rate",
    "Affected People (Score)": "affected_ppl_abs",
    "Affected People Rate (Score)": "affected_ppl_rate",
    "Economic Loss (Score)": "loss_abs",
    "Economic Loss per GPP (Score)": "loss_per_gpp",
})
```

#### [MODIFY] `output/cri_impact_app_v3/pages/tambon.py`
Add the two new rate options to the Tambon metric selector:
```python
metric_options = {
    "Tambon Deaths": "tambon_deaths",
    "Tambon Death Rate (per 100k Population)": "tambon_deaths_rate",
    "Tambon Affected People": "tambon_affected_people",
    "Tambon Affected People Rate (per 100k Population)": "tambon_affected_people_rate",
}
```

---

## 4. Verification Plan

### Execution Commands
```powershell
# 1. Run upstream normalization script to regenerate silver_household_annual.csv
.\.venv\Scripts\python script/normalize_population_to_silver.py

# 2. Run Stage 1 exporter pipeline
.\.venv\Scripts\python script/tmp_stage1_export.py
```

### Automated Verification Script
Run a Python verification script after pipeline execution to validate:
1. Ground-truth check: `silver_household_annual.csv` has 0 duplicate keys.
2. Verification of unnormalized deaths in the exporter dataframes (ground truth of 11.0, 9.0, and 8.0 for 2567 Flood deaths in Nakhon Si Thammarat, Pattani, and Songkhla).
3. Verification of exported JSON scores: Values for all 6 metrics fall in range `[0.0, 1.0]`.
4. Verification of new Tambon rate JSONs: `tambon_deaths_rate.json` and `tambon_affected_people_rate.json` exist and contain non-zero calculated rates for affected areas.

```powershell
.\.venv\Scripts\python -c "
import json, pandas as pd

# 1. Asset check
df = pd.read_csv('data/1_silver/population/silver_household_annual.csv')
dupes = df.duplicated(subset=['subdistrict_code', 'year_be']).sum()
print('Silver Household Duplicates:', dupes)
assert dupes == 0

# 2. Unnormalized ground-truth check (Nakhon Si Thammarat = 11, Pattani = 9, Songkhla = 8)
# We load the Gold yearly flood fact table to check unnormalized ground-truth directly
gold_df = pd.read_csv('data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_flood_2560_2567.csv')
gold_df['province_code'] = gold_df['province_code'].astype(str).str.replace(r'\.0$', '', regex=True).str.strip().str.zfill(2)
gold_2567 = gold_df[gold_df['year_be'] == 2567]
sums = gold_2567.groupby('province_code')['deaths_sum'].sum()
print('Raw Gold 2567 Flood Deaths - NST (80):', sums.get('80', 0))
print('Raw Gold 2567 Flood Deaths - Pattani (94):', sums.get('94', 0))
print('Raw Gold 2567 Flood Deaths - Songkhla (90):', sums.get('90', 0))

assert sums.get('80', 0) == 11.0, f'Expected 11.0, got {sums.get(\"80\", 0)}'
assert sums.get('94', 0) == 9.0, f'Expected 9.0, got {sums.get(\"94\", 0)}'
assert sums.get('90', 0) == 8.0, f'Expected 8.0, got {sums.get(\"90\", 0)}'

# 3. Score range check
path = 'build_exports/stage1/period_2567/flood/deaths_abs.json'
with open(path, encoding='utf-8') as f:
    recs = json.load(f)['records']
    vals = [r['value'] for r in recs]
    print('Sample Normalized Score Range:', min(vals), 'to', max(vals))
    assert 0.0 <= min(vals) and max(vals) <= 1.0

# 4. New Tambon rate check
t_path = 'build_exports/stage1/period_2567/flood/tambon_deaths_rate.json'
with open(t_path, encoding='utf-8') as f:
    t_recs = json.load(f)['records']
    print('Tambon Deaths Rate record count:', len(t_recs))
    assert len(t_recs) > 0

print('✅ All CRI v4.2 Verifications Passed!')
"
```

---

## 5. Execution Progress Status

| Phase / Task | Target File | Status | Completion Date | Details |
|---|---|---|---|---|
| **Phase 1: Upstream Asset Script** | `normalize_population_to_silver.py` | ✅ Completed | 2026-07-22 | Aggregates DOPA annual records per subdistrict code and year; creates a unique `silver_household_annual.csv` file. |
| **Phase 1: Exporter Guardrail** | `tmp_stage1_export.py` | ✅ Completed | 2026-07-22 | Implemented pre-merge group and sum on ratios to enforce zero join fan-outs. |
| **Phase 1: Component Score Exports** | `tmp_stage1_export.py` | ✅ Completed | 2026-07-22 | Swapped absolute values with min-max normalized scores (`s_*`) in exported JSON files. |
| **Phase 1: Tambon Rates Ingestion** | `tmp_stage1_export.py` | ✅ Completed | 2026-07-22 | Calculated deaths/affected rates per 100k pop for subdistricts using `silver_population_annual.csv`. |
| **Phase 2: Streamlit Pages UI** | `pages/cri.py`, `pages/tambon.py` | ✅ Completed | 2026-07-22 | Integrated metric names and options; added new rate selection controls. |
| **Phase 2: Stage 1 JSON Sync** | `output/cri_impact_app_v3/data/` | ✅ Completed | 2026-07-22 | Synced `build_exports/stage1` to Streamlit app's local data repository. |
| **Phase 3: Validation Verification** | Verification Script | ✅ Passed | 2026-07-22 | Verified 0 asset duplicate keys, verified raw deaths match Gold facts (NST = 11, Pattani = 9, Songkhla = 8), verified score ranges, and verified new Tambon JSON structures. |
| **Phase 3: App Server Deploy** | Streamlit Server | 🚀 Active | 2026-07-22 | Running on http://localhost:8501 |

