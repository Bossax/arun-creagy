# Granular Impact Index Plan from Current CRI Silver and Gold Datasets

## Objective

Define how to process the currently normalized CRI datasets into the **best granular impact index possible**, while being explicit about what can be done faithfully, what can only be approximated, and what remains blocked by data grain constraints.

## Core conclusion

The current data estate supports **two different index tracks**:

1. **Province-level full CRI-style impact index**
   - closest to the pilot methodology in [`Climate Risk Index (CRI) Pilot Methodology.md`](ψ/incubate/DCCE/CRI/inbox_source/Climate%5C%20Risk%5C%20Index%20%28CRI%29%5C%20Pilot%5C%20Methodology.md:35)
   - includes both human and economic impact pillars
   - should remain the official full impact index

2. **Granular subprovince impact products**
   - can be strong for human impact
   - can be useful for local planning
   - must **not** be presented as the same full CRI impact index unless economic and denominator layers are available at matching granularity

---

## 1. Best achievable geography level by metric family

### 1.1 Human impact

**Best achievable geography:** tambon/subdistrict

Primary assets:
- [`fact_ddpm_tambon_impact_climate_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv:1)
- hazard-specific DDPM Gold facts such as [`fact_ddpm_tambon_impact_climate_flood_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_flood_2560_2567.csv:1)

Usable variables:
- `affected_households_sum`
- `affected_people_sum`
- `deaths_sum`
- hazard-specific canonical disaster typing where available

Constraint:
- Heatwave is only province-level in [`silver_heatwave_impact_long.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/heatwave/silver_heatwave_impact_long.csv:1), so it cannot enrich subprovince human-impact scoring directly.

### 1.2 Economic impact

**Best achievable geography:** province

Primary assets:
- [`silver_eco_loss_annual_long.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/eco_loss/silver_eco_loss_annual_long.csv:1)
- [`silver_eco_loss_period_total.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/eco_loss/silver_eco_loss_period_total.csv:1)
- [`silver_gpp_annual_long.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/gpp/silver_gpp_annual_long.csv:1)

Usable variables:
- annual economic loss by province/hazard/year
- cumulative economic loss by province/hazard/period
- annual GPP by province/year
- annual GPP per capita as contextual variable

Constraint:
- no district or tambon economic-loss surface
- no subprovince GPP denominator

### 1.3 Population denominator and exposure

**Best achievable geography:** province and below, with quality filtering

Primary assets:
- [`silver_population_annual.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/population/silver_population_annual.csv:1)
- [`silver_population_period_total.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/population/silver_population_period_total.csv:1)
- [`silver_population_monthly.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/population/silver_population_monthly.csv:1)

Use guidance:
- province annual rows are the cleanest denominators
- subprovince rows can support granular human-impact normalization where `geography_join_ready` and record class are acceptable
- monthly rows are useful for snapshot analysis, not core annual index scoring

---

## 2. Index architecture to adopt

### 2.1 Official full index: province-year CRI-style impact index

This should be the formal continuation of the pilot logic.

Use:
- human impact from province-compatible DDPM impacts and Heatwave province facts
- economic impact from Eco loss annual facts
- GPP denominator/context from GPP Silver
- population denominator from Population annual Silver

Output table recommendation:
- [`province_year_cri_impact_index`](plans/2026-06-14_granular-impact-index-plan.md)

### 2.2 Granular human-impact index: tambon-year

This should be a separate product, not labeled as the full CRI impact index.

Use:
- tambon DDPM impact facts
- subprovince-capable population denominators
- geography joins from [`dim_location_master.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/dopa/dim_location_master.csv:1)

Output table recommendation:
- [`tambon_year_human_impact_index`](plans/2026-06-14_granular-impact-index-plan.md)

### 2.3 Hybrid granular impact-intensity profile

This is the best possible “below province” product if economic context must be shown.

Use:
- tambon human-impact score
- province economic-loss context
- province GPP context
- province Heatwave context where relevant

This should be labeled as a **hybrid profile** or **impact-intensity index**, not as a fully methodology-equivalent CRI.

Output table recommendation:
- [`tambon_year_hybrid_impact_context_profile`](plans/2026-06-14_granular-impact-index-plan.md)

---

## 3. Processing pipelines by pillar

### 3.1 Human-impact pipeline

1. Start from tambon Gold DDPM facts such as [`fact_ddpm_tambon_impact_climate_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv:1)
2. Derive province aggregates where needed for direct comparability with economic data
3. Join population denominators from [`silver_population_annual.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/population/silver_population_annual.csv:1)
4. Compute:
   - deaths
   - deaths per 100k
   - affected people
   - affected people per 100k
5. Optionally integrate Heatwave province metrics from [`silver_heatwave_impact_long.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/heatwave/silver_heatwave_impact_long.csv:1) into province-level human scoring only
6. Normalize using min-max by the chosen comparison scope

### 3.2 Economic-impact pipeline

1. Start from [`silver_eco_loss_annual_long.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/eco_loss/silver_eco_loss_annual_long.csv:1)
2. Aggregate hazards where the final score needs all-hazard economic loss
3. Join GPP from [`silver_gpp_annual_long.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/gpp/silver_gpp_annual_long.csv:1)
4. Compute:
   - total loss
   - loss/GPP
5. Normalize using min-max at province-year scope

### 3.3 Denominator and exposure pipeline

1. Filter [`silver_population_annual.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/population/silver_population_annual.csv:1) to province-safe rows for official index denominators
2. Build a separate subprovince denominator layer from join-ready subdistrict/registration-office classes only
3. Keep [`silver_population_period_total.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/population/silver_population_period_total.csv:1) for cumulative denominator use only if explicitly required
4. Keep [`silver_population_monthly.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/population/silver_population_monthly.csv:1) for seasonal or monthly extensions, not the base annual CRI score

---

## 4. Metric-to-index role assignment

### 4.1 Human impact metrics

Use directly in scoring:
- deaths
- deaths per 100k
- affected people
- affected people per 100k

Optional Thailand-specific extension:
- affected households

### 4.2 Economic impact metrics

Use directly in scoring:
- total economic loss
- loss/GPP

Optional contextual metrics:
- GPP per capita

### 4.3 Metrics not to use directly in the core full CRI score

Do not use directly as core score components:
- population monthly counts
- GPP “population (1,000 persons)” from [`silver_gpp_annual_long.csv`](ψ/incubate/DCCE/CRI/data_system/data/1_silver/gpp/silver_gpp_annual_long.csv:1) because Population Silver is richer and more controlled
- Eco loss period totals when annual facts exist

---

## 5. Validation and governance rules

### 5.1 Missing vs zero

Follow the warning in [`Climate Risk Index (CRI) Pilot Methodology.md`](ψ/incubate/DCCE/CRI/inbox_source/Climate%5C%20Risk%5C%20Index%20%28CRI%29%5C%20Pilot%5C%20Methodology.md:150) and the project caution in [`Data-dictionary-for-CRI-impact-indicator.md`](ψ/incubate/DCCE/CRI/inbox_note/Data-dictionary-for-CRI-impact-indicator.md:53).

Rules:
- explicit numeric `0` may be treated as zero
- missing row or failed geography join must not be converted to zero
- every index-ready mart should carry:
  - `data_completeness_flag`
  - `join_readiness_flag`
  - `zero_vs_missing_note`

### 5.2 Geography consistency

- province-level full index may combine all four Silver families
- subprovince index products may only use metrics truly available below province
- province-only metrics must not be downscaled and presented as if they were observed subprovince facts

### 5.3 Time consistency

- official comparable scoring should use annual facts where available
- period totals should be used for cumulative reporting, not mixed into annual normalized score spaces
- Heatwave should be handled as either:
  - a `2567` snapshot extension, or
  - a `2561–2567` cumulative extension
  but not falsely treated as a full `2560–2567` annual panel

### 5.4 Numeric governance

Apply the approved GPP tolerance policy:
- `abs difference <= 0.000001` = informational only
- `> 0.000001 and <= 0.001` = warning
- `> 0.001` = failure or material inconsistency

---

## 6. Output marts to build

### 6.1 Official province-year marts
- `province_year_human_impact_metrics`
- `province_year_economic_impact_metrics`
- `province_year_cri_pilot_compatible_index`
- `province_year_extended_climate_impact_index`

### 6.2 Granular marts
- `tambon_year_human_impact_metrics`
- `tambon_year_human_impact_index`
- `tambon_year_hybrid_impact_context_profile`

### 6.3 QA and governance marts
- `index_input_completeness_audit`
- `zero_vs_missing_review_table`
- `province_vs_tambon_consistency_check`

---

## 7. Execution order

1. Build province denominator and province economic marts
2. Build province human-impact mart
3. Compute province-year full CRI-style impact index
4. Build tambon human-impact mart
5. Compute tambon human-impact index
6. Add province economic context downward to create hybrid granular profile
7. Compare rank behavior across province and tambon products
8. Publish governance notes clearly distinguishing:
   - full CRI-compatible index
   - granular human-only index
   - hybrid granular context profile

---

## 8. Final recommendation

The best path is not to force one single “granular CRI” product.

Instead, produce:

1. **Official province-level full impact index** using human + economic pillars
2. **Tambon-level human-impact index** using real granular human and population data
3. **Hybrid granular impact-context profile** for local planning support

This preserves methodological honesty while still extracting the maximum value from the current Silver and Gold datasets.

## Decision note

Until subprovince economic-loss and subprovince GPP equivalents exist, any below-province “full CRI impact index” would be methodologically weaker than the province model and should be explicitly labeled as a proxy or hybrid product rather than a direct continuation of the pilot index.
