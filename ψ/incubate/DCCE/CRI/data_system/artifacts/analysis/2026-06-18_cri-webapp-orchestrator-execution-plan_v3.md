# CRI Web App v3 — Orchestrator Execution Plan

## Purpose

This is the updated build execution plan for **app v3** of the CRI Impact Index web app.

It replaces guesswork with explicit structural rules so Orchestrator cannot repeat the failures documented in [`2026-06-18-fix-cri-impact-index-app.md`](../../../inbox_note/2026-06-18-fix-cri-impact-index-app.md:2) and [`2026-06-18_v2-app-structural-drift-corrective-plan.md`](./2026-06-18_v2-app-structural-drift-corrective-plan.md:1).

This plan is not a minor iteration note. It is a **pitfall-hardened execution contract** for a clean v3 implementation.

## Versioning and preservation rule

- The original plan in [`2026-06-17_cri-webapp-orchestrator-execution-plan.md`](./2026-06-17_cri-webapp-orchestrator-execution-plan.md:1) remains preserved as the earlier baseline.
- This file is the explicit **v3 successor plan**.
- Orchestrator must treat this file as the primary implementation plan for the next build attempt.

## Authoritative source hierarchy

Orchestrator must resolve implementation details in this order:

1. **This v3 execution plan**: [`2026-06-18_cri-webapp-orchestrator-execution-plan_v3.md`](./2026-06-18_cri-webapp-orchestrator-execution-plan_v3.md:1)
2. **Working notebook example**: [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb)
3. **Analytical freeze**: [`2026-06-17_phase0-workstream1-metric-freeze.md`](./2026-06-17_phase0-workstream1-metric-freeze.md:1)
4. **Methodology freeze**: [`2026-06-17_phase0-workstream2-methodology-freeze.md`](./2026-06-17_phase0-workstream2-methodology-freeze.md:1)
5. **Data contract outline**: [`2026-06-17_phase0-data-contract-outline.md`](./2026-06-17_phase0-data-contract-outline.md:1)
6. **Client request note**: [`2026-06-17-CRI-Impact-Index-dashboard.md`](../../../inbox_note/2026-06-17-CRI-Impact-Index-dashboard.md:1)
7. **Observed failure note**: [`2026-06-18-fix-cri-impact-index-app.md`](../../../inbox_note/2026-06-18-fix-cri-impact-index-app.md:2)
8. **Structural drift diagnosis**: [`2026-06-18_v2-app-structural-drift-corrective-plan.md`](./2026-06-18_v2-app-structural-drift-corrective-plan.md:1)

If a later implementation choice conflicts with this v3 plan, the implementation choice is wrong.

## Design source hierarchy

UI work must follow:

1. [`coral-stay-DESIGN.md`](../../../../../../memory/design/coral-stay-DESIGN.md)
2. [`DESIGN.md`](./DESIGN.md:1)
3. the user’s app requirements in [`2026-06-17-CRI-Impact-Index-dashboard.md`](../../../inbox_note/2026-06-17-CRI-Impact-Index-dashboard.md:1)
4. the pitfall corrections in [`2026-06-18-fix-cri-impact-index-app.md`](../../../inbox_note/2026-06-18-fix-cri-impact-index-app.md:2)

The design template is not optional. [`DESIGN.md`](./DESIGN.md:1) is the canonical app-specific starter design for this project, and [`coral-stay-DESIGN.md`](../../../../../../memory/design/coral-stay-DESIGN.md) is the upstream reference. Together they govern color, typography, spacing, card style, buttons, chips, navigation, and overall feel.

## Non-negotiable build rules

- Do not invent new metric definitions.
- Do not mix `2560–2567 average` with `2567 only` in the same calculation.
- Do not expose internal filenames, pipeline paths, stage labels, or self-referential implementation talk in the public UI.
- Do not change the frozen household denominator policy.
- Do not merge heat deaths and heat injured into a combined heat metric.
- Do not start with UI polish before the data contract is frozen.
- Do not build in the legacy app folder [`output/cri_impact_app`](../../output/cri_impact_app/).
- Do not patch legacy files unless the task is explicitly a revert or rollback.
- Do not create standalone pages or tabs for layout concepts such as “paired maps”, “rankings”, or “period controls”.
- Do not invent new period keys such as `cumulative` or `specific_year` when the Stage 1 export contract already defines canonical keys.
- Do not separate ranking tables from the maps they describe.
- Do not add non-working or decorative controls.

---

## 1. Orchestrator operating principle

Orchestrator must assign subtasks in dependency order.

Do **not** start UI shell work, deployment hardening, or styling polish before the following are complete:

1. metric definitions are frozen
2. methodology wording is frozen
3. data contract is frozen
4. build-time export shape is defined
5. v3 folder structure is defined
6. navigation contract is frozen

Orchestrator should keep subtasks narrowly scoped and merge only after each dependency gate passes.

Orchestrator must reject any subtask proposal that introduces:

- detached ranking screens
- detached period-control screens
- internal engineering language in public text
- layout abstractions masquerading as product sections

---

## 2. v3 isolation and preservation rules

### 2.1 Folder rule

The new implementation must live in a **new app v3 directory** under [`output/`](../../output/).

Accepted pattern:

- [`output/cri_impact_app_v3/`](../../output/cri_impact_app_v3/)

Forbidden targets:

- [`output/cri_impact_app/`](../../output/cri_impact_app/)
- ad hoc reuse of the v2 folder without an explicit migration decision

### 2.2 Legacy preservation rule

The legacy implementation in [`output/cri_impact_app/`](../../output/cri_impact_app/) is preserved history.

- It is not the workspace for v3.
- If accidental edits are made, rollback must follow the pre-agreed revert path.
- New work must not be mixed into legacy files.

### 2.3 App version labeling rule

All planning, build notes, and artifact paths must explicitly label the new implementation as **v3** so it is impossible to confuse with the legacy app or the structurally broken v2 attempt.

---

## 3. Visible product contract for v3

The visible product contract is frozen to exactly **four top-level tabs**:

1. **Methodology**
2. **CRI**
3. **Tambon-Level Human Impact**
4. **Heat Mortality**

This four-tab contract is mandatory.

### 3.1 Forbidden top-level sections

The following must **not** exist as standalone tabs, pages, or sibling routes:

- Overview
- Paired Maps
- Rankings
- Period Controls
- Province CRI & Heat
- any generic “maps” page that merges CRI and heat into one section

### 3.2 Meaning of “paired maps”

For v3, “paired maps” means a **visual arrangement**, not a page type:

- one row with 2 map panels
- each map panel taking roughly half of the content width
- one ranking-table row directly below that map row
- each table visually associated with its map

This means paired maps are a reusable **layout primitive inside a tab**, not a route.

### 3.3 Table placement rule

Ranking tables must sit directly below the map or map pair they describe.

Detached table-only screens are forbidden.

### 3.4 Table schema rule

The public tables should show only three columns:

1. rank
2. Thai name
3. value

Implementation-specific columns such as codes, duplicate labels, or internal fields must not leak into the visible table.

---

## 4. Period-control contract for v3

### 4.1 Canonical time modes

The app supports exactly two public time modes:

- `2560–2567 average`
- `2567 only`

### 4.2 Canonical export keys

All frontend data loading must resolve to the Stage 1 export folders:

- [`period_2560_2567`](../../build_exports/stage1/period_2560_2567/)
- [`period_2567`](../../build_exports/stage1/period_2567/)

The frontend may display friendly labels, but loader-facing values must remain the exact Stage 1 keys.

### 4.3 Forbidden invented keys

The frontend must never invent alternative runtime period keys such as:

- `cumulative`
- `specific_year`
- `average_mode`
- `single_year`

unless those keys are explicitly mapped back to the exact Stage 1 folder keys **before** any file resolution happens.

### 4.4 Placement rule for period controls

Preferred behavior:

- each plot or plot pair has its own local time-period selector

Fallback behavior if necessary:

- each tab has its own local time-period selector positioned below the tab chips and above the tab content

Forbidden behavior:

- a confusing “Global time period” control with unclear scope
- a separate period-controls page
- non-working or duplicate period widgets

---

## 5. Public wording and UI safety rules

### 5.1 Public text must be client-safe

The UI must not contain:

- self-talk
- stage references such as “Stage 3 landing page”
- internal engineering explanations
- filenames
- folder paths
- temporary logic notes

### 5.2 Header and chrome rules

The v3 app must not include:

- a banner that wastes vertical space
- non-clickable chips pretending to be navigation
- non-functional dropdown cards
- explanatory callout blocks that repeat the obvious and crowd the screen

### 5.3 Tab descriptions

Each tab may contain a short, richer client-facing description, but it must be:

- concise
- useful
- content-oriented
- free of internal implementation language

---

## 6. Build sequence

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

**Additional pitfall-hardened Stage 1 rules**
- The Stage 1 owner must explicitly validate that `period_2560_2567` and `period_2567` tambon outputs are not accidentally identical.
- The Stage 1 owner must verify that the yearly DDPM fact contains all required tambon linkage fields for frontend drilldown.
- The Stage 1 owner must not change export folder names after frontend work starts.

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
- confirm period folder names are exactly `period_2560_2567` and `period_2567`

**Completion condition**
- Data export subtasks must hand off exact file outputs defined by the contract, not just a conceptual bundle.
- Stage 1 is incomplete unless a downstream frontend agent can build Stages 4–6 by reading only the Stage 1 exports plus spatial assets.

### Stage 2 — v3 app shell and navigation contract

**Goal**: create the top-level v3 frame consistent with Coral Stay and the explicit four-tab contract.

**Authoritative source to follow**
- Visual system in [`coral-stay-DESIGN.md`](../../../../../../memory/design/coral-stay-DESIGN.md)
- App-specific design baseline in [`DESIGN.md`](./DESIGN.md:1)
- pitfall note in [`2026-06-18-fix-cri-impact-index-app.md`](../../../inbox_note/2026-06-18-fix-cri-impact-index-app.md:2)

**Logic to preserve**
- coral primary actions
- warm neutral surfaces
- rounded cards and inputs
- readable dense map layout
- no banner-heavy chrome

**Required outputs**
- v3 app scaffold in a new folder such as [`output/cri_impact_app_v3/`](../../output/cri_impact_app_v3/)
- reusable shell primitives
- exactly four top-level tabs
- local tab or plot-level period selector pattern

**Explicit anti-pitfall rules**
- Do not create radio-navigation plus tabs at the same time.
- Do not create unclickable chips that imitate tabs.
- Do not create a separate rankings tab.
- Do not create a separate period-controls tab.
- Do not create a generic “overview” section if Methodology is the intended tab.

**Completion condition**
- the shell renders only the approved navigation contract and no speculative sections.

### Stage 3 — Methodology tab

**Goal**: deliver the landing tab first.

**Authoritative source to follow**
- client requirements in [`2026-06-17-CRI-Impact-Index-dashboard.md`](../../../inbox_note/2026-06-17-CRI-Impact-Index-dashboard.md:1)
- methodology freeze in [`2026-06-17_phase0-workstream2-methodology-freeze.md`](./2026-06-17_phase0-workstream2-methodology-freeze.md:1)

**Logic to preserve**
- no internal filenames or pipeline paths in the public tab
- explain source ownership, temporal coverage, limitations, and app scope in plain language
- explain that affected rate uses household denominator
- explain both time modes
- explain that heat is shown as two separate maps

**Required outputs**
- Methodology as the default landing tab
- sections for score logic, data sources, limitations, and scope
- client-safe dataset cards or callouts only if they are concise and useful

**Forbidden content**
- “Methodology landing page” as self-referential copy
- stage references
- engineering diary text
- file-path leakage

**Completion condition**
- Methodology can be reviewed by a client without engineering context or internal language bleed.

### Stage 4 — CRI tab

**Goal**: implement the primary province-level dashboard.

**Execution boundary**
- Stage 4 is a **read-only frontend stage**.
- The Stage 4 owner must not recompute CRI metrics, recompute rankings, or derive alternative analytics from raw CSV sources.
- Stage 4 may only consume the exported Stage 1 JSON files and province geometry assets.
- If a Stage 4 result suggests analytical drift, the issue must be sent back to Stage 1 rather than patched in frontend code.

**Authoritative source to follow**
- province scoring block in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb)
- metric freeze in [`2026-06-17_phase0-workstream1-metric-freeze.md`](./2026-06-17_phase0-workstream1-metric-freeze.md:1)

**Logic to preserve**
- six metric maps plus one CRI map
- top 10 highest and lowest province tables below each map or map pair
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

**Layout contract**
- use 1x2 map rows wherever metrics are presented in pairs
- each row is followed immediately by the corresponding 1x2 table row
- “paired maps” is a layout pattern, not a sibling page

**Frontend inputs to read**
- `manifest.json`
- the selected-period CRI metric JSON files from Stage 1
- `spatial/province_boundaries.geojson` or optimized equivalent

**Completion condition**
- the CRI tab is interactive and fully backed by the exported metric assets without detached screens.

### Stage 5 — Tambon-Level Human Impact tab

**Goal**: implement the zoomable human-impact views.

**Execution boundary**
- Stage 5 is a **read-only frontend stage**.
- The Stage 5 owner must not recalculate tambon metrics from source CSVs.
- Stage 5 may only consume the exported Stage 1 tambon metric JSON files plus province/tambon spatial assets.
- If province-filtered or zoom-filtered results appear incorrect, the defect must be treated as either a Stage 1 export issue or a frontend filtering/rendering issue.

**Authoritative source to follow**
- tambon map block in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb)
- DDPM yearly fact source family validated in earlier lineage checks

**Logic to preserve**
- country view defaults to province overlays
- province dropdown zooms into tambon detail
- ranking tables change grain with zoom state
- tambon deaths and tambon affected-households are the two core views

**Required outputs**
- tambon deaths map
- tambon affected-households map
- province overlay layer
- province dropdown control
- grain-aware ranking tables

**Layout contract**
- the two tambon metrics should be displayed as a paired 1x2 visual pattern where technically feasible
- ranking tables must stay directly below the associated visuals

**Frontend inputs to read**
- `manifest.json`
- `period_<mode>/tambon_deaths.json`
- `period_<mode>/tambon_affected_households.json`
- `spatial/province_boundaries.geojson` or optimized equivalent
- `spatial/tambon/<province_code>.geojson` or optimized equivalent

**Explicit validation checks**
- selected province mode must still show tambon boundaries of that province
- the table output must be reduced to public-safe columns only
- duplicate-code columns must not reach the rendered table

**Completion condition**
- Tambon-Level Human Impact behaves as a zoomable province-to-tambon drilldown with attached tables.

### Stage 6 — Heat Mortality tab

**Goal**: implement the two-map heat view.

**Execution boundary**
- Stage 6 is a **read-only frontend stage**.
- The Stage 6 owner must not merge, reshape, or analytically recompute heat metrics beyond selecting the exported period payload.
- Stage 6 may only consume the exported Stage 1 heat JSON files and province geometry assets.
- If heat values or rankings appear inconsistent, the correction must happen in Stage 1 exports, not in the frontend layer.

**Authoritative source to follow**
- heat block in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb)
- heat terminology in [`2026-06-17_phase0-workstream1-metric-freeze.md`](./2026-06-17_phase0-workstream1-metric-freeze.md:1)

**Logic to preserve**
- heat is two province maps
- one map is heat deaths
- one map is heat injured
- each map has its own ranking table

**Required outputs**
- heat deaths map
- heat injured map
- top/bottom province table for each map

**Layout contract**
- the default heat presentation should be one 1x2 row: left `heat_deaths`, right `heat_injured`
- tables sit directly below
- do not create a merged “Province CRI & Heat” page

**Completion condition**
- Heat Mortality is shown as a dedicated tab with two separate maps, not a combined chart and not a mixed CRI/heat page.

### Stage 7 — Local hardening and testing

**Goal**: finish a locally testable v3 build before any deployment decision.

**Required outputs**
- local production-like build
- smoke-test evidence
- responsive behavior validation
- local run instructions

**Mandatory v3 regression checklist**
- verify there are exactly four tabs
- verify no detached rankings page exists
- verify no detached period-controls page exists
- verify no runtime path references `cumulative`
- verify no runtime path references `specific_year`
- verify all tables show only rank, Thai name, and value
- verify tambon province drilldown still renders province-specific tambon boundaries
- verify Methodology contains no internal engineering text

**Completion condition**
- v3 is locally testable and stable enough for a human review session.

### Stage 8 — Deployment

**Goal**: deploy only when the human explicitly requests release.

**Completion condition**
- the app is publicly accessible and accepted for client-facing use.

---

## 7. Recommended orchestrator task map for v3

### Subtask A — Data / export engineer

Owns:

- metric export bundles
- manifest generation
- spatial asset packaging
- period-mode validation

Must validate concrete period-key integrity against [`2026-06-17_phase0-data-contract-schema-freeze.md`](./2026-06-17_phase0-data-contract-schema-freeze.md:1).

### Subtask B — v3 scaffold engineer

Owns:

- v3 folder creation
- shell setup
- navigation contract implementation
- local period-control primitives

Must enforce the four-tab contract and forbid page drift.

### Subtask C — Methodology content writer

Owns:

- landing tab text
- dataset descriptions
- limitations wording
- client-safe source narrative

Must explicitly remove internal implementation talk.

### Subtask D — CRI tab engineer

Owns:

- CRI tab implementation
- paired 1x2 map rows
- attached ranking tables

Must treat paired maps as layout only.

### Subtask E — Tambon interaction engineer

Owns:

- tambon zoom behavior
- province dropdown
- tambon boundary rendering
- tambon ranking tables

Must preserve province-to-tambon drilldown semantics.

### Subtask F — Heat tab engineer

Owns:

- heat deaths map
- heat injured map
- heat-specific tables

Must keep Heat Mortality as its own dedicated tab.

### Subtask G — Release / QA engineer

Owns:

- smoke tests
- responsive checks
- local hardening
- regression check against known v2 pitfalls

Must validate against this v3 plan, not only against visual intuition.

---

## 8. Dependency gates

### Gate 1 — Data contract complete

No frontend work starts until metric exports, manifest shape, and canonical period keys are frozen.

### Gate 2 — Navigation contract complete

No deeper UI implementation starts until the four-tab contract is fixed and accepted.

### Gate 3 — Public wording complete

No Methodology copy merges until public wording is checked against the methodology freeze and the pitfall note.

### Gate 4 — Core dashboard complete

No release work starts until CRI, Tambon-Level Human Impact, and Heat Mortality render correctly with attached tables.

### Gate 5 — Regression acceptance

No release is marked complete until known v2 structural failures are explicitly re-tested and absent.

---

## 9. Orchestrator assignment rules

1. **Do not mix concerns** in one subtask.
2. **One dependency, one owner** where possible.
3. **Start from data**, then navigation contract, then narrative, then maps, then release.
4. **Keep heat separate** from CRI and tambon work.
5. **Do not re-open frozen decisions** unless a new explicit decision is requested.
6. **Do not interpret layout vocabulary as product vocabulary**.
7. **Do not let reusable abstractions override the visible client contract**.

---

## 10. Execution checkpoint outputs

At the end of each stage, Orchestrator should capture:

- completed subtasks
- open dependencies
- any newly discovered blockers
- explicit pass/fail against the anti-pitfall rules
- next subtask to assign

These checkpoints should be short and auditable.

---

## 11. Current build-ready baseline for v3

The following are already frozen and should not be re-litigated during build:

- affected rate uses households
- two time modes exist
- heat is two maps: deaths and injured
- methodology must be client-safe
- data is precomputed for the web app
- paired maps are a layout pattern, not a page
- tables belong directly below the plots they describe
- navigation is exactly four top-level tabs

This is the execution plan Orchestrator should follow for the v3 build.
