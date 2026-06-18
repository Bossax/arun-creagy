# 2026-06-18 — Corrective Plan for v2 App Structural Drift

## Status

Drafted as a corrective implementation plan after the current v2 app drifted away from the freeze documents, the execution plan, and the explicit UI feedback in [`2026-06-18-fix-cri-impact-index-app.md`](../../../inbox_note/2026-06-18-fix-cri-impact-index-app.md:2).

---

## 1. Problem Statement

The current v2 implementation under [`output/cri_impact_app_v2`](../../output/cri_impact_app_v2/) introduced a structural abstraction that does **not** match the frozen product contract.

The main failure is not a minor bug. It is a **UI architecture drift**:

1. the app was broken into internal “pages” such as [`pages/paired_maps.py`](../../output/cri_impact_app_v2/pages/paired_maps.py:1), [`pages/tables.py`](../../output/cri_impact_app_v2/pages/tables.py), and [`pages/periods.py`](../../output/cri_impact_app_v2/pages/periods.py)
2. “paired maps” was implemented as a separate navigation/page concept instead of a **layout pattern**
3. rankings were split away from the maps even though the frozen requirement says tables belong **below each map**
4. period controls were modeled with abstract keys such as `cumulative` and `specific_year` in [`components/period_controls.py`](../../output/cri_impact_app_v2/components/period_controls.py:1), even though Stage 1 exports are organized by concrete folder keys such as [`period_2560_2567`](../../build_exports/stage1/period_2560_2567/) and [`period_2567`](../../build_exports/stage1/period_2567/)
5. the top-level UX stopped reflecting the required four-tab contract described by the user and reinforced by the freeze documents

This produced both a conceptual mismatch and the concrete runtime break where [`load_metric()`](../../output/cri_impact_app_v2/runtime/data.py:33) was asked to resolve a nonexistent `cumulative` folder.

---

## 2. Evidence of Drift

### 2.1 Entrypoint mismatch

[`app.py`](../../output/cri_impact_app_v2/app.py:10) currently wires both a radio-navigation shell and a five-tab layout:

- Overview
- Province CRI & Heat
- Tambon Drilldown
- Rankings
- Period Controls

This is structurally off-spec because the frozen app contract is:

1. Methodology
2. CRI
3. Tambon-Level Human Impact
4. Heat Mortality

There is no frozen requirement for standalone “Rankings” or “Period Controls” sections.

### 2.2 Layout misunderstanding

[`paired_maps.py`](../../output/cri_impact_app_v2/pages/paired_maps.py:1) treats paired maps as its own page category.

The user feedback is explicit: paired maps means **1x2 plot layout inside a tab**, not a separate route or product area.

### 2.3 Data-contract mismatch

[`DEFAULT_PERIODS`](../../output/cri_impact_app_v2/components/period_controls.py:15) currently uses:

- `cumulative`
- `specific_year`

But Stage 1 frontend inputs in the execution plan require:

- [`period_2560_2567/tambon_deaths.json`](../../build_exports/stage1/period_2560_2567/tambon_deaths.json)
- [`period_2567/tambon_deaths.json`](../../build_exports/stage1/period_2567/tambon_deaths.json)

and the same folder pattern for other metrics.

That mismatch is the direct cause of the missing-file failure.

### 2.4 Freeze-document contradiction

The methodology freeze requires the public app to include:

1. a methodology page
2. CRI province-level maps
3. tambon-level human impact maps
4. heat impact maps
5. a time-period selector
6. ranking tables below each map

See [`2026-06-17_phase0-workstream2-methodology-freeze.md`](./2026-06-17_phase0-workstream2-methodology-freeze.md:217).

The current v2 structure violates item 6 by separating tables from the associated plots.

### 2.5 Execution-plan contradiction

The execution plan says:

- Stage 4 CRI tab contains maps plus top/bottom tables below each map
- Stage 5 Tambon tab contains zoomable human-impact views and grain-aware ranking tables
- Stage 6 Heat tab contains two heat maps and ranking tables for each map

See:

- [`2026-06-17_cri-webapp-orchestrator-execution-plan.md`](./2026-06-17_cri-webapp-orchestrator-execution-plan.md:260)
- [`2026-06-17_cri-webapp-orchestrator-execution-plan.md`](./2026-06-17_cri-webapp-orchestrator-execution-plan.md:302)
- [`2026-06-17_cri-webapp-orchestrator-execution-plan.md`](./2026-06-17_cri-webapp-orchestrator-execution-plan.md:343)

Nothing in the plan authorizes standalone pages for rankings or period controls.

---

## 3. Root Cause Analysis

### 3.1 Internal componentization overrode the product contract

The v2 implementation optimized for engineering reuse by creating generic internal modules and conceptual “pages”. That abstraction was not inherently wrong in code terms, but it overrode the actual product grammar defined by the freeze documents.

### 3.2 “Paired maps” was interpreted as taxonomy instead of composition

The implementation treated paired maps as a new screen type. The frozen meaning is simpler:

- a plot row with two map panels side by side
- each map occupying half-width
- each table sitting directly under its corresponding map

So the misunderstanding was semantic before it was technical.

### 3.3 Period selection was abstracted away from the Stage 1 export contract

The code introduced generic UI labels first, then expected runtime loaders to understand them. That reversed the dependency direction. The frontend must adapt to the Stage 1 contract, not invent a new one.

### 3.4 Shell/navigation duplicated responsibility

[`render_navigation()`](../../output/cri_impact_app_v2/components/shell.py:93) plus [`st.tabs()`](../../output/cri_impact_app_v2/app.py:27) created two simultaneous navigation systems. This added confusion and encouraged the wrong page split.

---

## 4. Non-Negotiable Correction Rules

The next implementation pass must follow these rules exactly:

1. **Only four top-level tabs**
   - Methodology
   - CRI
   - Tambon-Level Human Impact
   - Heat Mortality

2. **No standalone pages for layout patterns**
   - “paired maps” is a rendering pattern, not an app section
   - “rankings” is subordinate content under each plot block, not a tab
   - “period controls” is a local control pattern, not a tab

3. **All period controls must resolve to actual Stage 1 folder keys**
   - [`period_2560_2567`](../../build_exports/stage1/period_2560_2567/)
   - [`period_2567`](../../build_exports/stage1/period_2567/)

4. **Tables stay under the visual they describe**
   - no detached table-only screens
   - no screen-level ranking summary that loses plot association

5. **Frontend remains read-only with respect to analytics**
   - use exported JSON only
   - do not recompute province or tambon metrics from raw CSVs

6. **Public UI text must remain client-safe**
   - no internal engineering commentary
   - no pipeline-path leakage
   - no self-referential implementation notes

---

## 5. Correct Target Structure

The codebase may keep internal modules, but they must map to the visible product contract.

### 5.1 Visible app contract

The app must render exactly four `st.tabs(...)` sections in [`app.py`](../../output/cri_impact_app_v2/app.py:10):

1. **Methodology**
2. **CRI**
3. **Tambon-Level Human Impact**
4. **Heat Mortality**

### 5.2 Acceptable internal module split

Internal modules are acceptable only if they support the four-tab UX. A valid internal structure would look like:

- [`app.py`](../../output/cri_impact_app_v2/app.py)
- `tabs/methodology.py`
- `tabs/cri.py`
- `tabs/tambon_human_impact.py`
- `tabs/heat_mortality.py`
- shared components for map blocks, tables, and period selectors

The current naming under [`pages/`](../../output/cri_impact_app_v2/pages/) should either be removed or refactored to reflect tab-level ownership.

### 5.3 Shared layout primitive

The shared primitive should be a **map-and-table block**, not a “page”.

One block should own:

1. local period selector
2. 1x2 map row
3. 1x2 ranking-table row directly underneath

This is the real reusable unit.

---

## 6. Required Fixes by File Area

### 6.1 [`app.py`](../../output/cri_impact_app_v2/app.py:10)

Must be simplified to:

- set page config
- apply minimal shell style
- render title/subtitle only if still approved
- create exactly four tabs
- delegate each tab to one renderer

Must remove:

- radio navigation from [`render_navigation()`](../../output/cri_impact_app_v2/components/shell.py:93)
- extra tabs for rankings and periods
- Overview / Province CRI & Heat naming drift

### 6.2 [`components/period_controls.py`](../../output/cri_impact_app_v2/components/period_controls.py:1)

Must replace abstract keys with data-contract keys:

- `period_2560_2567` with a public label like `2560–2567 average`
- `period_2567` with a public label like `2567 only`

If a function returns a period key, it must return the exact folder key the loader expects.

### 6.3 [`runtime/data.py`](../../output/cri_impact_app_v2/runtime/data.py:33)

Must preserve [`load_metric()`](../../output/cri_impact_app_v2/runtime/data.py:33) as the single path resolver, but all callers must pass valid Stage 1 keys.

Audit every caller for illegal values such as:

- `cumulative`
- `specific_year`

Tambon helper mapping should be reduced or eliminated if it exists only to bridge a self-created abstraction.

### 6.4 [`pages/paired_maps.py`](../../output/cri_impact_app_v2/pages/paired_maps.py:1)

Must be dissolved or renamed because the concept is wrong at the product level.

Its contents should be split into:

- CRI tab rendering
- Heat tab rendering

with each tab using paired half-width maps as a local layout pattern.

### 6.5 [`pages/tables.py`](../../output/cri_impact_app_v2/pages/tables.py)

Should be removed from the visible routing model.

Any useful table-formatting logic should move into shared helpers only.

### 6.6 [`pages/periods.py`](../../output/cri_impact_app_v2/pages/periods.py)

Should be removed from the visible routing model.

Any useful control logic should be folded into local tab blocks.

### 6.7 [`pages/tambon.py`](../../output/cri_impact_app_v2/pages/tambon.py:58)

Needs restructuring so the tab presents two map panels side by side:

- tambon deaths
- tambon affected households

with ranking tables directly below those visuals.

The province selector can remain tab-scoped if a per-plot selector is too heavy, but the period control should still honor the frozen time modes and the tables must remain visually attached.

### 6.8 [`pages/overview.py`](../../output/cri_impact_app_v2/pages/overview.py)

Must become the Methodology tab implementation, or be renamed to match that contract.

Its text must be checked against the methodology freeze to ensure:

- no internal filenames
- both time modes explained plainly
- affected-household denominator explained
- heat described as two separate maps

---

## 7. Corrective Build Sequence

### Step 1 — Freeze the visible contract

Lock the top-level UI to the four required tabs in [`app.py`](../../output/cri_impact_app_v2/app.py:10).

### Step 2 — Remove parallel navigation systems

Delete or disable radio navigation in [`components/shell.py`](../../output/cri_impact_app_v2/components/shell.py:93) so only tabs define navigation.

### Step 3 — Repair period-key integrity first

Before layout work, replace all abstract period values with real Stage 1 keys in [`components/period_controls.py`](../../output/cri_impact_app_v2/components/period_controls.py:15) and all downstream callers.

This should eliminate the `cumulative` file-path failure.

### Step 4 — Recompose content by tab

Rebuild the app around four tab renderers:

1. Methodology
2. CRI
3. Tambon-Level Human Impact
4. Heat Mortality

### Step 5 — Rebuild CRI as map blocks

Inside the CRI tab:

- use 1x2 map rows
- place 1x2 top/bottom tables directly underneath each row
- cover all required CRI metrics plus CRI score

### Step 6 — Rebuild Tambon tab as paired drilldown views

Inside the Tambon tab:

- keep country-view vs selected-province logic if needed
- render deaths and affected-households as the paired visual focus
- keep tables attached below
- preserve province overlay and tambon boundary logic from the validated Stage 1 contract

### Step 7 — Rebuild Heat tab as two-map layout

Inside the Heat tab:

- left map: heat deaths
- right map: heat injured
- tables directly below each map

### Step 8 — Re-audit public wording

Check Methodology and tab descriptions against [`2026-06-17_phase0-workstream2-methodology-freeze.md`](./2026-06-17_phase0-workstream2-methodology-freeze.md:90).

### Step 9 — Runtime validation

Validate that:

- no code references `cumulative`
- no code references `specific_year`
- all tabs render
- all tables remain attached below their maps
- tambon selected-province mode still renders province-specific tambon boundaries

---

## 8. Acceptance Criteria for the Fix

The corrective pass is complete only when all of the following are true:

1. the app shows exactly four top-level tabs:
   - Methodology
   - CRI
   - Tambon-Level Human Impact
   - Heat Mortality

2. there is no standalone page or tab for:
   - paired maps
   - rankings
   - period controls

3. all period selectors resolve to real Stage 1 folders:
   - [`period_2560_2567`](../../build_exports/stage1/period_2560_2567/)
   - [`period_2567`](../../build_exports/stage1/period_2567/)

4. every plot block uses the intended composition:
   - 1x2 map row
   - 1x2 ranking-table row directly below

5. the CRI tab remains province-level and read-only against Stage 1 exports

6. the Tambon-Level Human Impact tab remains a province-to-tambon drilldown

7. the Heat Mortality tab shows two separate heat maps, not a merged view

8. the public text contains no internal implementation talk

9. the `cumulative/cri_score.json` failure is gone because the invalid folder key no longer exists in the UI flow

---

## 9. Immediate Recommendation

Do **not** patch the current route structure incrementally.

The cleaner path is:

1. keep only reusable low-level helpers that are still valid
2. discard the current visible page taxonomy
3. rebuild the visible app contract directly from the four frozen tabs
4. bind every period selector to real Stage 1 folder keys from the start

That is the shortest path back to structural integrity.

---

## 10. Implementation Note

This document is a planning correction artifact only. It does not authorize frontend code changes by itself. It defines the repair path so the next execution pass can proceed without repeating the same structural drift.
