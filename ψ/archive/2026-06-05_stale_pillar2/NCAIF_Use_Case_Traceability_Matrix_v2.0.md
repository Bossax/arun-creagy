# NCAIF Use Case Inventory: Human-Readable Traceability Matrix

**Status**: Definitive Index (Full Exhaustive List - Activity 1 & 2)
**Version**: 2.0 (Complete Forensic Merge)
**Date**: 2026-06-08
**Context**: This document provides the human-readable "Logic Bridge" between raw stakeholder interviews (Activity 1), consultation workshop outputs (Activity 2), and the final Service Intelligence Report (v4.3). It contains all 40 validated Use Cases.

---

## 1. Parent Files & Lineage
To maintain **Institutional Sovereignty**, every entry in this matrix is derived from:
1.  **Technical Basis**: `Pillar_02_UseCases_FunctionalSpecs_Technical_Specification_v4.0.md`
2.  **Evidence Base 1 (Interviews)**: `user_use_case_raw.md` 
3.  **Evidence Base 2 (Workshop)**: `activity2_master_analysis.md`
4.  **Source of Truth**: `P2_Hard_Dependencies_Inventory.json` (The technical master list).

---

## S01: National Authoritative Data Catalog & Discovery (SSOT)

| UC ID | Agency | Use Case / Decision Moment | Key Technical Specs | Source Anchors |
| :--- | :--- | :--- | :--- | :--- |
| **UC-02** | **DCCE** | Provincial Risk Profiles | Provincial (with Sub-district drill-down); Hazard Baselines, Provincial Vulnerability Index, Exposure Layers | `[S1]`, `[S3]`, `[Matrix-R1]` |
| **UC-03** | **TBA** | Standardized Sectoral Damage Functions | Asset-level (Point/Building); Sectoral Damage Functions, Depth-Damage Curves, Asset Type Classification | `[TBA]`, `[S1]`, `[Matrix-R2]`, `[Raw-G1-1]` |
| **UC-04** | **TBA** | Asset-level Probabilistic Risk Maps | Asset-level (Point Location); Flood Depth, Flood Duration, Flood Type (Pluvial/Riverine/Coastal) | `[TBA]`, `[S1]`, `[Matrix-R2]`, `[Raw-G1-2]` |
| **UC-24** | **NSO** | Consolidated Official Dataset | Varies; Environment Statistics (FDES), Official Sectoral Baselines, Metatdata standards | `[NSO]`, `[S1]`, `[Matrix-R12]`, `[Raw-G5-77]`, `[Raw-G5-81]` |
| **UC-27** | **ONEP** | Ecosystem Risk Repository | Park/Protected Area Scale; Vegetation Indices, Habitat Suitability, Ecosystem Service Maps | `[ONEP]`, `[S1]`, `[Matrix-R14]`, `[S1-2]` |
| **UC-28** | **ONEP** | Climate-Adjusted Biodiversity Baselines | Ecosystem/Ecoregion; Species Range Shifts, Bioclimatic Envelopes, Thermal Thresholds | `[ONEP]`, `[S1]`, `[Matrix-R14]`, `[S1-2]` |
| **UC-32** | **DGA** | GDX Authoritative Exchange Entitlement | System-to-system; Data Sharing Permissions, Encryption Keys, User Access Level | `[DGA]`, `[S1]`, `[Matrix-R17]`, `[Raw-G5-63]`, `[Raw-G5-67]` |

## S02: Socio-Economic & Sectoral Vulnerability Analytics

| UC ID | Agency | Use Case / Decision Moment | Key Technical Specs | Source Anchors |
| :--- | :--- | :--- | :--- | :--- |
| **UC-15** | **MSDHS** | Human Settlement Habitability Projections | Neighborhood / Sub-district; Permanent Inundation Risk, Habitability Score, Relocation Urgency | `[MSDHS]`, `[S1]`, `[Matrix-R8]`, `[Raw-G2-20]` |
| **UC-16** | **MSDHS** | Priority Evacuation Registry | Individual / Household level; Bedridden Patient Locations, Elderly Locations, Flood Hazard Zone Overlay | `[MSDHS]`, `[S1]`, `[Matrix-R8]`, `[Raw-G2-19]`, `[Raw-G3-39]` |
| **UC-23** | **NSO** | EA-level Population Exposure Analytics | Enumeration Area (EA) ~250 buildings; Population Count, Household Type, Housing Material | `[NSO]`, `[S1]`, `[Matrix-R12]`, `[Raw-G2-32]` |
| **UC-30** | **UDDC** | Neighborhood-scale Double Vulnerability Maps | Urban Block / Neighborhood; Physical Risk overlay, Poverty Indicators, Asset Vulnerability | `[UDDC]`, `[S1]`, `[Matrix-R16]`, `[Raw-G4-46]` |
| **UC-40** | **LDD** | Ag-Sector Carbon & Recovery Support | Plot-level (Agricultural); Plot-level Rainfall/Temp/Damage, Soil Moisture, Crop Impact | `[G78-C9]`, `[G78-C10]` |

## S03: Climate Investment ROI & Fiscal Planning

| UC ID | Agency | Use Case / Decision Moment | Key Technical Specs | Source Anchors |
| :--- | :--- | :--- | :--- | :--- |
| **UC-18** | **BMA** | Infrastructure Resilience Audit | Asset/Network level; Pump Performance, Drainage Tunnel Capacity, Climate-adjusted Runoff | `[BMA]`, `[S1]`, `[Matrix-R9]`, `[S5-4]` |
| **UC-19** | **DLA** | Local Resilience Justification Pack | Municipality (Tesaban); Localized Hazard Intensity, Economic Value at Risk, Mitigation ROI | `[DLA]`, `[S1]`, `[Matrix-R10]`, `[Raw-G1-10]` |
| **UC-31** | **UDDC** | NbS ROI Justification | Project / Site Level (20cm drone res); Water Retention Capacity, Heat Mitigation Benefit, Cost of Grey Infrastructure Avoidance | `[UDDC]`, `[S1]`, `[Matrix-R16]`, `[Raw-G1-17]` |

## S04: Climate Loss & Damage Assessment

| UC ID | Agency | Use Case / Decision Moment | Key Technical Specs | Source Anchors |
| :--- | :--- | :--- | :--- | :--- |
| **UC-09** | **NESDC** | Macro-Economic True Loss Reports | Sectoral / National; Direct Asset Damage, Indirect Economic Loss, Supply Chain Disruption Cost | `[NESDC]`, `[S1]`, `[Matrix-R5]`, `[Raw-G1-5]` |
| **UC-21** | **DDPM** | Disaster Declaration Justification Certificate | District / Sub-district; Hazard Magnitude, Area Affected, Impact Magnitude (Death/Injured/Damage) | `[DDPM]`, `[S1]`, `[Matrix-R11]`, `[S4-2]` |
| **UC-22** | **DDPM** | Sectoral Impact Valuation | Sectoral / National; Damage Proxy Values, Physical Loss Statistics, Sendai Sectoral Categories | `[DDPM]`, `[S1]`, `[Matrix-R11]`, `[Raw-G1-8]`, `[Raw-G5-61]` |
| **UC-33** | **MOTS** | Tourism Resilience Info System | Provincial/Destination; Tourism Economic Vulnerability, Loss & Damage Data, Sensitivity Analysis | `[G1-C3]`, `[G1-C4]` |

## S05: Infrastructure Risk & Engineering Specifications

| UC ID | Agency | Use Case / Decision Moment | Key Technical Specs | Source Anchors |
| :--- | :--- | :--- | :--- | :--- |
| **UC-05** | **OTP** | Climate-Adjusted Engineering Parameters | Infrastructure Network Level; Rainfall Intensity, Peak Flow, Temperature Extremes | `[OTP]`, `[S1]`, `[Matrix-R3]`, `[Raw-G2-26]` |
| **UC-06** | **OTP** | Highway KM-marker Hazard Projections | KM-marker (Point/Segment); Inundation Depth at KM, Landslide Risk at KM | `[OTP]`, `[S1]`, `[Matrix-R3]`, `[Raw-G2-37]` |
| **UC-07** | **DPT** | Resilient Urban Planning Guidance | Urban/Neighborhood Scale; Hazard Zonation, Land Use Suitability, Ecosystem Service Value | `[DPT]`, `[S1]`, `[Matrix-R4]`, `[Raw-G2-27]` |
| **UC-08** | **DPT** | Climate-Adjusted Rainfall Intensity Tables | Station/City Grid; IDF Curves, Hourly Rainfall Intensity, Climate Change Factors | `[DPT]`, `[S1]`, `[Matrix-R4]`, `[Raw-G2-26]` |
| **UC-29** | **DMR** | Predictive Geologic Hazard Mapping | Site-specific / 1:50,000 Scale; Landslide Susceptibility, Sinkhole Risk Zones, Soil Stability | `[DMR]`, `[S1]`, `[Matrix-R15]` |
| **UC-38** | **MD** | Marine Infrastructure Risk Assessment | Port/Coastal Segment; Sea Level Rise (SLR) Projections, Coastal Erosion Rates | `[G4-C7]` |

## S06: Multi-Hazard & Environmental Resource Monitoring

| UC ID | Agency | Use Case / Decision Moment | Key Technical Specs | Source Anchors |
| :--- | :--- | :--- | :--- | :--- |
| **UC-13** | **FTI** | Industrial Water Scarcity Economic Loss Models | Industrial Estate / 10 sqkm; Water Supply-Demand Gap, Production Loss per m3 Water Scarcity | `[FTI]`, `[HII]`, `[Matrix-R7]`, `[Raw-G2-30]` |
| **UC-14** | **FTI** | Water Supply-Demand Forecasts | Basin / EEC Scale; Reservoir Inflow Projections, Industrial Water Demand History (10y+), Supply Projections | `[FTI]`, `[S1]`, `[Matrix-R7]`, `[Raw-G2-31]` |
| **UC-17** | **BMA** | Neighborhood Heat-Risk Intensity Index | Neighborhood / 100m Grid; Surface Temperature, Humidex, Cooling Center Locations | `[BMA]`, `[S1]`, `[Matrix-R9]`, `[Raw-G3-44]` |
| **UC-25** | **DOH** | Health Risk Surveillance System | Sub-district / Health District; Heat Index, Disease Vector Density, Respiratory Risk Index | `[DOH]`, `[S1]`, `[Matrix-R13]`, `[S6-3]` |
| **UC-26** | **DOH** | Heat-Stress Mortality Projections | Regional / Provincial; Wet Bulb Globe Temperature (WBGT), Mortality Coefficients, Vulnerable Demographic Count | `[DOH]`, `[S1]`, `[Matrix-R13]`, `[S6-3]` |
| **UC-34** | **DMCR** | Real-time Marine Ecosystem Monitoring | Coastal Grids / Stations; Sea Surface Temperature, Coral Bleaching Alerts, Water Quality Parameters | `[G1-C10]`, `[G3-C3]` |
| **UC-36** | **ONWR** | Integrated Water Management Projections | Basin Level; Flood/Drought Forecasts, Water Quality, Economic Loss Assessment | `[G3-C9]` |
| **UC-37** | **TMD** | Localized Flood Risk Maps | Sub-district; Water Absorption Thresholds, Localized Rainfall Peaks | `[G3-C10]` |
| **UC-39** | **HII** | EEC Water Scarcity Planning Service | EEC Industrial Zones; Raw Water Sources, Future Scarcity Projections | `[G78-C1]` |

## S07: Policy Monitoring & NAP Compliance

| UC ID | Agency | Use Case / Decision Moment | Key Technical Specs | Source Anchors |
| :--- | :--- | :--- | :--- | :--- |
| **UC-01** | **DCCE** | National Adaptation Compliance Dashboard | National/Provincial; NAP Progress Indicators, Sectoral Adaptation Targets, GGA Alignment Metrics | `[S1]`, `[S3]`, `[Matrix-R1]` |
| **UC-10** | **NESDC** | SDG Baseline Indicators | National / Provincial; SDG 13.1.1 (Death/Affected), Indicator 11.b.2 (DRR Strategy), Unified Baseline Metrics | `[NESDC]`, `[S1]`, `[Matrix-R5]`, `[Raw-G5-58]` |
| **UC-11** | **NXPO** | Adaptation Research Priority Dashboard | Thematic/Sectoral; Research Funding Allocation, Technology Maturity (TRL), Adaptation Gap Analysis | `[NXPO]`, `[S1]`, `[Matrix-R6]`, `[Raw-G2-34]` |
| **UC-12** | **NXPO** | Climate Innovation Opportunity Maps | Regional/Spatial; Climate Vulnerability hotspots, Innovation Sandbox Locations, Market Demand for Adapt-Tech | `[NXPO]`, `[S1]`, `[Matrix-R6]`, `[Raw-G2-35]` |
| **UC-20** | **DLA** | Performance Index (LPA) Alignment | LAO (Local Administrative Organization); LPA Climate Indicators, Local Adaptation Progress, National Target Mapping | `[DLA]`, `[S1]`, `[Matrix-R10]`, `[Raw-G1-11]` |
| **UC-35** | **PMUA** | Learning Data Repository | Regional; Area-based Planning Data, Future Hazard Alerts | `[G2-C1]` |

---
*NCAIF Forensic Traceability Matrix — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Use_Case_Traceability_Matrix_v2.0.md*
