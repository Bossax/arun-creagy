# Workstream 1 — Analytical Definition Freeze

## Status

Executed against the current CRI Phase 1 notebook baseline in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb:1) and the hardened denominator decision recorded in [`12.05_cri-denominator-hardening.md`](../../../../../../memory/retrospectives/2026-06/17/12.05_cri-denominator-hardening.md:9).

This artifact freezes the metric dictionary, period logic, denominator policy, and geography/grain assumptions that must be treated as ground truth for the web app build.

---

## 1. Frozen operating modes

The app supports exactly two period modes:

1. **2560–2567 average**
2. **2567 only**

No mixed-period joins are allowed in the web app contract.

---

## 2. Metric dictionary

| Metric key | Display label | Geography | Numerator | Denominator | Scaling / Unit | Period logic | Source family | Notes |
|---|---|---|---|---|---|---|---|---|
| `deaths_abs` | Total Deaths (Absolute) | Province | `deaths_sum` | None | Annual deaths | Sum across 2560–2567, then divide by 8.0 for average; or filter `year_be = 2567` | DDPM human impacts | Used in CRI score |
| `deaths_rate` | Death Rate | Province | `deaths_abs` | `population_total` | Per 100,000 population | Average mode uses 8-year averaged deaths and averaged population; 2567 mode uses year-specific values | DDPM + Population | Population-based denominator remains correct |
| `affected_hh_abs` | Total Affected Households (Absolute) | Province | `affected_households_sum` | None | Annual households | Sum across 2560–2567, then divide by 8.0 for average; or filter `year_be = 2567` | DDPM human impacts | Used in CRI score |
| `affected_rate` | Affected Rate | Province | `affected_hh_abs` | `household_total` | Per 100 households | Average mode uses 8-year averaged affected households and averaged household totals; 2567 mode uses year-specific values | DDPM + Household Silver | **Frozen denominator is households, not population** |
| `loss_abs` | Total Economic Loss | Province | `value` from government advance payment | None | Million THB, annual average | Sum across 2560–2567, then divide by 8.0 for average; or filter `year_be = 2567` | Govt advance payment Silver | Used in CRI score |
| `loss_per_gpp` | Loss per Unit GPP | Province | `loss_abs` | `gpp_avg` | Ratio | Average mode uses annual-average loss divided by annual-average GPP; 2567 mode uses year-specific values | Govt advance payment Silver + GPP Silver | Used in CRI score |
| `cri_score` | CRI Phase 1 Score | Province | Weighted normalized component scores | N/A | 0–1 composite | Computed after min-max normalization within the selected period mode | Derived from 6 CRI indicators | Not a direct raw-data metric |
| `tambon_deaths` | Tambon Deaths | Tambon | `deaths_sum` | None | Annual deaths | Average mode uses 8-year average at tambon grain; 2567 mode uses year-specific rows | DDPM yearly fact | For tambon map tab |
| `tambon_affected_households` | Tambon Affected Households | Tambon | `affected_households_sum` | None | Annual households | Average mode uses 8-year average at tambon grain; 2567 mode uses year-specific rows | DDPM yearly fact | For tambon map tab |
| `heat_deaths` | Heat-Related Deaths | Province | `value` where `metric_code = 'DEATHS'` | None | Annual deaths | Average mode uses the available multi-year heat scope; 2567 mode uses `time_scope = year_2567` | Heatwave Silver | Rendered as one of two heat maps |
| `heat_injured` | Heat-Related Injured | Province | `value` where `metric_code = 'INJURED'` | None | Annual injuries | Average mode uses the available multi-year heat scope; 2567 mode uses `time_scope = year_2567` | Heatwave Silver | Rendered as one of two heat maps |

---

## 3. Period matrix

| Metric key | 2560–2567 average | 2567 only | Availability / constraint |
|---|---|---|---|
| `deaths_abs` | Use 8-year average of annual DDPM values | Use `year_be = 2567` from yearly DDPM fact | Cleanly supported by yearly fact for 2567 |
| `deaths_rate` | `deaths_abs / population_total * 100000` using period average inputs | Same formula using 2567-only inputs | Population data supports annual slicing |
| `affected_hh_abs` | Use 8-year average of annual affected household values | Use `year_be = 2567` from yearly DDPM fact | Cleanly supported by yearly fact for 2567 |
| `affected_rate` | `affected_hh_abs / household_total * 100` using period average inputs | Same formula using 2567-only inputs | Household denominator is now frozen |
| `loss_abs` | 8-year average annual loss from govt advance payment | `year_be = 2567` from annual long file | Supported by annual-long source |
| `loss_per_gpp` | `loss_abs / gpp_avg` using period average inputs | Same formula using 2567-only inputs | Supported by annual-long sources |
| `cri_score` | Normalized sum of 6 indicator scores computed inside selected mode | Same normalization within 2567-only mode | Must not mix modes |
| `tambon_deaths` | 8-year average at tambon level | `year_be = 2567` tambon rows only | Supported by yearly DDPM fact |
| `tambon_affected_households` | 8-year average at tambon level | `year_be = 2567` tambon rows only | Supported by yearly DDPM fact |
| `heat_deaths` | Use the available heat multi-year scope for the selected view | `time_scope = year_2567` | Heat source coverage begins at 2561 |
| `heat_injured` | Use the available heat multi-year scope for the selected view | `time_scope = year_2567` | Heat source coverage begins at 2561 |

---

## 4. Geography and grain rules

### Province grain

Use province grain for:

- `deaths_abs`
- `deaths_rate`
- `affected_hh_abs`
- `affected_rate`
- `loss_abs`
- `loss_per_gpp`
- `cri_score`
- `heat_deaths`
- `heat_injured`

### Tambon grain

Use tambon grain for:

- `tambon_deaths`
- `tambon_affected_households`

### Zoom behavior

The tambon tab must support:

1. country view with provincial overlays
2. province zoom view with tambon detail

Ranking-table grain must follow the visible map grain.

---

## 5. Normalization and weighting freeze

The CRI score uses the same 6 weighted indicators already defined in the notebook baseline.

### Human pillar

- `deaths_abs` weight = 7.5%
- `deaths_rate` weight = 22.5%
- `affected_hh_abs` weight = 5.0%
- `affected_rate` weight = 15.0%

### Economic pillar

- `loss_abs` weight = 12.5%
- `loss_per_gpp` weight = 37.5%

### Normalization rule

Min-max scaling is retained for the selected period mode only.

No normalization window may mix 2560–2567 with 2567-only records.

---

## 6. Source-family freeze

### DDPM

- Aggregate file supports 2560–2567 average logic.
- Yearly fact file supports 2567-only extraction.

### Population

- Annual long table supports year-specific denominators.

### Household

- Annual household table supports year-specific denominators.

### GPP

- Annual long table supports year-specific denominators and annual averages.

### Govt advance payment

- Annual long table supports year-specific and average-mode extraction.

### Heatwave

- `time_scope = year_2567` supports 2567-only heat maps.
- `time_scope = range_2561_2567` supports the longer aggregate heat view.

---

## 7. Cross-checks resolved in this workstream

1. **Affected rate denominator** is household-based.
2. **Heat UI** is two maps, not one combined map.
3. **DDPM 2567 slicing** requires the yearly fact source, not the aggregate source.
4. **Heat coverage** is available from 2561 onward, so the average-mode heat scope is coverage-limited.

---

## 8. Implementation implication for the next workstream

The frontend data contract must expose:

- metric key
- human-readable label
- selected period mode
- geography grain
- unit label
- rank payload
- map payload

This artifact is the frozen analytical baseline for the app build.
