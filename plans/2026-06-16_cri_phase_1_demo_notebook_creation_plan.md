# Plan: Creation of CRI Phase 1 Demo Notebook

## Objective
Implement a high-fidelity Jupyter notebook (`cri_phase_1_demo.ipynb`) that demonstrates the CRI Phase 1 methodology, establishes data lineage for core and supplementary metrics (Tambon Impact and Heat Mortality), and provides production-ready visualizations for stakeholder review.

---

## Data Pipeline Guardrails (Technical Integrity)

To ensure the implementation remains grounded in the "sealed" methodology from `cri_methodology_comparison.ipynb`, the following guardrails are mandatory:

### 1. Scoring Logic & Weights
- **Normalization**: All indicators MUST use **Min-Max Scaling** to the range [0, 1].
- **Weights**:
    - **Human Impact (50%)**: 
        - Total Deaths (Absolute): **7.5%**
        - Death Rate (per 100k): **22.5%**
        - Total Affected Households (Absolute): **5.0%**
        - Affected Rate (per 100k): **15.0%**
    - **Economic Impact (50%)**:
        - Total Economic Loss (Absolute): **12.5%**
        - Loss per Unit GPP: **37.5%**

### 2. Lineage & Aggregation Logic (Phase 1: B.E. 2560-2567)
All metrics MUST be averaged over the 8-year period to produce the **Annual Average Impact**.

#### Human Pillar (Source: `fact_ddpm_tambon_impact_climate_2560_2567.csv`)
1.  **Total Deaths (Absolute)**: `sum(deaths_sum) / 8.0`
2.  **Death Rate**: `(Total Deaths (Absolute) / avg(population)) * 100,000`
3.  **Total Affected Households (Absolute)**: `sum(affected_households_sum) / 8.0` (Note: Social proxy)
4.  **Affected Rate**: `(Total Affected Households (Absolute) / avg(population)) * 100,000`

#### Economic Pillar (Source: `silver_govt_adv_payment_annual_long.csv`)
5.  **Total Economic Loss (Absolute)**: `Average of (Annual Provincial Sum of 'value')`
6.  **Loss per Unit GPP**: `Total Economic Loss (Absolute) / (avg(Total GPP) * 1,000,000)`

#### Denominators (Silver Sources)
-   **Population**: `silver_population_annual.csv` (DOPA).
-   **GPP**: `silver_gpp_annual_long.csv` (NESDC) filtered for `GPP_CURRENT_MARKET_PRICE`.


---

## Notebook Structure & Content

### 1. CRI Methodology (Explanation)
- **Goal**: Formally define the scoring logic and indicators.
- **Content**:
    - Table of 6 indicators and weights.
    - Mathematical formula for Min-Max Scaling and Weighted Summing.
    - Terminal-style documentation of the Python environment and kernel.

### 2. Tambon-Level Human Impacts Data Lineage
- **Goal**: Trace the origin of granular impact data.
- **Content**:
    - **Dataset**: Gold fact table (`fact_ddpm_tambon_impact_climate_2560_2567.csv`).
    - **Join Key**: 6-digit DOPA subdistrict code (`subdistrict_code`).
    - **Note**: Highlights the 2.5x higher reporting reliability of Households vs. People.

### 3. Heat Mortality Data Lineage
- **Goal**: Introduce the climate-health hazard layer.
- **Content**:
    - **Dataset**: `silver_heatwave_impact_long.csv`.
    - **Metric**: Mortality (death)

### 4. Calculation and Visualization of CRI Score (Province Level)
- **Implementation**:
    - Reproduce the 6 normalized metrics.
    - **Visualization**: Side-by-side GeoPandas choropleths (`OrRd` colormap).
    - **Validation**: Include Rank Correlation vs. Pilot to demonstrate proxy stability ($\rho \approx 0.79$).

### 5. Calculation and Visualization of Tambon-Level Impacts
- **Implementation**:
    - Average Deaths and Affected HH per year (`metric / 8.0`).
    - **Visualization**: Subdistrict granularity maps with `OrRd` colormap.
    - **Context**: Use `THA_Province.shp` for outer boundaries.

### 6. Visualization of Heat Mortality
- **Implementation**:
    - Standardize mortality at the province level.
    - **Visualization**: Choropleth map using the `YlOrBr` (Yellow-Orange-Brown) colormap.

---

## Technical Specifications
- **Kernel**: Python (CRI-Pillar1)
- **Libraries**: `pandas`, `geopandas`, `matplotlib`, `seaborn`, `scipy.stats`.
- **Formatting**: Use Markdown for lineage; code cells must be atomic.
- **Font Support**: Matplotlib configured for 'Tahoma' or 'TH Sarabun New'.

## Acceptance Criteria
1. Notebook runs end-to-end without path errors.
2. All 6 CRI metrics match the rehearsed weights and denominators.
3. Visualization outputs use correct colormaps (`OrRd` for impacts, `YlOrBr` for heat).
4. Lineage descriptions cite the correct Bronze/Silver/Gold sources.

## Execution Sequence
1.  **Stage 1: Scaffolding**: Create notebook and document Sections 1–3.
2.  **Stage 2: Province Calculation**: Implement province-level scoring (6 indicators).
3.  **Stage 3: Tambon & Heat Viz**: Implement granular maps and health overlay.
4.  **Stage 4: Validation**: Append the "Bangkok Paradox" analysis and rank correlation.
