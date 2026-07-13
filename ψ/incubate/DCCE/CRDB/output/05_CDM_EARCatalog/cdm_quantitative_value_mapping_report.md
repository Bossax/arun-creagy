# Common Data Model (CDM) Quantitative Value Mapping & Gap Analysis Report

**Date**: 2026-07-13  
**Context**: Bossax/arun_creagy  
**Source data**: [quantitative_value.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/A-BTR_requirement_analysis/quantitative_value.csv)  
**Target Schema**: [Entities-v3.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Entities-v3.csv) & [Relationships-v4.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Relationships-v4.csv)

---

## 1. Executive Summary

This report documents the updated semantic mapping of **147 raw quantitative metrics** extracted from the UNFCCC A-BTR requirements database to the updated v3 conceptual Common Data Model (CDM) entities. The purpose of this mapping is to verify whether the physical CDM database can successfully house and report all structured numeric outputs required for A-BTR compliance (the "business requirement" test).

All 147 indicators have been mapped with **100% coverage (0 unmapped)**, demonstrating that the updated Lightweight and MVD-synced target schema is structurally complete.

---

## 2. Metric-to-Entity Mapping Matrix

The extracted metrics from `quantitative_value.csv` have been classified into semantic clusters and mapped to their corresponding target entities:

| Metric Cluster / Examples | Representative Metrics | Target CDM Entity | Mapping Type | Count | Status / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Demographic Baseline Stats** | `population`, `urbanization_rate` | `VULNERABILITY_DETERMINANT` | Existing | 2 | Maps baseline normalization variables. |
| **Observed Climate Anomalies** | `observed_annual_mean_temperature` | `METEOROLOGICAL_OBSERVATION` | Existing | 9 | station-measured weather anomalies. |
| **Long-term Physical States** | `historical_sea_level_rise_rate` | `CLIMATE_DRIVER` | Existing | 9 | slow-onset driver trends. |
| **Topographic / Base Datasets** | `elevation_msl_min`, `elevation_msl_max` | `ENVIRONMENTAL_DATA` | Existing | 2 | Topographic baselines mapped as dataset metadata. |
| **Scenario-Based Projections** | `projected_annual_rainfall_increase` | `CLIMATE_PROJECTION` | New Entity | 44 | Solves scenario projections under SSPs. |
| **Hazard Behaviors** | `cyclone_synthetic_intensity_class` | `HAZARDOUS_EVENT` | Existing | 10 | Realized hazard profile metadata. |
| **Disaster Summary Counts** | `flooded_provinces_count`, `fatalities` | `DISASTER_EVENT` | MVD Synced | 30 | Layer A emergency event card human impact stats. |
| **Physical Damage Valuation** | `flood_damage_cost_housing` | `LD_PHYSICAL_DAMAGE` | MVD Synced | 3 | Layer B stock asset loss valuations. |
| **Economic Loss Flows** | `agricultural_production_loss` | `LD_ECONOMIC_LOSS` | MVD Synced | 2 | Layer B counterfactual operating/revenue losses. |
| **Ecological Loss** | `wildfire_burned_area_total` | `ENVIRONMENTAL_LOSS_RECORD` | Existing | 11 | Non-monetized ecosystem and forest impacts. |
| **Project Output KPIs** | `crop_insurance_farmers_covered` | `ADAPTATION_OUTPUT` | Existing | 8 | Immediate project deliverables. |
| **Project Outcome Targets** | `hnap_progress_substantial` | `ADAPTATION_OUTCOME` | Existing | 5 | Capacity building and systemic change targets. |
| **National Index Scores** | `global_climate_risk_index_ranking` | `COMPOSITE_INDEX` | Existing | 6 | Policy indexing and risk score aggregation. |
| **Framework Planning Limits** | `priority_sectors_count` | `DECISION_CONTEXT` | Existing | 3 | Planning scope bounding conditions. |
| **Planning Thresholds** | `extreme_heat_threshold_c` | `RISK_TOLERANCE_PROFILE` | Existing | 3 | Bounding climate thresholds for safety. |
| **Total** | | | | **147** | **100% Classification Complete** |

---

## 3. Resolution of Schema Gaps

1. **Scenario projections**: Mapped successfully to the new **`CLIMATE_PROJECTION`** table. This connects future model outputs directly to scenarios and spatial units.
2. **Topographic baseline metrics**: Mapped to **`ENVIRONMENTAL_DATA`** to avoid schema bloating. Rather than creating custom tables for elevation, it is cataloged as a GIS layer metadata descriptor.
3. **Disaster and Loss & Damage split**: Synced with the LDM MVD design, separating immediate counts (`DISASTER_EVENT`) from validated structural valuations (`LD_PHYSICAL_DAMAGE`) and flow losses (`LD_ECONOMIC_LOSS`).
