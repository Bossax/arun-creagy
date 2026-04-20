# Research Plan: CRI Phase 1 Methodology Enhancement (TEI Baseline + WorldPop Integration)

**Strategic Objective:** To formulate and validate a methodology that enhances the spatial resolution of the TEI CRI Pilot's administrative impact data (Human and Economic) using high-resolution spatial proxies, while explicitly identifying and mitigating the limitations of both our baseline data and external datasets.

## Phase 1: Baseline Audit and Limitation Profiling
*Before integrating new data, we must fully understand the structure, lineage, and constraints of our existing "Gold Spine."*

*   **Task 1.1: Data Lineage Verification:** Confirm the exact data pipeline from the raw `0_bronze/tei_pilot` files (casualties, relief, population, GPP averages) to our current `2_gold` analytical tables (`fact_impact.csv`, `fact_relief.csv`). *Note: Bronze files are protected/ignored by system configuration to preserve raw data integrity; analysis will focus on Silver/Gold derivatives.*
*   **Task 1.2: Administrative Gap Analysis:** Quantify the "missing vs. zero" reporting issue within `fact_impact` and `fact_relief`. How pervasive is the lack of DDPM/OAE reporting in certain provinces or hazard types?
*   **Deliverable:** A documented baseline profile detailing the exact constraints we are trying to solve with spatial disaggregation.

## Phase 2: Systematic WorldPop Resource Evaluation
*We will conduct a curious, critical audit of the WorldPop Data Catalog to identify candidate spatial proxies, explicitly documenting their limitations.*

*   **Task 2.1: Catalog Inventory:** Systematically explore `worldpop.org/datacatalog/` for Thailand-specific datasets.
    *   *Target Categories*: Demographics (Age/Sex structures), Built Environment (Building footprints, classifications), Economic Proxies (Nighttime lights).
*   **Task 2.2: Limitation Profiling:** For every candidate dataset, document:
    *   **Vintage**: What year does the source imagery or data represent? Does it align with our baseline (2559-2566)?
    *   **Modeling Assumptions**: Is the data directly observed or modeled? (e.g., top-down disaggregation errors).
    *   **Resolution Constraints**: Are there discrepancies between the 100m grid and our `dim_location_master` village boundaries?
*   **Deliverable:** A formal "Candidate Proxy Inventory" matrix evaluating potential, vintage, and documented limitations.

## Phase 3: Hypothesis Formulation and Verification Strategy
*Based on the inventory, we will formulate specific questions regarding how to map WorldPop datasets to the TEI methodology's Human and Economic pillars, and design tests to verify these relationships.*

*   **Hypothesis Group A (Human Impact - Track A):**
    *   **Question**: Can WorldPop's gridded population and age/sex structures provide a statistically significant improvement over uniform administrative averaging when distributing `fact_impact` (affected persons/fatalities)?
    *   **Verification**: Perform dasymetric mapping on a pilot province. Compare the resulting village-level distribution against any known localized historical impact reports to assess accuracy improvements.
*   **Hypothesis Group B (Economic/Structural Impact - Track B):**
    *   **Question**: Which combination of WorldPop Built Environment variables (building count, volume, or land-use classification) best correlates with the fiscal damage recorded in `fact_relief`?
    *   **Verification**: Extract building footprint metrics and Nighttime Lights for a pilot province. Perform correlation analysis between these covariates and the provincial relief spending.
*   **Methodological Question:**
    *   **Question**: Based on the correlation results, what is the most robust statistical method (e.g., simple weighted distribution, Geographically Weighted Regression, or Machine Learning approaches) to execute the final downscaling without introducing excessive modeling artifacts?
    *   **Verification**: Test 2-3 candidate models on the pilot province data and evaluate their performance and interpretability.

## Phase 4: Synthesis and Methodology Drafting
*Only after empirical verification will we commit to a final workflow.*

*   **Task 4.1**: Draft the final, validated "CRI Phase 1 Hybrid Methodology" detailing the selected proxies, their verified downscaling algorithms, and the acknowledged limitations of the final output.
