# CRI Web App — Orchestrator Execution Plan

## Purpose

This is the build execution plan for the CRI Impact Index web app.

It must be specific enough that Orchestrator can assign subtasks without guessing the logic, the outputs, or the source of truth.

## Authoritative source hierarchy

Orchestrator must resolve implementation details in this order:

1. **Working notebook example**: [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb)
2. **Analytical freeze**: [`2026-06-17_phase0-workstream1-metric-freeze.md`](./2026-06-17_phase0-workstream1-metric-freeze.md)
3. **Methodology freeze**: [`2026-06-17_phase0-workstream2-methodology-freeze.md`](./2026-06-17_phase0-workstream2-methodology-freeze.md)
4. **Data contract outline**: [`2026-06-17_phase0-data-contract-outline.md`](./2026-06-17_phase0-data-contract-outline.md)
5. **Client request note**: [`2026-06-17-CRI-Impact-Index-dashboard.md`](../../../inbox_note/2026-06-17-CRI-Impact-Index-dashboard.md)

## Design source hierarchy

UI work must follow:

1. [`coral-stay-DESIGN.md`](../../../../../../memory/design/coral-stay-DESIGN.md)
2. [`DESIGN.md`](./DESIGN.md)
3. the user’s app requirements in [`2026-06-17-CRI-Impact-Index-dashboard.md`](../../../inbox_note/2026-06-17-CRI-Impact-Index-dashboard.md)

The design template is not optional. [`DESIGN.md`](./DESIGN.md) is the canonical app-specific starter design for this project, and [`coral-stay-DESIGN.md`](../../../../../../memory/design/coral-stay-DESIGN.md) is the upstream reference. Together they govern color, typography, spacing, card style, buttons, chips, navigation, and overall feel.

## Non-negotiable build rules

- Do not invent new metric definitions.
- Do not mix `2560–2567 average` with `2567 only` in the same calculation.
- Do not expose internal filenames in the public methodology page.
- Do not change the frozen household denominator policy.
- Do not merge heat deaths into a single combined heat metric; heat is two maps: deaths and injured.
- Do not start with UI polish before the data contract is frozen.

---

## 1. Orchestrator operating principle

Orchestrator must assign subtasks in dependency order.

Do **not** start UI polishing or deployment hardening before the following are complete:

1. metric definitions are frozen
2. methodology wording is frozen
3. data contract is frozen
4. build-time export shape is defined

Orchestrator should keep subtasks narrowly scoped and merge only after each dependency gate passes.

---

## 2. Build sequence

### Stage 1 — Data foundation

**Goal**: produce the app-ready data layer from the working notebook logic.

**Authoritative source to follow**
- Province scoring and denominator logic in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb)
  - loading and normalization setup around lines 108–149
  - province scoring logic around lines 155–283
  - tambon map logic around lines 405–421
  - heat logic around lines 424–440
- Concrete upstream source assets listed in [`2026-06-17_phase0-data-contract-outline.md`](./2026-06-17_phase0-data-contract-outline.md:20)

**Exact source files to use**
- [`fact_ddpm_tambon_impact_climate_2560_2567.csv`](../data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv:1)
- [`fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv`](../data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv:1)
- [`silver_population_annual.csv`](../data/1_silver/population/silver_population_annual.csv:1)
- [`silver_household_annual.csv`](../data/1_silver/population/silver_household_annual.csv:1)
- [`silver_govt_adv_payment_annual_long.csv`](../data/1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv:1)
- [`silver_gpp_annual_long.csv`](../data/1_silver/gpp/silver_gpp_annual_long.csv:1)
- [`silver_heatwave_impact_long.csv`](../data/1_silver/heatwave/silver_heatwave_impact_long.csv:1)
- [`province_boundaries_enriched.shp`](../data/1_silver/dopa/province_boundaries_enriched.shp)
- [`tambon_boundaries_enriched.shp`](../data/1_silver/dopa/tambon_boundaries_enriched.shp)

**Logic to preserve**
- `deaths_abs` and `affected_hh_abs` are derived from DDPM impact sums and averaged over the selected period.
- `deaths_rate` uses `population_total` as denominator.
- `affected_rate` uses `household_total` as denominator.
- `loss_abs` uses govt advance payment values averaged over the selected period.
- `loss_per_gpp` uses GPP as the economic denominator.
- `cri_score` is the weighted min-max composite of the six province metrics.
- tambon human impact uses `subdistrict_code` grouping.
- heat uses two separate province maps: deaths and injured.

**Exact formulas and mode rules to preserve**
- `deaths_abs`
  - `2560–2567 average`: annualized from DDPM period logic
  - `2567 only`: filtered from yearly DDPM fact
- `deaths_rate`
  - `deaths_abs / population_total * 100000`
- `affected_hh_abs`
  - `2560–2567 average`: annualized from DDPM period logic
  - `2567 only`: filtered from yearly DDPM fact
- `affected_rate`
  - `affected_hh_abs / household_total * 100`
- `loss_abs`
  - `2560–2567 average`: annualized from govt advance payment long rows
  - `2567 only`: filtered to `year_be = 2567`
- `loss_per_gpp`
  - `loss_abs / gpp_value`
- `cri_score`
  - weighted sum of min-max normalized component metrics using the frozen weights
- `heat_deaths`
  - must read the deaths metric from heatwave source
- `heat_injured`
  - must read the injured metric from heatwave source

**Stage 1 task contract**

The Stage 1 owner must complete these internal steps in order:

1. Read the source files listed below and confirm mode-specific eligibility.
2. Reconstruct province-level metrics from the notebook logic without changing formulas.
3. Reconstruct tambon-level metrics for deaths and affected households.
4. Reconstruct heat metrics as separate deaths and injured exports.
5. Generate embedded top/bottom ranking payloads for each required metric file.
6. Generate `manifest.json` and `spatial/manifest.json`.
7. Validate every output against [`2026-06-17_phase0-data-contract-schema-freeze.md`](./2026-06-17_phase0-data-contract-schema-freeze.md:1).

**Source-to-output mapping**

- [`fact_ddpm_tambon_impact_climate_2560_2567.csv`](../data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv:1)
  - supports period-average human metrics
- [`fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv`](../data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv:1)
  - supports `2567 only` human metrics and tambon metrics
- [`silver_population_annual.csv`](../data/1_silver/population/silver_population_annual.csv:1)
  - supports `deaths_rate`
- [`silver_household_annual.csv`](../data/1_silver/population/silver_household_annual.csv:1)
  - supports `affected_rate`
- [`silver_govt_adv_payment_annual_long.csv`](../data/1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv:1)
  - supports `loss_abs`
- [`silver_gpp_annual_long.csv`](../data/1_silver/gpp/silver_gpp_annual_long.csv:1)
  - supports `loss_per_gpp`
- [`silver_heatwave_impact_long.csv`](../data/1_silver/heatwave/silver_heatwave_impact_long.csv:1)
  - supports `heat_deaths` and `heat_injured`
- [`province_boundaries_enriched.shp`](../data/1_silver/dopa/province_boundaries_enriched.shp)
  - supports province geometry export
- [`tambon_boundaries_enriched.shp`](../data/1_silver/dopa/tambon_boundaries_enriched.shp)
  - supports tambon geometry export

**Required outputs**
- `manifest.json`
- one metric JSON file per metric per period mode
- one province geometry file
- one tambon geometry strategy file or manifest
- ranking payloads for each metric file

**Minimum exported files**
- `period_2560_2567/deaths_abs.json`
- `period_2560_2567/deaths_rate.json`
- `period_2560_2567/affected_hh_abs.json`
- `period_2560_2567/affected_rate.json`
- `period_2560_2567/loss_abs.json`
- `period_2560_2567/loss_per_gpp.json`
- `period_2560_2567/cri_score.json`
- `period_2560_2567/tambon_deaths.json`
- `period_2560_2567/tambon_affected_households.json`
- `period_2560_2567/heat_deaths.json`
- `period_2560_2567/heat_injured.json`
- `period_2567/deaths_abs.json`
- `period_2567/deaths_rate.json`
- `period_2567/affected_hh_abs.json`
- `period_2567/affected_rate.json`
- `period_2567/loss_abs.json`
- `period_2567/loss_per_gpp.json`
- `period_2567/cri_score.json`
- `period_2567/tambon_deaths.json`
- `period_2567/tambon_affected_households.json`
- `period_2567/heat_deaths.json`
- `period_2567/heat_injured.json`
- `spatial/province_boundaries.geojson` or optimized equivalent
- `spatial/tambon/<province_code>.geojson` or optimized equivalent

**Mandatory export location rule**
- All Stage 1 deliverables must be written into one build-export directory with the structure defined in [`2026-06-17_phase0-data-contract-schema-freeze.md`](./2026-06-17_phase0-data-contract-schema-freeze.md:20).
- The Stage 1 owner must not invent alternative filenames or period keys.

**Mandatory ranking rule**
- Rankings must be embedded in every metric file.
- `top_10` sorted descending by metric value.
- `bottom_10` sorted ascending by metric value.
- tie handling must follow the frozen descending-rank rule in [`2026-06-17_phase0-data-contract-schema-freeze.md`](./2026-06-17_phase0-data-contract-schema-freeze.md:214).

**Validation checks**
- confirm `2567 only` can be derived from the yearly sources
- confirm `2560–2567 average` reproduces the notebook’s average-mode logic
- confirm `affected_rate` denominator remains household-based
- confirm heat exports include both deaths and injured

**Schema checks**
- every output file must conform to the exact shapes frozen in [`2026-06-17_phase0-data-contract-schema-freeze.md`](./2026-06-17_phase0-data-contract-schema-freeze.md:1)
- `manifest.json` must enumerate periods, metric groups, and spatial references
- province metric files must contain `records[]`, `legend`, and embedded `rankings`
- tambon metric files must contain province linkage fields for filtering
- heat files must remain separate and must not be merged

**Completion condition**
- Data export subtasks must hand off exact file outputs defined by the contract, not just a conceptual bundle.
- Stage 1 is incomplete unless a downstream frontend agent can build Stages 4–6 by reading only the Stage 1 exports plus spatial assets.

### Stage 2 — App shell

**Goal**: create the top-level web app frame consistent with Coral Stay.

**Authoritative source to follow**
- Visual system in [`coral-stay-DESIGN.md`](../../../../../../memory/design/coral-stay-DESIGN.md)

**Logic to preserve**
- coral primary actions
- warm neutral surfaces
- rounded cards and inputs
- sticky header behavior
- DM Sans / Nunito Sans typography pairing

**Required outputs**
- Next.js app scaffold
- Tailwind theme tokens based on Coral Stay colors and typography
- sticky header
- shared global time-period selector
- reusable page shell

**Validation checks**
- buttons, cards, chips, inputs, and nav visually map to Coral Stay specs
- layout remains readable at the map-card density required by the CRI tab

**Completion condition**
- app shell renders the layout, navigation, and period selector without any metric logic yet.

### Stage 3 — Methodology page

**Goal**: deliver the landing page first.

**Authoritative source to follow**
- client requirements in [`2026-06-17-CRI-Impact-Index-dashboard.md`](../../../inbox_note/2026-06-17-CRI-Impact-Index-dashboard.md)
- methodology freeze in [`2026-06-17_phase0-workstream2-methodology-freeze.md`](./2026-06-17_phase0-workstream2-methodology-freeze.md)

**Logic to preserve**
- no internal filenames or pipeline paths in the public page
- explain source ownership, temporal coverage, limitations, and app scope in plain language
- explain that affected rate uses household denominator
- explain both time modes

**Required outputs**
- landing page as default route
- methodology sections for score logic, data sources, limitations, and scope
- client-safe dataset cards or callouts

**Validation checks**
- public text contains no internal file names
- public text states the two time modes and the household denominator choice

**Completion condition**
- methodology page is ready as the app landing page and can be reviewed without engineering context.

### Stage 4 — CRI tab

**Goal**: implement the primary province-level dashboard.

**Execution boundary**
- Stage 4 is a **read-only frontend stage**.
- The Stage 4 owner must not recompute CRI metrics, recompute rankings, or derive alternative analytics from raw CSV sources.
- Stage 4 may only consume the exported Stage 1 JSON files and province geometry assets.
- If a Stage 4 result suggests analytical drift, the issue must be sent back to Stage 1 rather than patched in frontend code.

**Authoritative source to follow**
- province scoring block in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb) around lines 155–283
- metric freeze in [`2026-06-17_phase0-workstream1-metric-freeze.md`](./2026-06-17_phase0-workstream1-metric-freeze.md)

**Logic to preserve**
- six metric maps plus one CRI map
- top 10 highest and lowest province tables below each map
- selected period mode must drive every metric consistently

**Required outputs**
- `deaths_abs` map
- `deaths_rate` map
- `affected_hh_abs` map
- `affected_rate` map
- `loss_abs` map
- `loss_per_gpp` map
- `cri_score` map
- ranking tables for each map

**Frontend inputs to read**
- `manifest.json`
- the selected-period CRI metric JSON files from Stage 1
- `spatial/province_boundaries.geojson` or optimized equivalent

**Validation checks**
- the CRI score reproduces the notebook’s weighted sum logic for the selected period mode
- the tables match the same province grain as the maps
- the frontend does not contain substitute analytical calculations for province metrics

**Completion condition**
- the province dashboard is interactive and fully backed by the exported metric assets.

### Stage 5 — Tambon human-impact tab

**Goal**: implement the zoomable human-impact views.

**Execution boundary**
- Stage 5 is a **read-only frontend stage**.
- The Stage 5 owner must not recalculate tambon metrics from source CSVs.
- Stage 5 may only consume the exported Stage 1 tambon metric JSON files plus province/tambon spatial assets.
- If province-filtered or zoom-filtered results appear incorrect, the defect must be treated as either a Stage 1 export issue or a frontend filtering/rendering issue, not an excuse to introduce new analytical logic.

**Authoritative source to follow**
- tambon map block in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb) around lines 405–421
- DDPM yearly fact source family validated in the earlier dataset lineage checks

**Logic to preserve**
- country view defaults to province overlays
- province dropdown zooms into tambon detail
- ranking tables change grain with zoom state

**Required outputs**
- tambon deaths map
- tambon affected-households map
- province overlay layer
- province dropdown control
- grain-aware ranking tables

**Frontend inputs to read**
- `manifest.json`
- `period_<mode>/tambon_deaths.json`
- `period_<mode>/tambon_affected_households.json`
- `spatial/province_boundaries.geojson` or optimized equivalent
- `spatial/tambon/<province_code>.geojson` or optimized equivalent

**Validation checks**
- tambon data loads only when needed or by province partition
- overlay boundaries remain legible at both country and province zoom states
- the frontend does not recompute tambon metrics from raw analytical inputs

**Completion condition**
- tambon human-impact tab behaves as a zoomable province-to-tambon drilldown.

### Stage 6 — Heat tab

**Goal**: implement the two-map heat view.

**Execution boundary**
- Stage 6 is a **read-only frontend stage**.
- The Stage 6 owner must not merge, reshape, or analytically recompute heat metrics beyond selecting the exported period/mode payload.
- Stage 6 may only consume the exported Stage 1 heat JSON files and province geometry assets.
- If heat values or rankings appear inconsistent, the correction must happen in Stage 1 exports, not in the frontend layer.

**Authoritative source to follow**
- heat block in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb) around lines 424–440
- heat terminology in [`2026-06-17_phase0-workstream1-metric-freeze.md`](./2026-06-17_phase0-workstream1-metric-freeze.md)

**Logic to preserve**
- heat is two province maps
- one map is heat deaths
- one map is heat injured
- each map has its own ranking table

**Required outputs**
- heat deaths map
- heat injured map
- top/bottom province table for each map

**Frontend inputs to read**
- `manifest.json`
- `period_<mode>/heat_deaths.json`
- `period_<mode>/heat_injured.json`
- `spatial/province_boundaries.geojson` or optimized equivalent

**Validation checks**
- `year_2567` or the selected period mode is used consistently for heat
- the labels match the frozen metric names
- the frontend does not create a combined heat metric or substitute new calculations

**Completion condition**
- heat is shown as two distinct tabs or stacked panels, not a combined chart.

### Stage 7 — Local hardening and testing

**Goal**: finish a locally testable build before any deployment decision.

**Authoritative source to follow**
- the app shell and export outputs created in earlier stages

**Logic to preserve**
- free-tier hosting assumptions
- small-traffic responsiveness
- client-safe copy

**Required outputs**
- local production-like build
- smoke-test evidence
- responsive behavior validation
- local run instructions

**Validation checks**
- load states are visible
- empty states do not break layout
- geometry performance is acceptable for small concurrent usage

**Completion condition**
- the app is locally testable and stable enough for a human review session.

### Stage 8 — Deployment

**Goal**: deploy only when the human explicitly requests release.

**Authoritative source to follow**
- the locally validated build from Stage 7

**Required outputs**
- public URL
- deployment notes

**Validation checks**
- deployed build matches the locally approved behavior

**Completion condition**
- the app is publicly accessible and accepted for client-facing use.

---

## 3. Recommended orchestrator task map

### Subtask A — Data / export engineer

Owns:

- metric export bundles
- manifest generation
- spatial asset packaging
- period-mode validation

Must follow the notebook logic in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb) and the exact output contract in [`2026-06-17_phase0-data-contract-outline.md`](./2026-06-17_phase0-data-contract-outline.md).

### Subtask B — App scaffold engineer

Owns:

- Next.js setup
- design system setup
- shared app shell
- period selector state

Must follow [`coral-stay-DESIGN.md`](../../../../../../memory/design/coral-stay-DESIGN.md) for tokens and layout.

### Subtask C — Methodology content writer

Owns:

- landing page text
- dataset descriptions
- limitations wording
- client-safe source narrative

Must follow the public wording constraints in [`2026-06-17_phase0-workstream2-methodology-freeze.md`](./2026-06-17_phase0-workstream2-methodology-freeze.md).

### Subtask D — Province dashboard engineer

Owns:

- CRI tab implementation
- ranking tables
- province map rendering

Must follow the province scoring logic in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb) and the metric freeze in [`2026-06-17_phase0-workstream1-metric-freeze.md`](./2026-06-17_phase0-workstream1-metric-freeze.md).

### Subtask E — Tambon interaction engineer

Owns:

- tambon zoom behavior
- province dropdown
- tambon ranking tables

Must follow the tambon section in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb).

### Subtask F — Heat-tab engineer

Owns:

- heat deaths map
- heat injured map
- heat-specific tables

Must follow the heat section in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb) and the two-map heat freeze in [`2026-06-17_phase0-workstream1-metric-freeze.md`](./2026-06-17_phase0-workstream1-metric-freeze.md).

### Subtask G — Release / QA engineer

Owns:

- smoke tests
- responsive checks
- local hardening
- deployment hardening only after explicit human request

Must validate the delivered build against the design template [`coral-stay-DESIGN.md`](../../../../../../memory/design/coral-stay-DESIGN.md) and the client request note [`2026-06-17-CRI-Impact-Index-dashboard.md`](../../../inbox_note/2026-06-17-CRI-Impact-Index-dashboard.md).

---

## 4. Dependency gates

### Gate 1 — Data contract complete

No frontend work starts until metric exports and manifest shape are frozen.

### Gate 2 — Public wording complete

No methodology page work starts until public wording is approved.

### Gate 3 — Core dashboard complete

No heat-tab polish or release work starts until CRI and tambon tabs render correctly.

### Gate 4 — Performance acceptance

No release is marked complete until province-level rendering is stable and tambon loading is acceptable.

---

## 5. Orchestrator assignment rules

1. **Do not mix concerns** in one subtask.
2. **One dependency, one owner** where possible.
3. **Start from data**, then shell, then narrative, then maps, then release.
4. **Keep heat separate** from CRI and tambon work.
5. **Do not re-open frozen decisions** unless a new explicit decision is requested.

---

## 6. Execution checkpoint outputs

At the end of each stage, Orchestrator should capture:

- completed subtasks
- open dependencies
- any newly discovered blockers
- next subtask to assign

These checkpoints should be short and auditable.

---

## 7. Current build-ready baseline

The following are already frozen and should not be re-litigated during build:

- affected rate uses households
- two time modes exist
- heat is two maps: deaths and injured
- methodology must be client-safe
- data is precomputed for the web app

This is the execution plan Orchestrator should follow when assigning build subtasks.
