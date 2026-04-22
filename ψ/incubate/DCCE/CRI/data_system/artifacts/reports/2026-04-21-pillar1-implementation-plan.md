# Pillar 1 Implementation Plan: Data Preparation and Comparative Dasymetric Analysis

## Phase 1: Housekeeping & Auditing (Bronze -> Silver)
These `.py` scripts will run independently to handle data cleaning, schema validation, and spatial joining. They ensure that only analysis-ready, perfectly keyed data reaches the analytical notebook.

### 1. TEI Baseline Prep (`prep_tei_casualties.py`)
*   **Inputs:** `0_bronze/tei_pilot/casualties_by_hazard_2559_2566.csv` and `2_gold/dim_location_master.csv`.
*   **Logic:** Audit and clean legacy provincial names. Map them to the canonical 2-digit `province_code` using the DOPA gold spine.
*   **Output:** `1_silver/tei_pilot/provincial_casualties_clean.csv`

### 2. DDPM Climate Filter & Aggregation (`prep_ddpm_climate_history.py`)
*   **Inputs:** `1_silver/ddpm/master_village_disaster_stat_2557_2567.csv` and `2_gold/dim_hazard_canonical.csv`.
*   **Logic:** 
    *   Join the DDPM statistics with `dim_hazard_canonical.csv` to identify climate-related events based on the `hazard_group` field.
    *   Filter out non-climate events (like fire or disease).
    *   Aggregate `Affected Households` from the 8-digit village level up to the canonical 6-digit Tambon (`subdistrict_code`) level.
*   **Output:** `1_silver/ddpm/tambon_climate_affected_household_aggregate_ddpm_village_stat.csv`

### 3. DOPA Geometry Enrichment (`prep_dopa_boundaries.py`)
*   **Inputs:** `0_bronze/dopa/thailanda-administrative-boundary/THA_Tambon.shp` and `2_gold/dim_location_master.csv`.
*   **Logic:** Audit the shapefile's Coordinate Reference System (CRS). Attach the canonical 6-digit DOPA `subdistrict_code` to the geometries to guarantee clean joins downstream.
*   **Output:** `1_silver/dopa/tambon_boundaries_enriched.shp` (Saved strictly as a Shapefile format).

### 4. WorldPop Zonal Statistics (`prep_worldpop_exposure.py`)
*   **Inputs:** `0_bronze/worldpop/tha_pop_2020_CN_100m_R2025A_v1.tif` and the enriched `tambon_boundaries_enriched.shp`.
*   **Logic:** Overlay the enriched Tambon boundaries onto the WorldPop raster. Calculate the total population per Tambon using zonal statistics.
*   **Outputs:** 
    *   `1_silver/worldpop/tambon_population_count_worldpop.tif` (Rasterized output format as requested).
    *   *Note: A tabular `.csv` version of these zonal counts will also be generated alongside the `.tif` to allow for seamless pandas merges in the notebook.*

---

## Phase 2: Core Analysis & Mapping (Silver -> Gold)
Implemented in a Jupyter Notebook to ensure a human-readable, report-style narrative free of ETL boilerplate.

**Notebook File:** `script/notebooks/pillar1_comparative_dasymetric_analysis.ipynb`

### Analytical Steps:
1.  **Load & Join:** Read the prepared Silver tables (`provincial_casualties_clean.csv`, `tambon_climate_affected_household_aggregate_ddpm_village_stat.csv`, and the WorldPop zonal stats CSV) and merge them smoothly on `subdistrict_code` and `province_code`.
2.  **Model A (Exposure-Based Dasymetric):** 
    *   Calculate each Tambon's share of the total Provincial Population.
    *   Distribute the TEI Provincial Casualties to the Tambon level using this population weight.
3.  **Model B (Impact-Based Dasymetric):** 
    *   Calculate each Tambon's share of the total Provincial Historical Affected Households.
    *   Distribute the TEI Provincial Casualties to the Tambon level using this historical impact weight.
4.  **Synthesis & Visualization:** 
    *   Generate comparative delta maps showing where the exposure model diverges from the historical impact model.
    *   Provide narrative markdown explaining the anomalies (e.g., highly populated areas with low historical climate casualties vs. sparsely populated areas with high casualties).
5.  **Publish to Gold:** Export the final analytical tables to the `2_gold/` directory for downstream use in dashboards or index calculations.
