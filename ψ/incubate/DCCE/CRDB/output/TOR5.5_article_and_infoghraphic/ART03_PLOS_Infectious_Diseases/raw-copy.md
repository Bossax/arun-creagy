# Step 1A

Here is the section outline for the source titled "Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand":

- **Author summary**
- **Introduction**
- **Methods**
    - Disease case data
    - Historical meteorological data
    - Demographic data
    - Future projection and estimation of excess risk due to extreme weather scenarios
- **Association of diseases with extreme weather**
- **Overall change in disease risk during periods of extreme weather**
- **Trends of dengue excess risk during extreme weather in SSP245**
- **Trends of influenza excess risk during extreme weather in SSP245**
- **Sensitivity analysis**
- **Discussion**
- **References**

# Step 1B

**Methods**

- **Disease case data:** Monthly disease case counts (Japanese encephalitis virus (JEV), malaria, dengue, pneumonia, influenza, leptospirosis, and melioidosis).
- **Historical meteorological data:** Air temperature at 2m, dewpoint temperature, total precipitation, daily minimum and maximum temperature, daily total precipitation.
- **Demographic data:** Population size, annual population projections.
- **Extreme weather events:** Daily maximum temperature, Standardised Precipitation Index-1 (SPI).
- **Meteorological data under climate change scenarios:** Projected monthly minimum temperature, maximum temperature, total precipitation, monthly number of wet days, daily precipitation, daily maximum and daily minimum temperature, monthly number of extreme heat days.
- **Climate change scenarios:** Radiative forcing by 2100 (W/m2).
- **Statistical model:** Case count of disease ($y_{t,d,l}$), province population ($P_{a[t], l}$), SPI ($x_{1,t-k}$), number of extreme heat days in a month ($x_{2,t-j}$), calendar month ($m[t]$), population density ($x_{3,a[t], l}$), contemporaneous relative humidity ($z_{t,l}$).
- **Estimation of incidence rate ratio and population attributable fraction:** Incidence rate ratio (IRR), population attributable fraction (PAF), estimated incidence rate of the disease ($\hat{y}_{d,l}$).
- **Future projection and estimation of excess risk due to extreme weather scenarios:** Estimated incidence rate ($\hat{y}_{proj,d,m,t,l,s}$), fitted historical incidence ($y_{hist,d,m,l}$), province excess risk (Province $ER_{d,t,l,s,q}$), annual national-level ER.
- **Model evaluation:** Akaike information criterion (AIC), root mean squared error (RMSE).

**Results**

- **Future climate change scenarios:** Monthly SPI, monthly extreme heat days.
- **Association of diseases with extreme weather:** Incidence rate ratios (IRR), population attributable fractions (PAF).
- **Overall change in disease risk during periods of extreme weather:** Excess risk.
- **Change in disease risk by individual extreme weather events:** Excess risk, relative humidity.
- **Trends of dengue excess risk during extreme weather in SSP245:** Province-level changes in incidence rate/excess risks.
- **Trends of influenza excess risk during extreme weather in SSP245:** Province-level excess risks.
- **Model evaluation:** Akaike information criterion (AIC).

**Sensitivity analysis**

- Excess risks.

# Step 1C

Extract only the tables for the exact title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand". If the title is missing or ambiguous, stop and report that explicitly. Do not summarize or harmonize.

For the exact title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand", the provided source text does not contain any actual tabular data. It only contains the following table captions and in-text references:

- **Table 1**: Mentions the Shared Socioeconomic Pathway (SSP) framework (SSP126, SSP245, SSP370 and SSP585 scenarios).
- **S1 Table. Overdispersion test.** Cameron and Trivedi test was done on the case counts of each disease respectively to check if the data was overdispersed. Overdispersed data warrants the use of the negative binomial distribution to count data.
- **S2 Table. Model selection criteria.** Disease-specific generalized additive models were trained taking lagged extreme heat days, lagged standardized precipitation index (SPI), relative humidity and population density as variables. Thin plate splines were used to model non-linear relationships between lagged extreme heat days, lagged SPI and monthly disease case counts. Models including different number of lags were assessed and compared based on the Akaike information criterion (AIC), with lower values indicating better model fit to observations while penalizing for model complexity. The number of variable lags selected for models of each disease are bolded and underlined.
- **S3 Table. AIC of the GAM and GLM models for each disease.** Disease-specific generalized additive models (GAM) and generalised linear models (GLM) were trained with relative humidity, lagged extreme heat days, lagged standardized precipitation index (SPI) and population density as variables. The Akaike information criterion (AIC) of each model was calculated to compare model fit of GLM against GAM.
- **S4 Table. AIC of each model with and without relative humidity as a predictor.** Disease-specific generalized additive models (GAM) were trained with and without relative humidity (RH) respectively, together with lagged extreme heat days, lagged standardized precipitation index (SPI) and population density as variables. The lags chosen for extreme heat days and SPI are indicated in Supplementary Table S2. Thin plate splines were used to model non-linear relationships between lagged extreme heat days, lagged SPI and monthly disease case counts. The Akaike information criterion (AIC) of each model was calculated to compare model fit with inclusion of relative humidity as a predictor. AIC is used to assess model fit as it balances goodness of fit with model complexity. Lower AIC values which indicated better model fit are bolded.
- **S6 Table. Annual national projected excess risk of each disease attributable to overall extreme weather, extreme heat, extreme dry and extreme wet weather across time periods and climate change scenarios.** Disease-specific generalized additive models (GAM) were trained on historical data from 2003-2019 and used to project future case counts of the respective disease across 4 time periods (2021–2040, 2041–2060, 2061–2080, 2081–2100) and 4 climate change scenarios (SSP126, SSP245, SSP370, SSP585) during periods of extreme weather. National-level excess risk was calculated using the mean disease case counts across the historical period and the projected case counts at a respective time period and climate change scenario. Excess risk represents the percentage change in disease cases compared to historical levels. Values in asterisk are statistically significant.

# Step 1D

Extract only the figures for the exact title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand". If the title is missing or ambiguous, stop and report that explicitly. Do not summarize or harmonize.

Here are the figures extracted from the source titled "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand":

**Main Figures**

- **Fig 1.** Historical and projected monthly SPI and extreme heat days. (A) Monthly SPI and (B) monthly extreme heat days from 2003 to 2021 and during the periods 2021–2040, 2041–2060, 2061–2080, 2081–2100 with climate change scenarios SSP126, SSP245, SSP370 and SSP585 in Thailand. Climate projections are based on the MIROC6 GCM.
- **Fig 2.** National level incidence rate ratio (IRR) and population attributable fraction (PAF) over days of extreme heat and standardised precipitation index (SPI) for dengue, JEV, influenza, malaria, pneumonia, leptospirosis and melioidosis. Bars represent 95% confidence intervals and red bars represent statistically significant points.
- **Fig 3.** Excess risk of pneumonia, influenza, JEV, malaria, dengue, melioidosis and leptospirosis during periods of extreme weather, across 2021 to 2100, in climate change scenarios SSP126, SSP245, SSP370 and SSP585. Excess risk represents the percentage change in annual disease case counts from the historical baseline from 2003 to 2020.
- **Fig 4.** Excess risk (ER) of JEV, malaria and dengue during periods of extreme heat, extreme dry weather and extreme wet weather, across 2021 to 2100, in climate change scenarios SSP126, SSP245, SSP370 and SSP585. Excess risk represents the percentage change in annual disease case counts from the historical baseline from 2003 to 2020.
- **Fig 5.** Excess risk (ER) of influenza, pneumonia, leptospirosis and melioidosis during periods of extreme heat, extreme dry weather and extreme wet weather, across 2021 to 2100, in climate change scenarios SSP126, SSP245, SSP370 and SSP585. Excess risk represents the percentage change in annual disease case counts from the historical baseline from 2003 to 2020.
- **Fig 6.** (A) Excess risk of the five provinces with the historically highest incidence of dengue during periods of extreme weather, under SSP245 from 2021–2100. (B) Province-level excess risks of dengue under SSP245 from 2021–2100. Asterisks indicate a statistically significant excess risk value. Excess risk represents the percentage change in annual disease case counts from the historical baseline from 2003 to 2020.
- **Fig 7.** (A) Excess risk of the five provinces with the historically highest incidence of influenza during periods of extreme weather, under SSP245 from 2021–2100. (B) Province-level excess risks of influenza under SSP245 from 2021–2100. Asterisks indicate a statistically significant excess risk value. Excess risk represents the percentage change in annual disease case counts from the historical baseline from 2003 to 2020.

**Supplementary Figures**

- **S1 Fig.** Days of extreme heat and SPI across climate change scenarios by province under the MIROC6 general circulation model.
- **S2 Fig.** Days of extreme heat and SPI across climate change scenarios by province under the IPSL-CM6A-LR general circulation model.
- **S4 Fig.** Incidence rate ratio of dengue over days of extreme heat (EH) for each province.
- **S5 Fig.** Incidence rate ratio of Japanese encephalitis virus over days of extreme heat (EH) for each province.
- **S6 Fig.** Incidence rate ratio of influenza over days of extreme heat (EH) for each province.
- **S7 Fig.** Incidence rate ratio of leptospirosis over days of extreme heat (EH) for each province.
- **S8 Fig.** Incidence rate ratio of malaria over days of extreme heat (EH) for each province.
- **S9 Fig.** Incidence rate ratio of melioidosis over days of extreme heat (EH) for each province.
- **S10 Fig.** Incidence rate ratio of pneumonia over days of extreme heat (EH) for each province.
- **S11 Fig.** Incidence rate ratio of dengue over days of SPI for each province.
- **S12 Fig.** Incidence rate ratio of Japanese encephalitis virus over days of SPI for each province.
- **S14 Fig.** Incidence rate ratio of leptospirosis over days of SPI for each province.
- **S15 Fig.** Incidence rate ratio of malaria over days of SPI for each province.
- **S16 Fig.** Incidence rate ratio of melioidosis over days of SPI for each province.
- **S17 Fig.** Incidence rate ratio of pneumonia over days of SPI for each province.
- **S18 Fig.** Population attributable fraction of dengue over days of SPI and extreme heat for each province.
- **S19 Fig.** Population attributable fraction of Japanese encephalitis virus over days of SPI and extreme heat for each province.
- **S20 Fig.** Population attributable fraction of influenza over days of SPI and extreme heat for each province.
- **S21 Fig.** Population attributable fraction of leptospirosis over days of SPI and extreme heat for each province.
- **S22 Fig.** Population attributable fraction of malaria over days of SPI and extreme heat for each province.
- **S23 Fig.** Population attributable fraction of melioidosis over days of SPI and extreme heat for each province.
- **S24 Fig.** Population attributable fraction of pneumonia over days of SPI and extreme heat for each province.
- **S25 Fig.** Lag–response curves showing the relative risk of seven infectious diseases (dengue, JEV, influenza, pneumonia, leptospirosis, melioidosis, and malaria) per 1-unit increase in standardized precipitation index (SPI) and extreme heat.
- **S26 Fig.** Projected excess risk of diseases in extreme heat when relative humidity is held constant.
- **S27 Fig.** Incidence rate ratio of diseases across different levels of relative humidity.
- **S28 Fig.** Province-level excess risk of dengue attributable to extreme weather across time and climate change scenarios.
- **S29 Fig.** Province-level excess risk of Japanese Encephalitis attributable to extreme weather across time and climate change scenarios.
- **S30 Fig.** Province-level excess risk of Japanese Encephalitis attributable to extreme weather across time and climate change scenarios.
- **S31 Fig.** Province-level excess risk of leptospirosis attributable to extreme weather across time and climate change scenarios.
- **S32 Fig.** Province-level excess risk of malaria attributable to extreme weather across time and climate change scenarios.
- **S33 Fig.** Province-level excess risk of melioidosis attributable to extreme weather across time and climate change scenarios.
- **S34 Fig.** Province-level excess risk of pneumonia attributable to extreme weather across time and climate change scenarios.
- **S35 Fig.** Province-level distribution of extreme heat and excess risks of dengue under SSP245.
- **S36 Fig.** Province-level distribution of extreme heat and excess risks of influenza under SSP245.
- **S37 Fig.** Excess risk of dengue attributable to extreme weather taking into account future population.
- **S38 Fig.** Excess risk of Japanese encephalitis attributable to extreme weather taking into account future population.
- **S39 Fig.** Excess risk of influenza attributable to extreme weather taking into account future population.
- **S40 Fig.** Excess risk of leptospirosis attributable to extreme weather taking into account future population.
- **S41 Fig.** Excess risk of malaria attributable to extreme weather taking into account future population.
- **S42 Fig.** Excess risk of melioidosis attributable to extreme weather taking into account future population.
- **S43 Fig.** Excess risk of pneumonia attributable to extreme weather taking into account future population.
- **S44 Fig.** Excess risk of pneumonia, influenza, JEV, malaria, dengue, melioidosis and leptospirosis during periods of extreme weather, across 2021–2100, in climate change scenarios SSP126, SSP245, SSP370 and SSP585 using CMCC-ESM2 climate change model.
- **S45 Fig.** Excess risk of pneumonia, influenza, JEV, malaria, dengue, melioidosis and leptospirosis during periods of extreme weather, across 2021–2100, in climate change scenarios SSP126, SSP245, SSP370 and SSP585 using IPSL-CM6A-LR climate change model.
- **S46 Fig.** Excess risk of pneumonia, influenza, JEV, malaria, dengue, melioidosis and leptospirosis during periods of extreme weather, across 2021–2100, in climate change scenarios SSP126, SSP245, SSP370 and SSP585 using multi-model ensemble climate change model.
- **S47 Fig.** Excess risk (ER) of JEV, malaria and dengue during periods of extreme heat, extreme dry weather and extreme wet weather, across 2021–2100, in climate change scenarios SSP126, SSP245, SSP370 and SSP585 using CMCC-ESM2 climate change model.
- **S48 Fig.** Excess risk (ER) of JEV, malaria and dengue during periods of extreme heat, extreme dry weather and extreme wet weather, across 2021–2100, in climate change scenarios SSP126, SSP245, SSP370 and SSP585 using IPSL-CM6A-LR climate change model.
- **S49 Fig.** Excess risk (ER) of influenza, pneumonia, leptospirosis and melioidosis during periods of extreme heat, extreme dry weather and extreme wet weather, across 2021–2100, in climate change scenarios SSP126, SSP245, SSP370 and SSP585 using CMCC-ESM2 climate change model.
- **S50 Fig.** Excess risk (ER) of influenza, pneumonia, leptospirosis and melioidosis during periods of extreme heat, extreme dry weather and extreme wet weather, across 2021–2100, in climate change scenarios SSP126, SSP245, SSP370 and SSP585 using IPSL-CM6A-LR climate change model.
- **S51 Fig.** Excess risk of diseases attributable to extreme heat sub-scenarios.
- **S52 Fig.** Excess risk of diseases attributable to extreme dry weather sub-scenarios.
- **S53 Fig.** Excess risk of diseases attributable to extreme wet weather sub-scenarios.


# Step 1E

Extract only the core hypothesis plus named study areas, diseases, scenarios, and exposure-event labels for the exact title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand". If the title is missing or ambiguous, stop and report that explicitly. Do not summarize or harmonize.

 Here is the extracted information for the exact title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand":

**Core Hypothesis**

- Climate change is postulated to impact infectious disease transmission, as extreme weather events (such as heatwaves and droughts) are expected to rise in frequency, duration, and intensity, and consequentially impact the risk and burdens of infectious diseases.

**Named Study Areas**

- Thailand
- 77 provinces
- Northern Thailand
- Central Thailand
- Southern Thailand
- Northeastern Thailand
- Eastern Thailand
- Bangkok
- Nakhon Ratchasima
- Ubon Ratchathani
- Chiang Mai
- Chiang Rai
- Nong Khai
- Bueng Khan
- Ratchaburi
- Si Sa Ket
- Buri Ram

**Diseases**

- Japanese encephalitis virus (JEV)
- Malaria
- Dengue
- Pneumonia
- Influenza
- Leptospirosis
- Melioidosis

**Scenarios**

- **Climate Change Scenarios / Shared Socioeconomic Pathways (SSP):** SSP126, SSP245, SSP370, SSP585.
- **Climate Models:** MIROC6, CMCC-ESM2, and IPSL-CM6A-LR.
- **Extreme Weather Sub-scenarios:** Extreme heat and no extreme dry weather; extreme heat and no extreme wet weather; extreme heat with no extreme dry and no extreme wet weather; extreme wet weather and no extreme heat; and extreme dry weather and no extreme heat.

**Exposure-Event Labels**

- Extreme heat (or extreme heat days)
- Extreme dry weather (or SPI $\le$ -1.5)
- Extreme wet weather (or SPI $\ge$ 1.5)

# Step 2A

Extract only the paper's actual risk relationships, disease categories, exposure variables, temporal/scenario structure, and key qualitative findings for the exact title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand". If the title is missing or ambiguous, stop and report that explicitly. Do not summarize or harmonize.

Here is the extracted information from the exact source title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand":

**Risk Relationships**

- **Extreme heat:** Positively associated with the risks of dengue, Japanese encephalitis virus (JEV), influenza, pneumonia, and melioidosis. Negatively associated with the risks of malaria and leptospirosis.
- **Extreme wet weather (SPI $\ge$ 1.5):** Historically associated with a lower incidence of dengue, pneumonia, and influenza. Historically associated with a higher incidence of JEV, pneumonia, and melioidosis.
- **Extreme dry weather (SPI $\le$ -1.5):** Historically associated with a higher incidence of JEV, and lower incidence of dengue and pneumonia. Also historically associated with increased influenza and malaria risks.
- **Relative humidity:** Lower levels of relative humidity were historically associated with reduced dengue risk.

**Disease Categories**

- **Vector-borne diseases:** Dengue, malaria, and Japanese encephalitis virus (JEV).
- **Air-borne diseases / Respiratory:** Pneumonia and influenza.
- **Water-borne / Food-borne / Animal-borne diseases:** Leptospirosis and melioidosis.

**Exposure Variables**

- **Number of extreme heat days:** Defined as daily maximum temperatures above a threshold of 34.9°C (the 90th percentile of national daily maximum temperature) for at least 3 consecutive days.
- **Standardised Precipitation Index-1 (SPI):** Measures precipitation anomalies, where an SPI lower than -1.5 characterizes extreme dry weather and an SPI higher than 1.5 characterizes extreme wet weather.
- **Contemporaneous relative humidity**.
- **Population density**.

**Temporal/Scenario Structure**

- **Historical baseline:** Surveillance and climate data spanning 2003 to 2019 (with some indices utilizing 2003–2020 or 2003-2021).
- **Future projection time periods:** 20-year intervals covering 2021–2040, 2041–2060, 2061–2080, and 2081–2100.
- **Climate change scenarios:** Shared Socioeconomic Pathways (SSP) frameworks including SSP126, SSP245, SSP370, and SSP585.
- **Climate models:** Projections derived from three general circulation models (GCMs): MIROC6, CMCC-ESM2, and IPSL-CM6A-LR.

**Key Qualitative Findings**

- Historically, extreme heat was associated with an increase in all infectious disease incidences, with the exceptions of malaria and leptospirosis.
- Dengue risk is projected to decline in most future climate change scenarios, except under the moderate SSP245 scenario where extreme heat drives a significant rise in Northern and Central Thailand from 2021 to 2060.
- Nationwide dengue risk is expected to decrease substantially by 24.9% during future periods of extreme weather from 2061–2080 compared to historical baselines, largely driven by lower relative humidity.
- Influenza risk is expected to increase under SSP245 in 2021–2060 influenced by heat and dry weather in the Northeastern and Central regions, before subsequently decreasing with heavier rainfall.
- Pneumonia and melioidosis risks are expected to increase in the future during periods of extreme weather, particularly under the highest carbon emission scenario, SSP585.
- Malaria risk is expected to increase during periods of extreme weather across all climate change scenarios and time periods, with the exception of the 2021–2040 and 2081–2100 periods under SSP245.
- JEV risk is projected to decrease from 2061–2080 across all climate change scenarios except SSP585.
- Leptospirosis risk is expected to decline during periods of extreme weather across all time periods and climate change scenarios.
- Projected changes in disease risk exhibit significant heterogeneity across provinces, highlighting a critical need to integrate localized public health interventions and climate resilience planning to manage escalating extreme weather events.

# Step 2B

Extract only missing major findings or trends not covered by the prior query for the exact title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand". If the title is missing or ambiguous, stop and report that explicitly. Do not summarize or harmonize.

**Quantitative Findings and Specific Risk Trends**

- Nationwide dengue risk is expected to decrease by 24.9% (95% CI: 9.68%, 40.0%) during future periods of extreme weather from 2061–2080 compared to historical baselines.
- Influenza risk in Nakhon Ratchasima is expected to increase by 36.8% (95% CI: 9.83%, 63.8%) in 2021–2040 under the SSP245 scenario.
- At SPI levels of 3 (extreme wet weather), the historical dengue incidence rate ratio (IRR) was 0.66 (95% CI: 0.62, 0.69), while the JEV IRR was 1.29 (95% CI: 1.19, 1.40).
- At SPI levels of -3 (extreme dry weather), the historical dengue IRR was 0.88 (95% CI: 0.83, 0.92), while the JEV IRR was 1.21 (95% CI: 1.12, 1.30).
- During periods of extreme heat under SSP245, a large increase of 26.2% (95% CI: 0.90%, 51.7%) in dengue risk is expected from 2021–2040.
- The expected decrease in dengue risk during extreme dry weather ranges from -52.1% (95% CI: -63.2%, -41.0%) in 2081–2100 under SSP370 to -25.4% (95% CI: -41.0%, -9.77%) in 2021–2040 under SSP245.
- Dengue risk during extreme wet weather is expected to decrease the most by 52.9% (95% CI: 43.0%, 62.8%) in 2041–2060 under SSP370 and decrease the least by 35.0% (95% CI: 21.1%, 48.7%) in 2021–2040 under SSP245.
- From 2021–2040 under SSP245, provinces with historically high dengue incidence such as Bangkok are expected to experience an increased risk of 42.2% (95% CI: 13.6%, 70.7%) during periods of extreme weather, while other provinces like Chiang Mai are expected to see a decrease of 24.6% (95% CI: -40.1%, -9.00%).
- From 2061–2080 under SSP245, a notable decrease in dengue risk during periods of extreme weather is expected in Chiang Rai (ER: -34.2%, 95% CI: -47.2%, -21.1%).

**Regional Climate Divergence Trends**

- Northern Thailand is projected to experience more extreme dry weather than the rest of Thailand, while Central and Eastern Thailand are projected to experience more extreme heat.

**Statistical and Model Evaluation Findings**

- The Akaike information criterion (AIC) of each Generalised Additive Model (GAM) was lower than its corresponding Generalised Linear Model (GLM) for all 7 diseases, indicating that the incorporation of smooth functions to model predictors improved the model fit.
- The inclusion of relative humidity as a predictor improved the fit of all 7 models, as evidenced by lower AIC values compared to models without relative humidity.
- Excess risks attributable to extreme heat resembled the excess risks attributable to extreme heat with no extreme dry or wet weather, indicating that the estimated excess risks were not confounded by other concurrent extreme weather conditions.
- Predictions using future population as an offset and future population density as a predictor were heavily skewed by future population projections because models were unable to handle population projections that exceed current observations, validating the methodological choice to hold populations at historical mean values to isolate extreme weather impacts.

# Step 3A

Extract only limitations, uncertainties, model parameters, source data gaps, and author warnings for the exact title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand". If the title is missing or ambiguous, stop and report that explicitly. Do not summarize or harmonize.

Here is the extracted information regarding limitations, uncertainties, model parameters, source data gaps, and author warnings from the exact title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand":

**Model Parameters**

- **Model Type:** Generalised additive models (GAMs) with a negative binomial distribution.
- **Covariates:** Lagged monthly Standardised Precipitation Index (SPI), lagged number of monthly extreme heat days, population density, and contemporaneous relative humidity.
- **Offset:** The logarithm of the province population at year $a[t]$ was used as an offset for the at-risk population.
- **Splines:** Thin-plate splines with a basis dimension of 10 were used to model non-linear relationships.
- **Spatial Effects:** Spatial random effects ($\gamma_l$) were used for each province to account for differences in transmission dynamics across provinces.
- **Estimation Method:** Restricted maximum likelihood (REML) was used to estimate the splines.
- **Extreme Heat Threshold:** Defined as the 90th percentile of the national daily maximum temperature (34.9°C) for at least 3 consecutive days, with the reference period being 2003–2021.
- **Precipitation Index (SPI):** An accumulation period of 1 month was chosen to account for short-term impacts.
- **Variable Lags:** Lags of up to 2–3 months for extreme heat and SPI for dengue and JEV; 1-month heat lag and 3-month rainfall lag for malaria; 3-month lags for both extreme heat and SPI for pneumonia, leptospirosis, and influenza; and immediate heat effect with a 3-month SPI lag for melioidosis.

**Limitations and Source Data Gaps**

- Future monthly temperature had to be disaggregated to daily temperature to determine the number of extreme heat days using a daily weather generator, which may not accurately capture the true variability and daily extremes within each month.
- Additional bias correction was not applied to the global climate model (GCM) inputs.
- Did not account for variables such as changes in land use, use of intervention, and proximity to amplifying hosts that may drive the transmission of diseases like JEV and malaria.
- Unable to include an autocorrelation structure in the model due to convergence issues arising from the combination of lagged covariates and overdispersed count outcomes.
- Could not account for future population growth because incorporating future population projections that exceeded historical maxima led to implausibly large and uncertain estimates.
- Did not account for potential changes in reporting rates over time.
- Unable to incorporate population immunity dynamics and future interventions into the model.

**Uncertainties**

- Weather extremes may have been under-estimated or over-estimated due to the lack of bias correction on GCM inputs.
- Extreme SPI values appeared less frequently in the GCM projections compared to the historical period because each monthly value represents a 20-year average that smooths out year-to-year extremes, meaning the results might underestimate the impact of extreme dry or wet weather on disease risk.
- Wide confidence intervals were observed for melioidosis during extreme wet weather, which could be explained by low monthly case counts across provinces.
- There is a risk that fluctuations in reported cases could be influenced by reporting practices rather than true epidemiological patterns.
- Short-term events, such as influenza pandemics or disruptions to surveillance, may have temporarily affected reported historical case counts.

**Author Warnings**

- Because predictions using future population as an offset were heavily skewed by future population projections, the authors assumed that the population would remain at historical levels (based on 2003 to 2021 data) so that excess risk could be solely attributed to extreme weather events.
- Without adjusting for potential changes in reporting rates, authors warn there is a risk that fluctuations in reported cases could be influenced by reporting practices.
- Future research should focus on the development of GCM outputs that provide continuous monthly data for future periods to allow for a more accurate representation of interannual climate variability and extreme events.
- Further work is needed to assess the projected impact of extreme weather on infectious diseases in other climatic and socioeconomic contexts, requiring the refining of predictions when immunity and intervention data become available.

# Phase 3 Delta Packet — 2026-06-24

## Phase 3 Query 01 — Exact anchors for core KEEP claims

For the exact source title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand", extract only the exact source anchors and values needed for these already-selected claims. For each item, return the exact number, confidence interval if shown, the comparison basis, and the exact figure/table/page/section anchor where it appears. Do not summarize beyond the source wording.

Items to extract
- Historical baseline finding that extreme heat increased most infectious diseases except malaria and leptospirosis.
- Nationwide dengue excess-risk decrease of 24.9% in 2061–2080.
- Influenza excess-risk increase of 36.8% in Nakhon Ratchasima in 2021–2040 under SSP245.
- Any exact province examples already highlighted in the paper for dengue or influenza under SSP245.

### Raw response

Here are the exact source anchors and values extracted for your selected claims based on the paper _"Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand"_:

**1. Historical baseline finding that extreme heat increased most infectious diseases except malaria and leptospirosis**

- **Exact Wording/Values:** "Historically, extreme heat was associated with an increase in all infectious disease incidences except malaria and leptospirosis." / "In dengue, JEV, influenza, pneumonia and melioidosis, the number of extreme heat days in a month was positively associated with disease risk... On the other hand, increasing days of extreme heat days in a month was negatively associated with malaria and leptospirosis risk".
- **Comparison Basis:** Number of extreme heat days in a month vs. no days of extreme heat.
- **Exact Anchor:** Abstract; Results Section ("Association of diseases with extreme weather"), Fig 2.

**2. Nationwide dengue excess-risk decrease of 24.9% in 2061–2080**

- **Exact Number:** Decrease of 24.9%.
- **Confidence Interval:** (95%CI:9.68%,40.0%).
- **Comparison Basis:** "during future periods of extreme weather from 2061–2080 compared to historical baselines".
- **Exact Anchor:** Abstract.

**3. Influenza excess-risk increase of 36.8% in Nakhon Ratchasima in 2021–2040 under SSP245**

- **Exact Number:** Increase of 36.8%.
- **Confidence Interval:** (95%CI:9.83%,63.8%) / (95% CI: 9.83%, 63.8%).
- **Comparison Basis:** "in 2021–2040 under SSP245" / "during periods of extreme weather" compared to historical burden.
- **Exact Anchor:** Abstract; Results Section ("Trends of influenza excess risk during extreme weather in SSP245"), Fig 7A.

**4. Exact province examples highlighted in the paper for dengue or influenza under SSP245**

- **Dengue in Bangkok:** Increased risk of 42.2% | **CI:** (95% CI: 13.6%, 70.7%) | **Comparison Basis:** From 2021–2040 during periods of extreme weather | **Anchor:** Results Section ("Trends of dengue excess risk during extreme weather in SSP245"), Fig 6A.
- **Dengue in Chiang Mai:** Decrease in dengue risk / ER: -24.6% | **CI:** (95% CI: -40.1%, -9.00%) | **Comparison Basis:** From 2021–2040 during periods of extreme weather | **Anchor:** Results Section ("Trends of dengue excess risk during extreme weather in SSP245"), Fig 6A.
- **Dengue in Chiang Rai:** Decrease in risk / ER: -34.2% | **CI:** (95% CI: -47.2%, -21.1%) | **Comparison Basis:** From 2061–2080 during periods of extreme weather | **Anchor:** Results Section ("Trends of dengue excess risk during extreme weather in SSP245"), Fig 6A.

---



## Phase 3 Query 02 — Exact numbers for the diseases still missing in the draft logic

For the exact source title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand", extract only the exact projected excess-risk values and anchors needed to support the kept narrative for pneumonia, melioidosis, malaria, Japanese encephalitis virus, and leptospirosis. Return only values that clarify direction, magnitude, time period, scenario, and whether the value is statistically significant. Include the exact figure/table/page/section anchor for each value. Do not summarize beyond the source wording.

### Raw response

Here are the exact projected excess-risk values, trends, and anchors extracted for your specified diseases from _"Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand"_:

**Melioidosis**

- **Direction & Magnitude:** Increases by 27.8% | **CI:** (95% CI: -39.4%, 94.9%)
    - **Time Period & Scenario:** By 2100 during periods of extreme heat under SSP585.
    - **Significance:** "confidence intervals remain wide" (not statistically significant as CI crosses zero).
    - **Exact Anchor:** Results Section ("Change in disease risk by individual extreme weather events"), Fig 5J.
- **Direction & Magnitude:** Increase / ER: 25.4% | **CI:** (95% CI: -32.1%, 82.8%)
    - **Time Period & Scenario:** From 2041–2060 during periods of extreme wet weather under SSP585.
    - **Significance:** "confidence intervals are wide" (not statistically significant as CI crosses zero).
    - **Exact Anchor:** Results Section ("Change in disease risk by individual extreme weather events"), Fig 5L.

**Japanese encephalitis virus (JEV)**

- **Direction & Magnitude:** Decline / ER: -18.2% | **CI:** (95% CI: -43.4%, 6.96%)
    - **Time Period & Scenario:** 2081–2100 during periods of extreme dry weather under SSP245.
    - **Significance:** CI crosses zero (not statistically significant).
    - **Exact Anchor:** Results Section ("Change in disease risk by individual extreme weather events"), Fig 4E.
- **General Trend (no exact values provided in text):** "A decrease in JEV risk from 2061–2080 is observed across all four climate change scenarios, except for SSP585, where there is an expected increased risk".
    - **Exact Anchor:** Results Section ("Overall change in disease risk during periods of extreme weather"), Fig 3E-3H.

_(Note: The source text does not provide exact numerical projected excess-risk percentages or confidence intervals for pneumonia, malaria, or leptospirosis. Only the exact directional trends are stated, as extracted below)._

**Pneumonia**

- **Direction / Trend:** "Pneumonia and melioidosis risks are expected to increase".
- **Time Period & Scenario:** "in the future during periods of extreme weather, particularly in the highest carbon emission scenario, SSP585 respectively".
- **Exact Anchor:** Results Section ("Overall change in disease risk during periods of extreme weather"), Fig 3D.

**Malaria**

- **Direction / Trend:** "An increase in malaria risk is expected".
- **Time Period & Scenario:** "during periods of extreme weather across all climate change scenarios and time periods... The exception is in SSP245, which sees a decrease in 2021–2040 and 2081–2100".
- **Exact Anchor:** Results Section ("Overall change in disease risk during periods of extreme weather"), Fig 3I-3L.
- **Secondary Trend:** "malaria risk is expected to increase during periods of extreme dry weather and wet weather, but more so during extreme dry weather".
- **Exact Anchor:** Results Section ("Change in disease risk by individual extreme weather events"), Fig 4H, 4I.

**Leptospirosis**

- **Direction / Trend:** "leptospirosis risk is expected to decrease".
- **Time Period & Scenario:** "during periods of extreme weather, across all climate change scenarios and time periods".
- **Exact Anchor:** Results Section ("Overall change in disease risk during periods of extreme weather").

## Phase 3 Query 03 — Baseline comparison needed by the active draft

For the exact source title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand", extract only the historical baseline information that helps interpret how large the projected shifts are. Return any exact historical-period disease burden statements, ranking statements, mean case-count references, or baseline comparison language used by the authors for dengue, influenza, pneumonia, malaria, leptospirosis, melioidosis, and Japanese encephalitis virus. Include the exact table/figure/page/section anchor. If the paper does not provide a direct baseline ranking or current burden comparison for a requested disease, state that explicitly.

### Raw response

Based on the source _"Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand"_, here is the exact historical baseline information, burden statements, and baseline comparison language used by the authors:

**Dengue**

- **Burden/Ranking Statement:** The authors specifically focused their finer analysis on the "five provinces which had the highest dengue burden from 2003 to 2019".
- **Baseline Comparison Language:** "Provinces with historically high dengue incidence, such as Bangkok".
- **Anchor:** Results Section ("Trends of dengue excess risk during extreme weather in SSP245"); Fig 6A caption ("five provinces with the historically highest incidence of dengue").

**Influenza**

- **Burden/Ranking Statement:** The authors focused their analysis on the "five provinces with the historically highest incidence of influenza".
- **Baseline Comparison Language:** "Nakhon Ratchasima, a province with historically high influenza burden".
- **Anchor:** Results Section ("Trends of influenza excess risk during extreme weather in SSP245"); Fig 7A caption.

**Melioidosis**

- **Case-Count Reference:** The authors note that "Broad confidence intervals could be explained by low monthly case counts across provinces".
- **Anchor:** Results Section ("Change in disease risk by individual extreme weather events").

**Pneumonia, Malaria, Leptospirosis, and Japanese Encephalitis Virus (JEV)**

- **General Comparison Language:** The authors group these diseases together with the others as "seven major infectious diseases circulating in Thailand" and note they were "chosen among the common infectious diseases in Thailand as the risk of transmission from these diseases are plausibly influenced by weather conditions".
- **Anchor:** Methods Section ("Disease case data").
- **Explicit Statement on Missing Information:** The paper **does not provide** a direct baseline ranking, specific mean case-count numbers, or direct current burden comparison language for pneumonia, malaria, leptospirosis, or Japanese encephalitis virus (JEV). The methodology mentions that excess risk was calculated using the "mean disease case counts across the historical period" (2003-2019), but the exact baseline numbers for these specific diseases are not published in the text.

## Phase 3 Query 04 — Short method and uncertainty anchors for public-facing caveats

For the exact source title "3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand", extract only the exact method and limitation details needed for a short public-facing caveat box. Return concise source-bound statements with anchors for these items only
- study period and geographic coverage
- model family used
- climate scenarios used
- why future population growth was excluded
- the daily-temperature disaggregation limitation
- the lack of bias correction for GCM inputs
- the warning that these are risk trajectories from extreme weather pressure rather than guaranteed future case counts

### Raw response

Here are the exact method and limitation details extracted for the caveat box, based on the source _"Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand"_:

- **Study period and geographic coverage:** The models used "historical data from 2003 to 2019" across "77 provinces in Thailand" to project future excess risk "from 2021–2100". **(Anchors: Author summary; Introduction)**
- **Model family used:** "Generalised additive models (GAMs) with a negative binomial distribution were used to model the associations". **(Anchor: Methods Section, "Statistical model")**
- **Climate scenarios used:** The study considered "4 of the CMIP6 climate change scenarios - SSP126, SSP245, SSP370, SSP585". **(Anchor: Results Section, "Future climate change scenarios")**
- **Why future population growth was excluded:** The authors noted they "could not account for future population growth as future population exceeded historical maxima, hence incorporating future population in projections led to implausibly large and uncertain estimates". Additionally, they aimed to "observe the change in risk solely from extreme weather and not population levels". **(Anchors: Results Section, "Model evaluation"; Discussion)**
- **The daily-temperature disaggregation limitation:** "Future monthly temperature was disaggregated to daily temperature to determine the number of extreme heat days. However, this approach may not accurately capture the true variability and daily extremes within each month". **(Anchor: Discussion)**
- **The lack of bias correction for GCM inputs:** "We did not apply additional bias correction to the GCM inputs, so weather extremes may have been under-estimated or over-estimated, which could influence the estimated impact of extreme weather on disease outcomes". **(Anchor: Discussion)**
- **The warning that these are risk trajectories from extreme weather pressure rather than guaranteed future case counts:** The methodology specifies that the analysis "ensures that excess risk reflects the impact of future extreme weather while holding all other covariates constant". The authors explicitly warn that they "did not account for variables such as changes in land use, use of intervention and proximity to amplifying hosts" and "were unable to incorporate population immunity dynamics and future interventions in our model. This would require refining of our predictions in the future when such data is available". **(Anchors: Methods Section, "Future projection and estimation of excess risk due to extreme weather scenarios"; Discussion)**
