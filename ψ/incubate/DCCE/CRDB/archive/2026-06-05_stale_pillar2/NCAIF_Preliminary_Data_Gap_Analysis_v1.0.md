# Preliminary Data Gap Analysis: NCAIF Service Platforms (40 Use Cases)

**Status**: Draft for Governance Sprint (Pillar 6)
**Date**: 2026-06-09
**Baseline**: NCAIF Service Intelligence Report v6.0 & Data Inventory v3.0

---

## 1. Executive Summary
This report provides the results of a preliminary "Stress Test" of the **40 stakeholder use cases** against the **260 datasets** currently cataloged in the Pillar 3 Inventory. The objective is to identify which services are "Build-Ready" and which require significant data recovery or regulatory intervention before the 2027 system implementation.

---

## 2. Readiness Matrix (Dimension A: Data Availability)

| UC ID | Service Platform | Demand (Data Requirement) | Supply Status (Pillar 3 Evidence) | Readiness | Primary Gap / Blocker |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **UC-01** | S07: M&E | NAP Progress Indicators | No Institutional M&E data | 🔴 Low | Missing reporting metadata. |
| **UC-02** | S01: Data Vault | Provincial Risk Profiles | DCCE_3_1 (Risk Maps) | 🟢 High | **READY.** Baseline data exists. |
| **UC-03** | S01: Data Vault | Standardized Damage Functions | PDF Research Papers only | 🔴 Low | Missing **Executable Code/CSV**. |
| **UC-04** | S01: Data Vault | Probabilistic Flood Maps | GISTDA_5_1 (Annual Hazard) | 🟡 Med | Missing **Return Period modeling**. |
| **UC-05** | S05: Engineering | Adjusted Design Parameters | Raw TMD Rainfall records | 🔴 Low | Missing **Hydrological Conversion**. |
| **UC-09** | S04: L&D | Economic True Loss Reports | DDPM_3_2 (Loss Records) | 🟡 Med | Missing **Indirect/NEL Valuation**. |
| **UC-13** | S06: Early Warning | Industrial Water Scarcity | HII_2_1 (Drought Exposure) | 🟢 High | **READY.** EEC Water data exists. |
| **UC-16** | S02: High-Res | Priority Evacuation Registry | DOPA_2_1 (Census Data) | 🟡 Med | **Privacy (PDPA)** Blocker. |
| **UC-17** | S06: Early Warning | Neighborhood Heat Index | GISTDA/TMD Raw Surface Temp | 🟡 Med | Missing **Real-time API Feed**. |
| **UC-19** | S03: Finance | Local Justification Pack | DLA/Tesaban level hazards | 🟢 High | **READY.** Municipal data exists. |
| **UC-31** | S03: Finance | NbS ROI Justification | Nature-based asset maps | 🔴 Low | Missing **Avoided-Loss Curves**. |
| **UC-37** | S06: Early Warning | Localized Flood Thresholds | LDD Soil Quality data | 🟡 Med | Missing **Soil Saturation Logic**. |
| **UC-40** | S02: High-Res | Plot-level Ag-Recovery | GISTDA 40m Crop Grid | 🟢 High | **READY.** Plot-res exists. |

*(Note: Full 40-UC mapping maintained in internal project database; selected critical path items shown above.)*

---

## 3. Dimensional Gaps (Structural Obstacles)

### Dimension A: Data Quality & Availability
*   **The "Modeling" Gap**: 60% of Service 3 and 5 requirements are not "Data" but "Models" (Damage Functions, ROI curves). The project has the scientific papers but lacks the digital artifacts to run these in the NCAIF.
*   **The "Telemetry" Gap**: Service 6 (Early Warning) is currently based on static forecasts. We lack "Live API" feeds from sensor networks (BMA/TMD) for real-time impact warnings.

### Dimension B: Legal & Institutional Readiness
*   **The "Authoritative Seal"**: Service 1 requires a legal mandate for DCCE to "Certify" data from other agencies.
*   **The "Privacy" Barrier**: 20% of Use Cases (Social/Health) require Individual-level or Household-level data currently protected by PDPA and agency-specific silos.

### Dimension C: Technical Infrastructure
*   **Interoperability**: While metadata exists, only 30% of cataloged datasets have confirmed stable APIs for automated ingestion via GDX.

---

## 4. Strategic Recommendations for Governance (Pillar 6)
To move from "Gaps" to "Readiness," the Governance Operating Model must implement:
1.  **Tiered Data Access Policy**: Create a formal "Tier 2 Download" protocol for restricted datasets (PDPA-protected) to enable UC-16 and UC-23.
2.  **Model Governance Framework**: Define how "Damage Functions" and "ROI Curves" are updated and certified to ensure the "Financial ROI" (S03) is legally defensible.
3.  **Mandatory Metadata Standard**: Enforce GDA-aligned metadata for all incoming agency feeds to fix the "Discovery" issues in S01.

---
*NCAIF Preliminary Data Gap Analysis — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Preliminary_Data_Gap_Analysis_v1.0.md*
