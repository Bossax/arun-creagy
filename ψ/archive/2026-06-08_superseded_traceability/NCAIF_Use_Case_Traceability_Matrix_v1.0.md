# NCAIF Use Case Inventory: Human-Readable Traceability Matrix

**Status**: SUPERSEDED by v1.1 (Moved to Archive)
**Version**: 1.0 (Human-Readable Merge)
**Date**: 2026-06-08
**Context**: This document provides the human-readable "Logic Bridge" between raw stakeholder interviews and the final Service Intelligence Report (v4.2).

---

## 1. Parent Files & Lineage
To maintain **Institutional Sovereignty**, every entry in this matrix is derived from the following parent documents:

1.  **Technical Basis**: `Pillar_02_UseCases_FunctionalSpecs_Technical_Specification_v4.0.md` (Defines the "Forensic" methodology).
2.  **Evidence Base**: `user_use_case_raw.md` (The 55+ raw interview bullets from 13+ agencies).
3.  **Intermediate Step**: `Pillar_02_v4_Intermediate_Extraction_Matrix.md` (The initial thematic grouping).
4.  **Source of Truth**: `P2_Hard_Dependencies_Inventory.json` (The machine-readable master list).

---

## 2. Group 1: Economic & Financial (Fiscal Shield)

| UC ID     | Agency    | Use Case / Decision Moment             | Key Technical Specs                                                   | Source Anchors                |
| :-------- | :-------- | :------------------------------------- | :-------------------------------------------------------------------- | :---------------------------- |
| **UC-03** | **TBA**   | Standardized Sectoral Damage Functions | Asset-level resolution; Depth-Damage curves for ICAAP stress testing. | `[Raw-G1-1]`, `[Matrix-R2]`   |
| **UC-04** | **TBA**   | Asset-level Probabilistic Risk Maps    | 10y, 50y, 100y return periods; GeoTIFF/Vector API formats.            | `[Raw-G1-2]`, `[Matrix-R2]`   |
| **UC-09** | **NESDC** | Macro-Economic True Loss Reports       | Direct asset damage + Indirect logistics/Supply chain loss.           | `[Raw-G1-5]`, `[Matrix-R5]`   |
| **UC-19** | **DLA**   | Local Resilience Justification Pack    | ROI for **Accumulated Funds (เงินสะสม)**; Tesaban-level resolution.   | `[Raw-G1-10]`, `[Matrix-R10]` |
| **UC-31** | **UDDC**  | NbS ROI Justification                  | 20cm drone resolution; Grey vs. Green infrastructure avoidance costs. | `[Raw-G1-17]`, `[Matrix-R16]` |

---

## 3. Group 2: Spatial Planning & Engineering (Technical Seal)

| UC ID     | Agency  | Use Case / Decision Moment           | Key Technical Specs                                                  | Source Anchors                |
| :-------- | :------ | :----------------------------------- | :------------------------------------------------------------------- | :---------------------------- |
| **UC-05** | **OTP** | Climate-Adjusted Engineering Params  | Department of Highways (DoH) design code revision; 100y projections. | `[Raw-G2-26]`, `[Matrix-R3]`  |
| **UC-06** | **OTP** | Highway KM-marker Hazard Projections | **Kilometer Marker** resolution; GIS-linked utility asset IDs.       | `[Raw-G2-37]`, `[Matrix-R3]`  |
| **UC-07** | **DPT** | Resilient Urban Planning Guidance    | 20-year Planning Horizon; Land-use suitability zonation.             | `[Raw-G2-27]`, `[Matrix-R4]`  |
| **UC-08** | **DPT** | Climate-Adjusted Rainfall Tables     | Hourly Rainfall Intensity; IDF Curves for drainage redesign.         | `[Raw-G2-26]`, `[Matrix-R4]`  |
| **UC-23** | **NSO** | EA-level Population Exposure         | **Enumeration Area (EA)** units (~250 buildings) census-linked.      | `[Raw-G2-32]`, `[Matrix-R12]` |

---

## 4. Group 3: Operations & Surveillance (Intelligence Core)

| UC ID     | Agency    | Use Case / Decision Moment       | Key Technical Specs                                               | Source Anchors               |
| :-------- | :-------- | :------------------------------- | :---------------------------------------------------------------- | :--------------------------- |
| **UC-13** | **FTI**   | Industrial Water Scarcity Models | EEC Scale; Production loss per m3 water scarcity coefficients.    | `[Raw-G2-30]`, `[Matrix-R7]` |
| **UC-16** | **MSDHS** | Priority Evacuation Registry     | Bedridden/Elderly patient ID matching with live flood zones.      | `[Raw-G3-39]`, `[Matrix-R8]` |
| **UC-17** | **BMA**   | Neighborhood Heat-Risk Index     | 100m City Grid; WBGT/Humidex near real-time alerts.               | `[Raw-G3-44]`, `[Matrix-R9]` |
| **UC-21** | **DDPM**  | Disaster Declaration Certificate | Ministry of Finance relief fund activation; District-level.       | `[S4-2]`, `[Matrix-R11]`     |
| **UC-25** | **DOH**   | Health Risk Surveillance System  | [Enrichment] Heat Index; Epidemiological R506 format integration. | `[S6-3]`, `[Matrix-R13]`     |

---

## 5. Group 4: Policy & Governance (Authoritative Baseline)

| UC ID | Agency | Use Case / Decision Moment | Key Technical Specs | Source Anchors |
| :--- | :--- | :--- | :--- | :--- |
| **UC-01** | **DCCE** | National Adaptation Dashboard | NAP Progress Indicators; GGA Alignment; Quarterly latency. | `[Matrix-R1]` |
| **UC-11** | **NXPO** | Adaptation Research Priorities | Technology Readiness Levels (TRL); Research funding gap analysis. | `[Raw-G2-34]`, `[Matrix-R6]` |
| **UC-24** | **NSO** | Consolidated Official Dataset | FDES Environment Statistics; Metadata quality standards. | `[Raw-G5-81]`, `[Matrix-R12]` |
| **UC-32** | **DGA** | GDX Authoritative Exchange | Digital Govt Act (Article 15); Data masking/anonymization API. | `[Raw-G5-67]`, `[Matrix-R17]` |

---
*NCAIF Forensic Traceability Matrix — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Use_Case_Traceability_Matrix_v1.0.md*
