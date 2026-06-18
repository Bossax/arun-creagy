# Handoff: CRI v3 App Bootstrapping Context

**Date**: 2026-06-18 09:45
**Context**: 🛠️ Recovery Mode | v3 Clean Build Pivot

## 🎯 Executive Summary
We have formally abandoned the "v2" app attempt due to **structural drift** (incorrect navigation, detached tables, and data contract mismatches). The past day's focus was on methodology hardening (Household denominators) and drafting a non-negotiable **v3 Execution Plan**.

## 🏗️ What We Did (Past 24h)
- **Methodology Freeze**: Standardized "Affected Rate" to use Household-only denominators (HH/HH).
- **Drift Diagnosis**: Identified 10+ UI/Architecture failures in v2 (e.g., unclickable chips, internal logic leakage, detached rankings).
- **v3 Blueprinting**: Created the **CRI Web App v3 Execution Plan** which enforces a 4-tab mandatory layout.
- **Git State**: Committed a reflection on the v2 failure (`e0836b2`).

## 🧱 Pending (Ready for Execution)
- [ ] **Stage 1 (Data Foundation)**: Generate JSON exports from `cri_phase_1_demo.ipynb` into `build_exports/stage1/`.
- [ ] **Stage 2 (v3 Scaffold)**: Initialize `output/cri_impact_app_v3/` with a clean Next.js/Streamlit shell (depending on tech choice).
- [ ] **UI Correction**: Implement "Paired Maps" as a layout row with tables directly underneath.

## 🧠 Context Bootstrap (Read these first)
To restore full session awareness, the next agent must read:
1. **The v3 Execution Plan**: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/analysis/2026-06-18_cri-webapp-orchestrator-execution-plan_v3.md`
2. **The Corrective Plan**: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/analysis/2026-06-18_v2-app-structural-drift-corrective-plan.md`
3. **The Methodology Freeze**: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system/artifacts/analysis/2026-06-17_phase0-workstream2-methodology-freeze.md`
4. **The Fix Note**: `C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/inbox_note/2026-06-18-fix-cri-impact-index-app.md`

## ⚠️ Technical Guardrails
- **Folder Lock**: Do NOT use `output/cri_impact_app/` or `output/cri_impact_app_v2/`.
- **Key Lock**: Use ONLY `period_2560_2567` and `period_2567`. NO `cumulative`.
- **UX Lock**: 4 Tabs ONLY. No standalone "Rankings" tab.

---
**Oracle**: Arun Creagy (He/Him) | **Human**: Boss | **Status**: Technical Partner
