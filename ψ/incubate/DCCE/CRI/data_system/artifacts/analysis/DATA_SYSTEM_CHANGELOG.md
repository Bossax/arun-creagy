# CRI Data System Module Change Log (`data_system`)

All notable technical changes, schema updates, pipeline bugfixes, and version releases for the **CRI Data System** module (`ψ/incubate/DCCE/CRI/data_system/`) are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [v4.3.0] - Planned Release (Complete DDPM Medallion Rebuild Specification)

### 🚨 Fixed (Critical Bug Fixes)
* **Complete Rebuild of All DDPM-Derived Datasets**: Rebuild `1_silver/ddpm/master_village_disaster_stat_2557_2567.csv` and `2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv` from raw Bronze CSV files with strict `parse_clean_numeric()` comma sanitization to recover **1.1 Million Households** silently lost due to uncleaned comma coercion.
* **Mandatory Comma-String Sanitization Wrapper (`parse_clean_numeric`)**: Enforce explicit `.astype(str).str.replace(',', '').str.strip()` prior to numerical conversion across all ETL, audit, and exporter scripts to prevent `pd.to_numeric(errors='coerce')` from silently dropping numbers $\ge 1,000$ as `NaN` (0).
* **Single-Year Data Leakage Bug in Exporter**: Fix column key lookup mismatch in `tmp_stage1_export.py` where single-year 2567 exports (`period_2567/all/affected_hh_abs.json`) look up missing column `s_affected_hh_abs`, falling back to `prov_avg_cri` and silently leaking the 7-year annualized average (`16,117.17`) into the single-year 2567 export folder.
* **Financial Data Overwrite in `loss_abs.json`**: Fix critical data loss bug where `tmp_stage1_export.py` replaces raw government advance relief amounts (`197,934,176.28 THB`) with MinMax normalized score `1.0` (because Nakhon Si Thammarat is Rank #1), obliterating raw financial numbers from exported JSON payloads.

### 🏷️ Changed (Schema Governance)
* **Unified JSON Payload Schema**: Standardize exported JSON records across `build_exports/stage1/` to explicitly expose `raw_value`, `normalized_score`, `display_value`, and `rank_desc`.
* **Explicit Payload Metadata**: Add root `unit_metadata` block to declare primary unit (`baht`, `households`, `people`) and demographic multiplier application level ($R_{\text{subdistrict}}$).

### 🗑️ Deprecated & Removed
* **Legacy Period Directory Purge**: Officially mark `period_2560_2567` (8-year window) as **LEGACY**. Remove legacy build code in `tmp_stage1_export.py` to standardize pipeline outputs strictly on `period_2567` (single-year) and `period_2561_2567` (canonical 7-year window).

### 🛡️ Added (Verification Gates)
* **Automated Medallion Pre-Flight Gate**: Integrate `run_nakhon_audit_stage3.py` into the build pipeline as a blocking assertion to verify 100% financial and casualty lineage fidelity from Bronze raw files $\rightarrow$ Silver $\rightarrow$ Gold $\rightarrow$ Build Exports before publishing UI assets.

---

## [v4.2.0] - 2026-07-30 (Current Production Baseline)

* Active running dashboard release (`output/cri_impact_app_v3/app.py`).

---

## [v4.1.0] - 2026-07-16 (Demographic Multiplier & Hazard Exclusions)

* Dynamic DOPA Household Multipliers ($R_{\text{subdistrict}}$) & Complete Hazard Verification.

---

## [v4.0.0] - 2026-06-19 (Disaggregated Stage 1 Export Engine)

* Stage 1 Exporter Engine (`tmp_stage1_export.py`).
