import re
import os

with open("ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Service_Intelligence_Report_v4.2.md", encoding="utf-8") as f:
    txt = f.read()

txt = txt.replace("v4.2", "v4.3")
txt = txt.replace("Version: 4.2 (Inclusive Service Synthesis - Merge Release)", "Version: 4.3 (Complete Forensic Restoration - Activity 1 & 2 Merge)")

# Add S02 module
s02_mod = """    4.  **Agricultural Resilience Module**: 
        *   *Institutional Scenario*: Agricultural planners (LDD) tracking plot-level climate variables to justify agricultural recovery policies and support emerging carbon credit markets.
        *   *Technical Enrichment*: [LDD - Carbon & Recovery] Plot-level (10m) soil moisture and crop damage models.
*   **Traceability**: UC-15, UC-16, UC-23, UC-30, UC-40;"""
txt = txt.replace("*   **Traceability**: UC-15, UC-16, UC-23, UC-30;", s02_mod)

# Add S04 module
s04_mod = """    3.  **Tourism Economic Impact Module**: 
        *   *Institutional Scenario*: Tourism authorities (MOTS) quantifying the economic vulnerability of specific destinations to guide recovery funds and adaptation plans.
        *   *Technical Enrichment*: [MOTS - Tourism Info] Destination-level sensitivity analysis and loss coefficients.
*   **Traceability**: UC-09, UC-21, UC-22, UC-33;"""
txt = txt.replace("*   **Traceability**: UC-09, UC-21, UC-22;", s04_mod)

# Add S05 module
s05_mod = """    4.  **Marine Infrastructure Module**: 
        *   *Institutional Scenario*: Marine authorities (MD) modeling sea-level rise and coastal erosion impacts to revise port maintenance regulations and infrastructure budgets.
        *   *Technical Enrichment*: [MD - Marine Infra] Coastal erosion rates; 50-year Sea Level Rise (SLR) projections.
*   **Traceability**: UC-05, UC-06, UC-07, UC-08, UC-29, UC-38;"""
txt = txt.replace("*   **Traceability**: UC-05, UC-06, UC-07, UC-08, UC-29;", s05_mod)

# Add S06 modules
s06_mod = """    3.  **Marine Ecosystem Monitoring**: 
        *   *Institutional Scenario*: Marine biologists (DMCR) tracking real-time sea surface temperatures to issue coral bleaching alerts and direct conservation interventions.
        *   *Technical Enrichment*: [DMCR - Coral Alerts] Coastal grid resolution; 30-day marine temperature forecasts.
    4.  **Integrated Water Projections**: 
        *   *Institutional Scenario*: National water authorities (ONWR, HII) forecasting basin-level supply and demand to manage drought operations, specifically in critical economic zones like the EEC.
        *   *Technical Enrichment*: [ONWR/HII - Basin Forecasts] API integration for seasonal drought/flood forecasts and raw water source mapping.
    5.  **Localized Flood Thresholds**: 
        *   *Institutional Scenario*: Meteorologists (TMD) setting dynamic, area-specific water absorption thresholds to trigger early warnings before peak rainfall events.
        *   *Technical Enrichment*: [TMD - Local Thresholds] Sub-district rainfall peak monitoring; soil absorption threshold mapping.
*   **Traceability**: UC-13, UC-14, UC-17, UC-25, UC-26, UC-34, UC-36, UC-37, UC-39;"""
txt = txt.replace("*   **Traceability**: UC-13, UC-14, UC-17, UC-25, UC-26;", s06_mod)

# Add S07 module
s07_mod = """    3.  **Learning Data Repository**: 
        *   *Institutional Scenario*: Research funding bodies (PMUA) leveraging consolidated spatial alerts to direct area-based planning grants and monitor future hazard risks.
        *   *Technical Enrichment*: [PMUA - Area Planning] Regional API access for strategic funding allocation.
*   **Traceability**: UC-01, UC-10, UC-11, UC-12, UC-20, UC-35;"""
txt = txt.replace("*   **Traceability**: UC-01, UC-10, UC-11, UC-12, UC-20;", s07_mod)

with open("ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Service_Intelligence_Report_v4.3.md", "w", encoding="utf-8") as f:
    f.write(txt)

print("v4.3 Report successfully generated.")
