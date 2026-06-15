# Handoff: Terminology Refactor & CRI Analytical Update

**Date**: 2026-06-15 18:00
**Context**: Climate Risk Index (CRI) Phase 1 Hardening

## What We Did
- **Global Terminology Refactor**: Successfully replaced "Eco-Loss" with **"Government Advance Payment" (เงินทดรองราชการ)** across all scripts, metadata, and data paths. 
- **Workbook Renaming**: Source workbook is now `CRI Data - Government_Advanced_Payment.xlsx`.
- **Pipeline Update**: Rewrote extraction (`extract_govt_adv_payment_hazard_sheets.py`) and normalization (`normalize_govt_adv_payment_to_silver.py`) scripts to match new terminology.
- **Analytical Hardening**: 
    - Updated CRI scoring weights to align with Pilot methodology: **Deaths/100k (22.5%)**, **Affected/100k (15.0%)**, and **Loss/GPP (37.5%)**.
    - Implemented **Final Score Re-normalization** (0.0 to 1.0) in the demo notebook.
- **Strategic Roadmap**: Detailed the **"Alpha Wedge" (Service 4)** in the `NCAIF-Service-Enrichment-Roadmap.md` to bridge fiscal relief and true economic damage.

## Pending
- [ ] Compare CRI Phase 1 results with CRI Pilot project (TEI pilot datasets).
- [ ] Investigate drivers of provincial ranking shifts (Bangkok Paradox vs. Weighting updates).

## Hypotheses for Next Session (Audit Required)
- [ ] **Hypothesis 1**: Differences between Phase 1 and Pilot results are significantly driven by the inclusion of "Director-General's budget" (วงเงินอำนาจอธิบดี) in the current dataset, which affects urban relief management totals (especially Bangkok).
- [ ] **Hypothesis 2**: Shifting "Deaths/100k" from 5% (previous demo) to 22.5% (Pilot) will de-emphasize large-population impact counts in favor of relative risk in smaller provinces (e.g., Mae Hong Son).

## Key Files
- `ψ/incubate/DCCE/CRI/data_system/data/0_bronze/2026-06-12_cri_proj_data/CRI Data - Government_Advanced_Payment.xlsx`
- `ψ/incubate/DCCE/CRI/data_system/script/analysis_notebooks/cri_province_impact_demo.ipynb`
- `ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/2026-06-15_NCAIF-Service-Enrichment-Roadmap.md`
- `ψ/incubate/DCCE/CRI/data_system/data/0_bronze/tei_pilot/` (Target for next session)
