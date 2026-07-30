# Evidence Map — Climate Data Downscaling Roll-ups

## Overview
This document maps every core claim, data parameter, and methodological distinction to an authoritative evidence source. It establishes visual treatment boundaries to prevent misleading representations.

---

## 1. Rollup 01 Claims (Climate Projection Data & Scenarios)

| Claim ID | Claim / Thesis Statement | Source Anchor | Status | Permitted Visual Treatment | Prohibited Visual Treatment |
|---|---|---|---|---|---|
| C01-01 | Climate projections represent model-derived estimates under plausible future socio-economic scenarios (SSPs), not deterministic weather forecasts. | SCI-02, IMG-01 | VERIFIED | Scenario pathway timeline / branching spectrum. | Weather forecast calendar icons, daily rain predictions. |
| C01-02 | Projections support decision-making under uncertainty for water, agriculture, disaster risk, infrastructure, and policy planning in Thailand. | WEB-02, IMG-01 | VERIFIED | Sector icon grid (water drop, crop, dam, policy shield). | Guaranteed damage statistics or specific unverified baht loss values. |
| C01-03 | CMIP6 Global Climate Models (GCMs) operate at coarse spatial resolution (~100 km grid), necessitating spatial downscaling for local Thailand application. | SCI-01, SCI-02 | VERIFIED | Scale contrast diagram (100 km coarse grid vs 5 km fine grid over Thailand map). | High-resolution local details directly inside GCM coarse grid boxes. |
| C01-04 | Decision interpretation requires evaluating model ensembles, scenario selection, time horizon, variable, and spatial scale together. | SCI-02, IMG-01 | VERIFIED | 5-element interpretation checklist / multi-layer stacked diagram. | Single-model single-scenario reliance callouts. |

---

## 2. Rollup 02 Claims (Downscaling & Product Family)

| Claim ID | Claim / Thesis Statement | Source Anchor | Status | Permitted Visual Treatment | Prohibited Visual Treatment |
|---|---|---|---|---|---|
| C02-01 | Statistical downscaling uses empirical/statistical relationships (e.g. Random Forest, bias correction) between GCM predictors and local weather station data. | SCI-02, IMG-02, IMG-03 | VERIFIED | High-speed data processing pipeline / mathematical bridge illustration. | Atmospheric physics/cloud dynamics illustration for statistical models. |
| C02-02 | Dynamical downscaling nests Regional Climate Models (RCMs like RegCM5 and WRF-Chem) within GCMs to simulate atmospheric physics and local topography effects. | SCI-01, SCI-02, IMG-02, IMG-03 | VERIFIED | Nested atmospheric grid box over complex terrain / elevation profile. | Statistical regression formula graphics applied to RCM physics. |
| C02-03 | **GridData Product**: Gridded downscaled climate variables ready for spatial risk modeling (NetCDF / CSV format). | WEB-01, IMG-04 | VERIFIED | GIS spatial raster grid preview / file format badges (`.nc`, `.csv`). | Actual download interface imitation presented as real screenshot without live validation. |
| C02-04 | **WRF-Chem Product**: High-resolution dynamical RCM output incorporating atmospheric chemistry, aerosols, and air quality dynamics. | WEB-01, SCI-01, IMG-02 | VERIFIED | Dual atmosphere-chemistry layer diagram / aerosol-climate interaction icon. | Pure weather-only icon without chemistry/aerosol distinction. |
| C02-05 | **RegCM5 Product**: High-resolution regional climate model outputs focusing on regional climate physics and extreme event dynamics. | WEB-01, SCI-01 | VERIFIED | Regional atmospheric circulation / extreme event physics visual block. | Misspelling product name (must use exact string `RegCM5`). |
| C02-06 | **Statistical Downscaling Product**: High-speed empirical downscaled dataset for rapid scenario evaluation across local stations. | WEB-01, IMG-02, IMG-03 | VERIFIED | Station-to-grid calibration flow / rapid scenario evaluation matrix. | Claiming statistical downscaling creates new physical atmospheric laws. |
| C02-07 | Specific grid resolution numbers (e.g., 5 km, 25 km) or temporal coverage bounds across products. | IMG-02, IMG-04 | PROVISIONAL / UNRESOLVED | Qualitative resolution comparison badge with `[PROVISIONAL]` note in layout source text. | Presenting sample resolution figures as universal platform constants. |

---

## 3. Visual Treatment Rules & Boundaries

1. **Comparison Tables**: Use structured side-by-side matrices for Statistical vs. Dynamical downscaling and the 4 Product family features.
2. **Infographic Metaphors**: Use flat vector iconography for scale translation (Global GCM 100km → Regional RCM 25km → Local Grid 5km).
3. **Text Rules**: All labels, figures, and parameters must remain fully editable text components.
4. **Prohibited Content**: No synthetic pseudo-data charts, unverified baht damage values, or mock UI screenshots presented as live portal interfaces.
