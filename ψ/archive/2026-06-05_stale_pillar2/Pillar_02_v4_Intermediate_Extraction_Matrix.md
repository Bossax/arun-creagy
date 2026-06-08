# Pillar 2: Forensic Extraction Matrix (v4.0)

**Status**: Phase 1 Artifact (Forensic Extraction Complete)
**Objective**: Document the Intelligence Value Chain and Institutional Scenarios for 35 key Use Cases across 13 agencies.

---

## 1. Group 1: Economic & Financial Services (The Fiscal Shield)

| ID | Agency | Decision Moment | Institutional Scenario (The Narrative) | Intelligence Product | Hard Technical Specs | Originator Tag |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **G1-01** | **TBA** | Credit Portfolio Stress Testing | Bank risk officers are required by the **Bank of Thailand (BoT)** to integrate climate stress testing into their **ICAAP** standards. They need to move from broad provincial indexes to asset-level financial modeling to prevent systemic financial instability. | Asset-level Probabilistic Flood Maps | Probability at specific coordinates; metrics for depth/duration; CMIP5 scenarios. | `[TBA - Stress Test - Interview Summary TBA]` |
| **G1-02** | **NESDC** | GDP Forecast Adjustment | When major disasters strike (e.g., Hat Yai floods), national economists must adjust quarterly GDP forecasts. Current data only shows government compensation, which is an order of magnitude lower than the **True Economic Loss**. They need to capture business interruption and supply chain friction. | Event-level Macro-Economic L&D Report | Direct asset damage + indirect opportunity costs + logistics bottlenecks. | `[NESDC - GDP Adjustment - Interview Summary NESDC]` |
| **G1-03** | **DLA** | Local Budget Approval | Local administrators face **State Audit Office (OAG)** scrutiny when using **Accumulated Funds (เงินสะสม)** for proactive projects. They need a certified ROI to prove the investment prevents future loss, providing them with a regulatory shield. | Standardized Climate Investment ROI | Certified ROI metrics; cost-benefit ratios vs. baseline risk. | `[DLA - Accumulated Funds - Interview Summary DLA]` |
| **G1-04** | **FTI** | Green Loan Rate Setting | Banks provide **"Green Loans"** to SMEs, but require proof of impact. FTI acts as the verifier, measuring emissions before and after the loan to justify the discounted interest rates. | SME Emission Verification Certificate | Scope 1 & 2 carbon footprint; pre- vs. post-investment comparison. | `[FTI - Green Loan - Interview Summary FTI]` |
| **G1-05** | **FTI** | Manufacturing Productivity Planning | Factory managers need to translate "35°C forecast" into "Financial Loss." They need to know the specific cost of labor productivity drops and heat-stroke risk to decide on cooling investments. | Heat-Loss & Productivity Model | 10 sq km heatwave projections; labor productivity loss coefficients. | `[FTI - Heat Impact - Interview Summary FTI]` |

## 2. Group 2: Spatial Planning & Engineering (The Technical Seal)

| ID | Agency | Decision Moment | Institutional Scenario (The Narrative) | Intelligence Product | Hard Technical Specs | Originator Tag |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **G2-01** | **UDDC** | Neighborhood Strategic Planning | City planners operate in a fragmented data environment. To move from conceptual design to **Legally-Binding Plans**, they need a "Neighborhood Data Lake" that resolves inconsistencies between municipal and national datasets. | 1m-Resolution Future Inundation Map | 1m DEM; SSP3/SSP5 downscaled to city level; future habitability zones. | `[UDDC - City Scale - Interview Summary UDDC]` |
| **G2-02** | **MSDHS** | Vulnerable Group Evacuation | During rapid-onset floods, social workers must identify "Bedridden" or "Disabled" individuals in the water's path. They need to match **Personal Welfare Registries** with live hazard maps to trigger physical rescue. | Vulnerable Group Spatial Overlay | Individual/Household-level Welfare IDs matched to flood depth; sub-district level. | `[MSDHS - Evacuation - Interview Summary MSDHS]` |
| **G2-03** | **DPT** | Drainage Infrastructure Engineering | Engineers designing urban drainage systems can no longer rely on 30-year historical rainfall. They need **"Climate-Adjusted Rainfall"** projections to ensure new infrastructure doesn't fail under "Rain Bomb" scenarios. | Climate-Adjusted Intensity-Duration-Frequency (IDF) | 50-100 year return periods; climate-adjusted rainfall coefficients. | `[DPT - Drainage Design - Interview Summary DPT]` |
| **G2-04** | **OTP** | Transport Resilience Retrofitting | OTP must decide which highway sections or railway utility poles need elevation. They model risk down to the **Kilometer Marker** to justify massive construction costs to the Bureau of Budget. | High-Res Infrastructure Hazard Flow Map | GIS-linked utility pole/KM-marker IDs; 50-100yr hydrological models. | `[OTP - KM-Marker - Interview Summary OTP]` |
| **G2-05** | **NSO** | High-Res Exposure Mapping | NSO provides the **Enumeration Area (EA)** logic—the most granular spatial unit in Thailand (~250 buildings). This provides the "Pipe" for DCCE to see exactly which houses are exposed to risk. | EA-Level Exposure Baseline | Enumeration Area boundaries; building counts per block; census-linked. | `[NSO - EA Unit - Interview Summary NSO]` |

## 3. Group 3: Operation & Information Services (The Single Source of Truth)

| ID | Agency | Decision Moment | Institutional Scenario (The Narrative) | Intelligence Product | Hard Technical Specs | Originator Tag |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **G3-01** | **BMA** | Short-Term Flood Response | BMA operators must decide when to open pumping gates. They need to integrate **Upstream River Levels** (from RID) with **City Rain Sensors** and **Tide Forecasts** in a single operational view. | Integrated Basin-City Operational View | Near real-time API feeds (rain/canal/tide); 1-3 hour lead time. | `[BMA - Flood Ops - Interview Summary BMA]` |
| **G3-02** | **NXPO** | Research Funding Prioritization | Policy makers are overwhelmed by "Billions of Baht" in historical research. They need an **AI-Driven Knowledge Map** to identify what we *don't* know about climate impacts before approving new grants. | AI-Driven Research Gap Analysis | Unstructured data ingestion (PDFs/Reports); thematic clustering. | `[NXPO - Gap Analysis - Interview Summary NXPO]` |
| **G3-03** | **DGA** | National Data Interoperability | Agencies are hesitant to share data due to **PDPA Fears**. DGA provides the "Secure Highway" (GDX) and masking techniques to transform "Forbidden Private Data" into "Usable Open Research." | Secure Data Exchange Highway (GDX) | GDX API integration; data masking/anonymization protocols. | `[DGA - GDX Highway - Interview Summary DGA]` |

---
*Oracle Extraction Matrix v4.0 — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_v4_Intermediate_Extraction_Matrix.md*
