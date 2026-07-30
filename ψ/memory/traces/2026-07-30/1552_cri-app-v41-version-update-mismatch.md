---
type: trace
traceId: TRACE-20260730-CRI-APP-V41-RELEASE
date: 2026-07-30
query: "find the recent issues about CRI datasets that required us to revisit the data processing scripts. We got mismatched results between the computed CRI shown on the app and hand calculated. this issue required us to update the cri app version"
target: "CRI App Version Upgrade (v4.1 & v3.1 Data Pipeline Fixes)"
mode: smart
timestamp: 2026-07-30 15:52
friction_score: 1.0
coverage: [oracle, files, git, memory, session]
confidence: high
---

# Trace: CRI Score Mismatch & App Version Upgrade (v3.1 & v4.1 Release)

**Target**: CRI Web App & Stage 1 Analytical Exporter (`tmp_stage1_export.py` & `app.py`)  
**Mode**: smart | **Friction**: 1.0 | **Confidence**: high  
**Time**: 2026-07-30 15:52  

## Executive Summary

The calculation mismatch between hand-calculated CRI scores and the web app's computed CRI scores directly forced a structural overhaul of the export pipeline and **an official upgrade of the CRI App version to `v4.1`** (and previously `v3.1`). 

The core issue was that the web app was computing composite CRI scores by averaging across incomplete hazard dimensions and un-converted household units, causing the app's composite scores to diverge from hand-calculated benchmarks.

---

## 🔍 The Root Cause & Required App Version Upgrades

### 1. Composite Score Distortions from Incomplete Hazards (Trigger `T-CRI-015` $\rightarrow$ App `v4.1`)
* **The Issue**: Hand-calculated benchmark scores only included hazards with complete disaster damage and financial relief data (Flood, Drought, Windstorm). However, the app's export pipeline was averaging all 6 hazards—including Landslide, Wildfire, and Cold Spell (which lack financial relief records)—causing missing values/zeros to dilute the composite CRI average.
* **The Fix**: Refactored `tmp_stage1_export.py` to enforce **Complete-Hazard Strictness**:
  - The overall composite CRI score is calculated strictly from **Flood, Drought, and Windstorm**.
  - Incomplete hazards (Landslide, Wildfire, Cold Spell) are omitted from the composite score average.
  - CRI score selectors for incomplete hazards are disabled in the app UI (`pages/cri.py`).
* **App Version Update**: Upgraded app version metadata in `app.py`, `README.md`, and `pages/methodology.py`, and released/tagged **`v4.1`** (`cri-dcce-impact-dashboard-demo`).

---

### 2. Household vs. People Unit Scale Mismatch (Trigger `T-CRI-015` $\rightarrow$ App `v4.1`)
* **The Issue**: DDPM disaster records report impacted units in **Households**, whereas hand calculations and policy reporting expect **Affected People**. Static 1:1 assumptions created severe scale mismatches.
* **The Fix**: Integrated dynamic DOPA demographic multipliers (`apply_conversion_and_clean_keys`) inside `tmp_stage1_export.py` to convert raw household counts to actual population counts on-the-fly, producing an explicit audit log (`household_to_people_conversion_audit.csv`).

---

### 3. Relief vs. GPP Economic Ratio Mismatch (Trigger `T-CRI-014` $\rightarrow$ App `v3.1`)
* **The Issue**: In an earlier release (v3.0), the app attempted to compute fiscal vulnerability ratios by directly dividing raw Relief (in Baht) by GPP (in Million Baht), producing a 1,000,000x scale error compared to hand-calculated ratios.
* **The Fix**: Corrected unit normalization across Silver and Gold export layers to align Relief (Baht) and GPP (Baht).
* **App Version Update**: Upgraded layout and economic ratio calculations in **`v3.1`** (`CH-CRI-014`, `D-CRI-018`).

---

## 🏛️ Potential Ledger Yields (T-E-D-A Hypotheses)

- **[T] Potential Trigger**: Mismatch between computed CRI shown on the web app and hand-calculated benchmarks due to incomplete hazard averaging and household-to-people unit conversion errors.
- **[E] Supporting Evidence**: 
  - `ψ/memory/retrospectives/2026-07/16/12.16_cri_v4.1_release_and_demographic_multiplier.md`
  - `ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md` (`D-CRI-019` - CRI Impact Dashboard v4.1)
  - `ψ/incubate/DCCE/CRI/CRI-Change-Log.md` (`CH-CRI-014`, `CH-CRI-015`)
- **[D] Potential Decision**: Restrict composite CRI calculations strictly to complete-data hazards (Flood, Drought, Windstorm) and dynamically multiply DOPA demographic ratios on-the-fly under release version `v4.1`.
- **[A] Target Asset**: `ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/app.py` & `tmp_stage1_export.py`

---

**Trace Log**: `file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/traces/2026-07-30/1552_cri-app-v41-version-update-mismatch.md`
