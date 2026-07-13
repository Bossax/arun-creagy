# Perplexity Double-Check: Hazard Model Input Data Entities

**Date**: 2026-07-13  
**Query Model**: Perplexity Sonar  

## Perplexity Response

To simulate and model hazard maps for the five specified hazards, the necessary input data entities must be categorized into **Terrain/Bathymetry**, **Meteorology/Climatology**, **Geotechnical/Soil**, **Hydrology**, and **Land Cover/Surface Roughness**. Below are the specific physical input variables required for each hazard, grouped by these logical categories.

### 1. Riverine (Fluvial) and Pluvial Flooding

**Riverine Flooding** requires hydraulic modeling of river networks, while **Pluvial Flooding** focuses on urban drainage and surface runoff from rainfall exceeding infiltration capacity.

| Data Category | Specific Physical Input Variables |
| :--- | :--- |
| **Terrain/Bathymetry** | • **High-Resolution DEM** (e.g., LiDAR, 1–5 m resolution) to define ground surface and flow paths [1][7]<br>• **River Channel Bathymetry** (cross-sections, bank lines, stream centerlines) to define channel depth and capacity [1][5]<br>• **Topographic Curvature** and **Topographic Wetness Index (TWI)** to identify flow accumulation zones [1] |
| **Meteorology/Climatology** | • **Precipitation Time Series** (rainfall depth, intensity, duration) for design events (e.g., Q100, 1-in-100-year) [1][9]<br>• **Rainfall Quantitative Precipitation Estimates (QPE)** fields for stochastic storm modeling [9]<br>• **Climate Forcings** (for future scenario modeling, e.g., RCP4.5) [8] |
| **Hydrology** | • **Runoff/Discharge Data** (streamflow, bankfull discharge) derived from hydrological models (e.g., LISFLOOD, CaMa-Flood) [2][3][4]<br>• **Flood Frequency Analysis** results (Return Periods: 1-in-10 to 1-in-500 years) [2][3]<br>• **Soil Moisture** and **Antecedent Precipitation** to determine initial infiltration capacity [1] |
| **Geotechnical/Soil** | • **Soil Texture** and **Lithology** to define infiltration rates and permeability [1]<br>• **Permeability/Infiltration Coefficients** (e.g., Horton or Green-Ampt parameters) [1] |
| **Land Cover/Surface Roughness** | • **Land Use/Land Cover (LULC)** maps to assign roughness coefficients (e.g., Manning’s *n*) [1][5]<br>• **Normalized Difference Vegetation Index (NDVI)** to assess vegetation density and its impact on runoff [1]<br>• **Urban Drainage Infrastructure** (pipe networks, culverts) for pluvial modeling [8] |

---

### 2. Meteorological and Hydrological Drought

**Meteorological Drought** is defined by precipitation deficits, while **Hydrological Drought** involves deficits in surface and subsurface water supplies (streamflow, soil moisture, reservoir levels).

| Data Category | Specific Physical Input Variables |
| :--- | :--- |
| **Meteorology/Climatology** | • **Precipitation Anomalies** (long-term monthly/annual totals vs. historical mean) [2]<br>• **Temperature Data** (for evapotranspiration calculations) [2]<br>• **Standardized Precipitation Index (SPI)** and **Standardized Precipitation-Evapotranspiration Index (SPEI)** inputs [2] |
| **Hydrology** | • **Streamflow/Discharge Records** (low-flow indices, e.g., Q95) [2][3]<br>• **Soil Moisture Content** (volumetric water content) as a key indicator of hydrological drought [2]<br>• **Reservoir/Lake Levels** and **Groundwater Table Depth** [2] |
| **Geotechnical/Soil** | • **Soil Hydraulic Properties** (saturated conductivity, porosity) to model water retention and release [2]<br>• **Root Zone Depth** and **Crop Coefficients** (for agricultural drought assessment) [2] |
| **Land Cover/Surface Roughness** | • **LULC** to determine evapotranspiration rates and water demand [2]<br>• **Vegetation Health Indices** (e.g., NDVI anomalies) to detect drought stress [2] |
| **Terrain/Bathymetry** | • **Basin Topography** to define catchment boundaries for hydrological modeling [2] |

---

### 3. Sea Level Rise (Coastal Inundation)

This hazard models the long-term vertical rise of the ocean surface and its interaction with coastal topography, distinct from short-term storm events.

| Data Category | Specific Physical Input Variables |
| :--- | :--- |
| **Terrain/Bathymetry** | • **Coastal DEM** (high-resolution LiDAR) for land elevation [7]<br>• **Bathymetry** (seafloor depth) to model water propagation [8]<br>• **Tidal Datums** (Mean Sea Level, High/Low Water) as the baseline reference [5] |
| **Meteorology/Climatology** | • **Global Mean Sea Level (GMSL) Projections** (e.g., IPCC scenarios for 2035, 2050, 2100) [8]<br>• **Regional Sea Level Change Factors** (accounting for land subsidence/uplift) [8] |
| **Hydrology** | • **River Discharge at Coast** (to assess fluvial-coastal interaction) [8] |
| **Land Cover/Surface Roughness** | • **LULC** to define friction coefficients for water flow over land [1]<br>• **Coastal Defense Infrastructure** (dikes, seawalls) and their elevation [8] |
| **Geotechnical/Soil** | • **Soil Compaction/Subsidence Rates** (critical for accurate relative sea level rise) [8] |

---

### 4. Storm Surge

Storm surge is the short-term, wind-driven rise in water level during a storm, requiring dynamic coupling of meteorology and hydrodynamics.

| Data Category | Specific Physical Input Variables |
| :--- | :--- |
| **Meteorology/Climatology** | • **Wind Speed and Direction** (time-series, peak gusts) [8]<br>• **Atmospheric Pressure** (central pressure of the storm) [8]<br>• **Storm Track and Duration** (spatial path and temporal evolution) [8] |
| **Terrain/Bathymetry** | • **Coastal DEM** and **Bathymetry** (critical for surge amplification in shallow waters) [7][8]<br>• **Tidal Stage** at storm onset (surge + tide = total water level) [5] |
| **Hydrology** | • **Initial Water Levels** (pre-storm sea level) [8] |
| **Land Cover/Surface Roughness** | • **LULC** and **Manning’s *n*** for overland flow resistance [1]<br>• **Barrier Islands/Wetlands** extent (to attenuate surge) [8] |
| **Geotechnical/Soil** | • **Coastal Erosion Rates** (to update bathymetry/terrain dynamically if modeling long-term) [8] |

---

### 5. Landslides

Landslide modeling (slope stability) requires geotechnical parameters to calculate the balance between driving forces (gravity, water) and resisting forces (shear strength).

| Data Category | Specific Physical Input Variables |
| :--- | :--- |
| **Terrain/Bathymetry** | • **High-Resolution DEM** (to calculate **Slope Angle**, **Aspect**, and **Curvature**) [1]<br>• **Topographic Wetness Index (TWI)** to identify saturation zones [1] |
| **Meteorology/Climatology** | • **Precipitation Intensity and Duration** (triggering event) [1]<br>• **Rainfall Accumulation** (antecedent moisture) [1] |
| **Hydrology** | • **Soil Moisture** and **Pore Water Pressure** (critical for reducing shear strength) [1]<br>• **Groundwater Level** fluctuations [1] |
| **Geotechnical/Soil** | • **Shear Strength Parameters**: **Cohesion** ($c$) and **Angle of Internal Friction** ($\phi$) [1]<br>• **Soil Thickness** and **Unit Weight** (density) [1]<br>• **Lithology** and **Soil Texture** (to infer material properties) [1] |
| **Land Cover/Surface Roughness** | • **LULC** (root reinforcement from vegetation increases shear strength) [1]<br>• **NDVI** (vegetation density) [1] |

### Key Implementation Notes
*   **Resolution:** For pluvial flooding and landslides, **LiDAR-derived DEMs** (1 m resolution) are often mandatory to capture micro-topography and flow paths [1][7].
*   **Return Periods:** Flood and surge models typically require inputs for multiple return periods (e.g., 1-in-10 to 1-in-500 years) to generate probabilistic hazard maps [2][3].
*   **Dynamic vs. Static:** Drought and Sea Level Rise are often modeled with static or slowly changing inputs, whereas Storm Surge and Floods require **time-series dynamic inputs** (wind, rainfall) [8].
