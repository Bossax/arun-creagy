# Raw Copy: ART06_Species_Protected_Areas

- **Source Title**: `6-Vulnerability to climate change of species in protected areas in Thailand`
- **Notebook ID**: `crdb-tor-5-5-climate-risk-arti`
- **Mode**: Hybrid Manual-Paste Loop
- **Instruction**: Run each query in NotebookLM and paste the raw response directly below its matching block.

---

## Step 1A — Outline

**Query**

```text
For the source document "6-Vulnerability to climate change of species in protected areas in Thailand": Extract and list the full section outline of the paper. If the document is not found or the title is ambiguous, report that explicitly.
```

**Raw Response**
Based on the source document "6-Vulnerability to climate change of species in protected areas in Thailand," here is the full section outline extracted from the paper:

- **Results**
    - Data completeness and representativeness
    - Changes in the availability of suitable habitat for individual species
    - Impacts on species in protected areas
    - Projected changes in conservation status of species
- **Discussion**
- **Management recommendations**
- **Methods**
    - Study area
    - Environmental data
    - Species occurrence data
    - Species distribution modeling
    - Assessment of climate change impacts
- **Data availability**
- **References**
- **Acknowledgements**
- **Author contributions**

_(Note: An explicit "Introduction" section header is not present in the excerpts, as the text begins directly with the background and research questions prior to the "Results" section.)_


---

## Step 1B — Variables

**Query**

```text
For the source document "6-Vulnerability to climate change of species in protected areas in Thailand": Identify and list the primary variables, metrics, or qualitative concepts discussed in each section (e.g., climate parameters, biodiversity indicators, habitat suitability variables, extinction risk, conservation planning variables, or geographical exposure labels).
```

**Raw Response**
Here are the primary variables, metrics, and qualitative concepts discussed in each section of the source document "6-Vulnerability to climate change of species in protected areas in Thailand":

**Introduction (Implicit)**

- **Qualitative Concepts**: The vulnerability of protected areas (PAs) to climate change, the post-2020 Global Biodiversity Framework (targeting 30% terrestrial coverage by 2030), and Thailand's position within the Indo-Burma biodiversity hotspot.
- **Variables/Metrics**: Total land area, altitude ranges (0 to 2564 m), current forest cover percentage (31.7%), and existing PA land coverage percentage (22.8% to 25%).

**Results**

- **Data completeness and representativeness**:
    - _Metrics/Variables_: Taxonomic coverage (percentage of species recorded in Thailand for mammals, birds, reptiles, amphibians, and plants), the number of species modeled, the number of unique occurrence localities, and the altitudinal distribution of records (comparing areas <250 m vs. >250 m above sea-level).
- **Performance of the species distribution models**:
    - _Metrics_: The continuous Boyce Index (values >0.5 indicating acceptable model performance) representing SDM prediction consistency.
- **Changes in projected species richness under climate change**:
    - _Metrics_: Maximum species richness per 1x1 km grid cell, and the number of grid cells maintaining the highest species richness level under different climate scenarios (RCP2.6 and RCP8.5).
- **Changes in the availability of suitable habitat for individual species**:
    - _Variables/Metrics_: The percentage of species projected to lose >50% or 100% of their currently suitable habitat under "no dispersal" constraints, and the percentage of species projected to experience net expansions vs. contractions under "unlimited dispersal" constraints.
- **Impacts on species in protected areas**:
    - _Metrics_: The proportion (percentage) of currently suitable habitat that falls within existing PAs, and the percentage change in suitable habitat inside PAs projected for 2070 under RCP2.6 and RCP8.5.
- **Projected changes in conservation status of species**:
    - _Variables/Metrics_: The number and percentage of modeled species falling into IUCN Red List threat categories (Extinct, Critically Endangered, Endangered, Vulnerable, Near Threatened, Least Concern) under present and future (RCP2.6 and RCP8.5) conditions.

**Discussion**

- **Qualitative Concepts**: **Actual niche truncation** caused by anthropogenic factors (like lowland forest clearance and hunting that confine species to PAs) vs. **apparent niche truncation** caused by data limitations. Additional concepts include the pre-adaptation of open-country amphibians and reptiles to warmer conditions, biotic interactions, dispersal limitations, and the uncertainties introduced by stacking species distribution models.

**Management recommendations**

- **Qualitative Concepts**: Protected area complexes, ecological corridors, south-to-north and low-to-high altitude connectivity, assisted migration, and the necessity of long-term monitoring (e.g., using altitudinal transects) to detect early climate change impact signals.

**Methods**

- **Study area**:
    - _Variables/Concepts_: Geographic regions of Thailand and IUCN-defined PA categories (National Parks, Wildlife Sanctuaries, Non-hunting Areas, Forest Parks).
- **Environmental data**:
    - _Physical variables_: Altitude, slope, aspect, and soil pH.
    - _Bioclimatic variables_: Eight variables related to temperature, precipitation, and their seasonality.
    - _Vegetation variables_: Percentage forest cover and tree density per square kilometer.
    - _Climate scenarios_: Three Earth System Models (CNRM-CM5, GFDL-CM3, HadGEM2-ES) run under two Representative Concentration Pathways (RCP2.6 and RCP8.5).
- **Species occurrence data**:
    - _Metrics_: A minimum threshold of 10 unique occurrence records per species to be included in the models, after filtering duplicates and suspect records.
- **Species distribution modeling**:
    - _Variables/Metrics_: Maxent modeling outputs converted to binary presence-absence maps using a 10% cumulative logistic threshold, evaluated by the continuous Boyce Index.
- **Assessment of climate change impacts**:
    - _Metrics_: Habitat area classifications (gained, lost, or stable habitat).
    - _Variables_: Custom criteria thresholds modifying the IUCN Red List system to evaluate future extinction risk based strictly on projected habitat loss (e.g., Extinct = 100% loss of suitable habitat by 2070, Critically Endangered > 80% loss, Endangered = 50-80% loss).


---

## Step 1C — Tables

**Query**

```text
For the source document "6-Vulnerability to climate change of species in protected areas in Thailand": Extract and list only the tables mentioned, along with their exact titles/captions and their analytical focus. Do not summarize or harmonize.
```

**Raw Response**

Based on the source document "6-Vulnerability to climate change of species in protected areas in Thailand," here are the extracted tables, their exact captions, and their analytical focus:

- **Table 1**
    
    - **Exact Title/Caption:** "Numbers of species and location records used in the analyses for each taxonomic group from localities below and above 250 m above sea-level, and the percentage of the land area in each altitudinal belt protected."
    - **Analytical Focus:** Assesses the spatial coverage and representativeness of the biodiversity data by breaking down species and occurrence records across taxonomic groups based on altitude (<250m vs. >250m) and comparing it against the percentage of protected land in those altitudinal belts.
- **Table 2**
    
    - **Exact Title/Caption:** "Estimated maximum species richness (per km2) and the total area with the highest richness level for each region of Thailand for the present and projected for 2070, using three earth system models and two RCPs."
    - **Analytical Focus:** Analyzes spatial changes in biodiversity by comparing current species richness against projected future species richness (for the year 2070) across different geographical regions of Thailand under various climate models and emission scenarios.
- **Table 3**
    
    - **Exact Title/Caption:** "The extent of suitable habitat for species within protected areas in Thailand currently and projected for 2070 for five taxa using three earth system models and two RCPs."
    - **Analytical Focus:** Evaluates the climate change impacts on species within protected areas by calculating the current percentage of suitable habitat that falls within these zones and contrasting it with the projected percentage changes in suitable habitat inside protected areas for 2070.
- **Table 4**
    
    - **Exact Title/Caption:** "Current and projected 2070 conservation statuses of the modeled species."
    - **Analytical Focus:** Determines the vulnerability and projected extinction risk of species by estimating the percentage of modeled species that fall into different IUCN Red List threat categories (e.g., Extinct, Critically Endangered, Endangered, Vulnerable) under present conditions versus projected 2070 scenarios (RCP2.6 and RCP8.5).

---

## Step 1D — Figures

**Query**

```text
For the source document "6-Vulnerability to climate change of species in protected areas in Thailand": Extract and list only the figures mentioned, along with their exact titles/captions and their analytical focus. Do not summarize or harmonize.
```

**Raw Response**

Based on the source document "6-Vulnerability to climate change of species in protected areas in Thailand," here are the figures mentioned, along with their exact captions and their analytical focus:

- **Figure 1**
    
    - **Exact Title/Caption:** "Figure 1. Thailand: location and protected area system, showing the protected area complexes used for management (DNP 2019). Maps created in ArcMap 10.5 (https://support.esri.com/en/products/desktop/arcgis-desktop/arcmap/10-5-1)."
    - **Analytical Focus:** Visualizes the geographical layout of Thailand's protected area system, specifically highlighting the spatial distribution of the different protected area complexes designed to improve connectivity between fragmented habitats.
- **Figure 2**
    
    - **Exact Title/Caption:** "Figure 2. Maps of (a) the six regions of Thailand used in the text, and (b–f) species occurrence locations used in the analyses for each major taxon. Maps created in ArcMap 10.5 (https://support.esri.com/en/products/desktop/arcgis-desktop/arcmap/10-5-1)."
    - **Analytical Focus:** Displays the spatial coverage and patchiness of the baseline biodiversity data by mapping the distinct occurrence locations across Thailand's six regions for the specific taxa analyzed (amphibians, reptiles, mammals, birds, and plants).
- **Figure 3**
    
    - **Exact Title/Caption:** "Figure 3. Spatial patterns of predicted species richness levels for each major taxon under current conditions. Maps created in ArcMap 10.5 (https://support.esri.com/en/products/desktop/arcgis-desktop/arcmap/10-5-1)."
    - **Analytical Focus:** Establishes the baseline spatial distribution of species richness (classified into lowest to highest levels) across Thailand for the five major taxonomic groups modeled prior to introducing climate change projections.
- **Figure 4**
    
    - **Exact Title/Caption:** "Figure 4. Projected changes in suitable habitat by 2070 (a) without and (b) with dispersal to newly suitable habitat for species in five taxa with three earth system models and two RCPs. Red colors represent projected habitat loss, yellow stability, and green expansion."
    - **Analytical Focus:** Quantifies species vulnerability by illustrating the percentage of species in each taxon expected to lose, maintain, or gain suitable habitat by 2070. It compares these outcomes across different Earth System Models, emission scenarios (RCP2.6 and RCP8.5), and dispersal capabilities (no dispersal vs. unlimited dispersal).

---

## Step 1E — Hypothesis & Labels

**Query**

```text
For the source document "6-Vulnerability to climate change of species in protected areas in Thailand": Extract only the core research hypothesis plus named study areas, climate hazards, target variables, and geographical labels. Do not summarize or harmonize.
```

**Raw Response**

Based on the source document "6-Vulnerability to climate change of species in protected areas in Thailand," here is the extracted information:

**Core Research Hypothesis / Major Research Questions**

- How complete and representative is the available biodiversity data?
- How will patterns of species richness in Thailand change by 2070 under projected climate change?
- How will the availability of habitat change for individual species change by 2070 under projected climate change?
- What will be the impact of projected climate change on species within protected areas?

**Named Study Areas**

- Thailand
- Indo-Burma biodiversity hotspot
- Protected areas (PAs), specifically:
    - Wildlife Sanctuaries (IUCN category Ia)
    - National Parks (II)
    - Non-hunting Areas (IV)
    - Forest Parks (V)
- 17 ‘forest complexes’ and three marine complexes
- Chao Phraya River basin (implicitly contextualized in broader lowlands, though not specifically the focus of the models)
- Neighboring borders: Laos, Cambodia, Myanmar, and Malaysia

**Climate Hazards**

- Climate change / warming
- Warmer and sometimes drier conditions
- Changes in temperature and precipitation (and their seasonality)
- Climatic extremes (floods, droughts, and extreme temperature maxima)

**Target Variables**

- Species occurrence/location records
- Taxonomic and spatial coverage
- Species richness (classified into lowest, low, moderate, high, and highest)
- Suitable habitat area (gained habitat, lost habitat, and stable habitat)
- Conservation status/extinction risk (Extinct, Critically Endangered, Endangered, Vulnerable, Near Threatened, Least Concern)
- Physical variables: altitude, slope, aspect, and soil pH
- 8 bioclimatic variables related to precipitation, temperature, and their seasonality
- Continuous Boyce Index (for model predictive performance)

**Geographical Labels**

- North
- Northeast
- Central
- East
- South
- Western
- Lowlands (< 250 m elevation)
- Uplands / mountainous areas (> 250 m a.s.l.)

---

## Step 1F — Limitations / Uncertainties / Caveats

**Query**

```text
For the source document "6-Vulnerability to climate change of species in protected areas in Thailand": Extract only the explicit limitations, uncertainties, assumptions, caveats, or scope constraints stated by the authors. Return each item as a short bullet with the exact section and page number if available. Do not infer or rewrite. Stop and report if none are stated.
```

**Raw Response**
Based on the source document "6-Vulnerability to climate change of species in protected areas in Thailand," here are the explicit limitations, uncertainties, assumptions, caveats, and scope constraints stated by the authors. _(Note: Exact page numbers are not available in the provided text excerpts, but the exact sections are listed below)._

**Abstract**

- "SDMs [species distribution models] are sensitive to truncation of the climate space currently occupied by habitat loss and hunting, and apparent truncation by data limitations."
- "Niche truncation may therefore have resulted in overestimation of vulnerability for some mammal and plant species, while data limitations have likely led to underestimation of the threat to forest-dependent amphibians and reptiles."

**Introduction**

- "Accurate locality data for most taxa other than birds comes mainly from the PAs and even there is very incomplete."

**Results (Data completeness and representativeness & Projected changes in conservation status)**

- "For vertebrates, coverage largely reflected detectability in the field and many smaller species were surveyed inadequately, if at all... few bats and no insectivores were covered, and coverage of rodents and treeshrews was incomplete."
- Projected responses for individual species "...in some cases, may reflect data limitations more than climate-change vulnerability."

**Discussion**

- "The use of correlative species distribution models (SDMs) to model climate change impacts on species distributions rests on the assumption that the location data used to model the current distributions represents the entire climate space in which each species can live as part of a community."
- "If the climate space currently occupied has been truncated in some way, then the models will underestimate potential future distribution and thus potentially overestimate the impacts of climate change."
- "...the bias in our location dataset to existing PAs, particularly for mammals, and the exclusion of areas outside Thailand (because of sparse data from neighboring regions of Myanmar and Laos...)... are artificial cut-offs which may influence model projections."
- Amphibian and reptile datasets are "dominated by widespread open-country and forest edge species—because forest-dependent species need special techniques for effective surveys" and thus the projected increase in richness "probably masks a real threat to forest-dependent species."
- Because dispersal components for the vast majority of species would just be a guess, the authors assumed and modeled scenarios using strict ends of the spectrum: "‘no dispersal’ and ‘unlimited dispersal’ (i.e., all suitable niche space in Thailand is occupied) to bracket the range of possibilities."
- Vegetation and available habitat are strongly influenced by the fire regime, "which was not included in our models."
- "Secondly, our models also do not include the direct ecophysiological effects of rising carbon dioxide levels, which will likely favor C3 trees over C4 grasses..."
- "We also could not model the impacts of rare climatic extremes, such as floods, droughts, and extreme temperature maxima, or the secondary effects of primary impacts on important predator and prey species, and on essential mutualists."
- "...converting projections for changes in bioclimate into projections of conservation impacts is still prone to errors and uncertainties."

**Methods (Environmental data)**

- "For future projections, we assumed that temperature and precipitation were changing, and that other variables (topography, soil, and vegetation) were stable, so our analysis represents the impacts of climate alone."

---

## Step 2A — Data completeness and representativeness

**Query**

```text
For the source document "6-Vulnerability to climate change of species in protected areas in Thailand": Extract only the paper's findings on data completeness and representativeness across taxa and altitude bands. Include the taxonomic groups covered, the number of modeled species or locality records if stated, lowland versus upland coverage, and any explicit statements about sampling gaps or detectability bias. Do not infer or harmonize.
```

**Raw Response**

Based on the source document "6-Vulnerability to climate change of species in protected areas in Thailand," here are the findings regarding current and projected species richness patterns:

**Named Regions and Richness Categories**

- **Named Regions:** North, Northeast, Central, East, South, and Western.
- **Richness Categories:** Lowest, low, moderate, high, and highest.

**Current Species Richness Patterns**

- **Maximum Current Richness:** Estimated maximum species richness per 1x1 km grid cell is 31 species for amphibians, 49 for reptiles, 60 for mammals, 440 for birds, and 458 for plants.
- **Regional Concentration of Highest Richness:** Grid cells with the highest estimated current richness are concentrated in specific regions depending on the taxon:
    - _Amphibians:_ Central, East, and South regions.
    - _Reptiles:_ East region.
    - _Mammals:_ Western, Central, and Northeast regions.
    - _Birds and Plants:_ North region.

**Projected Species Richness Patterns for 2070**

- **General Trends:** Maximum species richness is projected to decline for all taxa under all scenarios, with the number of grid cells in the highest richness class declining for mammals, birds, and plants. Mammals are projected to experience the largest declines.
- **RCP2.6 vs. RCP8.5:** Reductions in species richness are generally most severe under the RCP8.5 emission scenario compared to RCP2.6.
- **Taxa-Specific Differences Across Models and Scenarios:**
    - _Mammals and Birds:_ Both groups show projected declines in all six regions under all three Earth System Models (CNRM-CM5, GFDL-CM3, HadGEM2-ES) and under both RCP2.6 and RCP8.5 scenarios.
    - _Plants:_ Plant richness shows consistent declines under the RCP8.5 scenario; however, under the RCP2.6 scenario, the projections are both model-dependent and region-dependent.
    - _Amphibians and Reptiles:_ Diversity for these taxa is generally projected to increase, though this projected increase is model- and region-dependent at the highest species richness levels.

---

## Step 2B — Species richness change by region

**Query**

```text
For the source document "6-Vulnerability to climate change of species in protected areas in Thailand": Extract only the findings on current and projected species richness patterns by region of Thailand for 2070. Include the named regions, richness categories or maximum richness values if stated, and how projections differ across earth system models and RCP2.6 versus RCP8.5. Do not infer or harmonize.
```

**Raw Response**

Based on the source document "6-Vulnerability to climate change of species in protected areas in Thailand," here are the findings on projected changes in suitable habitat for individual species by 2070:

**Taxa Compared** The analysis compared mammals, plants, birds, reptiles, and amphibians.

**Findings under the "No Dispersal" Assumption** _(Assuming expansion into newly suitable areas is not possible)_

- **Under the RCP2.6 scenario:**
    
    - **Mammals:** 1–4% of species are projected to lose all currently suitable habitat, and 26–64% are projected to lose more than half.
    - **Plants, Birds, and Reptiles:** 0–2% of species in these groups are projected to lose all suitable habitat. The percentage projected to lose more than half is 14–41% for plants, 23–48% for birds, and 4–26% for reptiles.
    - **Amphibians:** No species (0%) are projected to lose all suitable habitat, and 0–19% are projected to lose more than half.
- **Under the RCP8.5 scenario:**
    
    - **Mammals:** 1–11% of species are projected to lose all currently suitable habitat, and 60–65% are projected to lose more than half.
    - **Birds:** 1–8% of species are projected to lose all suitable habitat, and 57–62% are projected to lose more than half.
    - **Plants:** 1–5% of species are projected to lose all suitable habitat, and 41–54% are projected to lose more than half.
    - **Reptiles:** No species (0%) are projected to lose all suitable habitat, and 28–34% are projected to lose more than half.
    - **Amphibians:** No species (0%) are projected to lose all suitable habitat, and 10–35% are projected to lose more than half.

**Findings under the "Unlimited Dispersal" Assumption** _(Assuming species can expand into newly suitable areas anywhere in Thailand)_

- **Amphibians and Reptiles:** The proportion of species projected to experience a net expansion in suitable habitat is greater than the proportion projected to experience a net contraction.
- **Mammals, Birds, and Plants:** The proportion of species projected to experience a net contraction in suitable habitat is greater than the proportion projected to experience a net expansion.
- **Mammals specifically:** Under all scenarios, less than 25% of mammal species are projected to expand their ranges.

---

## Step 2C — Habitat change for individual species

**Query**

```text
For the source document "6-Vulnerability to climate change of species in protected areas in Thailand": Extract only the findings on projected changes in suitable habitat for individual species by 2070. Include results under both `no dispersal` and `unlimited dispersal` assumptions, the taxa compared, and any stated percentages or thresholds for habitat loss, stability, or expansion. Do not infer or harmonize.
```

**Raw Response**

Based on the source document "6-Vulnerability to climate change of species in protected areas in Thailand," here are the findings regarding projected changes in suitable habitat for individual species by 2070:

**Taxa Compared** The analysis compared mammals, plants, birds, reptiles, and amphibians.

**Findings under the "No Dispersal" Assumption** _(Assuming expansion into newly suitable areas is not possible)_

- **Under the RCP2.6 scenario:**
    
    - **Mammals:** 1–4% of species are projected to lose all currently suitable habitat, and 26–64% are projected to lose more than half.
    - **Plants, Birds, and Reptiles:** 0–2% of species in these groups are projected to lose all suitable habitat. The percentage of species projected to lose more than half is 14–41% for plants, 23–48% for birds, and 4–26% for reptiles.
    - **Amphibians:** No species (0%) are projected to lose all suitable habitat, and 0–19% are projected to lose more than half.
- **Under the RCP8.5 scenario:**
    
    - **Mammals:** 1–11% of species are projected to lose all currently suitable habitat, and 60–65% are projected to lose more than half.
    - **Birds:** 1–8% of species are projected to lose all suitable habitat, and 57–62% are projected to lose more than half.
    - **Plants:** 1–5% of species are projected to lose all suitable habitat, and 41–54% are projected to lose more than half.
    - **Reptiles:** No species (0%) are projected to lose all suitable habitat, and 28–34% are projected to lose more than half.
    - **Amphibians:** No species (0%) are projected to lose all suitable habitat, and 10–35% are projected to lose more than half.

**Findings under the "Unlimited Dispersal" Assumption** _(Assuming species can expand into newly suitable areas anywhere in Thailand)_

- **Amphibians and Reptiles:** The proportion of species projected to show a net expansion in suitable habitat is greater than the proportion projected to show a net contraction.
- **Mammals, Birds, and Plants:** The proportion of species projected to show a net contraction in suitable habitat is greater than those projected to show a net expansion.
- **Mammals (specifically):** Under all scenarios, fewer than 25% of mammal species are projected to expand their ranges.


---

## Step 2D — Protected area impacts

**Query**

```text
For the source document "6-Vulnerability to climate change of species in protected areas in Thailand": Extract only the findings on impacts within protected areas. Include the current proportion of suitable habitat inside protected areas, projected change by 2070 inside protected areas, differences across taxa, and differences across models or RCPs if stated. Do not infer or harmonize.
```

**Raw Response**

**Current Proportion of Suitable Habitat Inside Protected Areas (PAs)** The proportion of currently suitable habitat that falls within existing PAs varies significantly across taxa:

- **Mammals:** 43%.
- **Plants:** 37% (according to Table 3).
- **Birds:** 37% (according to the main text) or 26% (according to Table 3).
- **Reptiles:** 22%.
- **Amphibians:** 17%.

**Projected Change by 2070 Inside Protected Areas (Differences Across Taxa, Models, and RCPs)**

- **General Trends by Taxa:** Overall, the extent of suitable habitat within PAs is projected to increase for modeled amphibians and reptiles across all scenarios, while it is projected to decrease for mammals, birds, and plants, particularly under the RCP8.5 scenario.
- **Mammals:** Suitable habitat for mammals inside PAs is projected to experience losses of 26–38% under RCP8.5. Even assuming full dispersal capabilities, mammal richness is projected to decline in 59–82% of individual PAs under RCP2.6, and in 69–77% of PAs under RCP8.5.
- **Birds and Plants:** Projected impacts on birds and plants within PAs vary between the different Earth System Models under the RCP2.6 scenario, but declines dominate under the RCP8.5 scenario.
- **Amphibians and Reptiles:** In contrast to the other taxa, most PAs have large projected increases in amphibian and reptile richness across all models and scenarios.

**Impacts Across Protected Area Complexes**

- Under RCP8.5, all PA complexes have projected declines in the extent of suitable habitat for modeled mammals, birds, and plants, with the exception of the three northernmost complexes (where habitat changes vary among the models) and three complexes in the northern Central and Northeast regions specifically for birds.
- Conversely, all PA complexes have projected increases in suitable habitat for modeled amphibians and reptiles.

---

## Step 2E — Conservation status shifts

**Query**

```text
For the source document "6-Vulnerability to climate change of species in protected areas in Thailand": Extract only the findings on projected changes in conservation status by 2070. Include the present and future counts or percentages of species in each threat category if stated, and distinguish results by taxonomic group, earth system model, and RCP where available. Do not infer or harmonize.
```

**Raw Response**

Based on the source document "6-Vulnerability to climate change of species in protected areas in Thailand," here are the findings on projected changes in conservation status by 2070.

_(Note: The findings provide data broken down by taxonomic group and Representative Concentration Pathway (RCP) scenarios, but the specific conservation status percentages are not explicitly broken down by individual Earth System Models (ESMs) in the provided text)._

**General Findings**

- **Overall Threat Increase:** The overall percentage of modeled species assessed as threatened is projected to increase from 11% under current conditions to 35% under the RCP2.6 scenario, and to 54% under the RCP8.5 scenario.
- **Trend by Category:** The number of modeled species in all threat categories is projected to increase by 2070 under RCP2.6, while those rated as "Least Concern" will more than halve. Under RCP8.5, the numbers of Endangered, Critically Endangered, and Extinct species will specifically increase.
- **Projected Extinctions:** By 2070 under the RCP8.5 scenario, 11 modeled species are projected to become extinct in Thailand. This count includes one primate, six bird species, and four plant species.

**Detailed Percentages by Taxonomic Group and Threat Category (Current vs. 2070 Projections)** Below is the breakdown of the percentage of species in each IUCN threat category under Current, RCP2.6, and RCP8.5 conditions:

**Amphibians**

- **Extinct (EX):** Current (0%), RCP2.6 (0%), RCP8.5 (0%)
- **Critically Endangered (CR):** Current (0%), RCP2.6 (0%), RCP8.5 (3%)
- **Endangered (EN):** Current (0%), RCP2.6 (3%), RCP8.5 (10%)
- **Vulnerable (VU):** Current (0%), RCP2.6 (13%), RCP8.5 (13%)
- **Near Threatened (NT):** Current (6%), RCP2.6 (16%), RCP8.5 (13%)
- **Least Concern (LC):** Current (94%), RCP2.6 (68%), RCP8.5 (61%)
- **Total Threatened Species:** Current (0%), RCP2.6 (16%), RCP8.5 (26%)

**Reptiles**

- **Extinct (EX):** Current (0%), RCP2.6 (0%), RCP8.5 (0%)
- **Critically Endangered (CR):** Current (0%), RCP2.6 (0%), RCP8.5 (8%)
- **Endangered (EN):** Current (2%), RCP2.6 (9%), RCP8.5 (13%)
- **Vulnerable (VU):** Current (2%), RCP2.6 (13%), RCP8.5 (8%)
- **Near Threatened (NT):** Current (2%), RCP2.6 (17%), RCP8.5 (8%)
- **Least Concern (LC):** Current (94%), RCP2.6 (60%), RCP8.5 (64%)
- **Total Threatened Species:** Current (4%), RCP2.6 (23%), RCP8.5 (28%)

**Mammals**

- **Extinct (EX):** Current (0%), RCP2.6 (0%), RCP8.5 (1%)
- **Critically Endangered (CR):** Current (0%), RCP2.6 (1%), RCP8.5 (36%)
- **Endangered (EN):** Current (3%), RCP2.6 (30%), RCP8.5 (20%)
- **Vulnerable (VU):** Current (14%), RCP2.6 (30%), RCP8.5 (11%)
- **Near Threatened (NT):** Current (6%), RCP2.6 (16%), RCP8.5 (8%)
- **Least Concern (LC):** Current (78%), RCP2.6 (23%), RCP8.5 (24%)
- **Total Threatened Species:** Current (16%), RCP2.6 (61%), RCP8.5 (69%)

**Birds**

- **Extinct (EX):** Current (0%), RCP2.6 (0%), RCP8.5 (1%)
- **Critically Endangered (CR):** Current (0%), RCP2.6 (2%), RCP8.5 (25%)
- **Endangered (EN):** Current (1%), RCP2.6 (17%), RCP8.5 (22%)
- **Vulnerable (VU):** Current (10%), RCP2.6 (16%), RCP8.5 (11%)
- **Near Threatened (NT):** Current (9%), RCP2.6 (20%), RCP8.5 (13%)
- **Least Concern (LC):** Current (80%), RCP2.6 (44%), RCP8.5 (29%)
- **Total Threatened Species:** Current (11%), RCP2.6 (35%), RCP8.5 (59%)

**Plants**

- **Extinct (EX):** Current (0%), RCP2.6 (0%), RCP8.5 (1%)
- **Critically Endangered (CR):** Current (0%), RCP2.6 (2%), RCP8.5 (16%)
- **Endangered (EN):** Current (4%), RCP2.6 (14%), RCP8.5 (23%)
- **Vulnerable (VU):** Current (7%), RCP2.6 (19%), RCP8.5 (12%)
- **Near Threatened (NT):** Current (4%), RCP2.6 (30%), RCP8.5 (18%)
- **Least Concern (LC):** Current (85%), RCP2.6 (36%), RCP8.5 (31%)
- **Total Threatened Species:** Current (11%), RCP2.6 (35%), RCP8.5 (52%)

---

## Step 2F — Management recommendations

**Query**

```text
For the source document "6-Vulnerability to climate change of species in protected areas in Thailand": Extract only the explicit management recommendations proposed by the authors. Include references to protected area complexes, ecological corridors, south-to-north and low-to-high altitude connectivity, assisted migration, and long-term monitoring if mentioned. Do not infer or harmonize.
```

**Raw Response**

Based on the source document "6-Vulnerability to climate change of species in protected areas in Thailand," here are the explicit management recommendations proposed by the authors:

- **Protected Area Complexes and Corridors:** Address habitat fragmentation through the establishment of protected area (PA) complexes. Where possible, existing connections should be used to allow species movement, and options for connecting additional areas via ecological corridors or steppingstones should be investigated.
- **Directional Connectivity:** Prioritize establishing south-to-north and low-to-high altitude connectivity, which will be particularly important for allowing species to move in response to climate change.
- **Assisted Migration and In Situ Support:** Because many species will not be able to track rapid climate change over the next 50 years, mitigation impacts should include in situ support and assisted migration to other protected areas.
- **Long-term Monitoring:** Make long-term monitoring of species and communities a management priority to detect early signals of climate change impacts, given the certainty of future warming but uncertainty of biological responses.
- **Altitudinal Transects:** Establish permanent altitudinal transects in protected areas from south to north Thailand as a monitoring tool, since steep temperature gradients amplify expected warming responses. This monitoring over multiple decades will require leadership and supervision from the Department of National Parks, Wildlife and Plant Conservation (DNP).

---

## Step 3 — Synthesis / Gap Sweep

**Query**

```text
For the source document "6-Vulnerability to climate change of species in protected areas in Thailand": Extract only the explicit limitations, source data gaps, model assumptions, omitted processes, and uncertainties stated by the authors. Return each item as a short bullet with the exact section and page number if available. Do not infer or harmonize.
```

**Raw Response**

Based on the source document "6-Vulnerability to climate change of species in protected areas in Thailand," here are the explicit limitations, source data gaps, model assumptions, omitted processes, and uncertainties stated by the authors. _(Note: Exact page numbers are not available in the provided text excerpts)._

**Abstract**

- Species Distribution Models (SDMs) are sensitive to actual niche truncation caused by habitat loss and hunting, as well as apparent truncation caused by data limitations.
- Lowland forest clearance biases records for forest-dependent species toward cooler uplands, while hunting confines larger vertebrates to protected areas.
- Data for amphibians and reptiles is biased toward lowland non-forest taxa.
- Niche truncation may cause overestimation of vulnerability for mammal and plant species, while data limitations may cause underestimation of threats to forest-dependent amphibians and reptiles.
- There are many uncertainties regarding the actual biological responses to climate change.

**Introduction**

- The region is relatively data-poor with incomplete species lists, inadequate conservation assessments, and a lack of data on population sizes and trends for threatened species.
- Most plant and invertebrate species have not yet been globally assessed by the IUCN.
- Accurate locality data for most taxa (other than birds) comes mainly from protected areas and is very incomplete.

**Results: Data completeness and representativeness**

- Vertebrate data coverage largely reflected field detectability, meaning many smaller species were surveyed inadequately or not at all.
- Few bats and no insectivores were covered, and data for rodents and treeshrews was incomplete.
- Only 12% of Thailand's reptiles and 16% of amphibians were included, and no threatened species from either group had enough locality data (minimum 10 records) to be modeled.
- Projected responses of individual species may reflect data limitations more than their actual climate-change vulnerability.

**Discussion**

- **Assumption:** The use of correlative SDMs assumes that the location data used to model current distributions represents the entire climate space in which each species can live.
- If the occupied climate space is truncated, the models underestimate potential future distribution and thus overestimate the impacts of climate change.
- The location dataset's bias toward existing protected areas, and the exclusion of areas outside Thailand (due to sparse data from bordering Myanmar and Laos), are artificial cut-offs that may influence model projections.
- Amphibian and reptile datasets are dominated by widespread open-country and forest edge species because true forest-dependent species require special techniques for effective surveys.
- Because dispersal ability for the vast majority of species would just be a guess, the models assumed strict endpoints of "no dispersal" and "unlimited dispersal" to bracket possibilities.
- **Omitted Process:** The models do not include the fire regime, which strongly influences vegetation and available habitat.
- **Omitted Process:** The models do not include the direct ecophysiological effects of rising carbon dioxide levels (which will likely favor C3 trees over C4 grasses).
- **Omitted Process:** The models do not account for the impacts of rare climatic extremes (floods, droughts, extreme temperature maxima) or the secondary effects on predator/prey species and essential mutualists.
- Converting projections for bioclimatic changes into projections of conservation impacts remains prone to errors and uncertainties.

**Methods**

- Data for soil phosphorus, which is an important filter of plant distributions, is not available for Thailand with useful accuracy or spatial resolution.
- Our understanding of how tropical climates specifically filter species distributions is still weak, and the mechanistic basis of correlations between environmental variables and current distributions is rarely known.
- **Assumption:** For future projections, the authors assumed temperature and precipitation would change, but that topography, soil, and vegetation would remain stable, meaning the analysis represents the impacts of climate alone.
- Extinction risk assessments for individual species based only on climate change projections omit other non-climatic factors and unpredictable interactions, and thus should not be used in isolation for conservation planning.