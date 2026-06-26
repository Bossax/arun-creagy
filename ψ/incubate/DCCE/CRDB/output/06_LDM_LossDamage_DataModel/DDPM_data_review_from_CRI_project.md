# DDPM Data Review from CRI Project

## 1. Scope and reviewed sources

This review audits what DDPM-related data is actually available inside the CRI project for downstream loss-and-damage design work, using evidence from Bronze definition context, Silver normalized tables, Gold analytical tables, and the transformation code that connects them.

Reviewed sources:

- Lineage and dictionary context in [`metadata/data-lineage.md`](ψ/incubate/DCCE/CRI/data_system/metadata/data-lineage.md:1) and [`metadata/data-dictionary.md`](ψ/incubate/DCCE/CRI/data_system/metadata/data-dictionary.md:56)
- Bronze DDPM definition context in [`cri-data-govt-adv-payment.definition.md`](ψ/incubate/DCCE/CRI/data_system/data/0_bronze/2026-06-12_cri_proj_data/definition_sheet_extracts/cri-data-govt-adv-payment.definition.md:1) and [`cri-data-govt-adv-payment.definition.json`](ψ/incubate/DCCE/CRI/data_system/data/0_bronze/2026-06-12_cri_proj_data/definition_sheet_extracts/cri-data-govt-adv-payment.definition.json:1)
- Source-near DDPM village stream in [`master_village_disaster_stat_2557_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv:1)
- Silver DDPM financial outputs in [`silver_govt_adv_payment_annual_long.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv:1), [`silver_govt_adv_payment_period_total.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/silver_govt_adv_payment_period_total.csv:1), and [`govt_adv_payment_normalization_report.json`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/govt_adv_payment_normalization_report.json:1)
- Gold DDPM impact outputs in [`fact_ddpm_tambon_impact_climate_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv:1), [`fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv:1), hazard-specific Gold tables listed in [`data/2_gold/ddpm`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm), and QA output [`qa_invalid_code_totals_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/qa/qa_invalid_code_totals_2560_2567.csv:1)
- Transformation logic in [`build_gold_ddpm_tambon_impact_climate_2560_2567.py`](ψ/incubate/DCCE/CRI/data_system/script/ELT/build_gold_ddpm_tambon_impact_climate_2560_2567.py:180)

This review does **not** perform the separate CRDB MVD gap analysis.

## 2. Lineage summary of DDPM streams in CRI

The CRI project contains two distinct DDPM-related streams:

1. **Village disaster impact stream**
   - Documented in [`data-lineage.md`](ψ/incubate/DCCE/CRI/data_system/metadata/data-lineage.md:7)
   - Consolidated from DDPM yearly raw files into [`master_village_disaster_stat_2557_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv:1)
   - Used as the empirical base for Gold tambon-level climate impact tables via [`build_gold_ddpm_tambon_impact_climate_2560_2567.py`](ψ/incubate/DCCE/CRI/data_system/script/ELT/build_gold_ddpm_tambon_impact_climate_2560_2567.py:186)

2. **Government advance payment / financial relief stream**
   - Documented in [`data-lineage.md`](ψ/incubate/DCCE/CRI/data_system/metadata/data-lineage.md:135)
   - In the current CRI project this stream is represented by workbook-derived Bronze extracts and Silver normalized tables, not by a materialized [`1_silver/ddpm`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm) financial file set
   - Normalized into province-hazard-year and province-hazard-period tables in [`silver_govt_adv_payment_annual_long.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv:1) and [`silver_govt_adv_payment_period_total.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/silver_govt_adv_payment_period_total.csv:1)

The practical implication is that CRI does **not** expose one unified DDPM dataset. It exposes:

- a source-near village-event impact table, and
- a separate province-level government spending proxy.

Those two streams are analytically related in CRI, but they are not the same kind of reporting.

## 3. DDPM source dataset inventory

### 3.1 Source-near DDPM village stream

The operative source-near table available in CRI is [`master_village_disaster_stat_2557_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv:1). Its schema shows that it preserves incident-level and village-level DDPM reporting structure, including:

- incident identifiers and titles: `Incident Name`, `Title`
- disaster typing and timing: `ปี`, `Disaster Type`, `Disaster Date`, `Relief Declared Date`, `Disaster Area Date`, `Other Announce Date`, `End Disaster Date`
- administrative location fields: `Province Code`, `Province`, `District Code`, `District`, `Subdistrict Code`, `Subdistrict`, `Moo`, `Village Code`
- reporting context fields: `Zone Center Name`, `Cause`, `Status`, `Situation`
- human impact metrics: `Affected People`, `Affected Households`, `Evacuated People`, `Evacuated Households`, `Deaths`, `Missing`, `Injured`
- damage-category metrics: `Housing Damage`, `Business Damage`, `Agriculture Damage`, `Livestock Damage`, `Fishing Damage`, `Transport Damage`, `Health Damage`, `Culture Damage`, `Education/Sports`, `Utilities Damage`, `Govt Property Damage`, `Other Public Benefits_1`, `Other Public Benefits_2`

This is the richest DDPM-related dataset in CRI in terms of variable breadth.

### 3.2 Workbook-derived DDPM financial relief stream

Bronze definition context in [`cri-data-govt-adv-payment.definition.md`](ψ/incubate/DCCE/CRI/data_system/data/0_bronze/2026-06-12_cri_proj_data/definition_sheet_extracts/cri-data-govt-adv-payment.definition.md:7) shows that the Government Advance Payment workbook is specifically about **วงเงินทดรองราชการ** rather than direct damage accounting.

The definition explicitly states:

- Bangkok values include both Bangkok administration and affiliated supporting agencies
- drought includes drought and delayed-rain/rain-shortfall under the project interpretation
- the dataset **does not include** landslide and heat because relief values were not recorded for those hazards
- the dataset does not include local budget spending, agriculture compensation paid directly by the agriculture ministry, or donations

This means the financial stream is a partial fiscal response dataset, not a full monetary loss dataset.

## 4. Variable inventory by layer

### 4.1 Bronze / source-near DDPM reporting

#### A. Village impact reporting variables

Available in [`master_village_disaster_stat_2557_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv:1):

- event identity and narrative context
- raw DDPM hazard labels in `Disaster Type`
- event and declaration dates
- province/district/subdistrict/village codes and names
- human impact counts
- sector/damage-category counts or magnitudes across multiple categories

Important boundary: although this file sits in the CRI Silver folder structure, in practical analytical terms it is still **source-near DDPM reporting**. It preserves the DDPM event/village record model rather than a redesigned normalized fact schema.

#### B. Government advance payment Bronze reporting variables

The Bronze definition layer indicates the workbook reports, by province and hazard sheet:

- `จังหวัด`
- annual values for `2560` through `2567`
- period total `2560 - 2567`

This contract is recorded in [`govt_adv_payment_normalization_report.json`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/govt_adv_payment_normalization_report.json:97).

The Bronze reporting variable is therefore essentially one monetary measure: government advance payment amount, split by province, hazard, and time column.

### 4.2 Silver normalized variables

#### A. Silver government advance payment annual table

[`silver_govt_adv_payment_annual_long.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv:1) normalizes the workbook into one row per province + hazard + year with the fields:

- identity/geography: `record_id`, `province_code`, `province_name_th`, `location_id`, `admin_level`
- source hazard labels: `hazard_code`, `hazard_name_en`, `hazard_name_th`
- canonical hazard labels: `canonical_hazard_code`, `canonical_hazard_name_en`, `canonical_hazard_name_th`
- time: `year_be`, `year_ce`
- metric payload: `value`, `value_type`, `unit`
- lineage fields: `source_system`, `source_dataset`, `source_file`, `source_sheet`, `source_row_number`, `source_column`, `raw_value`

This is a proper normalized Silver fact table, but it only contains one substantive measure: annual payment amount in baht.

#### B. Silver government advance payment period-total table

[`silver_govt_adv_payment_period_total.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/silver_govt_adv_payment_period_total.csv:1) adds period semantics:

- `time_scope`, `time_scope_type`, `time_scope_label`
- `period_start_be`, `period_end_be`
- `raw_period_value`
- `raw_period_is_formula`
- `derived_from_annual_values`

This table is analytically useful because it separates raw workbook formula evidence from a CRI-derived numeric period total.

#### C. What is not materialized as a current CRI Silver table

[`data-lineage.md`](ψ/incubate/DCCE/CRI/data_system/metadata/data-lineage.md:190) still references [`master_financial_relief_by_hazard.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_financial_relief_by_hazard.csv) and related legacy paths, but [`data/1_silver/ddpm`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm) is not populated as a browsable directory in the current project listing. In practice, the operative Silver financial outputs are the workbook-normalized files under [`data/1_silver/govt_adv_payment`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment).

### 4.3 Gold analytical / derived variables

#### A. Gold tambon aggregate table

[`fact_ddpm_tambon_impact_climate_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv:1) contains one row per `subdistrict_code` with:

- `subdistrict_code`, `province_code`
- aggregated raw-impact metrics: `affected_households_sum`, `affected_people_sum`, `deaths_sum`
- derived trend metric: `avg_yoy_change`
- authoritative names from the spine: `province_name_th`, `district_name_th`, `subdistrict_name_th`
- national comparative metrics: `pct_national_affected_households_sum`, `pct_national_affected_people_sum`, `pct_national_deaths_sum`, `pct_national_avg_yoy_change`

The first three metrics are aggregated from DDPM reporting. The remaining fields are CRI-derived.

#### B. Gold yearly tambon panel

[`fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv:1) contains:

- `canonical_hazard_id`, `canonical_hazard_code`, `canonical_hazard_name_th`
- `subdistrict_code`, `province_code`
- `year_be`
- yearly summed metrics: `affected_households_sum`, `affected_people_sum`, `deaths_sum`
- derived trend component: `yoy_delta_affected_households`

This is already several steps removed from original DDPM reporting because it applies hazard mapping, climate filtering, geographic rollup to tambon, and zero-filling of missing year slots.

#### C. Hazard-specific Gold tables

Gold also includes hazard-specific period and yearly files such as:

- [`fact_ddpm_tambon_impact_climate_flood_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_flood_2560_2567.csv:1)
- [`fact_ddpm_tambon_impact_climate_drought_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_drought_2560_2567.csv:1)
- [`fact_ddpm_tambon_impact_climate_windstorm_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_windstorm_2560_2567.csv:1)
- [`fact_ddpm_tambon_impact_climate_landslide_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_landslide_2560_2567.csv:1)
- [`fact_ddpm_tambon_impact_climate_cold_spell_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_cold_spell_2560_2567.csv:1)

These files expose hazard-disaggregated outputs that are not directly available in the aggregate all-climate table.

## 5. What DDPM is actually reporting vs what CRI derives analytically

### 5.1 What DDPM is actually reporting in practice

Based on the source-near village table and workbook definitions, DDPM reporting available in CRI consists of:

1. **Village/event impact reporting**
   - event dates and administrative locations
   - hazard labels
   - affected people and households
   - evacuations
   - deaths, missing, injured
   - multiple damage-category fields

2. **Province-level government advance payment reporting**
   - annual and multi-year payment amounts
   - only for specific hazards represented in the workbook extracts

### 5.2 What CRI derives analytically from DDPM

CRI adds substantial derived structure, including:

- canonical hazard mapping
- climate-hazard filtering
- rollup from village to tambon
- rollup from events to yearly and multi-year aggregates
- zero-filled yearly panels for missing tambon-year combinations
- year-over-year deltas and average year-over-year change
- authoritative DOPA naming joins
- national percentile fields
- period totals reconstructed from annual values in the government payment stream

Therefore, many of the most design-friendly fields in Gold are **not** original DDPM reporting variables. They are CRI analytical products built on top of DDPM reporting.

## 6. Hazard coverage and exclusions

### 6.1 Village impact stream hazard coverage

The Gold build code in [`build_gold_ddpm_tambon_impact_climate_2560_2567.py`](ψ/incubate/DCCE/CRI/data_system/script/ELT/build_gold_ddpm_tambon_impact_climate_2560_2567.py:190) maps source hazard variants to canonical hazards and filters to `hazard_group == climate` at [`build_gold_ddpm_tambon_impact_climate_2560_2567.py`](ψ/incubate/DCCE/CRI/data_system/script/ELT/build_gold_ddpm_tambon_impact_climate_2560_2567.py:206).

Materialized hazard-specific Gold files show the practical covered hazard set:

- flood
- drought
- windstorm
- landslide
- cold spell

### 6.2 Financial stream hazard coverage

The Silver financial outputs only cover:

- flood
- drought
- windstorm

This is evidenced both by the normalization report counts in [`govt_adv_payment_normalization_report.json`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/govt_adv_payment_normalization_report.json:130) and by the Bronze definition text in [`cri-data-govt-adv-payment.definition.md`](ψ/incubate/DCCE/CRI/data_system/data/0_bronze/2026-06-12_cri_proj_data/definition_sheet_extracts/cri-data-govt-adv-payment.definition.md:14).

### 6.3 Explicit exclusions

The workbook definition explicitly excludes:

- landslide relief values
- heat relief values
- local budget spending by provinces/Bangkok
- agriculture compensation outside the DDPM advance-payment mechanism
- donations

So any design interpretation that treats this financial stream as “total DDPM losses” would be incorrect.

## 7. Spatial and temporal granularity

### 7.1 Spatial granularity

- Source-near village stream: **village/event-level**, with province, district, subdistrict, moo, and village code fields in [`master_village_disaster_stat_2557_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv:1)
- Silver government payment stream: **province-level**
- Gold impact stream: **tambon-level** for analytical impact outputs

The project therefore spans multiple incompatible grains. The financial stream cannot be interpreted as tambon-level DDPM reporting because it is only province-level in source form.

### 7.2 Temporal granularity

- Source-near village stream covers B.E. `2557–2567` in the consolidated file name and preserves event dates in source form
- Gold impact products are locked to `2560–2567` per the code and metadata in [`data-dictionary.md`](ψ/incubate/DCCE/CRI/data_system/metadata/data-dictionary.md:83)
- Silver financial stream provides annual columns for `2560–2567` plus a multi-year total `2560 - 2567`

This means CRI’s design-ready DDPM analytical window is narrower than the raw DDPM village history available in the source-near table.

## 8. Known data-quality and interpretation caveats

### 8.1 Invalid-code drops in Gold impact build

[`qa_invalid_code_totals_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/qa/qa_invalid_code_totals_2560_2567.csv:1) shows:

- `invalid_code_rows = 2089`
- `valid_code_rows = 188774`

These invalid-code rows are excluded from Gold tambon aggregation because Gold depends on a valid `subdistrict_code` built from DDPM reporting.

### 8.2 Geometry coverage is a hard QA gate

[`build_gold_ddpm_tambon_impact_climate_2560_2567.py`](ψ/incubate/DCCE/CRI/data_system/script/ELT/build_gold_ddpm_tambon_impact_climate_2560_2567.py:333) enforces a geometry-coverage QA gate. If subdistrict codes in the stats layer are missing from the enriched geometry layer, the build is designed to fail.

This is a strong integrity control, but it also means Gold outputs are shaped by spatial conformance requirements, not just source reporting.

### 8.3 Financial normalization warnings

[`govt_adv_payment_normalization_report.json`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment/govt_adv_payment_normalization_report.json:17) records these issues:

- 3 province rows could not join to the location dimension
- 9 period total rows were malformed
- 15 numeric period totals differed from derived annual sums
- annual and period output row counts were below expectation
- annual row expansion counts were uneven

This means the financial Silver outputs are usable but not clean enough to treat as fully frictionless canonical truth.

### 8.4 Legacy lineage references are partly stale

[`data-lineage.md`](ψ/incubate/DCCE/CRI/data_system/metadata/data-lineage.md:188) still references legacy DDPM Silver files such as [`master_financial_relief_by_hazard.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/ddpm/master_financial_relief_by_hazard.csv), while the practical current outputs are in [`data/1_silver/govt_adv_payment`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/govt_adv_payment).

Interpretation should therefore privilege materialized files and active scripts over prose lineage alone.

### 8.5 Gold metrics may look like direct reporting when they are not

Fields such as `avg_yoy_change`, `pct_national_*`, and `yoy_delta_affected_households` are CRI analytical constructs. They should not be catalogued as DDPM-reported variables in downstream design.

## 9. Practical DDPM data availability profile for CRDB loss-and-damage design

The practical DDPM availability profile in the CRI project is as follows:

1. **Strongest direct DDPM evidence is non-monetary and source-near**
   - DDPM provides rich village/event reporting on affected people, affected households, deaths, injuries, evacuations, and multiple damage-category fields.

2. **Monetary DDPM evidence in CRI is a limited fiscal-response proxy**
   - The available payment data is government advance payment by province, hazard, and year/period.
   - It is not full loss accounting and explicitly excludes several relevant categories and hazards.

3. **Design-friendly DDPM tables in Gold are analytical derivatives, not raw DDPM variables**
   - Tambon-level climate impact facts, zero-filled yearly panels, percentile ranks, and trend fields are all CRI-derived.

4. **Hazard coverage is asymmetric across streams**
   - Village impact stream supports at least flood, drought, windstorm, landslide, and cold spell in Gold.
   - Financial stream supports only flood, drought, and windstorm, with explicit exclusion of landslide and heat.

5. **Spatial granularity is mixed**
   - Source-near impacts are village/event-level.
   - Financial data is province-level.
   - Gold analytical outputs are tambon-level after aggregation.

## 10. Concise conclusion

Within the CRI project, DDPM is actually available in two materially different forms: a rich village/event impact reporting stream and a much narrower province-level government advance payment stream. The village stream is the primary evidence base for downstream impact design because it contains the real DDPM-reported human-impact and damage-category variables. The financial stream should be treated as a partial public-finance response proxy, not as a direct measure of total economic loss or total DDPM monetary damage.

For CRDB loss-and-damage design, the key boundary is this: **original DDPM reporting mostly gives event/village impact counts and damage-category fields, while many of the most usable subdistrict-level and ranked DDPM variables in CRI are Gold analytical derivatives created by CRI, not variables DDPM reported natively.**
