# NCAIF Service Intelligence Report (v4.3)

**Project Component**: Pillar 2 — Service Platform Consolidation & Functional Specifications
**Version**: 4.2 (Inclusive Service Synthesis - Merge Release)
**Status**: SUPERSEDED by v5.0 (Moved to Archive)
**Date**: 2026-06-05

---

## 1. Executive Summary
The National Climate Adaptation Information Framework (NCAIF) v4.3 represents the surgical integration of institutional decision-making scenarios with international technical benchmarks. This version moves beyond structural definitions to provide a functional "Intelligence Value Chain" for 13+ Thai state agencies. 

By anchoring every service module in a specific **Institutional Scenario** (the "Drama" of decision friction) and hardening them with benchmarks like **DCAT-AP 3.0**, **World Bank Triple Dividend**, and **PIANC Engineering Frameworks**, the NCAIF provides a regulatory and technical "Shield" for administrators, risk officers, and engineers.

---

## 2. The 7 National Climate Service Platforms

### S01: National Authoritative Data Catalog & Discovery (SSOT)
*   **The Common Core**: A foundational platform for discovery and metadata standardization, ensuring a "Single Source of Truth" across national repositories (NSO, DCCE, ONWR).
*   **Technical Standardization**: 
    *   **DCAT-AP 3.0.0 (June 2024)**: Implementation of mandatory classes (`Catalog`, `Dataset`, `Distribution`) and controlled vocabularies to enable federated discovery between DCCE and the Digital Government Agency (DGA).
*   **Contextual Modules**:
    1.  **Financial Verification Module**: 
        *   *Institutional Scenario*: Banks and FTI verifying "Green Impact" for SMEs to justify discounted interest rates. Verification of "Green Claims" against TGO-aligned methodologies.
        *   *Technical Enrichment*: [FTI - Green Loan] verification protocols; Scope 1 & 2 monitoring.
    2.  **Urban Data Management Module**: 
        *   *Institutional Scenario*: City planners (UDDC/BMA) resolving inconsistencies between municipal and national datasets to transform conceptual designs into legally-binding strategic plans.
        *   *Technical Enrichment*: [UDDC - City Scale] 1m-resolution DEM integration; neighborhood data lake protocols.
    3.  **Governance & Access Module**: 
        *   *Institutional Scenario*: Overcoming inter-agency PDPA fears by providing a "Secure Highway" (GDX) with automated masking and anonymization for cross-sector research.
        *   *Technical Enrichment*: [DGA - GDX Highway] API integration; Article 8/15 DGA compliance.
*   **Traceability**: UC-01, UC-24, UC-32; [NSO - EA Unit], [DGA - GDX Highway].

### S02: Socio-Economic Vulnerability Analytics
*   **The Common Core**: Integration of physical hazard data with socio-economic indicators at the block level.
*   **Technical Standardization**: 
    *   **Enumeration Area (EA) Logic**: Mapping risk to Thailand’s most granular spatial unit (~250 buildings) to move beyond provincial averages.
*   **Contextual Modules**:
    1.  **Economic Resilience Module**: 
        *   *Institutional Scenario*: Identifying specific household-level exposure to prevent systemic financial shocks from localized agricultural or industrial disruptions.
        *   *Technical Enrichment*: [NSO - EA Unit] census-linked exposure baselines; building-block resolution.
    2.  **Urban Vulnerability Module**: 
        *   *Institutional Scenario*: High-resolution (10m–30m) mapping of pluvial hazards overlaid with socio-economic status to identify habitability tipping points in urban corridors.
        *   *Technical Enrichment*: [UDDC - City Scale] SSP3/SSP5 downscaled projections.
    3.  **Social Welfare Support Module**: 
        *   *Institutional Scenario*: Matching 13-digit welfare IDs of bedridden/disabled individuals with live flood markers to trigger predictive rescue instead of reactive recovery.
        *   *Technical Enrichment*: [MSDHS - Evacuation] household-level welfare registry spatial overlays.
    4.  **Agricultural Resilience Module**: 
        *   *Institutional Scenario*: Agricultural planners (LDD) tracking plot-level climate variables to justify agricultural recovery policies and support emerging carbon credit markets.
        *   *Technical Enrichment*: [LDD - Carbon & Recovery] Plot-level (10m) soil moisture and crop damage models.
*   **Traceability**: UC-15, UC-16, UC-23, UC-30, UC-40; [MSDHS - Evacuation], [NSO - EA Unit].

### S03: Climate Investment ROI & Fiscal Planning
*   **The Common Core**: Analytical tools to evaluate economic feasibility and justify climate-related capital expenditure (CAPEX).
*   **Technical Standardization**: 
    *   **World Bank "Triple Dividend of Resilience"**: Standardized metrics for Avoided Losses, Unlocked Economic Potential, and Development Co-benefits (BCR targets 2:1 to 10:1).
*   **Contextual Modules**:
    1.  **Fiscal Risk Planning Module**: 
        *   *Institutional Scenario*: National economists (NESDC) capturing "True Economic Loss" (including business interruption) to adjust GDP forecasts and justify fiscal resilience buffers.
        *   *Technical Enrichment*: [NESDC - GDP Adjustment] direct asset damage + indirect logistics bottleneck modeling.
    2.  **Local Government Budgeting Module**: 
        *   *Institutional Scenario*: Local administrators (DLA) obtaining a "Regulatory Shield" (certified ROI) to justify using Accumulated Funds (เงินสะสม) to the State Audit Office (OAG).
        *   *Technical Enrichment*: [DLA - Accumulated Funds] proactive vs. post-disaster loss coefficients.
    3.  **NbS Evaluation Module**: 
        *   *Institutional Scenario*: Comparing the long-term ROI of nature-based solutions (mangroves, urban parks) vs. grey infrastructure to secure environmental funding.
        *   *Technical Enrichment*: [UDDC - Strategic Planning] Benefit-Cost Ratio (BCR) baseline risk adjustments.
*   **Traceability**: UC-03, UC-04, UC-19, UC-31; [DLA - Accumulated Funds], [FTI - Green Loan].

### S04: Climate Loss & Damage Assessment
*   **The Common Core**: Standardized accounting of economic and non-economic losses to support national reporting and international (Sendai/SDG) compliance.
*   **Technical Standardization**: 
    *   **Sendai Framework Target C (Economic Loss)**: Adoption of sub-indicators C-2 to C-6 using "Replacement Cost" methodology for direct economic loss calculation.
*   **Contextual Modules**:
    1.  **Relief Fund Support Module**: 
        *   *Institutional Scenario*: DDPM operators standardizing the documentation of asset damage to move beyond fixed government payout caps toward insurance-grade evidence.
        *   *Technical Enrichment*: [NESDC - GDP Adjustment] event-level macro-economic loss reporting.
    2.  **Macro-Economic Impact Module**: 
        *   *Institutional Scenario*: Risk officers at TBA/BoT moving from provincial-level indexes to asset-level financial modeling to prevent credit portfolio instability.
        *   *Technical Enrichment*: [TBA - Stress Test] asset-level coordinates; probabilistic flood metrics (depth/duration).
    3.  **Tourism Economic Impact Module**: 
        *   *Institutional Scenario*: Tourism authorities (MOTS) quantifying the economic vulnerability of specific destinations to guide recovery funds and adaptation plans.
        *   *Technical Enrichment*: [MOTS - Tourism Info] Destination-level sensitivity analysis and loss coefficients.
*   **Traceability**: UC-09, UC-21, UC-22, UC-33; [TBA - Stress Test], [NESDC - GDP Adjustment].

### S05: Infrastructure Risk & Engineering Specifications
*   **The Common Core**: Integration of climate projections into infrastructure design codes, asset management, and urban zoning.
*   **Technical Standardization**: 
    *   **PIANC WG 178 / TG 193 Framework**: 4-Stage Adaptation logic (Context -> Info -> Risk -> Options) and use of "Tipping Points" for asset operational thresholds.
*   **Contextual Modules**:
    1.  **Transport Infrastructure Module**: 
        *   *Institutional Scenario*: OTP engineers pinpointing risk down to specific Kilometer Markers or utility poles to justify multi-billion Baht retrofitting budgets to the Bureau of Budget.
        *   *Technical Enrichment*: [OTP - KM-Marker] GIS-linked asset IDs; 100yr hydrological flow maps.
    2.  **Urban Hydrology Module**: 
        *   *Institutional Scenario*: Engineers (DPT/BMA) shifting from 30-year historical rainfall to "Rain Bomb" climate-adjusted IDF curves to ensure new tunnels don't fail under intensification.
        *   *Technical Enrichment*: [DPT - Drainage Design] climate-adjusted rainfall intensity-duration-frequency (IDF) coefficients.
    3.  **Geological Hazard Module**: 
        *   *Institutional Scenario*: Integrating landslide susceptibility and soil stability analysis directly into building permit workflows to prevent construction in high-risk zones.
        *   *Technical Enrichment*: [DMR - Geological Hazard] soil stability thresholds; landslide susceptibility mapping.
    4.  **Marine Infrastructure Module**: 
        *   *Institutional Scenario*: Marine authorities (MD) modeling sea-level rise and coastal erosion impacts to revise port maintenance regulations and infrastructure budgets.
        *   *Technical Enrichment*: [MD - Marine Infra] Coastal erosion rates; 50-year Sea Level Rise (SLR) projections.
*   **Traceability**: UC-05, UC-06, UC-07, UC-08, UC-29, UC-38; [DPT - Drainage Design], [OTP - KM-Marker].

### S06: Multi-Hazard Monitoring & Early Warning
*   **The Common Core**: Near real-time monitoring of environmental thresholds to support operational decision-making.
*   **Technical Standardization**: 
    *   **Near Real-Time API Ingestion**: Moving from manual website checks to automated data streams (Rain/Canal/Tide/Heat) with 1–3 hour lead times.
*   **Contextual Modules**:
    1.  **Industrial Water Monitoring**: 
        *   *Institutional Scenario*: Factory managers (FTI) translating water supply-demand forecasts into specific productivity loss estimates to trigger alternative water sourcing.
        *   *Technical Enrichment*: [FTI - Heat Impact] water-productivity loss coefficients.
    2.  **Urban Heat & Health Monitoring**: 
        *   *Institutional Scenario*: BMA/DOH issuing neighborhood-scale health alerts based on the Wet Bulb Globe Temperature (WBGT) index to protect outdoor workers and elderly residents.
        *   *Technical Enrichment*: [BMA/DOH] 10 sq km heatwave projections; WBGT intensity thresholds.
    3.  **Marine Ecosystem Monitoring**: 
        *   *Institutional Scenario*: Marine biologists (DMCR) tracking real-time sea surface temperatures to issue coral bleaching alerts and direct conservation interventions.
        *   *Technical Enrichment*: [DMCR - Coral Alerts] Coastal grid resolution; 30-day marine temperature forecasts.
    4.  **Integrated Water Projections**: 
        *   *Institutional Scenario*: National water authorities (ONWR, HII) forecasting basin-level supply and demand to manage drought operations, specifically in critical economic zones like the EEC.
        *   *Technical Enrichment*: [ONWR/HII - Basin Forecasts] API integration for seasonal drought/flood forecasts and raw water source mapping.
    5.  **Localized Flood Thresholds**: 
        *   *Institutional Scenario*: Meteorologists (TMD) setting dynamic, area-specific water absorption thresholds to trigger early warnings before peak rainfall events.
        *   *Technical Enrichment*: [TMD - Local Thresholds] Sub-district rainfall peak monitoring; soil absorption threshold mapping.
*   **Traceability**: UC-13, UC-14, UC-17, UC-25, UC-26, UC-34, UC-36, UC-37, UC-39; [BMA - Flood Ops], [FTI - Heat Impact].

### S07: Policy Monitoring & NAP Compliance
*   **The Common Core**: Automated tracking of progress against national (NAP) and international (GGA) climate targets.
*   **Technical Standardization**: 
    *   **Thematic Clustering & Gap Analysis**: Using AI-driven analysis to identify research "Unknowns" and policy-implementation gaps.
*   **Contextual Modules**:
    1.  **Technology Tracking Module**: 
        *   *Institutional Scenario*: NXPO monitoring the Technology Readiness Levels (TRL) of national innovations to ensure research funding targets the specific gaps identified in NCAIF maps.
        *   *Technical Enrichment*: [NXPO - Gap Analysis] unstructured data ingestion; research gap thematic clustering.
    2.  **Local Policy Alignment Module**: 
        *   *Institutional Scenario*: Automating the integration of sub-district performance indicators with national targets to ensure local-national policy coherence under the Climate Change Act.
        *   *Technical Enrichment*: [DLA - Policy Alignment] local performance indicator mapping.
    3.  **Learning Data Repository**: 
        *   *Institutional Scenario*: Research funding bodies (PMUA) leveraging consolidated spatial alerts to direct area-based planning grants and monitor future hazard risks.
        *   *Technical Enrichment*: [PMUA - Area Planning] Regional API access for strategic funding allocation.
*   **Traceability**: UC-01, UC-10, UC-11, UC-12, UC-20, UC-35; [NXPO - Gap Analysis].

---
*NCAIF Pillar 2 Synthesis v4.3 — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Service_Intelligence_Report_v4.3.md*
