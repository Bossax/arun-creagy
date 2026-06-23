# Raw Extraction: ART02_ChaoPhraya_Rice_Adaptation
- **Source**: 2-Exploring the impacts of climate change and identifying potential adaptation strategies for sustainable rice production in Thailand
- **Date Extracted**: 2026-06-23

```json
{
  "metadata": {
    "source_filename": "2-Exploring the impacts of climate change and identifying potential adaptation strategies for sustainable rice production in Thailand",
    "extracted_at": "2026-06-23T06:53:22Z",
    "notebook_id": "crdb-tor-5-5-climate-risk-arti"
  },
  "core_hypothesis": "Tailored genotype- and management-based adaptation strategies can mitigate future climate change impacts on rice yield and irrigation water demand in Thailand's lower Chao Phraya River Basin.",
  "sections_outline": [
    "Abstract",
    "Introduction",
    "Materials and methods",
    "Field experiments and crop management for model evaluation",
    "DSSAT-CSM-CERES-Rice model",
    "Data collection",
    "Weather data",
    "Global climate model for future climate change projection",
    "Model calibration and evaluation",
    "Climate change adaptation strategies",
    "Climate change management practices for adaptations",
    "Virtual cultivars adaptations",
    "Results and discussion",
    "Impacts of future climate change on rice yield",
    "Impacts of changed management practices on predicted rice yield and irrigation water use",
    "Impact of simulated virtual cultivar on future rice yield and irrigation water use",
    "Conclusions",
    "Acknowledgements",
    "Author contribution",
    "Data availability",
    "Declarations",
    "Ethical approval",
    "Consent to participate",
    "Consent for publication",
    "Competing interests",
    "References"
  ],
  "tables_and_figures": [
    {
      "id": "Table 1",
      "title": "The observed datasets from the field experiments used for model calibration and evaluation",
      "focus": "Experimental management parameters used to calibrate and evaluate the crop model, including planting, fertilizer, and irrigation conditions."
    },
    {
      "id": "Table 2",
      "title": "Mechanical analysis and nutrient composition of the soil from the field experiment",
      "focus": "Baseline soil properties used as model inputs."
    },
    {
      "id": "Table 3",
      "title": "The five selected GCM from NEX-GDDP-CMIP6 datasets",
      "focus": "Global climate models selected to drive the future climate projections."
    },
    {
      "id": "Table 4",
      "title": "The selected adaptation strategies of the present study",
      "focus": "Management practices and virtual cultivar scenarios tested under future climate conditions."
    },
    {
      "id": "Table 5",
      "title": "The changes in weather variables under SSP126, SSP245, and SSP585 climate change scenarios in three future climatic periods...",
      "focus": "Projected changes in rainfall, solar radiation, and temperature across future periods and emissions scenarios."
    },
    {
      "id": "Table 6",
      "title": "Genotype parameters of DSSAT-CERES-Rice model adjusted during calibration and evaluation",
      "focus": "Default and calibrated genetic coefficients used in DSSAT model calibration."
    },
    {
      "id": "Table 7",
      "title": "Yield, anthesis (DAS), and maturity (DAS) of observed data and DSSAT simulation data during calibration and evaluation",
      "focus": "Observed versus simulated crop performance metrics used to evaluate model fit."
    },
    {
      "id": "Table 8",
      "title": "Model performance statistics for rice yield simulation",
      "focus": "Statistical performance metrics used to validate simulated rice yield."
    },
    {
      "id": "Table 9",
      "title": "The baseline simulation results for rice yield (kg ha-1) under SSP126, SSP245, and SSP585 climate change scenarios...",
      "focus": "Projected baseline rice yields under future climate scenarios without adaptation."
    },
    {
      "id": "Table 10",
      "title": "The baseline simulation results for irrigation water used (mm) under SSP126, SSP245, and SSP585 climate change scenarios...",
      "focus": "Projected baseline irrigation water requirements under future climate scenarios without adaptation."
    },
    {
      "id": "Table 11",
      "title": "The simulation results for changes in rice yield (%) due to changes in management strategies...",
      "focus": "Yield response to planting date, fertilizer timing/dose, and irrigation threshold adjustments."
    },
    {
      "id": "Table 12",
      "title": "The simulation results for changes in irrigation water use (%) due to changes in management strategies...",
      "focus": "Irrigation water response to planting date, fertilizer timing/dose, and irrigation threshold adjustments."
    },
    {
      "id": "Table 13",
      "title": "The simulation results for changes in rice yield (%) due to consideration of virtual cultivars...",
      "focus": "Yield response to hypothetical genetic crop traits."
    },
    {
      "id": "Table 14",
      "title": "The simulation results for changes in irrigation water use (%) due to consideration of virtual cultivars...",
      "focus": "Irrigation water response to hypothetical genetic crop traits."
    },
    {
      "id": "Figure 1",
      "title": "Study area, the lower Chao Phraya basin with AIT weather station",
      "focus": "Geographic and meteorological context of the study area."
    },
    {
      "id": "Figure 2",
      "title": "The pattern of average monthly rainfall (a), average monthly solar radiation (b), average monthly minimum temperature (c), and average monthly maximum temperature (d)...",
      "focus": "Seasonal patterns of projected climate variables across scenarios and time periods."
    },
    {
      "id": "Figure 3",
      "title": "The trend of average annual rainfall (a), average annual solar radiation (b), average annual minimum temperature (c), and average annual maximum temperature (d)...",
      "focus": "Long-term annual climate trajectories through the end of the century."
    },
    {
      "id": "Figure 4",
      "title": "Bar chart showing the comparison of measured and simulated rice yield during (a) model calibration and (b) model evaluation",
      "focus": "Visual comparison of observed and simulated yield for model validation."
    }
  ],
  "extracted_evidence": [
    {
      "evidence_id": "E01",
      "topic": "Study scope and analytical frame",
      "description": "The article evaluates future climate impacts on rice production and irrigation water use in the lower Chao Phraya River Basin using DSSAT-CERES-Rice and climate scenario projections.",
      "metrics_mentioned": ["SSP126", "SSP245", "SSP585", "early-century", "mid-century", "late-century"],
      "citations": ["Abstract", "Introduction", "Results and discussion"]
    },
    {
      "evidence_id": "E02",
      "topic": "Model calibration and evaluation coverage",
      "description": "The atomic outputs show a calibration workflow that compares observed and simulated rice yield, anthesis, and maturity using DSSAT genetic coefficients and standard performance metrics.",
      "metrics_mentioned": ["P1", "P2R", "P5", "P2O", "G1", "G2", "G3", "THOT", "TCLDP", "TCLDF", "d-index", "r2", "%RMSE", "PE"],
      "citations": ["Model calibration and evaluation", "Table 6", "Table 7", "Table 8", "Figure 4"]
    },
    {
      "evidence_id": "E03",
      "topic": "Climate variables tracked for future change",
      "description": "Future climate projections are framed around temperature, rainfall/precipitation, solar radiation, and related weather variables that influence rice growth and water demand.",
      "metrics_mentioned": ["Tmax", "Tmin", "Pr", "Rs"],
      "citations": ["Introduction", "Data collection", "Table 5", "Figure 2", "Figure 3"]
    },
    {
      "evidence_id": "E04",
      "topic": "Management adaptation scenarios",
      "description": "The paper tests management-based adaptation by changing planting dates, fertilizer timing/dose, and irrigation water thresholds.",
      "metrics_mentioned": ["planting date", "fertilizer application date", "fertilizer application dose", "irrigation water threshold"],
      "citations": ["Climate change adaptation strategies", "Table 4", "Table 11", "Table 12"]
    },
    {
      "evidence_id": "E05",
      "topic": "Virtual cultivar adaptation scenarios",
      "description": "The paper also evaluates hypothetical cultivar traits intended to improve tolerance or productivity under climate stress.",
      "metrics_mentioned": ["THOT", "RWUMX", "P1", "G1", "P5"],
      "citations": ["Virtual cultivars adaptations", "Table 4", "Table 13", "Table 14"]
    },
    {
      "evidence_id": "E06",
      "topic": "Study-area and crop-system specificity",
      "description": "The extracted outputs identify a dry-season rice system centered on the RD57 cultivar and compare management types such as direct seeding, transplanting, continuous flooding, and alternate wetting and drying.",
      "metrics_mentioned": ["RD57", "DDS", "WDS", "TP", "CF", "AWD15", "AWD30"],
      "citations": ["Named Study Areas, Crop Systems, Scenarios, and Adaptation Strategy Labels", "Figure 1"]
    }
  ],
  "limitations_and_uncertainties": []
}
```
