# NCAIF Service Intelligence Report (v4.0)

**Project Component**: Pillar 2 — Service Platform Consolidation & Functional Specifications
**Version**: 4.0 (Final Authoritative Release)
**Status**: Approved for Technical Implementation
**Date**: 2026-06-05

---

## 1. Executive Summary
The National Climate Adaptation Information Framework (NCAIF) is the authoritative decision-support architecture designed to operationalize Thailand's climate resilience strategy. The NCAIF functions as a unified digital ecosystem that translates complex climate projections and multi-sectoral data into actionable intelligence for state agencies, local governments, and financial institutions. 

This report consolidates the functional requirements of 32 distinct agency use cases—spanning infrastructure, health, finance, and urban planning—into seven standardized service platforms. By anchoring development in the Digital Government Act (DGA) and the draft Climate Change Act, the NCAIF ensures institutional interoperability and technical rigor. The framework establishes a "Single Source of Truth" (SSOT) to support statutory reporting, justify climate-related fiscal expenditures, and enable real-time risk monitoring across all sectors.

---

## 2. The 7 National Climate Service Platforms

The NCAIF architecture is structured around seven core service platforms. Each platform consists of a "Common Core" of shared technical capabilities and "Contextual Modules" tailored to specific agency mandates.

### S01: Centralized Data Catalog & Discovery
*   **The Common Core**: A foundational platform for the discovery, metadata standardization, and certification of national climate data. It ensures interoperability between national repositories (NSO, DCCE, ONWR).
*   **Contextual Modules**:
    1.  **Financial Verification Module**: Standardized data requirements for regulatory compliance and green finance.
    2.  **Urban Data Management Module**: Provision of high-resolution baselines for neighborhood-scale planning (UDDC/BMA).
    3.  **Governance & Access Module**: DGA-compliant authentication for secure inter-agency exchange.
*   **Traceability**: Derived from UC-01, UC-24, UC-32.

### S02: Socio-Economic Vulnerability Analytics
*   **The Common Core**: Integration of physical hazard data with socio-economic indicators to identify high-risk populations and assets.
*   **Contextual Modules**:
    1.  **Economic Resilience Module**: Tracking debt-to-asset ratios and agricultural holding exposure (NSO/FAO).
    2.  **Urban Vulnerability Module**: High-resolution mapping (10m–30m) of physical hazards overlaid with socio-economic status.
    3.  **Social Welfare Support Module**: Targeted registries for vulnerable populations (elderly, bedridden) in high-risk zones (MSDHS).
*   **Traceability**: Derived from UC-15, UC-16, UC-23, UC-30.

### S03: Climate Investment ROI & Fiscal Planning
*   **The Common Core**: Analytical tools to evaluate the economic feasibility of adaptation projects and justify capital expenditure (CAPEX) to budgetary authorities.
*   **Contextual Modules**:
    1.  **Fiscal Risk Planning Module**: Analysis of debt-to-GDP trajectories and contingent liabilities (IMF QCRAFT alignment).
    2.  **Local Government Budgeting Module**: Economic justification for the utilization of 'Accumulated Funds' for local adaptation (DLA).
    3.  **NbS Evaluation Module**: Comparative Benefit-Cost Ratio (BCR) analysis for nature-based vs. grey infrastructure (UDDC).
*   **Traceability**: Derived from UC-03, UC-04, UC-19, UC-31.

### S04: Climate Loss & Damage Assessment
*   **The Common Core**: Standardized accounting of economic and non-economic losses to support national reporting and relief mechanisms.
*   **Contextual Modules**:
    1.  **Relief Fund Support Module**: Documentation and assessment to support the activation of disaster relief funds (DDPM).
    2.  **Macro-Economic Impact Module**: Modeling of GDP impacts from sectoral disruptions and asset damage (NESDC).
*   **Traceability**: Derived from UC-09, UC-21, UC-22.

### S05: Infrastructure Risk & Engineering Specifications
*   **The Common Core**: Integration of climate projections into infrastructure design codes, asset management, and urban zoning.
*   **Contextual Modules**:
    1.  **Transport Infrastructure Module**: Hazard projections mapped to specific infrastructure segments and KM-markers (OTP).
    2.  **Urban Hydrology Module**: Climate-adjusted intensity-duration-frequency (IDF) curves for urban drainage (BPT/BMA).
    3.  **Geological Hazard Module**: Landslide susceptibility and soil stability analysis for building permits (DMR).
*   **Traceability**: Derived from UC-05, UC-06, UC-07, UC-08, UC-29.

### S06: Multi-Hazard Monitoring & Early Warning
*   **The Common Core**: Real-time monitoring of environmental thresholds to support operational decision-making.
*   **Contextual Modules**:
    1.  **Industrial Water Monitoring**: Supply-demand forecasts for industrial estates (FTI).
    2.  **Urban Heat & Health Monitoring**: Neighborhood-scale monitoring of heat intensity (WBGT index) to support public health interventions (BMA/DOH).
*   **Traceability**: Derived from UC-13, UC-14, UC-17, UC-25, UC-26.

### S07: Policy Monitoring & NAP Compliance
*   **The Common Core**: Automated tracking of progress against national (NAP) and international (SDG, GGA) climate targets.
*   **Contextual Modules**:
    1.  **Technology Tracking Module**: Monitoring of climate innovation funding and technology readiness levels (NXPO).
    2.  **Local Policy Alignment Module**: Integration of local performance indicators with national targets (DLA).
*   **Traceability**: Derived from UC-01, UC-10, UC-11, UC-12, UC-20.

---

## 3. Triple-Audit Readiness Summary

Each service has been evaluated against Data, Legal, and Technical dimensions.

### 3.1 Readiness Matrix
| ID | Service Platform Name | Data | Legal | Tech | Priority Tier |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **S01** | Centralized Data Catalog & Discovery | 5 | 4 | 5 | **Tier 1 (Immediate)** |
| **S07** | Policy Monitoring & NAP Compliance | 5 | 5 | 4 | **Tier 1 (Immediate)** |
| **S03** | Climate Investment ROI & Fiscal Planning | 3 | 3 | 4 | **Tier 2 (Mid-term)** |
| **S04** | Climate Loss & Damage Assessment | 3 | 4 | 3 | **Tier 2 (Mid-term)** |
| **S02** | Socio-Economic Vulnerability Analytics | 3 | 2 | 3 | **Tier 3 (Long-term)** |
| **S05** | Infrastructure Risk & Engineering Specs | 4 | 3 | 3 | **Tier 3 (Long-term)** |
| **S06** | Multi-Hazard Monitoring & Early Warning | 4 | 5 | 2 | **Tier 3 (Long-term)** |

### 3.2 Key Implementation Challenges
*   **Data Latency (S06)**: Current 4–6 hour ingestion cycles are insufficient for real-time alerts.
*   **Standardization Gap (S03)**: Lack of climate-adjusted ROI parameters recognized by the Bureau of the Budget.
*   **Privacy Constraints (S02)**: PDPA compliance limits the integration of individual-level social registries with high-resolution hazard maps.
*   **Technical Integration (S05)**: Substantial effort is required to embed climate projections directly into specialized engineering codes.

---

## 4. Year 1 Implementation Roadmap

Development is prioritized based on the readiness scores and institutional foundations.

*   **Phase 1: Foundational Services (Year 1: 2026–2027)**
    *   **Focus**: S01 (Data Catalog) and S07 (Policy Monitoring).
    *   **Rationale**: These services leverage existing mandates under the Digital Government Act and provide the governance foundation for all subsequent services. S01 establishes the interoperability standards, while S07 addresses immediate statutory reporting requirements.

*   **Phase 2: Economic & Fiscal Services (Year 2: 2027–2028)**
    *   **Focus**: S03 (Investment ROI) and S04 (Loss & Damage).
    *   **Rationale**: Addressing the economic evidence gap required for national and local budget approvals.

---

## 5. Regulatory Foundations

The NCAIF implementation is anchored in two primary legislative frameworks:

*   **Digital Government Act**:
    *   *Article 8*: Mandates the standardization of metadata and interoperability.
    *   *Article 15*: Authorizes inter-agency data exchange through the GDX platform.
*   **Draft Climate Change Act**:
    *   *Article 158*: Mandates the establishment of a National Climate Change Information System.
    *   *Article 163*: Requires sectoral data providers to submit standardized data for national monitoring.

---
*NCAIF Pillar 2 Deliverable — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Service_Intelligence_Report_v4.0.md*
