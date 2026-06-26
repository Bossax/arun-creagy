# Trace Log: what are the data fields of impact datasets of DDPM ?

- **Trace ID**: efdc9b6d-26e2-4e72-95bc-f1755734ffe4
- **Timestamp**: 2026-06-26T23:45:00+07:00
- **Friction Score**: 2/10 (Highly documented within local project files and metadata)

---

## 🔍 Discovered Evidence

Evidence was gathered from the following workspace assets:

1. **Detailed Audit Report**: [DDPM_data_review_from_CRI_project.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md) — Audits the available DDPM streams (village disaster impact and financial relief).
2. **Gold Processing Plan**: [2026-05-18_national-ddpm-tambon-impact-notebook-plan.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/2026-05-18_national-ddpm-tambon-impact-notebook-plan.md) — Outlines how the Silver village stats are aggregated to Gold tambon metrics.
3. **Index Architecture Plan**: [2026-06-14_granular-impact-index-plan.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/plans/2026-06-14_granular-impact-index-plan.md) — Distinguishes between human-impact metrics (tambon level) and economic metrics (province level).

---

## 📊 DDPM Data Fields and Structure

The DDPM (Department of Disaster Prevention and Mitigation) data estate in the CRI/CRDB projects is split into two distinct streams because the original datasets are reported at different spatial and thematic grains:

### 1. Village/Event disaster impact stream
*Source File: [master_village_disaster_stat_2557_2567.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv)*

This is the most granular, event-level and village-level table. It records physical damage and human casualties:

| Category | Field Name | Description |
|---|---|---|
| **Incident Identity** | `Incident Name` | Name of the disaster event |
| | `Title` | Descriptive title |
| **Hazard & Timing** | `ปี` | B.E. Year |
| | `Disaster Type` | Source-reported hazard type (e.g. flood, drought) |
| | `Disaster Date` | Start date of the disaster |
| | `Relief Declared Date` | Date when emergency relief was officially declared |
| | `Disaster Area Date` | Date when disaster area was designated |
| | `Other Announce Date` | Additional announcement dates |
| | `End Disaster Date` | Date the disaster situation ended |
| **Location Spine** | `Province Code` | Province administrative code |
| | `Province` | Province name (Thai) |
| | `District Code` | District administrative code |
| | `District` | District name (Thai) |
| | `Subdistrict Code` | Subdistrict (Tambon) administrative code |
| | `Subdistrict` | Subdistrict name (Thai) |
| | `Moo` | Moo/Village group number |
| | `Village Code` | Village administrative code |
| **Context** | `Zone Center Name` | Regional center |
| | `Cause` | Cause of the disaster |
| | `Status` | Event status |
| | `Situation` | Brief text description of the situation |
| **Human Impact** | `Affected People` | Number of affected persons |
| | `Affected Households` | Number of affected households |
| | `Evacuated People` | Number of evacuated persons |
| | `Evacuated Households` | Number of evacuated households |
| | `Deaths` | Number of fatalities |
| | `Missing` | Number of missing persons |
| | `Injured` | Number of injured persons |
| **Damage Categories** | `Housing Damage` | Count of houses damaged |
| | `Business Damage` | Count of businesses/shops damaged |
| | `Agriculture Damage` | Agricultural area or impact count |
| | `Livestock Damage` | Count of livestock lost |
| | `Fishing Damage` | Fish/aquaculture ponds damaged |
| | `Transport Damage` | Roads, bridges, or transport assets damaged |
| | `Health Damage` | Healthcare facilities damaged |
| | `Culture Damage` | Cultural sites damaged |
| | `Education/Sports` | Educational and sports facilities damaged |
| | `Utilities Damage` | Utility lines/infrastructure damaged |
| | `Govt Property Damage` | Government buildings/assets damaged |
| | `Other Public Benefits_1` | Miscellaneous public assets category 1 |
| | `Other Public Benefits_2` | Miscellaneous public assets category 2 |

---

### 2. Government Advance Payment / Financial Relief stream
*Source File: [silver_govt_adv_payment_annual_long.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv)*

This stream tracks the official disaster advance payments (**เงินทดรองราชการ**) allocated at the **province-level** for specific hazards (typically capped at 20M THB per declaration):

- **Identity & Geography**:
  - `record_id`: Unique identifier
  - `province_code`: 2-digit provincial DOPA code
  - `province_name_th`: Provincial name (Thai)
  - `location_id`: Spatial reference
  - `admin_level`: Level of admin unit (e.g. `province`)
- **Hazard Identifiers (Original & Canonical)**:
  - `hazard_code`, `hazard_name_en`, `hazard_name_th`
  - `canonical_hazard_code`, `canonical_hazard_name_en`, `canonical_hazard_name_th`
- **Temporal Dimensions**:
  - `year_be`, `year_ce`
- **Metric Payload**:
  - `value`: Amount allocated in **THB**
  - `value_type`: Nature of value (e.g. `actual_payment`)
  - `unit`: Currency unit (`THB`)
- **Lineage Fields**:
  - `source_system`, `source_dataset`, `source_file`, `source_sheet`, `source_row_number`, `source_column`, `raw_value`

---

### 3. Derived Gold Analytical Fields (CRI Products)
*Source File: [fact_ddpm_tambon_impact_climate_2560_2567.csv](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv)*

These fields are **analytically derived** by the CRI pipeline and are not natively reported by DDPM:

- **Aggregates**: `affected_households_sum`, `affected_people_sum`, `deaths_sum` (summed and climate-filtered over the B.E. 2560–2567 window).
- **Trend Metrics**: `avg_yoy_change` (yearly change rate based on households).
- **Percentiles**: `pct_national_affected_households_sum`, `pct_national_affected_people_sum`, `pct_national_deaths_sum`, `pct_national_avg_yoy_change` (percentile ranking nationwide `0..1`).

---

## ⚠️ Important Methodological Boundaries

1. **Financial vs. Physical Grains**: Physical impacts are reported down to the village level. Financial relief data is strictly **province-level** and cannot be downscaled to subdistricts without using modeled spatial proxies (e.g. building footprint ratios).
2. **Hazard Gaps**: The financial relief stream only captures **flood, drought, and windstorm**; it explicitly excludes landslides and heatwaves since emergency relief payments were not separately logged or capped for them.
3. **Relief $\neq$ Economic Loss**: The financial stream records government emergency advance payments, which are subject to administrative caps. It is a fiscal-response indicator rather than an estimation of absolute economic damage.

---

## 🔮 Potential Ledger Yields (T-E-D-A Hypothesis)

- **[T] Potential Trigger**: Distinguish raw administrative inputs from analytical derivatives to prevent downstream modeling errors and false validation.
- **[E] Supporting Evidence**: [DDPM_data_review_from_CRI_project.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md)
- **[D] Potential Decision**: Ensure the CRDB Loss and Damage conceptual data model handles spatial and temporal asymmetry by separating event-level counts from province-level relief.
- **[A] Target Asset**: [DDPM_data_review_from_CRI_project.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md)
