# Phase 2: Topic Selection & Decision Log - ART03_PLOS_Infectious_Diseases
- **Source**: 3-Projecting long-term excess risks of major infectious diseases associated with future extreme weather events in Thailand
- **Date**: 2026-06-23
- **Based on**: [`01_Raw_Extraction.md`](ψ/incubate/DCCE/CRDB/output/TOR5.5_article_and_infoghraphic/ART03_PLOS_Infectious_Diseases/01_Raw_Extraction.md)
- **Human Ownership Rule**: The `Decision` and `Human Comments` columns are reserved for human choice only. AI must not prefill `KEEP`, `DISCARD`, or `MAYBE`.

---

## 📖 Executive Summary & Scientific Narrative

This study models the long-term excess risks of seven major infectious diseases in Thailand—dengue, influenza, malaria, pneumonia, leptospirosis, melioidosis, and Japanese encephalitis (JEV)—under future extreme weather events. Using Generalized Additive Models (GAMs) and CMIP6 climate scenarios (SSP126 to SSP585), the research maps projected disease risks through the end of the century at a highly granular, province-by-province level.

The core takeaway is that climate change does not uniformly amplify all infectious diseases across the country. Instead, the projected risks are highly heterogeneous. While diseases like pneumonia and melioidosis will see increased burdens under high-emission scenarios (SSP585), other diseases like dengue and influenza exhibit complex, localized trajectories—sometimes declining nationally but surging sharply in specific regions (like Northern and Central Thailand) during specific decades. This spatial and temporal variability stresses the need for "precision public health" and localized adaptation strategies rather than blanket national policies.

---

## 🔬 Key Scientific & Policy Insights (How Thailand is Impacted)

### 1. The Complex, Localized Trajectory of Dengue and Influenza
*   **The Science**: Contrary to the simplistic assumption that a warmer climate means more disease everywhere, dengue is projected to decline nationwide by 24.9% (2061-2080) under certain models. However, under the moderate SSP245 scenario, extreme heat drives a localized surge in dengue risk in Northern and Central Thailand between 2021 and 2060. Similarly, influenza sees localized spikes, such as a projected 36.8% risk increase in Nakhon Ratchasima (2021-2040).
*   **The Cause**: Changes in extreme heat and extreme dry weather alter vector breeding cycles, viral incubation periods, and human behavioral patterns in geographically specific ways that do not average out neatly at the national level.
*   **Hazards Implication**: Broad national early-warning systems are less effective than localized, province-specific public health alerts targeting vulnerable regions during high-risk decades.

### 2. The High-Emissions Penalty: Pneumonia and Melioidosis
*   **The Science**: Under the most severe climate scenario (SSP585), the excess risk of pneumonia and melioidosis is expected to increase significantly during periods of extreme weather.
*   **The Cause**: Severe environmental stress—particularly extreme wet events and intense heat—compounds respiratory vulnerabilities in the population and increases exposure to the soil- and water-borne bacteria responsible for melioidosis.
*   **Hazards Implication**: If global emissions are not curbed, Thailand's healthcare infrastructure must prepare for heightened burdens of these specific diseases, requiring expanded diagnostic, hospital, and treatment capacities.

### 3. Declining Risks and Outliers: Leptospirosis, JEV, and Malaria
*   **The Science**: Interestingly, leptospirosis risk is projected to decline across all time periods and scenarios during extreme weather. JEV risk also generally decreases (except under SSP585). In contrast, malaria risk tends to increase during extreme weather across most scenarios.
*   **The Cause**: Changing precipitation patterns (SPI) and rising extreme heat may push certain pathogen/vector habitats (like those for leptospirosis) outside their viability thresholds, while expanding the environmental suitability for others (like malaria).
*   **Hazards Implication**: Climate adaptation in public health requires dynamic resource reallocation. Budgets and vector-control efforts can be shifted away from areas where environmental suitability is shrinking, and redirected toward newly emerging hotspots.

---

## 🎛️ Human Selection Table

*Please review the concepts below. Write **KEEP** or **DISCARD** and provide your storytelling angle/comments to guide the final draft.*

| Issue ID | Core Concept | Decision (KEEP / DISCARD) | Human Comments & Storytelling Angle / Connections |
| :--- | :--- | :--- | :--- |
| **E01** | **Historical Baseline**: The established historical association where extreme heat increased the incidence of most infectious diseases (except malaria and leptospirosis). | | |
| **E02** | **Dengue's Shifting Map**: The counter-intuitive projection of a 24.9% national decrease by 2061-2080, contrasted with severe localized spikes in the North and Central regions under SSP245. | | |
| **E03** | **Influenza Hotspots**: The projected increase in influenza risk driven by heat and dry weather, specifically noting the 36.8% jump in Nakhon Ratchasima (2021-2040). | | |
| **E04** | **High-Emission Burden**: The severe increase in pneumonia and melioidosis expected under the SSP585 extreme weather scenario. | | |
| **E05/E06** | **Diverging Paths (Malaria, JEV, Leptospirosis)**: Malaria risk increasing, while leptospirosis and JEV (mostly) decline, showing climate change creates "winners and losers" among pathogens. | | |
| **E07** | **The Need for Localized Models**: The statistical finding that province-level variation is so marked that it demands decentralized, localized public health interventions. | | |

---

## 📍 Candidate Narrative Directions

### Option A — "The Shifting Map of Dengue and Flu"
*   **Focus**: A narrative that disrupts the "global warming means more tropical disease everywhere" myth. Focus on how national averages hide dangerous, localized spikes in specific provinces (like Nakhon Ratchasima), demanding precision public health alerts.

### Option B — "The High-Emissions Health Penalty"
*   **Focus**: A more urgent, climate-policy-focused article highlighting what happens if we follow the SSP585 trajectory—specifically the surge in severe diseases like pneumonia and melioidosis.

### Option C — "Winners and Losers in a Warmer Thailand"
*   **Focus**: Exploring the complex biological reality that while diseases like leptospirosis might decline, others like malaria and dengue will shift to new territories, requiring agile healthcare responses.

---

## ✍️ Structural Narrative Blueprint (Human-Defined)
*Please write or outline how you want the story to flow for the public article:*

- **Opening Hook**: 
- **Body Flow**: 
- **Conclusion & Takeaways**: 

---

## 🛡️ Guardrails for Phase 3 and Drafting

1.  **Metric Extraction Mandate**: The raw extraction did not capture all the quantitative data. For any topics marked **KEEP**, the Phase 3 (Verify) agent **must** execute targeted extraction to pull the exact Incidence Rate Ratios (IRR), Population Attributable Fractions (PAF), or specific percentage changes from the source document (especially from Figures 2-7 and S6 Table) before drafting begins.
2.  **Contextual Limitations**: The draft must clearly state that these projections represent the *baseline environmental pressure* of extreme weather. The models explicitly exclude future population growth, land-use change, and future public health interventions. These are risk trajectories, not guaranteed future case counts.
3.  **Avoid National Flattening**: Do not describe the trends as uniform across Thailand. The localized, province-specific nature of the risk is the most important finding of the study.
