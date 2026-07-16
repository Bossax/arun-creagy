# Execution Plan: CRI Web App v4.1 — Score Calibration, Unit Conversion, and UI Bugs

**Date**: 2026-07-16
**Version**: v4.1.0
**Target**: Data Exporter Refactoring + UI Realignment + Data Verification Logging

---

## 1. Objective
This plan outlines the updates to upgrade the data exporter and Streamlit UI to **v4.1**:
1. **CRI Score Exclusions**: Restrict the composite `ALL` hazard `cri_score` to only compile from hazards possessing the full 6 metrics (Flood, Drought, Windstorm). Disable/omit hazard-specific `cri_score` for Landslide, Wildfire, and Cold Spell.
2. **Affected Households to People Conversion**: Convert all affected household counts to estimated affected people counts using annual tambon-level and province-level average people-per-household factors.
3. **Audit and Verification Logging**: Generate a detailed conversion statistics report inside the workspace analysis folder to track any data skews or fallbacks.
4. **Fix Subdistrict Nomenclature Mismatch (the `· -` bug)**: Source subdistrict and district names directly from the master location spine to prevent missing name entries.
5. **Prune Zero-Impact Tambon Tables**: Hide tambon ranking tables and show a clean placeholder when all metric values in a province are zero.
6. **Methodology Tab Transparency**: Add notes explaining the demographic assumptions and potential skews introduced by multiplying households by regional average sizes.
7. **Raw Wildfire Alignment**: Ingest raw household data (`Wildfire_hh_data.csv`) and apply the conversion pipeline to ensure consistency with other hazards.

---

## 2. Phase 1: CRI Score Exclusions (Incomplete Hazard Calibration)

### 1.1 Exclude from Composite (`ALL`) CRI Score
In [tmp_stage1_export.py](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/script/tmp_stage1_export.py):
* **Rebuild Strategy**: 
  * Create a helper function `rebuild_yearly_ddpm_fact_for_cri_score(ddpm_dir)` that globs and merges **only** the complete hazards:
    * `drought`
    * `flood`
    * `windstorm`
  * When calculating `prov_avg["cri_score"]` and `prov_2567["cri_score"]` for the `all` hazard directory, use this filtered fact database.
  * The general `ALL` hazard metrics (`deaths_abs`, `affected_hh_abs`) will continue to include all 6 hazards.

### 1.2 Omit Hazard-Specific CRI Scores
* In the hazard disaggregation loop:
  * If `h_key` is `landslide`, `wildfire`, or `cold_spell`:
    * Do **not** calculate the min-max scores `s_deaths_abs`, `s_loss_abs`, etc.
    * Do **not** write `cri_score.json` to their respective directories.
* Update `manifest.json` generation:
  * For the `metric_groups` -> `cri` list, dynamically check if `h_key` has a CRI score. If `h_key` is landslide, wildfire, or cold_spell, exclude `cri_score` from the available metrics list in the manifest.

---

## 3. Phase 2: Convert Affected Households to Affected People & Log Verification

### 2.1 Extract People-per-Household Ratios
* In the exporter script, load [silver_household_annual.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/population/silver_household_annual.csv).
* Compute a dictionary/mapping of:
  * **Tambon Ratio**: `tambon_ratio[subdistrict_code][year_be] = population_total / household_total`
  * **Province Ratio**: `province_ratio[province_code][year_be] = sum(population_total) / sum(household_total)` (grouped by province and year).

### 2.2 In-Memory Conversion Logic
* Before calculating averages or rates, join the ratios to the yearly DDPM dataframes.
* Compute estimated affected people:
  * `yearly_df["affected_people_estimated"] = yearly_df["affected_households_sum"] * yearly_df["ppl_per_hh_ratio"]`
  * Fall back to the province ratio if the tambon-level ratio is missing or division-by-zero occurs.
* Substitute `affected_people_estimated` for all occurrences of `affected_households_sum` in the exporter.

### 2.3 Verification & Audit Logging
* During the conversion loop, compile a log dataframe of all subdistrict records:
  * Columns: `subdistrict_code`, `year_be`, `affected_households_sum`, `tambon_ratio`, `province_fallback_ratio`, `used_ratio`, `estimated_people`, `fallback_applied` (Boolean).
* Save this audit log to:
  * [C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/analysis/household_to_people_conversion_audit.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/analysis/household_to_people_conversion_audit.csv)
  * This permits post-ingestion review of how many records used the fallback province-level average.

### 2.4 Rename Metric Keys & Update Denominators
* Rename the exported metric key:
  * `affected_hh_abs` (Affected Households) $\rightarrow$ `affected_ppl_abs` (Affected People).
* Update the rate calculation from `affected_rate` (per 100 households) to `affected_ppl_rate` (per 100,000 population):
  * `affected_ppl_rate = (affected_ppl_abs / population_annual_avg) * 100000`
* Update the manifest and exporter payload labels:
  * "Affected Households" $\rightarrow "Affected People"
  * "Annual households" $\rightarrow$ "Annual people"
  * "per 100 households" $\rightarrow$ "per 100k population"

---

## 4. Phase 3: UI Bugs & Fixes

### 3.1 Fix Subdistrict Nomenclature Mismatch (the `· -` bug)
* Currently, the exporter builds `tambon_lookup_ddpm` strictly from observed DDPM records. For new hazards like Wildfire, affected subdistricts may be missing from the historical DDPM spine, leading to `NaN` district/subdistrict names in the UI.
* **Fix**: In `tmp_stage1_export.py`, load the Gold location spine [dim_location_master.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/dopa/dim_location_master.csv) and use it as the definitive `tambon_lookup_ddpm` source:
  ```python
  location_spine = load_csv(SRC / "2_gold/dopa/dim_location_master.csv")
  # Filter for admin_level == 'subdistrict' and extract code, name_th, district_name_th, and province_code
  ```

### 3.2 Prune Zero-Impact Tambon Tables
* In [runtime/data.py](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/runtime/data.py), update the `tambon_rank_rows` function:
  * If the values of all tambons within the selected province are `0.0`, return an empty list `[]`.
* In [pages/tambon.py](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/pages/tambon.py):
  * If the rank rows list is empty, display an explicit message: *"All subdistricts in this province recorded zero impacts (0 deaths / 0 affected people) for the selected hazard."* instead of an arbitrary 0-filled table.
