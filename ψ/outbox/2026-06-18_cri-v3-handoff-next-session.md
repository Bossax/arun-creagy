# CRI Impact App v3 — Next Session Handoff

## What was started
A clean v3 implementation was scaffolded under [`ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/).

## Files created
- [`app.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/app.py:1)
- [`components/layout.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/components/layout.py:1)
- [`components/period_controls.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/components/period_controls.py:1)
- [`components/table_helpers.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/components/table_helpers.py:1)
- [`runtime/data.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/runtime/data.py:1)
- [`pages/methodology.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/pages/methodology.py:1)
- [`pages/cri.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/pages/cri.py:1)
- [`pages/tambon.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/pages/tambon.py:1)
- [`pages/heat.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/pages/heat.py:1)
- package markers and [`README.md`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/README.md:1)

## Contract encoded in the new scaffold
- Exactly four tabs: Methodology, CRI, Tambon-Level Human Impact, Heat Mortality.
- Period controls are bound to Stage 1 export keys only: [`period_2560_2567`](ψ/incubate/DCCE/CRI/data_system/build_exports/stage1/period_2560_2567/) and [`period_2567`](ψ/incubate/DCCE/CRI/data_system/build_exports/stage1/period_2567/).
- The frontend is read-only and consumes Stage 1 exports only.
- Ranking tables are constrained to rank / Thai name / value.
- Province and tambon map rendering are wired through Stage 1 spatial assets.

## Validation completed
- Python bytecode compilation completed successfully with [`python -m compileall -q ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3:1).

## What still needs checking in the next session
1. Run the app in Streamlit and confirm it boots without import/runtime errors.
2. Verify no v2 drift patterns remain:
   - no detached rankings section
   - no detached period-controls section
   - no five-tab layout drift
   - no `cumulative` or `specific_year` runtime path usage
3. Confirm the runtime root path in [`runtime/data.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/runtime/data.py:1) matches the actual workspace layout during live execution.

