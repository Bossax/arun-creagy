# CRI Phase 1 (Stage 3): Spatial Disaggregation & Asset-Based Mapping Plan (v2)

**Objective:** To define the datasets, decision points, and analytical pipelines required to disaggregate provincial-level casualties, damage, and relief data into high-resolution sub-district (Tambon) and spatial surfaces using WorldPop, ESA WorldCover, DDPM historical records, and TEI baselines.

---

## 1. Strategic Decision Points

Based on the Phase 1 audit and the shift towards a true dasymetric disaggregation model, the following critical decisions frame the approach:

1. **The TEI Anchor (Pillar 1):** We use the **TEI Provincial Baseline** (`casualties_by_hazard_2559_2566.csv`) as the primary basis for human impact. Audited provincial totals provide a stable historical metric compared to raw village counts.
2. **Prioritize Dense Administrative Indicators:** `Affected Households` and `Housing Damage` are the only indicators with sufficient density. Sparse indicators (livestock, utilities) are **dropped** to avoid "false precision."
3. **Comparative & Synthetic Disaggregation (Pillar 1):** We produce three models (Population, Empirical, and Hybrid) to identify and correct population bias in urban centers.
4. **The "Meta-Sector" Relief Grouping (Pillar 3/4):** DDPM financial relief categories are grouped into **Meta-Sectors** to reliably disaggregate funds based on physical assets (buildings) or land cover (agriculture).
5. **Bangkok Integration:** Bangkok is included by anchoring TEI provincial BMA records to the Bangkok sub-district structure, ensuring a complete national risk surface.

---

## 2. Approved Datasets for the Pipeline

### A. Administrative Basis (The "Known Totals")
*   **TEI Provincial Casualties**: Audited historical deaths and injuries by province.
*   **DDPM Sectoral Relief**: Provincial lump-sum payouts for sectoral disaggregation.
*   **DDPM Housing Damage**: Village-level counts used as a basis for Pillar 2.

### B. Spatial Weights & Disaggregators
*   **WorldPop Constrained Population (100m)**: `tha_pop_2020_CN_100m_R2025A_v1.tif`. Weight for human exposure.
*   **WorldPop Harmonized Building Metrics (100m)**: Building counts and area. Proxy for structural assets.
*   **DDPM Historical Impact Weight**: `tambon_climate_affected_household_aggregate_ddpm_village_stat.csv`. 
*   **ESA WorldCover (10m)**: Land cover masks (Cropland, Grassland, Water) for agricultural disaggregation.
*   **DOPA Administrative Shapefiles**: Enriched boundaries for Province and Tambon.

---

## 3. Analytical Pipelines (The 5-Pillar Strategy)

### Pillar 1: High Confidence - Human Impact Pipeline (Comparative)
We disaggregate TEI Provincial Casualties using three distinct weighting models:
*   **Model A (Population-Based)**: 
    *   *Weight*: Tambon share of Provincial Population.
    *   *Bias*: Systematically overestimates risk in safe, high-density urban areas.
*   **Model B (Empirical)**: 
    *   *Weight*: Tambon share of Historical Climate Impact (DDPM).
    *   *Bias*: Subject to self-reporting gaps and administrative variance.
*   **Model C (The Synthetic Hybrid - Bias Correction)**: 
    History is used as a spatial gate for population. We evaluate two options:
    * [x]   **Option 1: Probability Weight**: $Weight = Population \times Empirical (Affected-Household)$. Magnitude-scales risk by frequency.
    * [ ]   **Option 2: Binary Masked**: $Weight = Population$ (only in areas with any history). Uses history strictly as a footprint.

### Pillar 2: High Confidence - Residential/Structural Pipeline
*   **Target Data**: `Housing Damage` (DDPM Village Stats) aggregated to Provincial level.
*   **Spatial Proxy**: WorldPop Building Count + Building Area.
*   **Methodology**: Physical housing damage has a direct physical relationship with building footprints. We use WorldPop's building metrics to create a "Total Structural Asset" baseline and disaggregate provincial totals back to the Tambon level based on structural density.

### Pillar 3: Medium-High Confidence - Consolidated Fiscal Relief
*   **Target Data**: Provincial Social/Infrastructure relief categories.
*   **Spatial Proxy**: WorldPop Building Area + Infrastructure Connectivity (Distance to Roads).
*   **Methodology**: Fiscal relief for infrastructure correlates with built capital and connectivity. We distribute provincial lump sums to grid cells weighted by combined building and road density, then re-aggregate to the Tambon level.

### Pillar 4: Medium Confidence - Rural / Agricultural Relief Pipeline
*   **Target Data**: Agri-Relief provincial categories (`ด้านเกษตร_พืช`, `ด้านเกษตร_ประมง`, etc).
*   **Spatial Proxy**: ESA WorldCover (Cropland + Grassland + Water masks).
*   **Methodology**: Mask out urban/forested areas. Distribute provincial agricultural relief lump sums **only** to the remaining agricultural pixels. This corrects the TEI Pilot's flaw of dividing agricultural risk by total provincial GPP.

### Pillar 5: Low Confidence - Specific Sectoral Assets [DROPPED]
*   **Rationale**: Indicators like livestock or utility damage are severely under-reported. Disaggregating these individually would introduce "false precision" and noise.
