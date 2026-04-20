# WorldPop Global 2.0: Technical Summary and Methodology
**Source**: [YouTube - WorldPop Global 2.0](https://www.youtube.com/watch?v=Hif2A3dmWqU)

## 1. Overview and Objectives
WorldPop Global 2.0 provides high-resolution, contemporary population distribution data for the period 2015–2030. It serves as a critical evidence layer for climate risk assessment, disaster response, and developmental planning, aiming to estimate population counts within a 100m x 100m (3 arc-second) grid cell.

## 2. Methodology: Machine Learning Disaggregation
The dataset utilizes a **top-down disaggregation** approach powered by **Random Forest (RF)** machine learning models to redistribute administrative population counts into grid cells.

### **Geospatial Covariates**
Population distribution is predicted using a suite of correlated demographic variants:
- **Infrastructure & Built Environment**: Residential buildings, neighborhoods, and infrastructure networks.
- **Observational Data**: Nighttime lights (VIIRS) and vegetation indices (NDVI).
- **Mobility and Socio-Economic Patterns**: Mobile phone-derived mobility patterns and building damage assessments from disaster datasets.

### **Disaggregation Constraints**
- **Inclusionary Data**: Census data and official projections (2020 round) are used as the primary population anchor.
- **Exclusionary Data**: Settlement datasets (JRC, DLR) define areas where population presence is unlikely, acting as a spatial domain "clipper" to focus the ML analysis.

## 3. Building Footprints: The Primary Predictor
A defining feature of Global 2.0 is the integration of multi-source building footprint data (Google, Microsoft, OSM).
- **Quantitative Metrics**: Building count, volume, and surface area are the highest-weighted predictors in the model.
- **Semantic Consistency**: Distinguishing between commercial and residential land use significantly increases the accuracy of population density estimations.

## 4. Advancements over Global 1.0
- **Data Recency**: Transition from outdated census anchors to the 2020 round of global estimates.
- **Temporal Dynamics**: Implementation of intrapolated and extrapolated time-series (2015–2030) using dynamic geospatial covariates.
- **Urbanization Modeling**: Integration of the "Degree of Urbanization" and PyPopRF workflows to better characterize urban vs. rural transitions.

## 5. Limitations and Uncertainties
- **Error Propagation**: As a top-down model, inaccuracies in the input administrative counts or settlement masks can propagate to the grid level.
- **Data Gaps**: Performance varies based on the availability and quality of national-level census data (e.g., requiring verification of Thailand’s 2020 census integration).

## 6. Access and Interoperability
The dataset is engineered for high interoperability through:
- **Cloud-Native Platforms**: Google Earth Engine (GEE) and Microsoft Planetary Computer.
- **Programmatic Access**: STAC API and RESTful interfaces.
- **Direct Retrieval**: Web portal and FTP for bulk TIFF/CSV downloads.


Resource links:
1. https://www.worldpop.org/blog/worldpop-global2-global-high-resolution-population-estimates-for-2015-2030/
2. https://www.worldpop.org/datacatalog/
3. https://www.worldpop.org/sdi/introapi/
4. https://www.stacindex.org/catalogs/worldpop-stac-api#/
