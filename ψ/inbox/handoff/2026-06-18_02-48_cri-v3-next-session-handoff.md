# CRI Impact App v3 — Handoff for Next Session

## Context
Work started on a clean v3 implementation for the CRI web app under [`ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/).

## Completed so far
Created the v3 scaffold and tab modules:
- [`app.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/app.py:1)
- [`components/layout.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/components/layout.py:1)
- [`components/period_controls.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/components/period_controls.py:1)
- [`components/table_helpers.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/components/table_helpers.py:1)
- [`runtime/data.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/runtime/data.py:1)
- [`pages/methodology.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/pages/methodology.py:1)
- [`pages/cri.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/pages/cri.py:1)
- [`pages/tambon.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/pages/tambon.py:1)
- [`pages/heat.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/pages/heat.py:1)
- [`README.md`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/README.md:1)

## Contract already encoded
- Exactly four tabs: Methodology, CRI, Tambon-Level Human Impact, Heat Mortality.
- Period controls only use Stage 1 keys: [`period_2560_2567`](ψ/incubate/DCCE/CRI/data_system/build_exports/stage1/period_2560_2567/) and [`period_2567`](ψ/incubate/DCCE/CRI/data_system/build_exports/stage1/period_2567/).
- Read-only frontend posture: consume Stage 1 exports only.
- Ranking tables are constrained to rank / Thai name / value.
- Province and tambon geojson helpers are wired to Stage 1 spatial assets.

## Validation completed
- [`python -m compileall -q ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3:1) ran successfully.

## Known remaining checks
1. Smoke-test Streamlit startup and runtime imports.
2. Confirm no v2 drift patterns in v3:
   - no detached rankings page
   - no detached period-controls page
   - no five-tab drift
   - no `cumulative` or `specific_year` runtime path usage
3. Verify the runtime root path in [`runtime/data.py`](ψ/incubate/DCCE/CRI/data_system/output/cri_impact_app_v3/runtime/data.py:1) against the live workspace layout if needed.

## Note on previous handoff
A local outbox note was also created, but the authoritative session handoff now lives in Oracle inbox/handoff via this entry.