# CRI Phase 1: High-Resolution Hybrid Methodology Plan (TEI + WorldPop)

## 1. Objective
Refine the **CRI Phase 1** methodology by integrating **Official Administrative Statistics** (TEI Pilot Baseline) with **WorldPop Global 2.0 Spatial Proxies**. The goal is to downscale disaster impact data to a high-resolution 100m grid and align it with the 69k villages in `dim_location_master.csv`.

## 2. Methodology: Dual-Track Spatial Disaggregation

### **Track A: Human Impact & Social Vulnerability (Dasymetric Mapping)**
- **Baseline Data**: `fact_impact.csv` (Official affected/fatality counts).
- **Spatial Proxies (WorldPop)**:
    - **Gridded Population (2015–2030)**: High-resolution (100m) annual estimates.
    - **Age & Sex Structure**: Breakdown of vulnerable demographics (children/elderly).
- **Algorithm**: Dasymetric mapping based on WorldPop grid values within administrative boundaries.

### **Track B: Structural & Economic Exposure (Asset-Based Proxies)**
- **Baseline Data**: `fact_relief.csv` (Fiscal relief for agricultural and non-agricultural damage).
- **Spatial Proxies (WorldPop)**:
    - **Building Classification (Residential/Industrial/Commercial)**: Assets weighted by land-use type.
    - **Building Footprints (Count/Volume/Height)**: Structural intensity markers for urban and rural settlements.
    - **Nighttime Lights (VIIRS)**: High-resolution proxy for local economic activity and GPP.
- **Algorithm**: Hybrid weighting using a **Structural Exposure Index** (derived from building volume and land-use intensity).

## 3. Implementation Phasing

### **Phase I: Resource Ingestion & Cross-Walk**
1. **API Extraction**: Fetch 100m Geotiff layers for Thailand from WorldPop STAC/REST APIs (`iso3=THA`).
2. **Zonal Aggregation**: Compute spatial proxy scores for all 69,000 villages in `dim_location_master.csv`.
3. **Gold Spine Merge**: Append village-level covariate scores (Population Density, Building Volume, NTL Index) to the master data system.

### **Phase II: Downscaling & Index Refinement**
1. **Proxy Correlation**: Test the statistical correlation between WorldPop's **Building Count** and historical **Relief Spending** for pilot provinces.
2. **Disaggregation Execution**: Redistribute provincial/district `fact_impact` and `fact_relief` to village-level refined estimates.
3. **Administrative Gap Mitigation**: Use proxy-based "Expected Impact" to identify and flag administrative reporting gaps in the baseline.
