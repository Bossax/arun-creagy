# Execution Plan: CRI Web App v4 Data & Pipeline Integration

**Date**: 2026-07-16
**Version**: v4.0.0
**Target**: Data Pipeline Ingestion + Exporter Upgrade + Streamlit v4 Integration

---

## 1. Objective & Scope
The goal of this execution plan is to transition the **CRI Impact Dashboard** to **version 4 (v4)**. This involves:
1. Shifting the long-term average baseline from `2560–2567` (8 years) to `2561–2567` (7 years) for all hazards.
2. Integrating the raw **Wildfire** (`Wildfire_ppl_data.csv`) dataset from the bronze layer into gold facts.
3. Re-integrating the **Cold Spell** (`COLD_SPELL`) hazard from the existing gold files into the Stage 1 exporter.
4. Handling data unavailability (Landslide economic losses, Wildfire averages) by disabling them in the UI.

---

## 2. Phase 1: Raw-to-Gold ELT Ingestion for Wildfire

### Step 1.1: Register Canonical Wildfire Hazard
Append the following row to the canonical hazard dimension file:
* File: `data/2_gold/dim_hazard_canonical.csv`
* New entry:
  ```csv
  12,WILDFIRE,Wildfire,ไฟป่า,climate,draft
  ```

### Step 1.2: Build Wildfire Gold Processing Script
Create a new ELT script `data_system/script/ELT/build_gold_wildfire_ddpm_fact.py` to ingest the raw wildfire data:
1. Load `0_bronze/2026-07-16-cri-proj-data/Wildfire_ppl_data.csv`.
2. Clean `tambon_code` (pad to 6 digits) and `prov_code` (pad to 2 digits).
3. Pivot (melt) the wide columns:
   * Map `wildfire_death_XX` -> `deaths_sum` (where `XX` is `60` to `67`).
   * Map `wildfire_affected_XX` -> `affected_households_sum` (where `XX` is `60` to `67`).
4. Re-index and fill missing years with `0.0` to cover the full range `2560-2567` (since the 2560 column is missing in the raw file, set it to 0).
5. Output the files in the standard gold schema format to:
   * `data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_wildfire_2560_2567.csv`
   * `data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_wildfire_2560_2567.csv`

---

## 3. Phase 2: Exporter Hardening (`tmp_stage1_export.py`)

Modify `data_system/script/tmp_stage1_export.py` to implement the new baseline and hazard structures:

### Step 2.1: Shift Temporal Baseline parameters
* Locate lines 356–400.
* Change `period_years` to start from `2561`:
  ```python
  # Old: period_years = [str(y) for y in range(2560, 2568)]
  # New:
  period_years = [str(y) for y in range(2561, 2568)]
  ```
* Change the divisor for average calculations from `8.0` to `7.0` (for `deaths_abs` and `affected_hh_abs`):
  ```python
  # Old: human["deaths_abs"] = human["deaths_sum"] / 8.0
  # Old: human["affected_hh_abs"] = human["affected_households_sum"] / 8.0
  # New:
  human["deaths_abs"] = human["deaths_sum"] / 7.0
  human["affected_hh_abs"] = human["affected_households_sum"] / 7.0
  ```

### Step 2.2: Update the Hazards Map
* Locate the `HAZARDS` dictionary (around line 17):
* Update it to include `wildfire` and `cold_spell`:
  ```python
  HAZARDS = {
      "all": "ALL",
      "flood": "FLOOD",
      "drought": "DROUGHT",
      "windstorm": "WINDSTORM",
      "landslide": "LANDSLIDE",
      "cold_spell": "COLD_SPELL",
      "wildfire": "WILDFIRE"
  }
  ```

### Step 2.3: Re-integrate Cold Spell in Fact Rebuild
* Locate the `rebuild_yearly_ddpm_fact` function (lines 117–172).
* Remove the `cold_spell` exclusion:
  ```python
  # Old:
  source_files = sorted(
      p for p in ddpm_dir.glob("fact_ddpm_tambon_impact_climate_yearly_*_2560_2567.csv")
      if p.name != "fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv"
      and "cold_spell" not in p.name
  )
  # New:
  source_files = sorted(
      p for p in ddpm_dir.glob("fact_ddpm_tambon_impact_climate_yearly_*_2560_2567.csv")
      if p.name != "fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv"
  )
  ```

### Step 2.4: Regenerate Stage 1 JSONs
* Run the script using the project-local virtual environment:
  ```bash
  poetry run python script/tmp_stage1_export.py
  ```
* Verify that new hazard folders have been created under `build_exports/stage1/period_2561_2567/` and `period_2567/` for both `cold_spell` and `wildfire`.

---

## 4. Phase 3: Front-End UI Adjustments (Streamlit)

Update the page files in `output/cri_impact_app_v3/pages/` to handle the v4 specs:

### Step 3.1: Update `pages/cri.py` (Metric and Period selectors)
1. **Adjust Time Period Options**:
   * Change label `2560-2567 Average` to `2561-2567 Average`.
   * Ensure `PeriodOption` maps to `"period_2561_2567"`:
     ```python
     period_options = [
         PeriodOption("period_2561_2567", "2561-2567 Average"),
         PeriodOption("period_2567", "2567 Only"),
     ]
     ```
2. **Handle Wildfire Period Constraints**:
   * If `Selected Hazard` is `Wildfire (ไฟป่า)` and the selected period is `period_2561_2567`, render a warning message and bypass standard map loading:
     ```python
     if hazard_key == "wildfire" and period_key == "period_2561_2567":
         st.warning("Long-term historical wildfire average is not available. Please select '2567 Only'.")
         return
     ```
3. **Handle Landslide Economic Loss Gaps**:
   * If `Selected Hazard` is `Landslide (ดินโคลนถล่ม)` and the selected metric is `loss_abs` or `loss_per_gpp`, render an explicit data gap warning:
     ```python
     if hazard_key == "landslide" and selected_metric in ["loss_abs", "loss_per_gpp"]:
         st.info("Economic damage data is not recorded/available for landslide events.")
         return
     ```

### Step 3.2: Update `pages/tambon.py` (Tambon grain selectors)
1. Apply the same period choice label fixes: `2561-2567 Average`.
2. Disable the subdistrict-level maps for Wildfire under `period_2561_2567` by implementing the corresponding time/hazard check:
   ```python
   if hazard_key == "wildfire" and period_key == "period_2561_2567":
       st.warning("Long-term subdistrict-level wildfire average is not available.")
       return
   ```
