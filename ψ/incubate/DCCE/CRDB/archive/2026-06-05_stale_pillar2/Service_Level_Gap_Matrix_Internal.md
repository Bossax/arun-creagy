# Service-Level Data Gap Matrix (Internal Audit)

**Date**: 2026-06-09  
**Scope**: NCAIF Service Platforms S01–S08  
**Baseline**: Use Case Inventory v2.0 (40 UCs) & Data Catalog v3.0 (260 Datasets)  
**Methodology**: 5-Dimension Gap Typology (Phase 1 & 2 Execution)

---

## 1. Service Platform Readiness Overview

| ID | Service Platform | UCs | Supply | Readiness | Primary Typology Gap |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **S01** | Data Vault & Authoritative Certification | 7 | 58 | 🟡 Med | **Authoritative/Certification** (Missing official seals) |
| **S02** | High-Resolution Spatial Analytics | 5 | 171 | 🟢 High | **Granularity/Resolution** (Plot-level downscaling) |
| **S03** | Financial & Budgetary Decision Support | 3 | 17 | 🔴 Low | **Translational/Analytical** (Missing ROI/Damage Curves) |
| **S04** | Historical L&D Assessment | 4 | 13 | 🟡 Med | **Institutional/Legal** (Disaster records taxonomy) |
| **S05** | Resilient Engineering Parameters | 6 | 12 | 🔴 Low | **Translational/Analytical** (Climate-Adjusted IDF) |
| **S06** | Multi-Hazard Early Warning & Impact | 9 | 31 | 🟡 Med | **Temporal/Telemetry** (Real-time API connectivity) |
| **S07** | Policy M&E & Compliance | 6 | 39 | 🟢 High | **Authoritative/Certification** (M&E Metadata) |
| **S08** | Uncertainty & Evidence Management | 0 | 0 | ⚪ N/A | Migrated to Pillar 7 Governance Backlog |

---

## 2. Dimensional Gap Matrix (Phase 2 Results)

### S01: Data Vault & Authoritative Certification
*   **Foundational Primitives**: Hazard Baselines, Provincial Risk Maps, Official Sectoral Baselines.
*   **Identified Gaps**: 
    *   *Asset Type Classification*: Lack of standardized taxonomy across agencies (**Authoritative**).
    *   *Depth-Damage Curves*: Data exists as research papers but not as executable vault artifacts (**Translational**).
*   **Evidence (Supply IDs)**: DCCE_2_1, DCCE_3_1, NSO_1_7, GISTDA_5_1.

### S02: High-Resolution Spatial Analytics
*   **Foundational Primitives**: Population Count (EA-level), Plot-level Soil Moisture, Bedridden Patient Locations.
*   **Identified Gaps**:
    *   *Flood Hazard Zone Overlay*: Requires 1m-resolution DEM not yet integrated into national grid (**Granularity**).
    *   *Vulnerable Target Registry*: Protected by PDPA; requires Tier 2 access protocols (**Institutional**).
*   **Evidence (Supply IDs)**: GISTDA_1_10, DOPA_1_1, MSDHS_1_1, UDDC_1_2.

### S03: Financial & Budgetary Decision Support
*   **Foundational Primitives**: Localized Hazard Intensity, Mitigation ROI, Economic Value at Risk.
*   **Identified Gaps**:
    *   *Avoided-Loss Curves*: Critical for NbS ROI; currently missing systematic modeling (**Translational**).
    *   *Climate-adjusted Runoff*: Hydrological models for drainage tunnel justification lack certification (**Authoritative**).
*   **Evidence (Supply IDs)**: DCCE_3_1, DLA_1_1 (derived), NESDC_1_1.

### S04: Historical L&D Assessment
*   **Foundational Primitives**: Direct Asset Damage, Indirect Economic Loss, Sendai Sectoral Statistics.
*   **Identified Gaps**:
    *   *Indirect Economic Loss*: Post-disaster surveys do not capture supply chain disruption systematically (**Translational**).
    *   *Disaster Declaration Justification*: Requires automated cross-referencing with satellite evidence (**Authoritative**).
*   **Evidence (Supply IDs)**: DDPM_2_1, DDPM_3_2, DMCR_2_1, MOTS_1_1.

### S05: Resilient Engineering Parameters
*   **Foundational Primitives**: Rainfall Intensity, Temperature Extremes, Sea Level Rise (SLR) Projections.
*   **Identified Gaps**:
    *   *Hourly Rainfall Intensity*: Raw TMD data needs conversion to "Climate-Adjusted IDF" curves (**Translational**).
    *   *KM-marker Hazard Projections*: Mapping national projections to highway segments is incomplete (**Granularity**).
*   **Evidence (Supply IDs)**: TMD_1_1, MD_1_2, OTP_1_1, DOH_2_1.

### S06: Multi-Hazard Early Warning & Impact
*   **Foundational Primitives**: Heat Index, Reservoir Inflow, Localized Flood Thresholds, Coral Bleaching Alerts.
*   **Identified Gaps**:
    *   *Real-time API Feed*: Many datasets (TMD/BMA) are available as images/web-viz but lack programmatic API access (**Temporal**).
    *   *Soil Saturation Logic*: Necessary for localized flood warnings; missing as a dynamic data feed (**Translational**).
*   **Evidence (Supply IDs)**: BMA_1_1, TMD_1_5, HII_2_1, DMCR_3_4.

### S07: Policy M&E & Compliance
*   **Foundational Primitives**: NAP Progress Indicators, Sectoral Targets, SDG Baseline Metrics.
*   **Identified Gaps**:
    *   *LPA Climate Indicators*: Municipal performance index not yet aligned with National NAP goals (**Institutional**).
    *   *Research Funding Allocation*: Lack of a unified tracking system for climate innovation ROI (**Authoritative**).
*   **Evidence (Supply IDs)**: DCCE_1_1, NESDC_2_1, NXPO_1_1.

---

## 3. Findings & Foundational Primitives Identification

1.  **The "Primitive" Shortfall**: The analysis shows that while "Data" (raw records) is abundant (Supply Count > 200), "Primitives" (refined, certified, and executable data units) are missing for S03, S05, and S06.
2.  **Dominant Gap Typology**: The **Translational/Analytical** gap is the most severe bottleneck. The NCAIF project has access to data but lacks the "Scientific Conversion" to turn raw meteorological/hydrological data into actionable engineering or financial parameters.
3.  **Governance Priority**: Addressing the **Institutional/Legal** barrier for S02 is critical for the "High-Resolution" mandate, requiring the Pillar 6 Governance Framework to establish restricted data exchange entitlements.

---
*NCAIF Service-Level Data Gap Matrix — Internal Document (ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Service_Level_Gap_Matrix_Internal.md)*
