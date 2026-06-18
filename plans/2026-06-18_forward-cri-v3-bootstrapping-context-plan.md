# Next-Session Plan — CRI v3 Bootstrapping Context

**Handoff Reference**: [`C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/inbox/handoff/2026-06-18_09-45_cri-v3-bootstrapping-context.md`](C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/inbox/handoff/2026-06-18_09-45_cri-v3-bootstrapping-context.md)

## Current Status
We have a hardened v3 plan and a clear diagnosis of why v2 failed. We are ready to begin Stage 1 (Data Foundation) and Stage 2 (App Shell).

## Proposed Path: Stage 1 & 2 Kickoff
1. **Initialize v3 Environment**: Create `output/cri_impact_app_v3/` and revert accidental legacy changes.
2. **Generate Stage 1 Exports**: Run the logic from `cri_phase_1_demo.ipynb` to produce canonical JSON files in `build_exports/stage1/`.
3. **Draft Methodology Text**: Finalize the client-safe copy for the landing tab.

## Next Session: Pick Your Path

| Option | Command | What It Does |
|--------|---------|--------------|
| **Start v3 Clean Build** | `/recap` | Begin Stage 1 data export and Stage 2 shell setup. |
| **Cleanup Legacy First** | `git status` -> `git checkout` | Revert v2 drift in legacy folders, then continue. |
| **Audit Methodology** | `/recap --quick` | Review the methodology freeze before any code is written. |

### 🛠️ Cleanup Checklist
- [ ] Revert changes in `output/cri_impact_app/` (v2 attempt).
- [ ] Ensure `build_exports/stage1/` is empty and ready for fresh v3 data.
