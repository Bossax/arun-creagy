# raw-copy — ART01_CMIP6_Water_Crop

- **Source Title Target**: `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf`
- **Purpose**: Phase 3A targeted gap-retrieval after human edit and decision-log review
- **Rule**: Paste NotebookLM responses verbatim under each query block. Do not harmonize inside NotebookLM.

---

## Phase 3A Packet A — Cropping system definitions and study setup

### Query A1 — Cropping system labels
For the source document `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf`: Extract the exact definitions of the cropping-system labels `RRR`, `RR`, `RM`, `RS`, `RB`, `MM`, and `CS`. For each label, list the crop sequence, whether it is irrigated or rain-fed, and the relevant season or planting-calendar reference. If the document is missing or the title is ambiguous, stop and report that explicitly.

#### Raw Response

**RRR (Triple cropping of rice)**

- **Exact Definition & Crop Sequence:** A business-as-usual cropping system consisting of the triple cropping of rice cultivated three times a year (first, second, and third rice crops).
- **Irrigation Status:** Irrigated areas.
- **Relevant Season/Planting Calendar:** Cultivated year-round. The third rice crop is grown from mid-February to May, the first rice crop is grown in the rainy season from June to mid-October, and the second rice crop is grown in the dry season from mid-October to mid-February.

**RR (Double cropping of rice)**

- **Exact Definition & Crop Sequence:** A business-as-usual cropping system consisting of the double cropping of rice cultivated twice a year (first and second rice crops).
- **Irrigation Status:** Rain-fed areas.
- **Relevant Season/Planting Calendar:** The first rice crop is grown in the rainy season from June to mid-October, and the second rice crop is grown in the dry season from mid-October to mid-February.

**RM (First rice and maize)**

- **Exact Definition & Crop Sequence:** An adaptation strategy consisting of the double cropping of rice cultivated once (first rice crop) followed by maize.
- **Irrigation Status:** Rain-fed areas.
- **Relevant Season/Planting Calendar:** The first rice crop is grown in the rainy season from June to mid-October, and the maize crop is grown in the dry season from mid-October to January.

**RS (First rice and soybean)**

- **Exact Definition & Crop Sequence:** An adaptation strategy consisting of the double cropping of rice cultivated once (first rice crop) followed by soybean.
- **Irrigation Status:** Rain-fed areas.
- **Relevant Season/Planting Calendar:** The first rice crop is grown in the rainy season from June to mid-October, and the soybean crop is grown in the dry season from mid-October to January.

**RB (First rice and mung bean)**

- **Exact Definition & Crop Sequence:** An adaptation strategy consisting of the double-cropping of rice cultivated once (first rice crop) followed by mung bean.
- **Irrigation Status:** Rain-fed areas.
- **Relevant Season/Planting Calendar:** The first rice crop is grown in the rainy season from June to mid-October, and the mung bean crop is grown in the dry season from mid-October to January.

**MM (Twice cropping of maize)**

- **Exact Definition & Crop Sequence:** An adaptation strategy consisting of the double cropping of maize cultivated twice a year (first and second maize crops).
- **Irrigation Status:** Rain-fed areas.
- **Relevant Season/Planting Calendar:** The first maize crop is grown in the rainy season from June to mid-October, and the second maize crop is grown in the dry season from mid-October to January.

**CS (Cassava)**

- **Exact Definition & Crop Sequence:** An adaptation strategy consisting of a single continuous cassava production crop.
- **Irrigation Status:** Rain-fed areas.
- **Relevant Season/Planting Calendar:** Cassava is cultivated over an extended period, spanning from roughly March to February of the following year.


---

### Query A2 — Study area grounding
For the source document `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf`: Extract the exact description of the study area. List the province, districts or sub-districts if specified, and the paper’s explanation of why this area was selected. Cite the exact section, table, or figure anchor. If the document is missing or the title is ambiguous, stop and report that explicitly.

#### Raw Response
Based on the source document, here is the exact description of the study area and the rationale for its selection:

**Description of the Study Area**

- **Province:** The study area is **Phichit province**, which is located in the lower north of Thailand, where the Yom and Nan rivers flow parallel to each other before merging (Section 2.1. Study areas).
- **Districts and Sub-districts:** The specific sampling sites are broken down by cropping systems across seven districts and their respective sub-districts (Table 1):
    - **Sam Ngam** district (Rang Nok sub-district)
    - **Taphan Hin** district (Thap Man sub-district)
    - **Wang Sai Phun** district (Nong Phra sub-district)
    - **Pho Prathap Chang** district (Phai Tha Pho sub-district)
    - **Bueng Na Rang** district (Pho Sai Ngam sub-district)
    - **Dong Charoen** district (Samnak Kun Nen sub-district)
    - **Thap Khlo** district (Thap Khlo sub-district)

**Why the Area Was Selected** According to the paper, Phichit province was chosen as a case study specifically "due to drought and flood events occurring every year in rain-fed and irrigated areas, respectively" (Section 1. Introduction). The authors explain that during the dry season, both rain-fed and irrigated areas experience water shortages, whereas flood events predominantly damage the areas situated near the Yom and Nan rivers (Section 1. Introduction). This unique geography and its specific vulnerabilities made it an ideal site for investigating adaptation strategies to cope with repeated flood and drought events.

---

### Query A3 — Method chain
For the source document `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf`: Extract the exact methodology setup. Identify the historical baseline period, future periods, SSP scenarios, and the roles of the `EPIC` and `CROPWAT 8.0` models. Also list the main data inputs used for crop, soil, and climate simulation. Cite the exact section anchors. If the document is missing or the title is ambiguous, stop and report that explicitly.

#### Raw Response

**Historical baseline period:** The historical climate data from **1981–2014** served as the baseline scenario (Section 2.2.1. Climate data).

**Future periods:** The future projections were divided into three specific periods: the **near future (2015–2039)**, the **mid future (2040–2069)**, and the **far future (2070–2100)** (Section 2.2.1. Climate data).

**SSP scenarios:** The methodology assessed two specific Shared Socioeconomic Pathways from the CMIP6 global circulation model: **SSP245** (representing a medium radiation emission scenario at 538.9 ppm CO2 equivalent) and **SSP585** (representing the highest radiation emission scenario at 936.4 ppm CO2 equivalent) (Section 2.2.1. Climate data).

**Roles of the models:**

- **EPIC model:** The Environmental Policy Integrated Climate (EPIC) model version 0810 was utilized to **simulate crop yields**. It functions as an integrated model of the soil-water-atmosphere system to evaluate the impacts of climate change, tracking factors like carbon and nitrogen cycling, nutrient leaching, and crop growth stressors (Section 2.3. Crop yield simulation).
- **CROPWAT 8.0 model:** This model was employed to **calculate evapotranspiration** using the FAO Penman–Monteith method. The evapotranspiration rates calculated by this model were essential for determining crop water use (CWU) to calculate the green and blue water footprints (Section 2.6. WF calculation).

**Main data inputs:**

- **Climate simulation:** The model required daily historical and future climate projections for **precipitation, maximum and minimum temperatures**, alongside historical daily **relative humidity, wind speed, and wind direction** (Section 2.2.1. Climate data).
- **Crop simulation:** Inputs included data for five major crops (rice, maize, soybean, mung bean, and cassava) over the 2020/2021 crop year. Specific variables tracked included the **date of planting, maturity date, harvest date, crop yield, amount and type of fertilizer, and irrigation management** (Section 2.2.2. Crop data).
- **Soil simulation:** Soil samples were collected at three distinct depths (0–10, 10–20, and 20–30 cm) and analyzed for numerous properties: **soil bulk density, soil texture, pH, electrical conductivity (ECe), cation exchange capacity (CEC), organic carbon, available phosphorus, potassium, calcium, and magnesium**, as well as the **wilting point and field capacity** parameters (Section 2.2.3. Soil data).
---

## Phase 3A Packet B — BAU irrigated vs rain-fed yield contrasts

### Query B1 — BAU irrigated rice yields
For the source document `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf`: Extract the exact findings for business-as-usual irrigated rice yields from `Table 4` and any directly relevant surrounding text. Separate results by rice crop in the sequence, scenario, and future period. Include exact table or section citations. If the document is missing or the title is ambiguous, stop and report that explicitly.

#### Raw Response

**Overview of Irrigated Rice Findings** In business-as-usual irrigated areas (the "RRR" cropping system, where rice is grown three times a year), the historical baseline yields are 6,300 kg ha⁻¹ for the first rice, 5,850 kg ha⁻¹ for the second rice, and 6,150 kg ha⁻¹ for the third rice.

According to **Section 3.2 (Major crop yield changes under CMIP6 climate scenarios)**, under the SSP245 scenario, the crop yields for all three irrigated rice crops are predicted to gradually rise across all three future projection periods. In contrast, under the highest radiation emission scenario (SSP585), all three crops are expected to see only a slight yield increase of 0.4–1.0% in the near future, followed by marked declines of 8.9–11.4% in the mid future and 12.6–18.5% in the far future.

Here are the exact yield results and change projections extracted from **Table 4**:

**First Rice Crop**

- **SSP245 Scenario:** Overall yields are projected to increase by 10.1–12.6%.
    - **2015–2039:** 6,937 kg ha⁻¹ (an increase of 637 kg ha⁻¹)
    - **2040–2069:** 7,055 kg ha⁻¹ (an increase of 755 kg ha⁻¹)
    - **2070–2100:** 7,093 kg ha⁻¹ (an increase of 793 kg ha⁻¹)
- **SSP585 Scenario:**
    - **2015–2039:** 6,327 kg ha⁻¹ (an increase of 27 kg ha⁻¹)
    - **2040–2069:** 5,580 kg ha⁻¹ (a decrease of 720 kg ha⁻¹)
    - **2070–2100:** 5,264 kg ha⁻¹ (a decrease of 1,036 kg ha⁻¹)

**Second Rice Crop**

- **SSP245 Scenario:** This crop sequence will receive the highest positive yield change, increasing by 19.7–33.0% overall.
    - **2015–2039:** 7,000 kg ha⁻¹ (an increase of 1,150 kg ha⁻¹)
    - **2040–2069:** 7,395 kg ha⁻¹ (an increase of 1,545 kg ha⁻¹)
    - **2070–2100:** 7,780 kg ha⁻¹ (an increase of 1,930 kg ha⁻¹)
- **SSP585 Scenario:**
    - **2015–2039:** 5,910 kg ha⁻¹ (an increase of 60 kg ha⁻¹)
    - **2040–2069:** 5,330 kg ha⁻¹ (a decrease of 520 kg ha⁻¹)
    - **2070–2100:** 5,112 kg ha⁻¹ (a decrease of 738 kg ha⁻¹)

**Third Rice Crop**

- **SSP245 Scenario:** Overall yields are projected to increase by 7.1–15.4%.
    - **2015–2039:** 6,585 kg ha⁻¹ (an increase of 435 kg ha⁻¹)
    - **2040–2069:** 6,909 kg ha⁻¹ (an increase of 759 kg ha⁻¹)
    - **2070–2100:** 7,097 kg ha⁻¹ (an increase of 947 kg ha⁻¹)
- **SSP585 Scenario:**
    - **2015–2039:** 6,214 kg ha⁻¹ (an increase of 64 kg ha⁻¹)
    - **2040–2069:** 5,530 kg ha⁻¹ (a decrease of 620 kg ha⁻¹)
    - **2070–2100:** 5,012 kg ha⁻¹ (a decrease of 1,138 kg ha⁻¹)
---

### Query B2 — BAU rain-fed rice yields
For the source document `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf`: Extract the exact findings for business-as-usual rain-fed rice yields from `Table 4` and any directly relevant surrounding text. Separate results by first and second rice crop, scenario, and future period. Include exact table or section citations. If the document is missing or the title is ambiguous, stop and report that explicitly.

#### Raw Response
**Overview of Rain-Fed Rice Findings** In business-as-usual rain-fed areas (the "RR" cropping system, where rice is grown twice a year), the historical baseline yields are **5,930 kg ha⁻¹ for the first rice crop** and **5,850 kg ha⁻¹ for the second rice crop**.

According to **Section 3.2 (Major crop yield changes under CMIP6 climate scenarios)**, the RR cropping system currently produces slightly lower yields than the irrigated RRR system and will face more severe negative impacts under future climate change. Specifically, under the SSP585 scenario, first and second rice crop yields are projected to experience overall reductions of 6.0–14.4% and 7.4–17.7%, respectively. The text notes that these negative impacts in rain-fed areas are driven by elevated temperatures exceeding optimal levels for crop growth, which negate the benefits of increased precipitation and atmospheric CO2. Fortunately, under the SSP245 scenario, first and second rice crop yields will rise in the near-future period by 3.0% and 4.3%, respectively.

Here are the exact yield results and change projections extracted from **Table 4**:

**First Rice Crop**

- **SSP245 Scenario:** Yields are projected to slightly increase in the near and mid future before declining in the far future.
    - **2015–2039:** 6,106 kg ha⁻¹ (an increase of 176 kg ha⁻¹).
    - **2040–2069:** 5,975 kg ha⁻¹ (an increase of 45 kg ha⁻¹).
    - **2070–2100:** 5,804 kg ha⁻¹ (a decrease of 127 kg ha⁻¹).
- **SSP585 Scenario:** Yields are projected to decrease steadily across all future periods.
    - **2015–2039:** 5,576 kg ha⁻¹ (a decrease of 355 kg ha⁻¹).
    - **2040–2069:** 5,185 kg ha⁻¹ (a decrease of 745 kg ha⁻¹).
    - **2070–2100:** 5,075 kg ha⁻¹ (a decrease of 855 kg ha⁻¹).

**Second Rice Crop**

- **SSP245 Scenario:** Yields are expected to increase in the near future but face mild reductions in the mid and far future periods.
    - **2015–2039:** 6,100 kg ha⁻¹ (an increase of 250 kg ha⁻¹).
    - **2040–2069:** 5,795 kg ha⁻¹ (a decrease of 55 kg ha⁻¹).
    - **2070–2100:** 5,780 kg ha⁻¹ (a decrease of 70 kg ha⁻¹).
- **SSP585 Scenario:** Yields are projected to decline severely across all future projection periods.
    - **2015–2039:** 5,417 kg ha⁻¹ (a decrease of 433 kg ha⁻¹).
    - **2040–2069:** 5,130 kg ha⁻¹ (a decrease of 720 kg ha⁻¹).
    - **2070–2100:** 4,812 kg ha⁻¹ (a decrease of 1,038 kg ha⁻¹).

---

### Query B3 — Divergence explanation
For the source document `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf`: Extract the authors’ explicit explanation for why irrigated and rain-fed systems diverge under future climate stress. Quote or list only the mechanisms directly stated by the authors. Include exact section, table, or figure citations. If the document is missing or the title is ambiguous, stop and report that explicitly.

#### Raw Response

The authors explicitly identify the following mechanisms to explain how and why irrigated and rain-fed systems diverge under future climate stress:

- **Lack of Irrigation Causing Dry-Season Water Shortages:** The authors note that the business-as-usual cropping system in rain-fed areas (RR) faces more negative impacts than the irrigated system (RRR) because it is "commonly practiced in rain-fed areas due to the lack of an irrigation system, resulting in water shortages in the dry season" (**Section 3.2**, referencing **Table 4**).
- **Temperatures Exceeding Optimal Growth Levels in Rain-Fed Areas:** Under the severe SSP585 climate scenario, the authors explicitly state that "excessive elevated CO2, supernumerary of the optimal temperature from increasing the maximum and minimum temperatures, was predicted to reduce rice yield, especially in rain-fed areas" (**Section 3.2**, referencing **Table 4** and **Fig. 4(a) and (b)**).
- **Offsetting Factors Benefiting Irrigated Areas:** Conversely, under the moderate SSP245 scenario, rice yields are expected to increase, "especially in irrigated areas due to increased precipitation and elevated CO2 concentration, which will negate the increment of maximum and minimum temperatures" (**Section 3.2**).
- **High Sensitivity to Water Stress and Increased Need for "Blue Water":** The authors explain that rice requires two to three times more water than alternative crops (like maize or soybean) and is highly sensitive to water stress. They state that "the effects of climate change will lead to an increase in the requirement of blue WF [blue water footprint / irrigation water] in the future, especially in rain-fed areas," placing systems without dedicated irrigation at a distinct disadvantage (**Section 3.3**).
---

## Phase 3A Packet C — Water footprint and adaptation logic

### Query C1 — Water footprint definitions
For the source document `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf`: Extract the exact definitions of green, blue, grey, and total water footprint used in the study, including any formula or methodological explanation the authors provide. Cite the exact section anchor. If the document is missing or the title is ambiguous, stop and report that explicitly.

#### Raw Response
**Definitions and Methodological Explanations of Water Footprints**

The study conceptually defines the three specific types of water footprints (WFs) in **Section 1. Introduction** as follows:

- **Green WF:** Precipitation.
- **Blue WF:** Surface water and groundwater.
- **Grey WF:** Freshwater resources used to assimilate pollutants.

The exact methodological calculations and formulas for these footprints are detailed in **Section 2.6. WF calculation**:

**1. Total Water Footprint ($WF_{total}$)**

- **Definition:** The total water footprint in the crop growing process, expressed in cubic meters per ton (m³ ton⁻¹).
- **Formula:** It is the sum of green, blue, and grey water: $WF_{total} = WF_{green} + WF_{blue} + WF_{grey}$.

**2. Green Water Footprint ($WF_{green}$)**

- **Formula:** $WF_{green} = \frac{CWU_{green}}{Y} = 10 \times \frac{\sum_{d=1}^{lgp} ET_{green}}{Y}$.
- **Methodological Explanation:** The green WF is calculated by dividing the green crop water use ($CWU_{green}$) by the crop yield ($Y$). Green water evapotranspiration ($ET_{green}$) is determined by taking the minimum value between actual crop evapotranspiration ($ET_c$) and the effective rainfall available ($P_{eff}$).

**3. Blue Water Footprint ($WF_{blue}$)**

- **Formula:** $WF_{blue} = \frac{CWU_{blue}}{Y} = 10 \times \frac{\sum_{d=1}^{lgp} ET_{blue}}{Y}$.
- **Methodological Explanation:** The blue WF is calculated by dividing the blue crop water use ($CWU_{blue}$) by the crop yield ($Y$). Blue water evapotranspiration ($ET_{blue}$) is calculated as the actual crop evapotranspiration ($ET_c$) minus the effective rainfall available ($P_{eff}$). If the effective rainfall exceeds the crop evapotranspiration, the $ET_{blue}$ value is recorded as ‘0’.

_Note for Green and Blue WFs:_ The Crop Water Use (CWU) is derived by accumulating daily evapotranspiration over the complete growing period ($lgp$). To find these rates, the authors used the CROPWAT 8.0 model, which employs the FAO Penman–Monteith method to calculate reference evapotranspiration based on parameters like net radiation, soil heat flux, air temperature, wind speed, and vapor pressure.

**4. Grey Water Footprint ($WF_{grey}$)**

- **Formula:** The grey WF (in m³ ha⁻¹) is mathematically expressed in the text's equation as factoring the pollutant load divided by the crop yield ($Y$).
- **Methodological Explanation:** The grey WF calculation accounts for the freshwater needed to assimilate nitrogen pollutants to meet water quality standards. The variables include:
    - **$\alpha$:** The leaching-runoff fraction (set at 0.1 for nitrogen).
    - **$ON$:** The rate of organic amendments (kg N ha⁻¹), factoring in nitrogen percentages.
    - **$C_{max}$:** The maximum acceptable concentration of the pollutant load. The authors set this as $NO_3-N < 5$ mg L⁻¹, based on Thailand's surface water standard (category 3).
    - **$C_{nal}$:** The natural nitrogen concentration (set to 0 kg m⁻³).
    - **$Y$:** Crop yield (ton ha⁻¹ year⁻¹).

---

### Query C2 — Irrigated and rain-fed water footprint contrasts
For the source document `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf`: Extract the exact water-footprint findings for irrigated `RRR` and rain-fed `RR` systems from `Fig. 5`, `Fig. 6`, and any directly relevant surrounding text. Report which crop in the sequence has the highest green, blue, grey, and total water footprint, with exact citations. If the document is missing or the title is ambiguous, stop and report that explicitly.

#### Raw Response
Based on **Section 3.3 (WF changes under the CMIP6 climate scenarios)** and the corresponding figures, here are the exact water footprint (WF) findings for the irrigated (RRR) and rain-fed (RR) systems:

**Irrigated Area: RRR Cropping System (Triple Cropping of Rice)** According to the text, the total WF of the RRR system is projected to decline from the near to far-future periods under the moderate SSP245 scenario, but will increase in the mid and far-future periods under the severe SSP585 scenario.

- **Highest Green WF:** The **first rice crop** requires the highest green water footprint, ranging from 758–1,318 m³ ton⁻¹. _(Note: The text cites "Fig. 5(a)" for the first rice crop)._
- **Highest Blue WF:** The **third rice crop** requires the highest blue water footprint, ranging from 803–1,194 m³ ton⁻¹. The second rice crop is next (628–790 m³ ton⁻¹), followed by the first rice crop (55.4–95 m³ ton⁻¹). _(Note: The authors mistakenly cite "Fig. 5(d)" for the third rice crop in the text, though it corresponds to Fig. 5(c))._
- **Highest Grey WF:** The authors do not single out one crop as having the highest grey WF, but instead provide an overall range of **223–349 m³ ton⁻¹** for the entire sequence across all periods (Fig. 5(a), (b), and (c)).
- **Highest Total WF:** Visually based on **Fig. 5**, the **third rice crop (Fig. 5(c))** reaches the highest overall total WF peak, exceeding 1,800 m³ ton⁻¹ in the far future (2070–2100) under the SSP585 scenario.

**Rain-fed Area: RR Cropping System (Double Cropping of Rice)** In the RR cropping system, the total WF of both the first and second rice crops is expected to decrease slightly in the near-future period under the SSP245 scenario. However, the total WF for the first rice crop will steadily increase in the far-future period under SSP245 and across all periods under SSP585. The second rice crop's total WF is expected to increase for all other periods under both the SSP245 and SSP585 scenarios.

- **Highest Green WF:** The **first rice crop** has the highest green water footprint. _(Cited in text as Fig. 6(a) and (b))._
- **Highest Blue WF:** The **second rice crop** has the highest blue water footprint. _(Cited in text as Fig. 6(a) and (b))._
- **Highest Grey WF:** The text states the grey WF for the RR system ranges from **258 to 350 m³ ton⁻¹** overall (Fig. 6(a) and (b)), explicitly noting that this is **higher than the RRR cropping system**.
- **Highest Total WF:** Based on the charts in **Fig. 6**, while the second rice crop has a slightly higher historical baseline, the **first rice crop (Fig. 6(a))** reaches the highest projected peak total WF of ~1,700 m³ ton⁻¹ during the far future (2070-2100) under the SSP585 scenario.

---

### Query C3 — Adaptation crop water footprint and resilience
For the source document `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf`: Extract the exact findings for maize, soybean, mung bean, and cassava under adaptation strategies from `Table 5`, `Fig. 7`, and any directly relevant surrounding text. Compare them against rice systems using exact values or author-stated comparisons for yield and water footprint. Include exact citations. If the document is missing or the title is ambiguous, stop and report that explicitly.

#### Raw Response
Based on the source document, here are the exact findings for the alternative crops under adaptation strategies, along with their comparisons to rice systems:

**1. Maize (RM and MM Cropping Systems)**

- **Yield Findings:** Under the RM system (maize after first rice), maize yield will increase by 0.2–1.2% in near and mid-future periods under both SSP245 and SSP585 scenarios, but it is projected to decline by 1.3–1.6% in the far future. Under the MM system (twice cropping of maize), the first maize crop's yield increases across all periods (0.5–15.8%). The second maize crop's yield increases by 2.8–6.0% in near and mid-future periods but declines by 6.0–6.3% in the far future. _(Source: Table 5, Section 3.2)_.
- **Water Footprint (WF) Findings:** For both RM and MM systems, the total WF of maize is projected to decline slightly in the near and mid-future periods but increase in the far-future period under both scenarios. In the MM system specifically, the second maize crop's total WF is higher than the first maize crop due to higher blue and grey WFs. _(Source: Fig. 7(a), Fig. 7(d), Section 3.3)_.

**2. Soybean (RS Cropping System)**

- **Yield Findings:** Soybean yields are expected to rise by 0.2–1.5% in the near and mid-future periods under both scenarios, but face a slight reduction of 0.9–1.3% in the far-future period. _(Source: Table 5, Section 3.2)_.
- **WF Findings:** The total WF for soybean is projected to decrease in the near and mid-future periods under both scenarios, followed by an increase in the far-future period. _(Source: Fig. 7(b), Section 3.3)_.

**3. Mung Bean (RB Cropping System)**

- **Yield Findings:** Mung bean has the most resilient yield projection among the legumes; its yield is predicted to increase by 2.1–7.9% across **all** future periods under both scenarios. _(Source: Table 5, Section 3.2)_.
- **WF Findings:** The total WF for mung bean tends to decrease in all future periods compared to the baseline. The average green, blue, and grey WFs are 269, 88, and 70 m³ ton⁻¹, respectively. _(Source: Fig. 7(c), Section 3.3)_.

**4. Cassava (CS Cropping System)**

- **Yield Findings:** Cassava is predicted to "endure under future climate projections," showing a continuous increasing trend of 1.0–5.7% across all future periods under both scenarios. _(Source: Table 5, Section 3.2)_.
- **WF Findings:** Similar to mung bean, the total WF for cassava tends to decrease in all future periods compared to the baseline. Its average green, blue, and grey WFs are 178, 261, and 104 m³ ton⁻¹, respectively. _(Source: Fig. 7(e), Section 3.3)_.

---

### **Comparisons Against Rice Systems**

**Yield Comparison:** The authors state that switching from a second rice crop to less water-consuming crops like maize, soybean, or mung bean will "have a less negative impact on future climate change, especially mung bean". They also explicitly conclude that "changing from growing rice twice per year to maize and cassava cultivation increased favorability in rain-fed areas".

- **Exact Value Comparison:** Under the severe SSP585 scenario, rain-fed first and second rice crops are projected to suffer heavy yield reductions of **6.0–14.4% and 7.4–17.7%**, respectively. In stark contrast, alternative crops like cassava and mung bean see continuous yield _increases_ (1.0–5.7% and 2.1–7.9%, respectively) across all periods, while maize and soybean see only mild reductions (0.9–6.3%) isolated to the far-future period.

**Water Footprint Comparison:** The authors explicitly state that "the total WFs of maize, soybean, mung bean, and cassava production were roughly half that of rice production, indicating that these crops were suitable alternatives in the dry season". They point out that rice consumes "two to three times more water" than these crops and is highly sensitive to water stress.

- **Exact Value Comparison:** The paper records the baseline total WF for rice at **1,206–1,467 m³ ton⁻¹**. By comparison, the baseline WFs for the adaptation crops are drastically lower: maize is 682–866 m³ ton⁻¹, cassava is 575 m³ ton⁻¹, soybean is 542 m³ ton⁻¹, and mung bean is the lowest at 437 m³ ton⁻¹.

---

### Query C4 — Why mung bean and cassava
For the source document `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf`: Extract the authors’ explicit reasons for recommending mung bean and cassava as adaptation crops. Quote or list only the reasons directly stated by the authors, with exact section, table, or figure citations. If the document is missing or the title is ambiguous, stop and report that explicitly.

#### Raw Response
Based on the source document, the authors explicitly recommend mung bean and cassava as adaptation crops due to their resilience to future climate projections and lower water requirements. Here are the specific reasons directly stated by the authors:

**Reasons Applying to Both Mung Bean and Cassava**

- **Lower Water Footprint:** The authors explicitly note that "the total WFs of maize, soybean, mung bean, and cassava production were roughly half that of rice production, indicating that these crops were suitable alternatives in the dry season".
- **Drought Tolerance:** They are described as "less water-consuming crops". Furthermore, the authors state they are "generally grown in rain-fed conditions with high temperatures (>30 °C), low humidity, and low precipitation" and are "considered drought tolerant due to surviving on limited soil moisture and soil water content".
- **Overall Resilience:** The authors state that both mung bean and cassava are "predicted to endure under future climate projections".

**Reasons Specific to Mung Bean**

- **Consistent Yield Increases:** Mung bean is highlighted as having a "less negative impact on future climate change, especially mung bean, which is predicted to slightly increase in all periods under the SSP245 and SSP585 scenarios" (Section 3.2, referencing Table 5 and Fig. 4(e); Section 4).
- **Optimal Climate Matching:** The authors explain that the simulation showed increasing yields "due to changes in future climate not exceeding the optimum values for mung bean growth" (Section 3.2).
- **Avoidance of Biotic Stress:** The authors specifically note that "growing mung bean in the dry season can limit biotic stress, such as mung bean yellow mosaic disease (Begomovirus strains), due to high temperatures" (Section 3.2).

**Reasons Specific to Cassava**

- **Remarkable Yield Growth:** The authors recommend cassava because it demonstrates a "remarkable increasing trend (1.0–5.7%) in all periods under both the SSP245 and SSP585 scenarios" (Section 3.2, referencing Table 5 and Fig. 4(g); Section 4).
- **Favorable for Rain-fed Areas:** The text states that "changing from growing rice twice per year to... cassava cultivation increased favorability in rain-fed areas" (Section 3.2, Section 4, Abstract).
- **Robust Biological Traits:** The authors point out that cassava "is considered a drought-tolerant species, consumes less water, and tolerates high temperatures" and "can grow on poor soils" (Section 3.2).

---

## Phase 3A Packet D — Limitations and confidence framing

### Query D1 — Limitations and data gaps
For the source document `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf`: Extract the explicit limitations, model uncertainties, calibration constraints, and any stated uncertainty around `CO2` effects, heat stress, and water-footprint interpretation. Cite the exact section anchors. If the document is missing or the title is ambiguous, stop and report that explicitly.

#### Raw Response
Based on the source document, here are the exact limitations, uncertainties, and interpretations stated by the authors, along with their section citations:

**1. Model Uncertainties and Biases**

- **Climate Model Uncertainties:** In **Section 3.1. Future climate scenarios**, the authors state that a "multi-model ensemble average approach is widely used for climate modelling to reduce the large biases and uncertainties from model parameterization errors, model structures, assumptions, and input variables". They note that while CMIP6 models improve upon CMIP5, there is still "high uncertainty in wet regions," meaning the models "can be used for climate change projections after correcting the related biases and uncertainties".
- **Yield Simulation Complexity:** In **Section 3.2. Major crop yield changes under CMIP6 climate scenarios**, the authors note that "the assessment of climate change impacts on crop yield is quite complex because crop yields are multifaceted interactions between precipitation effects, CO2 concentration effects, and crop adaptability".

**2. Calibration Constraints**

- **Need for More Data:** In **Section 4. Conclusion**, the authors explicitly state a limitation regarding their calibration and validation data (which relied on crop yields from 2013–2014 and 2021): "It should be noted that a higher number of calibration and validation data are needed in a future study to reduce the uncertainty in the final results".

**3. Uncertainty Around CO2 Effects**

- **CO2 Negated as a Primary Driver:** In **Section 3.2**, the authors explicitly acknowledge debate around the impact of elevated CO2. They point out that "some studies negated considering the effect of CO2 level because the changes in CO2 concentration from year to year are small; therefore, the change in crop yield would be too small". The authors align their findings with this perspective, concluding that "crop yield in Thailand is more controlled by temperatures and precipitation than the benefit of elevated CO2 concentration".

**4. Heat Stress Interpretations**

- **Exacerbating Water Stress:** In **Section 3.2**, the authors explain that "temperatures rising above the optimum values for crop growth might lead to heat stress, resulting in crop yield reduction," and importantly, "higher temperatures enhance evapotranspiration and exacerbate water stress and drought conditions".
- **Crop-Specific Limits:** They also note heat-stress limitations for specific crops. For instance, while mung bean performs well, temperatures >40 °C "can reduce pollen viability during the reproductive stage, causing a decline in yield". Furthermore, while maize and soybean yields increase in near/mid-future periods, they will decline in the far future because "climate conditions will exceed the optimal conditions for crop growth," particularly noting that the flowering period is highly sensitive to heat anomalies.

**5. Water-Footprint Interpretation Constraints**

- **Nonlinear Responses and Management Practices:** In **Section 3.3. WF changes under the CMIP6 climate scenarios**, the authors caution against interpreting water footprint (WF) changes solely as a direct result of the climate. They state, "Notably, the variation in WFs were nonlinear responses to crop yields; thus, farmers’ management practices are very important to increase crop yield and reduce the total WF, rather than being climate-driven".

---

### Query D2 — Author recommendations
For the source document `1-Climate-change-impact-on-major-crop-yield-and-water-footprint-under-CMIP6-climate-projections.pdf`: Extract the authors’ concrete adaptation recommendations or policy implications for irrigated systems, rain-fed systems, and crop-switching decisions. Cite the exact section anchors. If the document is missing or the title is ambiguous, stop and report that explicitly.

#### Raw Response
Based on the source document, the authors provide the following concrete adaptation recommendations and policy implications for irrigated systems, rain-fed systems, and crop-switching decisions:

**1. Irrigated Systems**

- **Recommendation:** The authors explicitly recommend maintaining the business-as-usual **RRR cropping system** (growing rice three times a year) in irrigated areas. This recommendation is based on their findings that rice yields in irrigated areas are predicted to rise gradually under moderate climate scenarios (SSP245) due to increased precipitation and elevated CO2, which offset temperature increases (Section 3.2, Section 4. Conclusion).

**2. Rain-Fed Systems and Crop-Switching Decisions** The authors provide several targeted crop-switching recommendations for rain-fed areas, which lack irrigation systems and suffer from dry-season water shortages:

- **Replacing the Second Rice Crop:** Instead of attempting to grow a second rice crop in the dry season, the authors recommend that farmers switch to less water-consuming crops, specifically **growing maize, soybean, or mung bean after the first rice crop**.
- **Switching Away from Rice Entirely:** As alternative options for rain-fed areas, the authors state that completely switching from rice to **growing cassava** or **planting maize twice per year** are "good options" that have "increased favorability" under future climate projections (Section 3.2, Section 4. Conclusion).
- **Specific Crop Advantages:**
    - **Mung Bean:** Highlighted as a highly "effective adaptation strategy crop," mung bean is recommended for the dry season because it is projected to see yield increases across all future periods and scenarios. The authors note that the high temperatures of the dry season also help limit biotic stresses (like mung bean yellow mosaic disease) for this crop (Section 3.2).
    - **Cassava:** Identified as an excellent adaptation crop because it consumes less water, tolerates high temperatures, can grow in poor soils, and shows a remarkable, continuous increasing yield trend across all periods and scenarios (Section 3.2).

**3. Broad Policy and Management Implications**

- **Alignment with Government Policy:** The authors note that their recommendations align with existing policy, stating that "switching or changing crop species to less water-consuming crops (e.g., maize, soybean, mung bean, and cassava) is recommended by the Thai government to reduce rice yield loss and increase farming income" (Section 3.2).
- **The Importance of Farm Management:** The authors conclude that variations in water footprints (WFs) respond nonlinearly to crop yields. Consequently, a major policy and practical implication is that **"farmers’ management practices are very important to increase crop yield and reduce the total WF, rather than being climate-driven"** (Section 3.3).
