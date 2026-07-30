---
type: trace
traceId: TRACE-20260730-CRI-CALC-MISMATCH
date: 2026-07-30
query: "find the recent issues about CRI datasets that required us to revisit the data processing scripts. We got mismatched results between the computed CRI shown on the app and hand calculated."
target: "CRI Calculation Mismatch (App vs. Hand Calculation)"
mode: smart
timestamp: 2026-07-30 15:51
friction_score: 1.0
coverage: [oracle, files, git, memory, session]
confidence: high
---

# Trace: CRI Score Calculation Mismatch (App vs. Hand-Calculated Excel)

**Target**: CRI Calculation Engine & Data Normalization Scripts  
**Mode**: smart | **Friction**: 1.0 | **Confidence**: high  
**Time**: 2026-07-30 15:51  

## Executive Summary

The disparity between the computed CRI scores rendered on the Streamlit web app and hand-calculated Excel workbooks was traced to 5 fundamental data processing and methodology differences:

---

## Key Causes of Calculation Mismatch

### 1. Embedded Aggregate Double-Counting in Raw DOPA Workbooks
- **Hand Calculation Cause**: Raw DOPA population workbooks (`CRI Data - Population.xlsx`) contain embedded aggregate rows (`province_code = 0`, `office_code = 0`, and district summary lines) alongside subdistrict rows, as well as duplicate subdistrict codes reused across registration office contexts. Hand-summing Excel columns included these aggregate rows, double/triple-counting population denominators.
- **App Processing Script Fix**: `normalize_population_to_silver.py` introduced strict `geography_level` classification and `record_class` filtering to strip aggregate rows and separate colliding registration office grains.

### 2. Zero vs. NaN Ambiguity in Incomplete Hazard Layers (Trigger `T-CRI-015`)
- **Hand Calculation Cause**: In manual calculations, missing hazard records (e.g., cold spell or landslide data not reported for a tambon) were treated as `0.0`, artificially diluting the composite CRI average.
- **App Processing Script Fix**: App v4.1 implemented **Complete-Hazard Exclusions**, omitting missing/incomplete hazard dimensions from the composite score average so un-reported hazards do not distort the index.

### 3. Household-to-Person Demographic Unit Conversion (`CH-CRI-015`)
- **Hand Calculation Cause**: Manual workbooks directly treated raw household counts from DDPM disaster assistance records as individual person counts, assuming a 1:1 ratio.
- **App Processing Script Fix**: The analytical export pipeline dynamically applies DOPA demographic household-to-people multipliers per location on-the-fly, accurately converting impacted households into individual human impact counts.

### 4. Subdistrict Percentiles vs. Provincial Min-Max Normalization Protocol (`T-CRI-011`)
- **Hand Calculation Cause**: Early hand calculations used nationwide subdistrict percentile ranking (0–100 quantile scores).
- **App Processing Script Fix**: Standardized on a **Provincial Min-Max Scoring Protocol** (`D-CRI-015`) to enable presentation-ready regional comparisons across hazard metrics.

### 5. Temporal Window & Proxy Shift (2559–2566 vs 2560–2567)
- **Hand Calculation Cause**: Legacy manual sheets evaluated historical windows from 2559–2566 and relied on OAE agricultural loss proxies.
- **App Processing Script Fix**: Standardized on the 2560–2567 annual panel using DDPM Silver transactional facts (`fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv`) and Government Advance Payment relief proxies (`silver_govt_adv_payment_annual_long.csv`).

---

## Potential Ledger Yields (T-E-D-A Hypotheses)

- **[T] Potential Trigger**: Mismatch between Streamlit app computed CRI scores and hand-calculated Excel sheets caused by embedded DOPA aggregate rows, zero vs NaN treatment, and household unit conversions.
- **[E] Supporting Evidence**:
  - `ψ/incubate/DCCE/CRI/data_system/output/notebooks/cri_workbook_pipeline_explainer.html`
  - `ψ/incubate/DCCE/CRI/data_system/script/normalize_population_to_silver.py`
  - `ψ/incubate/DCCE/CRI/CRI-Change-Log.md` (`CH-CRI-015`)
- **[D] Potential Decision**: Standardize dynamic demographic multiplication, complete-hazard exclusions, and provincial Min-Max scaling in production app scripts.
- **[A] Target Asset**: `ψ/incubate/DCCE/CRI/data_system/script/normalize_population_to_silver.py` & `tmp_stage1_export.py`

---

**Trace Log**: `file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/traces/2026-07-30/1551_cri-calculation-mismatch-app-vs-hand.md`
