# Raw Extraction: ART04_ENSO_Precipitation_Northeast
- **Source**: 4-Influence of El Niño southern oscillation on precipitation variability in Northeast Thailand.pdf
- **Date Extracted**: 2026-06-23

```json
{
  "metadata": {
    "source_filename": "4-Influence of El Niño southern oscillation on precipitation variability in Northeast Thailand.pdf",
    "extracted_at": "2026-06-23T15:00:00+07:00",
    "notebook_id": "crdb-tor-5-5-climate-risk-arti"
  },
  "core_hypothesis": "The study investigates the influence and relationship between the El Niño Southern Oscillation (ENSO) and monthly precipitation anomalies (PPTA) in Northeast Thailand, exploring how the periodicity of ENSO impacts varies over time across different frequency bands.",
  "sections_outline": [
    "Abstract",
    "Specifications table",
    "Background",
    "Method details",
    "Method details -> Study area",
    "Method details -> Data acquisition",
    "Method details -> Data preprocessing",
    "Method details -> The Pearson correlation",
    "Method details -> Wavelet analysis",
    "Method validation",
    "Discussion",
    "Conclusion",
    "Limitations",
    "Ethics statements",
    "Declaration of competing interest",
    "Data availability",
    "Acknowledgments",
    "Funding",
    "References"
  ],
  "tables_and_figures": [
    {
      "id": "Table 1",
      "title": "Descriptive monthly PPT (mm) statistics in Northeast Thailand over 1993–2022.",
      "focus": "Descriptive statistics (minimum, maximum, mean, standard deviation) for precipitation across 27 meteorological stations over a 30-year period."
    },
    {
      "id": "Table 2",
      "title": "Pearson’s correlation between Niño indices and Monthly PPTA with time lag (0 – 12 months).",
      "focus": "Pearson correlation coefficients (r) and P-values demonstrating the delayed relationship between SSTA in Niño regions (1+2, 3, 3.4, 4) and monthly PPTA in Northeast Thailand over 0-12 month lags."
    },
    {
      "id": "Fig. 1",
      "title": "Southeast Asia and Northeast Thailand (study area).",
      "focus": "Geographical boundaries and province divisions of the Korat plateau region in Northeast Thailand."
    },
    {
      "id": "Fig. 2",
      "title": "Niño regions over the Pacific Ocean.",
      "focus": "Oceanic boundaries of the Niño 1+2, Niño 3, Niño 3.4, and Niño 4 regions in the equatorial Pacific Ocean."
    },
    {
      "id": "Fig. 3",
      "title": "Nino index over January 1993 to December 2022 (a) Niño 1 + 2, (b) Niño 3, (c) Niño 3.4 and (d) Niño 4.",
      "focus": "30-year historical time-series data identifying intensities, durations, and phases (El Niño, La Niña, Neutral) for the four indices."
    },
    {
      "id": "Fig. 4",
      "title": "Distribution of PPT for each month in Northeast Thailand over 1993–2022.",
      "focus": "Seasonal patterns, median values, and monthly precipitation variability across Northeast Thailand."
    },
    {
      "id": "Fig. 5",
      "title": "Annual PPTA (percentage) in Northeast Thailand over 1993–2022 (mean 1470.80 mm).",
      "focus": "30-year timeline of annual precipitation anomalies relative to the historical mean."
    },
    {
      "id": "Fig. 6",
      "title": "Pearson’s correlation between Niño index (a) Niño 1 + 2, (b) Niño 3, (c) Niño 3.4, (d) Niño 4 and PPTA of weak, medium, and strong for El Niño/La Niña.",
      "focus": "Correlation strengths stratified by the severity levels (weak, moderate, strong) of El Niño and La Niña events."
    },
    {
      "id": "Fig. 7",
      "title": "Wavelet coherence between Niño index (a) Niño 1 + 2, (b) Niño 3, (c) Niño 3.4, (d) Niño 4 and PPTA in Northeast Thailand.",
      "focus": "Time-frequency spectrum showing the periodicity and coherence between ENSO signals and precipitation anomalies over 0.25 to 8-year periods."
    },
    {
      "id": "Fig. 8",
      "title": "PPTA for each province in Northeast Thailand over El Niño years (a) 2015, (c) 2019 and La Niña years (b) 2017, (d) 2022.",
      "focus": "Spatial/provincial maps comparing precipitation anomaly distributions during representative El Niño (drought) and La Niña (wet) years."
    }
  ],
  "extracted_evidence": [
    {
      "evidence_id": "E01",
      "topic": "ENSO to Precipitation Anomalies Correlation",
      "description": "A general negative correlation exists between Sea Surface Temperature Anomalies (SSTA) in Niño regions and precipitation in Northeast Thailand. During El Niño, rainfall decreases, while during La Niña, rainfall increases. However, during strong La Niña events, Niño 1+2 displays a strong positive correlation, while Niño 3, 3.4, and 4 show moderate to strong negative correlations.",
      "metrics_mentioned": [
        "Strong La Niña correlations: 0.76 (positive) for Niño 1+2",
        "-0.64 for Niño 3",
        "-0.50 for Niño 3.4",
        "-0.65 for Niño 4"
      ],
      "citations": [
        "Step 2A - 1",
        "Step 2B - 2",
        "Fig. 6",
        "Fig. 8"
      ]
    },
    {
      "evidence_id": "E02",
      "topic": "ENSO-to-Rainfall Lag Propagation",
      "description": "The influence of ENSO on precipitation anomalies is delayed due to ocean-atmosphere waves, with negative correlations peaking at a 4 to 5-month delay.",
      "metrics_mentioned": [
        "Peak delay: 5-month lag for Niño 1+2 (r = -0.09, P = 0.09) and Niño 3 (r = -0.14, P = 0.01)",
        "Peak delay: 4-month lag for Niño 3.4 (r = -0.14, P = 0.01) and Niño 4 (r = -0.16, P = 0.00)",
        "Lag 0 correlation: Niño 1+2 (r = -0.08, P = 0.15), Niño 3 (r = -0.05, P = 0.31), Niño 3.4 (r = -0.11, P = 0.04), Niño 4 (r = -0.08, P = 0.13)"
      ],
      "citations": [
        "Step 2A - 2",
        "Step 2B - 2",
        "Table 2"
      ]
    },
    {
      "evidence_id": "E03",
      "topic": "Asymmetrical Impact of La Niña versus El Niño",
      "description": "La Niña events show a significantly more pronounced impact on precipitation patterns in Northeast Thailand than El Niño. Strong La Niña phases correspond to high correlations, while all severities of El Niño and weaker La Niña phases show only low-to-moderate correlation strengths.",
      "metrics_mentioned": [
        "La Niña correlations: 0.76 (positive) for Niño 1+2",
        "-0.64, -0.50, and -0.65 (negative) for Niño 3, 3.4, and 4",
        "El Niño and weak/moderate La Niña: Low-to-moderate correlations"
      ],
      "citations": [
        "Step 2A - 3",
        "Step 2B - 2",
        "Fig. 6"
      ]
    },
    {
      "evidence_id": "E04",
      "topic": "Time-Frequency Coherence Periodicity",
      "description": "Wavelet transform coherence (WTC) shows strong coherence between ENSO signals and precipitation anomalies at 2-7 year cycles, corresponding to natural ENSO periods. Additionally, short-term coherence of 0.5-1 year is detected, indicating modulation of semi-annual and annual seasonal cycles.",
      "metrics_mentioned": [
        "Wavelet range: 0.25 to 8 years",
        "Niño 1+2 coherence: 1.5 to 4 years (1993-1998, 2008-2018) and 0.5 years (2003-2008)",
        "Niño 3 and 3.4 coherence: 2 to 4 years, 4 to 7 years (1993-2003) and 0.5 to 1 year (2003-2013)",
        "Niño 4 coherence: 2 to 4 years (1998-2000)"
      ],
      "citations": [
        "Step 2A - 4",
        "Step 2B - 4",
        "Fig. 7"
      ]
    },
    {
      "evidence_id": "E05",
      "topic": "Baseline Rainfall and Extreme Anomalies",
      "description": "The study defines the baseline monthly and annual precipitation stats and highlights extreme rainfall deviations in Northeast Thailand over the 30-year period.",
      "metrics_mentioned": [
        "Historical mean annual rainfall: 1470.80 mm",
        "Annual rainfall range: 1100 mm to 1900 mm",
        "Highest rainfall: 1972.8 mm in 2017 (+34.13% / +502.0 mm anomaly during strong La Niña)",
        "Lowest rainfall: 1112.3 mm in 1993 (-24.38% anomaly during El Niño)",
        "Station monthly mean range: 91.3 mm to 194.3 mm",
        "Station SD range: 88.5 mm to 226.8 mm",
        "Station maximum monthly peaks: 419.2 mm to 1141.5 mm"
      ],
      "citations": [
        "Step 2B - 1",
        "Step 2B - 3",
        "Table 1",
        "Fig. 4",
        "Fig. 5"
      ]
    }
  ],
  "limitations_and_uncertainties": [
    {
      "issue": "Meteorological data from the 27 stations has inherent limitations in coverage, accuracy, and consistency across the 30-year study timeline.",
      "citation": "Step 3A - 1, Limitations"
    },
    {
      "issue": "Research timeframe is restricted to 1993-2022 due to limited availability of long-term climate variables data.",
      "citation": "Step 3A - 1, Limitations"
    },
    {
      "issue": "Geographical focus is limited strictly to Northeast Thailand (Isan/Korat plateau), meaning findings cannot be directly extrapolated to other regions of the country.",
      "citation": "Step 3A - 1, Study area"
    },
    {
      "issue": "Raw precipitation data contained missing values and errors, requiring the use of Multiple Linear Regression (MLR) to estimate and impute missing records from nearby stations.",
      "citation": "Step 3A - 1, Data preprocessing"
    },
    {
      "issue": "The Wavelet analysis requires Monte Carlo simulation to check significance against background noise, and is statistically bounded by the Cone of Influence (COI) boundary at a 95% level.",
      "citation": "Step 3A - 2, Wavelet analysis"
    }
  ]
}
```
