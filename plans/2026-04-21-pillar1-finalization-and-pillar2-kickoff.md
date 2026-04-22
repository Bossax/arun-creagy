# Next Session Plan: CRI Pillar 1 Finalization & Pillar 2 Kickoff

## 🎯 What We Accomplished
We executed a complete strategic pivot for **CRI Phase 1 (Stage 3)**.
*   Abandoned the flawed "Aggregation-as-Disaggregation" approach.
*   Archived all legacy Stage 3 scripts to prevent logic bleed.
*   Successfully implemented **Pillar 1 (Human Impact)** using audited TEI provincial baselines.
*   Created a robust, 4-script automated data preparation pipeline (`prep_tei`, `prep_ddpm`, `prep_dopa`, `prep_worldpop`).
*   Developed **Model C (The Synthetic Hybrid)** to explicitly neutralize the dasymetric population bias (where safe urban centers were previously assigned high risk).
*   Scaffolded a complete Jupyter Notebook with discrete percentile mapping, rank shift anomaly detection, and regional deep-dives.

## 📦 Pending Items Carried Forward
-   [ ] Run the final analysis in the notebook to generate the `human_impact_casualties_by_tambon_comparative.csv` Gold file.
-   [ ] Identify and formally document the Top 10 "Bias Zones" (Urban centers where the Population model overestimated risk compared to the Hybrid model).

## 🚀 Next Session Goals & Scope
1.  **Close Pillar 1**: Execute the notebook, review the hotspot maps, and save the Gold output.
2.  **Kickoff Pillar 2 (Structural Assets)**: Write `prep_building_exposure.py` using WorldPop building metrics (count and area) to disaggregate DDPM housing damage.
3.  **Prepare Pillar 4 (Agricultural)**: Begin the ingestion of ESA WorldCover 10m GeoTIFFs to create the spatial masks for cropland/grassland.

**Handoff File Reference**: `ψ/inbox/handoff/2026-04-21_12-50_cri-pillar1-pivot-complete.md`

---

## 🚦 Next Session: Pick Your Path

| Option | Command | What It Does |
|--------|---------|--------------|
| **Continue** | `/recap` | Review the handoff, execute the notebook to close Pillar 1, and start Pillar 2. |
| **Clean up first** | `/recap --quick` | Clear any remaining unused artifacts from the workspace before starting new scripts. |
| **Fresh start** | `/recap --quick` | Skip the notebook execution and immediately begin coding the building exposure script for Pillar 2. |
