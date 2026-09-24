# WP2 §5.1 Gap Analysis — Phase A: A-BTR Signal Tagging (A001–A122)

Source: `ψ/incubate/DCCE/CRDB/output/02_Data_Inventory/wp2-data-domain-highlight-draft.md`, §2 (122 numbered signals, subsections 2.1–2.9) and §7 (summary). These signals are DCCE's own international reporting obligation (Thailand's Biennial Transparency Report, adaptation chapter) rather than an external agency's demand — every `requesting_agency` below is tagged accordingly.

Item text is in English because the source signals are themselves documented in English (translated/summarized from the BTR draft text), unlike the D-series (D001–D238) which is Thai-language, drawn from the consultation workshop transcripts.

Every `risk_component` assignment is this analyst's best-guess reading, following the same convention the D-series pass used: governance/institutional/platform-framing items with no discrete physical-risk-chain content are tagged "Response" as the nearest TOR 5.3.5 fit, flagged as a coarse fit rather than a strong match. Items whose category assignment is genuinely uncertain, multi-component, or borderline are flagged explicitly in the `flags` column.

`flags` also carries over the Direct/Partial/Inferred/No-match confidence the source document's own §4.1 catalog-matching pass already assigned to each signal, where available — this is descriptive of what the *source document* found, not a re-verification by this pass. Part 2 of this gap-analysis task (see `demand-supply-register.csv`) translates these into the three-way มีและใช้ได้/มีแต่ใช้ประโยชน์ได้ยาก/ยังไม่มี status framework, and only for the ~101 items below NOT tagged "Response."

## Summary counts (risk_component × item_type)

| risk_component | dataset | product | total |
|---|---|---|---|
| Climatic Driver | 17 | 4 | 21 |
| Hazard | 45 | 3 | 48 |
| Exposure | 1 | 0 | 1 |
| Sensitivity | 3 | 1 | 4 |
| Adaptive Capacity | 1 | 3 | 4 |
| Impact | 9 | 0 | 9 |
| Response | 6 | 15 | 21 |
| Loss and Damage | 9 | 5 | 14 |
| **Total** | **91** | **31** | **122** |

**Structural note (parallel to the D-series document's own finding on Group 5):** unlike the D-series where "Response" dominance came from a governance-heavy consultation-workshop use-case group, here "Response" (21/122) is smaller in share because most of the 122 signals are drawn from the BTR's hazard/climate-variable-heavy technical chapters (SEC-004/005), not its institutional chapters (SEC-006/007/009/010) — those institutional-gap-statement signals (items 98–104, 106, 108, 114, 115, 120–122) are the ones tagged Response here, plus platform-framing items 3–5, 107, 109, 110.

## A. National-circumstances / platform-framing signals (A001–A007)

| item_id | item_text_th_or_en | item_type | risk_component | requesting_agency | source_anchor | flags |
|---|---|---|---|---|---|---|
| A001 | Population & urbanization baseline (65.95M, 34.3% urban, 2024) | dataset | Exposure | DCCE (A-BTR reporting obligation) | A-REQ-004, EVU-004 | Direct match (DOPA_1_1, NSO_1_2) per source §4.1 |
| A002 | Main population groups with heightened climate vulnerability (low-income, smallholder farmers, coastal communities, elderly, disabled, outdoor workers) | dataset | Sensitivity | DCCE (A-BTR reporting obligation) | A-REQ-010, EVU-010 | Direct multi-row match (NESDC_2_x, MSDHS_2_2, CDD_1_1) per source §4.1; merged VULNERABILITY-taxonomy caveat applies (see Notes) |
| A003 | Agency responsible for climate risk mapping/projections + dissemination platforms (DCCE, CCIC, Climate Data Services) | product | Response | DCCE (A-BTR reporting obligation) | A-REQ-016, EVU-016 | Direct match (DCCE_3_1–3_7, URL-level) per source §4.1; flag — primarily institutional-role language but names two concrete platforms, borderline dataset/institutional |
| A004 | National climate information platforms (DCCE Climate Data Services + CCIC) | product | Response | DCCE (A-BTR reporting obligation) | B-REQ-001, EVU-038 | Direct match per source §4.1; flag — platform description, not itself a dataset |
| A005 | Functional role differentiation of DCCE Climate Data Services vs CCIC (methods table) | product | Response | DCCE (A-BTR reporting obligation) | B-REQ-002, EVU-039 | Direct match per source §4.1; flag — borderline Climatic Driver, since the table itself lists downscaling methods/models |
| A006 | Named climate variables/hazard indicators/risk indices on national platforms (temp, rainfall, humidity, extreme indices, EHV indices) | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-003, EVU-040 | Direct match per source §4.1; flag — multi-component, also names hazard/exposure/sensitivity/adaptive-capacity indices |
| A007 | Scenario pathways available (SSP2-4.5, SSP5-8.5) | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-004, EVU-041 | Direct match per source §4.1 |

## B. Observed & projected temperature, rainfall, SST (A008–A033)

| item_id | item_text_th_or_en | item_type | risk_component | requesting_agency | source_anchor | flags |
|---|---|---|---|---|---|---|
| A008 | Observed 2024 annual mean temperature vs 30-yr baseline (28.5°C, +1.1°C) | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-007, EVU-044 | Direct match (DCCE_2_12/13/14, GridData) per source §4.1 |
| A009 | Regional 2024 temperature-anomaly characterization | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-008, EVU-045 | No match found per source §4.1 — catalog holds raw variables, not a pre-computed regional-anomaly product |
| A010 | Future temperature projection basis: CMIP6 EC-Earth3-Veg + RegCM | product | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-009, EVU-046 | Direct match per source §4.1 |
| A011 | Projected mean-temperature increases by period (2021–2100) | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-010, EVU-047 | Direct match per source §4.1 |
| A012 | SSP5-8.5 vs SSP2-4.5 temperature-increase comparison | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-011, EVU-048 | Direct match per source §4.1 |
| A013 | Projected Tmax increases | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-012, EVU-049 | Direct match per source §4.1 |
| A014 | Projected Tmin increases | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-013, EVU-050 | Direct match per source §4.1 |
| A015 | Diurnal Temperature Range (DTR) direction | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-014, EVU-051 | No match found per source §4.1 — DTR appears only as an input inside TMD_6_22's composite formula, not independently cataloged |
| A016 | Warm Spell Duration Index (WSDI) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-015, EVU-052 | Direct match (TMD_6_4) per source §4.1 |
| A017 | Summer Days index (SU35) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-016, EVU-053 | Direct match (TMD_6_7) per source §4.1 |
| A018 | Seasonal shift (longer hot season, shorter cool season) | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-017, EVU-054 | No match found per source §4.1 — no dataset captures season length/start date |
| A019 | Observed 2024 annual rainfall vs baseline (1,704.4mm, +5%) | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-018, EVU-055 | Partial match (DCCE_2_1) per source §4.1 — GridData ends 2023, does not cover cited 2024 figure |
| A020 | Heavy-rainfall flood linkage 2024 | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-019, EVU-056 | Direct/Partial cluster match per source §4.1 |
| A021 | Projected precipitation increase, spatial pattern | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-020, EVU-057 | Direct match per source §4.1 |
| A022 | Precipitation projection methodology (EC-Earth3-Veg + RegCM) | product | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-021, EVU-058 | Direct match per source §4.1 |
| A023 | Future rainfall variability (intense events + longer dry spells) | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-022, EVU-059 | Direct/Partial match per source §4.1 |
| A024 | Max 1-day precipitation index (Rx1day) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-023, EVU-060 | Direct match (TMD_6_9) per source §4.1 |
| A025 | Very heavy precipitation days index (R20mm) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-024, EVU-061 | Direct match (TMD_6_18) per source §4.1 |
| A026 | Consecutive Wet Days index (CWD) | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-025, EVU-062 | Direct match (TMD_6_15) per source §4.1 |
| A027 | Dry-days increase (drought counter-signal) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-026, EVU-063 | Direct match (TMD_6_16, CDD) per source §4.1 |
| A028 | Monsoon dynamics / rainy-season irregularity | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-027, EVU-064 | Not individually scored in source §4.1 (bundled in 20–28 cluster); flag — narrative, no discrete field |
| A029 | Observed May-2024 SST anomaly, Gulf of Thailand | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-028, EVU-065 | Partial match (GISTDA_2_1) per source §4.1 |
| A030 | Seasonal SST behavior (Gulf vs Andaman) | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-029, EVU-066 | Partial match (GISTDA_2_1) per source §4.1 |
| A031 | Future SST projection methodology (CORDEX SEA, 25×25km) | product | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-030, EVU-067 | No match found per source §4.1 — GISTDA_2_1 is confirmed observation data, not a projection product (Boss-reviewed, §6 item 4) |
| A032 | SST projected continuous increase | dataset | Climatic Driver | DCCE (A-BTR reporting obligation) | B-REQ-031, EVU-068 | No match found per source §4.1, same reasoning as A031 |
| A033 | SST → coral-bleaching ecological linkage | dataset | Impact | DCCE (A-BTR reporting obligation) | B-REQ-032, EVU-069 | Direct match (DMCR_2_1) per source §4.1; flag — dual Climatic-Driver-cause/Impact-effect content |

## C. Flood, drought, landslide, windstorm/cyclone, wildfire, SLR, extreme-heat hazards (A034–A083)

| item_id | item_text_th_or_en | item_type | risk_component | requesting_agency | source_anchor | flags |
|---|---|---|---|---|---|---|
| A034 | Floods = most damaging hazard 1989–2024 | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-033, EVU-070 | Direct/Partial match (GISTDA_5_1, GISTDA_3_1, LDD_1_1, DDPM_1_1) per source §4.1 |
| A035 | 2022 flooding across 69 provinces | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-034, EVU-071 | Partial match (DDPM_2_1) per source §4.1 |
| A036 | Flood-severity drivers (climatic + structural) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-035, EVU-072 | Not individually scored; flag — narrative driver-explanation, topically covered but no discrete field |
| A037 | Future flood-risk expansion (frequency, intensity, duration, area) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-036, EVU-073 | Direct (extent)/Inferred (return-period) per source §4.1 |
| A038 | Chao Phraya flood return-period compression | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-037, EVU-074 | Inferred per source §4.1 — no return-period field in any catalog row; flag ambiguous |
| A039 | 50% probability of 2011-equivalent flood by 2050 | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-038, EVU-075 | Inferred per source §4.1; flag ambiguous, same reasoning as A038 |
| A040 | Subnational flood-risk hotspot provinces | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-039, EVU-076 | Direct/Partial match per source §4.1 |
| A041 | Bangkok compound flood risk, elevation 0.5–1.5m + subsidence | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-040, EVU-077 | Not individually scored; flag — no elevation/subsidence field identified in catalog |
| A042 | Drought drivers (monsoon variability, El Niño) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-041, EVU-078 | Partial match (HII_1_1, DDPM_3_1/3_2, LDD_1_3/2_1) per source §4.1 |
| A043 | 2015 drought severity (worst in ~15 years) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-042, EVU-079 | Partial match per source §4.1 |
| A044 | Water-access inequality / irrigation coverage as drought-vulnerability structural factor | dataset | Adaptive Capacity | DCCE (A-BTR reporting obligation) | B-REQ-043, EVU-080 | Not individually scored; flag — merged VULNERABILITY-taxonomy caveat applies (see Notes) |
| A045 | Future flood-drought cycle intensification | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-044, EVU-081 | Not individually scored; flag — narrative, no discrete field |
| A046 | Drought-hotspot provinces under SSP5-8.5 | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-045, EVU-082 | Partial match per source §4.1 — no RCP/SSP-scenario field on drought rows |
| A047 | Landslide trigger mechanism (pore-water pressure, shear strength) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-046, EVU-083 | Direct (extent)/Inferred (mechanism) per source §4.1 |
| A048 | Landslide susceptibility amplifiers (deforestation, land-use) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-047, EVU-084 | Direct/Inferred per source §4.1 |
| A049 | 2024 landslide incident count (>310) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-048, EVU-085 | Direct match (DMR_1_1) per source §4.1 — event-year snapshot only, not a running tally |
| A050 | Landslide projection methodology (10 GCMs, RCP4.5/8.5) | product | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-049, EVU-086 | Inferred per source §4.1 |
| A051 | Landslide occurrence probability (100-yr event, 90%/80% area) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-050, EVU-087 | Inferred per source §4.1; flag ambiguous — no RCP-probability field in any row |
| A052 | High-hazard zone spatial expansion (foothills) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-051, EVU-088 | Inferred per source §4.1 |
| A053 | Mid-century landslide frequency/probability threshold (>0.9) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-052, EVU-089 | Inferred per source §4.1 |
| A054 | End-century landslide risk-regime shift | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-053, EVU-090 | Inferred per source §4.1 |
| A055 | Landslide rainfall-trigger threshold lowering | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-054, EVU-091 | Inferred per source §4.1 |
| A056 | Windstorm frequency: high but no clear trend | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-055, EVU-092 | Partial match (TMD_1_3/1_6, image-only format) per source §4.1 |
| A057 | Windstorm intensity/gust evidence | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-056, EVU-093 | Partial match per source §4.1 |
| A058 | Historical cyclone count/frequency 1951–2024 (206 events) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-057, EVU-094 | Partial match (TMD_4_1/3_1) per source §4.1 — TMD_4_1 requested, not yet received; flag prominently |
| A059 | Cyclone seasonal concentration statistics | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-058, EVU-095 | Partial match per source §4.1, same not-yet-received flag |
| A060 | Cyclone interannual variability, decline since ~2012 | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-059, EVU-096 | Partial match per source §4.1, same not-yet-received flag |
| A061 | Projected cyclone behavior change (slower, inland penetration, poleward shift) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-060, EVU-097 | No match found per source §4.1 |
| A062 | Cyclone projection methodology (64,000 synthetic cyclones) | product | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-061, EVU-098 | No match found per source §4.1 |
| A063 | Bangkok extreme wind-speed increase (>100%) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-062, EVU-099 | No match found per source §4.1 |
| A064 | Cyclone-impact duration increase (~72%) | dataset | Impact | DCCE (A-BTR reporting obligation) | B-REQ-063, EVU-100 | No match found per source §4.1; flag — dual Hazard/Impact content |
| A065 | Decade-scale wildfire burden (60,000 incidents, 1.4M rai) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-064, EVU-101 | Partial match (GISTDA_1_1/1_2, GISTDA_3_2) per source §4.1 — GISTDA_1_1's 2025–2026 window does not reach 2015–2024 historical figures |
| A066 | Northern-region wildfire hotspot stats 2015–2024 | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-065, EVU-102 | Partial match per source §4.1, same coverage-window caveat |
| A067 | Fire season pattern + human-caused share (>90%) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-066, EVU-103 | Not individually scored; flag — narrative, no discrete field |
| A068 | Repeated burning persistence stats | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-067, EVU-104 | Not individually scored; flag — no discrete field |
| A069 | Agricultural burning + PM2.5 health linkage | dataset | Impact | DCCE (A-BTR reporting obligation) | B-REQ-068, EVU-105 | Not individually scored; flag — dual Hazard/Impact, PM2.5 side covered by BMA_3_1 only |
| A070 | Wildfire spatial-ecological risk classification | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-069, EVU-106 | Not individually scored; flag — no discrete field |
| A071 | Wildfire-prone-area spatial distribution (>50% across 22 regions) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-070, EVU-107 | Partial match (GISTDA_1_1/1_2/3_2) per source §4.1 |
| A072 | Future fire-risk drivers (evapotranspiration, soil moisture) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-071, EVU-108 | Not individually scored; flag — no discrete field |
| A073 | Historical sea-level-rise station rates 1951–2014 | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-072, EVU-109 | Partial match (MD_1_2) per source §4.1 |
| A074 | Bangkok relative SLR before/after groundwater regulation | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-073, EVU-110 | Partial match per source §4.1 |
| A075 | Recent Gulf SLR rate + seasonal sea-level swing | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-074, EVU-111 | Partial match per source §4.1 |
| A076 | Future SLR projection scenarios (CMIP6/GeoMIP6/SRM) | product | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-075, EVU-112 | Not individually scored; flag — no discrete projection product |
| A077 | Future SLR rate by scenario | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-076, EVU-113 | Not individually scored; flag — no discrete field |
| A078 | BMR inundated-area expansion time series (2030–2090) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-077, EVU-114 | Not individually scored; flag — no discrete BMR-specific dataset |
| A079 | Compound flooding drivers (rainfall + discharge increase) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-078, EVU-115 | Not individually scored; flag — rainfall side covered, discharge-projection component absent |
| A080 | Extreme-heat threshold definitions (35.0–39.9°C "hot", ≥40°C "very hot") | product | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-079, EVU-116 | Partial match (TMD_2_1/5_1) per source §4.1 — this is a classification rule, not itself a dataset |
| A081 | 2024 annual mean + April extreme daily temperature (44.2°C) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-080, EVU-117 | Partial match per source §4.1, TMD_5_1 not yet received |
| A082 | Extreme-heat spatial hotspots | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-081, EVU-118 | Partial match per source §4.1 |
| A083 | Extreme-heat multi-scale drivers (ENSO, solar radiation, urbanization) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-082, EVU-119 | Not individually scored; flag — narrative, no discrete field |

## D. Impacts, risks, vulnerabilities (A084–A097)

| item_id | item_text_th_or_en | item_type | risk_component | requesting_agency | source_anchor | flags |
|---|---|---|---|---|---|---|
| A084 | Global Climate Risk Index 2026 ranking (17th) | dataset | Impact | DCCE (A-BTR reporting obligation) | B-REQ-083, EVU-120 | No match found per source §4.1 — external composite index, not reproduced in-catalog |
| A085 | Long-term (1995–2024) risk rankings | dataset | Impact | DCCE (A-BTR reporting obligation) | B-REQ-084, EVU-121 | No match found per source §4.1 |
| A086 | 2024 rankings vs long-term fatality rank | dataset | Impact | DCCE (A-BTR reporting obligation) | B-REQ-085, EVU-122 | No match found per source §4.1 |
| A087 | Projected GDP decline (7–14% by 2050) | dataset | Impact | DCCE (A-BTR reporting obligation) | B-REQ-086, EVU-123 | No match found per source §4.1 |
| A088 | Observed macroeconomic livelihood impacts (2024, agri sector contraction) | dataset | Impact | DCCE (A-BTR reporting obligation) | B-REQ-088, EVU-125 | Inferred match (OAE_1_1–1_5) per source §4.1 — semantic leap required, these are structural agri datasets, not GDP/employment time series |
| A089 | Disaster loss share of GDP (0.27%) | dataset | Loss and Damage | DCCE (A-BTR reporting obligation) | B-REQ-089, EVU-126 | No match found per source §4.1 |
| A090 | Table 1-2: disaster impact records 2015–2024 by hazard type | dataset | Loss and Damage | DCCE (A-BTR reporting obligation) | B-REQ-091, EVU-128 | Direct structural match (DDPM_2_1, DDPM_2_3) per source §4.1 — "single most business-critical structural match found," but catalog's own `use_limitations` flags data-quality weakness |
| A091 | Communicable disease + air-pollution illness burden 2024 | dataset | Impact | DCCE (A-BTR reporting obligation) | B-REQ-092, EVU-129 | Partial match (DOHealth_1_2, not received; BMA_3_1) per source §4.1 |
| A092 | Heat-related mortality profile 2024 (63 deaths) | dataset | Loss and Damage | DCCE (A-BTR reporting obligation) | B-REQ-093, EVU-130 | No match found per source §4.1 — no catalog row provides heat-attributable mortality counts |
| A093 | Malnutrition trend indicators (stunting/wasting) | dataset | Sensitivity | DCCE (A-BTR reporting obligation) | B-REQ-094, EVU-131 | No match found per source §4.1; flag — merged VULNERABILITY-taxonomy caveat would apply if matched (see Notes) |
| A094 | Coastal erosion 2019–2024 (>77 sub-districts) | dataset | Hazard | DCCE (A-BTR reporting obligation) | B-REQ-095, EVU-132 | Direct match (DMCR_1_1, DMCR_4_1) per source §4.1 |
| A095 | Coral bleaching nationwide/basin share (May 2024, 86.6%) | dataset | Impact | DCCE (A-BTR reporting obligation) | B-REQ-096, EVU-133 | Direct match (DMCR_2_1) per source §4.1 |
| A096 | Forest cover extent/trend 2024 + decade dynamics | dataset | Exposure | DCCE (A-BTR reporting obligation) | B-REQ-097, EVU-134 | Direct match (RFD_1_1, RFD_1_2) per source §4.1 |
| A097 | Risk-assessment scenario basis (SSP4.5/8.5) + CCIC risk maps | product | Response | DCCE (A-BTR reporting obligation) | B-REQ-099, EVU-136 | Direct match (DCCE_3_1–3_7) per source §4.1, same URL-level match as A003 |

## E. Institutional data-and-knowledge gaps (A098–A103) — gap statements, not dataset requests

| item_id | item_text_th_or_en | item_type | risk_component | requesting_agency | source_anchor | flags |
|---|---|---|---|---|---|---|
| A098 | Area-based risk/vulnerability data limitations (resolution, timeliness, coverage) | product | Response | DCCE (A-BTR reporting obligation) | C-REQ-020, EVU-163 | No match found by design per source §4.1 — this describes a deficiency in the data landscape, not a dataset request; matching it against the catalog would be a category error |
| A099 | Absence of standardized Loss & Damage assessment framework/system | product | Response | DCCE (A-BTR reporting obligation) | C-REQ-023, EVU-166 | No match found by design, same reasoning as A098 |
| A100 | L&D data dispersion across agencies | product | Response | DCCE (A-BTR reporting obligation) | C-REQ-024, EVU-167 | No match found by design |
| A101 | Absence of standardized adaptation outcome indicators | product | Response | DCCE (A-BTR reporting obligation) | C-REQ-025, EVU-168 | No match found by design |
| A102 | Fragmentation of climate databases / no centralized platform | product | Response | DCCE (A-BTR reporting obligation) | C-REQ-027, EVU-170 | No match found by design |
| A103 | Adaptation planning informed by climate projections, risk/vulnerability assessments, geospatial data | product | Response | DCCE (A-BTR reporting obligation) | C-REQ-066, EVU-209 | Not individually scored; flag — descriptive/general statement, not a dataset request |

## F. Implementation & M&E named data systems (A104–A112)

| item_id | item_text_th_or_en | item_type | risk_component | requesting_agency | source_anchor | flags |
|---|---|---|---|---|---|---|
| A104 | Deaths/missing-persons data collected, but not adaptation-linked (tracking gap) | product | Response | DCCE (A-BTR reporting obligation) | D-REQ-013, EVU-242 | No match found per source §4.1 — process/tracking gap, not a dataset |
| A105 | Disaster mortality/missing-person data systematically collected | dataset | Loss and Damage | DCCE (A-BTR reporting obligation) | D-REQ-019, EVU-248 | No match found per source §4.1, same category-error reasoning |
| A106 | Avoided-losses quantification gap (national) | product | Response | DCCE (A-BTR reporting obligation) | D-REQ-020, EVU-249 | No match found per source §4.1 |
| A107 | Named completed data systems: Spatial Climate Risk Database + national climate projections | product | Response | DCCE (A-BTR reporting obligation) | D-REQ-032, EVU-261 | Direct match (DCCE_3_1–3_7) per source §4.1, strongest URL-level match alongside A003 |
| A108 | National climate risk/impact knowledge database (ongoing) | product | Response | DCCE (A-BTR reporting obligation) | D-REQ-033, EVU-262 | Direct match per source §4.1 |
| A109 | Quantitative implementation evidence bundle (Agri-Map, crop insurance, tourism certifications, HNAP progress) | dataset | Response | DCCE (A-BTR reporting obligation) | D-REQ-042, EVU-271 | Partial match (OAE_1_1–1_5, DOT_2_2–2_6) per source §4.1 — topically adjacent, specific named programme datasets absent; flag — M&E/adaptation-progress content, tagged Response rather than forced into a risk-chain category |
| A110 | National indicator taxonomy: exposure, sensitivity, coping/adaptive capacity | product | Response | DCCE (A-BTR reporting obligation) | D-REQ-047, EVU-276 | No match found per source §4.1 (Boss-reviewed, revised from initial Inferred — see source §4.1 items 110–112); flag — multi-component taxonomy spanning 3 risk-chain categories at once |
| A111 | Named analytical output: Yearly Vulnerability Index | product | Sensitivity | DCCE (A-BTR reporting obligation) | D-REQ-048, EVU-277 | No match found per source §4.1 (Boss-reviewed confirmed gap — DCCE_3_1–3_7 composite index is a distinct product, not this index); merged VULNERABILITY-taxonomy caveat applies (see Notes) |
| A112 | Named analytical output: Climate Resilience Index | product | Adaptive Capacity | DCCE (A-BTR reporting obligation) | D-REQ-049, EVU-278 | No match found per source §4.1, same confirmed-gap reasoning as A111; merged VULNERABILITY-taxonomy caveat applies |

## G. Loss & Damage / disaster-response named data (A113–A119)

| item_id | item_text_th_or_en | item_type | risk_component | requesting_agency | source_anchor | flags |
|---|---|---|---|---|---|---|
| A113 | Economic + non-economic loss category scope | product | Loss and Damage | DCCE (A-BTR reporting obligation) | E-REQ-002, EVU-293 | Partial match (DDPM_2_1, DDPM_2_3, DOHealth_1_2, RFD_1_2) per source §4.1 |
| A114 | CBS hazard-type testing coverage (8 types, 2026 target) | product | Response | DCCE (A-BTR reporting obligation) | E-REQ-008, EVU-299 | No match found per source §4.1 — CBS is a dissemination channel, not a dataset |
| A115 | Multi-source data integration for risk maps (met/hydro/geospatial) | product | Response | DCCE (A-BTR reporting obligation) | E-REQ-015, EVU-306 | Inferred match (DCCE_3_1–3_7) per source §4.1 — composite-index rows are the product of integration, not integration-as-a-dataset itself |
| A116 | CBDRM-implementing communities count (15,851) | dataset | Adaptive Capacity | DCCE (A-BTR reporting obligation) | E-REQ-019, EVU-310 | No match found per source §4.1; merged VULNERABILITY-taxonomy caveat would apply if matched |
| A117 | Named post-disaster assessment methodologies (DANA/PDNA/DALA) | product | Loss and Damage | DCCE (A-BTR reporting obligation) | E-REQ-036, EVU-327 | No match found per source §4.1 — assessment methodology, not a dataset; directly relevant to WP7 gap analysis for disaster-loss-statistics domain |
| A118 | Assessment analysis levels (sectoral + macroeconomic) | product | Loss and Damage | DCCE (A-BTR reporting obligation) | E-REQ-037, EVU-328 | No match found per source §4.1 |
| A119 | Non-economic loss and damage (NELD) categories (health, quality of life, cultural heritage, social cohesion) | dataset | Loss and Damage | DCCE (A-BTR reporting obligation) | E-REQ-043, EVU-334 | Partial match (DOHealth_1_2, health component only) per source §4.1 — quality-of-life/cultural-heritage/social-cohesion dimensions have no catalog proxy |

## H. Recommendations-chapter named data assets (A120–A122)

| item_id | item_text_th_or_en | item_type | risk_component | requesting_agency | source_anchor | flags |
|---|---|---|---|---|---|---|
| A120 | CCIC + Climate Data Services named as good-practice data assets | product | Response | DCCE (A-BTR reporting obligation) | F-REQ-001, EVU-340 | Direct match (DCCE_3_1–3_7, DCCE_2_1–2_19) per source §4.1, restating platform identity already matched at A003/A107 |
| A121 | Climate Data Services explicit planning use | product | Response | DCCE (A-BTR reporting obligation) | F-REQ-002, EVU-341 | Direct match per source §4.1 |
| A122 | Data availability/consistency named as major M&E constraint | product | Response | DCCE (A-BTR reporting obligation) | F-REQ-036, EVU-375 | No match found by design per source §4.1; flag — weak evidence-unit linkage noted in source (EVU-375 is a bare section header, not substantive text) |

---

## Notes: merged VULNERABILITY-taxonomy caveat (carried forward from D-series document)

As with the D-series pass, `data_catalog_v4.csv`'s `cdm_sub_domain` field only carries a single merged **VULNERABILITY** category (72 rows) — it cannot distinguish Sensitivity from Adaptive Capacity content. Every A-BTR item above tagged Sensitivity or Adaptive Capacity (A002, A044, A093, A111, A112, A116) is, in the Part 2 matching step, checked only against this merged 72-row pool as a whole; the catalog's own taxonomy cannot confirm which side of the Sensitivity/Adaptive-Capacity split is actually covered. This is a supply-side taxonomy gap, not a matching-methodology choice, and is noted here rather than silently resolved.

## Overall coverage check

122 of 122 selected A-BTR signals tagged (A001–A122), matching the source document's own count of "122 signals selected as data-shaped" (§7 summary: "Selected as data-shaped and extracted into §2: 122 signals"). 21 tagged Response (governance/platform/gap-statement items); 101 tagged across the other 7 risk-chain categories and carried forward to Part 2 item-level supply matching.
