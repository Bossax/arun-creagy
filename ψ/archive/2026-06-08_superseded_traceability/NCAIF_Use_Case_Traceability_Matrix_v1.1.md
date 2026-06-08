# NCAIF Use Case Inventory: Human-Readable Traceability Matrix

**Status**: SUPERSEDED by v2.0 (Moved to Archive)
**Version**: 1.1 (Exhaustive Forensic Merge)
**Date**: 2026-06-08
**Context**: This document provides the human-readable "Logic Bridge" between raw stakeholder interviews and the final Service Intelligence Report (v4.2). It contains all 32 validated Use Cases.

---

## 1. Parent Files & Lineage
To maintain **Institutional Sovereignty**, every entry in this matrix is derived from:
1.  **Technical Basis**: `Pillar_02_UseCases_FunctionalSpecs_Technical_Specification_v4.0.md`
2.  **Evidence Base**: `user_use_case_raw.md` (The raw interview bullets).
3.  **Source of Truth**: `P2_Hard_Dependencies_Inventory.json` (The technical master list).

---

## 2. Group 1: Economic & Financial (Fiscal Shield)

| UC ID     | Agency    | Use Case / Decision Moment             | Key Technical Specs                                                   | Source Anchors                |
| :-------- | :-------- | :------------------------------------- | :-------------------------------------------------------------------- | :---------------------------- |
| **UC-03** | **TBA**   | Standardized Sectoral Damage Functions | Asset-level resolution; Depth-Damage curves for ICAAP stress testing. | `[Raw-G1-1]`, `[Matrix-R2]`   |
| **UC-04** | **TBA**   | Asset-level Probabilistic Risk Maps    | 10y, 50y, 100y return periods; GeoTIFF/Vector API formats.            | `[Raw-G1-2]`, `[Matrix-R2]`   |
| **UC-09** | **NESDC** | Macro-Economic True Loss Reports       | Direct asset damage + Indirect logistics/Supply chain loss.           | `[Raw-G1-5]`, `[Matrix-R5]`   |
| **UC-18** | **BMA**   | Infrastructure Resilience Audit        | Pump performance; Drainage tunnel capacity; 100y storm event.         | `[S5-4]`, `[Matrix-R9]`       |
| **UC-19** | **DLA**   | Local Resilience Justification Pack    | ROI for **Accumulated Funds (เงินสะสม)**; Tesaban-level resolution.   | `[Raw-G1-10]`, `[Matrix-R10]` |
| **UC-31** | **UDDC**  | NbS ROI Justification                  | 20cm drone resolution; Grey vs. Green infrastructure avoidance costs. | `[Raw-G1-17]`, `[Matrix-R16]` |

---

## 3. Group 2: Spatial Planning & Engineering (Technical Seal)

| UC ID | Agency | Use Case / Decision Moment | Key Technical Specs | Source Anchors |
| :--- | :--- | :--- | :--- | :--- |
| **UC-02** | **DCCE** | Provincial Risk Profiles | Provincial with Sub-district drill-down; Hazard Baselines. | `[Matrix-R1]` |
| **UC-05** | **OTP** | Climate-Adjusted Engineering Params | Department of Highways (DoH) design code revision; 100y projections. | `[Raw-G2-26]`, `[Matrix-R3]` |
| **UC-06** | **OTP** | Highway KM-marker Hazard Projections | **Kilometer Marker** resolution; GIS-linked utility asset IDs. | `[Raw-G2-37]`, `[Matrix-R3]` |
| **UC-07** | **DPT** | Resilient Urban Planning Guidance | 20-year Planning Horizon; Land-use suitability zonation. | `[Raw-G2-27]`, `[Matrix-R4]` |
| **UC-08** | **DPT** | Climate-Adjusted Rainfall Tables | Hourly Rainfall Intensity; IDF Curves for drainage redesign. | `[Raw-G2-26]`, `[Matrix-R4]` |
| **UC-15** | **MSDHS** | Human Settlement Habitability | 2-5 year Forecast; Permanent inundation risk; Community relocation. | `[Raw-G2-20]`, `[Matrix-R8]` |
| **UC-23** | **NSO** | EA-level Population Exposure | **Enumeration Area (EA)** units (~250 buildings) census-linked. | `[Raw-G2-32]`, `[Matrix-R12]` |
| **UC-29** | **DMR** | Predictive Geologic Hazard Mapping | Site-specific 1:50,000 Scale; Landslide susceptibility; Building permits. | `[Matrix-R15]` |
| **UC-30** | **UDDC** | Neighborhood-scale Double Vulnerability | Urban Block resolution; Physical risk overlay + Poverty indicators. | `[Raw-G4-46]`, `[Matrix-R16]` |

---

## 4. Group 3: Operations & Surveillance (Intelligence Core)

| UC ID | Agency | Use Case / Decision Moment | Key Technical Specs | Source Anchors |
| :--- | :--- | :--- | :--- | :--- |
| **UC-13** | **FTI** | Industrial Water Scarcity Models | EEC Scale; Production loss per m3 water scarcity coefficients. | `[Raw-G2-30]`, `[Matrix-R7]` |
| **UC-14** | **FTI** | Water Supply-Demand Forecasts | Monthly/Seasonal Reservoir Inflow Projections (EEC). | `[Raw-G2-31]`, `[Matrix-R7]` |
| **UC-16** | **MSDHS** | Priority Evacuation Registry | Bedridden/Elderly patient ID matching with live flood zones. | `[Raw-G3-39]`, `[Matrix-R8]` |
| **UC-17** | **BMA** | Neighborhood Heat-Risk Index | 100m City Grid; WBGT/Humidex near real-time alerts. | `[Raw-G3-44]`, `[Matrix-R9]` |
| **UC-21** | **DDPM** | Disaster Declaration Certificate | Ministry of Finance relief fund activation; District-level. | `[S4-2]`, `[Matrix-R11]` |
| **UC-22** | **DDPM** | Sectoral Impact Valuation | Damage Proxy Values; Sendai Framework sub-indicators (C-2 to C-6). | `[Raw-G1-8]`, `[Matrix-R11]` |
| **UC-25** | **DOH** | Health Risk Surveillance System | [Enrichment] Heat Index; Epidemiological R506 format integration. | `[S6-3]`, `[Matrix-R13]` |
| **UC-26** | **DOH** | Heat-Stress Mortality Projections | Wet Bulb Globe Temp (WBGT); Mortality coefficients. | `[S6-3]`, `[Matrix-R13]` |

---

## 5. Group 4: Policy & Governance (Authoritative Baseline)

| UC ID | Agency | Use Case / Decision Moment | Key Technical Specs | Source Anchors |
| :--- | :--- | :--- | :--- | :--- |
| **UC-01** | **DCCE** | National Adaptation Dashboard | NAP Progress Indicators; GGA Alignment; Quarterly latency. | `[Matrix-R1]` |
| **UC-10** | **NESDC** | SDG Baseline Indicators | death/affected (13.1.1); DRR Strategy (11.b.2); Verified series. | `[Raw-G5-58]`, `[Matrix-R5]` |
| **UC-11** | **NXPO** | Adaptation Research Priorities | Technology Readiness Levels (TRL); Research funding gap analysis. | `[Raw-G2-34]`, `[Matrix-R6]` |
| **UC-12** | **NXPO** | Climate Innovation Opportunity Maps | Innovation Sandbox Locations; 10-20 year Horizon. | `[Raw-G2-35]`, `[Matrix-R6]` |
| **UC-20** | **DLA** | Performance Index (LPA) Alignment | Local Performance Assessment indicators; National target mapping. | `[Raw-G1-11]`, `[Matrix-R10]` |
| **UC-24** | **NSO** | Consolidated Official Dataset | FDES Environment Statistics; Metadata quality standards. | `[Raw-G5-81]`, `[Matrix-R12]` |
| **UC-27** | **ONEP** | Ecosystem Risk Repository | [Enrichment] TH-BIF integration; Park/Protected Area scale. | `[S1-2]`, `[Matrix-R14]` |
| **UC-28** | **ONEP** | Climate-Adjusted Biodiversity Baselines | Species Range Shifts; Bioclimatic Envelopes (2050/2070). | `[S1-2]`, `[Matrix-R14]` |
| **UC-32** | **DGA** | GDX Authoritative Exchange | Digital Govt Act (Article 15); Data masking/anonymization API. | `[Raw-G5-67]`, `[Matrix-R17]` |

---
*NCAIF Forensic Traceability Matrix — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Use_Case_Traceability_Matrix_v1.1.md*
