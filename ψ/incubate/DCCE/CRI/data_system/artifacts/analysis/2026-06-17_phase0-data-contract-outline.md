# Phase 0 — Data Contract Outline Ground Truth

## Purpose

This file defines the baseline structure that the frontend data-contract subtask must refine and freeze.

It is not yet the final schema, but it is the ground-truth outline Orchestrator mode must use for task allocation.

---

## 1. Packaging principles

1. one JSON file per metric
2. one copy of each metric file per period mode
3. one manifest file for discovery
4. province geometry loaded globally
5. tambon geometry loaded lazily or partitioned by province

---

## 1.1 Authoritative source assets for the export layer

The data-contract subtask must use these concrete source assets as the upstream inputs for web-export generation.

### Core analytical CSV sources

- [`fact_ddpm_tambon_impact_climate_2560_2567.csv`](../data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv:1)
- [`fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv`](../data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv:1)
- [`silver_population_annual.csv`](../data/1_silver/population/silver_population_annual.csv:1)
- [`silver_household_annual.csv`](../data/1_silver/population/silver_household_annual.csv:1)
- [`silver_govt_adv_payment_annual_long.csv`](../data/1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv:1)
- [`silver_gpp_annual_long.csv`](../data/1_silver/gpp/silver_gpp_annual_long.csv:1)
- [`silver_heatwave_impact_long.csv`](../data/1_silver/heatwave/silver_heatwave_impact_long.csv:1)

### Spatial source assets

- [`province_boundaries_enriched.shp`](../data/1_silver/dopa/province_boundaries_enriched.shp)
- [`tambon_boundaries_enriched.shp`](../data/1_silver/dopa/tambon_boundaries_enriched.shp)

### Working logic source

- [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb:1)

### Mode-to-source rules

- `2560–2567 average` province human metrics may follow the aggregate-period logic demonstrated in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb:155).
- `2567 only` human metrics must switch to the yearly DDPM fact in [`fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv`](../data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv:1).
- `2567 only` population, household, GPP, and govt advance payment metrics must use their annual rows rather than period averages.
- Heat exports must preserve separate `heat_deaths` and `heat_injured` files from [`silver_heatwave_impact_long.csv`](../data/1_silver/heatwave/silver_heatwave_impact_long.csv:1).

---

## 2. Period folders

Required period partitions:

- `period_2560_2567`
- `period_2567`

Each period folder must contain the same metric-file pattern wherever the metric exists in both modes.

---

## 3. CRI metric files

Expected CRI metric files per period:

- `deaths_abs.json`
- `deaths_rate.json`
- `affected_hh_abs.json`
- `affected_rate.json`
- `loss_abs.json`
- `loss_per_gpp.json`
- `cri_score.json`

Each file should support:

- province choropleth rendering
- legend generation
- top 10 / bottom 10 ranking table

---

## 4. Tambon human-impact files

Expected files per period:

- `tambon_deaths.json`
- `tambon_affected_households.json`

These files must support:

- national view
- province zoom view
- ranking tables that can switch output grain

---

## 5. Heat files

Expected files per period:

- `heat_deaths.json`
- `heat_injured.json`

This two-file model is frozen by the Phase 0 decision baseline.

---

## 6. Spatial files

Expected spatial structure:

- `spatial/province_boundaries.geojson` or equivalent optimized format
- `spatial/tambon/<province_code>.geojson` or equivalent optimized format

The technical-architecture subtask may recommend TopoJSON instead of GeoJSON, but the partitioning rule must remain intact.

---

## 7. Manifest responsibilities

The manifest must allow the frontend to discover:

- available periods
- available metric keys
- human-readable metric labels
- units
- file paths or logical asset references
- last updated timestamp or version marker
- source asset lineage references for the export step

The manifest should also declare, per screen family, which exported JSON and spatial files are expected to be read by the frontend.

---

## 8. Common fields to evaluate in schema design

The data-contract subtask must evaluate whether the following fields should be standard across metric files:

- `province_code`
- `province_name_th`
- `province_name_en` if available
- `metric_key`
- `metric_label`
- `value`
- `unit_label`
- `rank_desc`
- `period_key`
- `period_label`

For map display, the subtask must also decide whether to include:

- precomputed legend bounds
- normalized score values
- display-friendly formatted values

---

## 9. Ranking-table strategy to freeze

The subtask must explicitly decide one of these:

1. ranking tables are embedded directly inside each metric file
2. ranking tables are derived client-side from metric records
3. ranking tables live in separate dedicated ranking files

The recommended baseline for the first build is **embedded rankings** to reduce frontend logic and eliminate drift.

---

## 10. Instruction to Orchestrator mode

Assign a dedicated subtask to convert this outline into a precise schema and file-contract artifact before implementation work starts.

That subtask must explicitly map each exported JSON file back to the concrete source CSV / spatial asset listed in [1.1](./2026-06-17_phase0-data-contract-outline.md:20).
