# Strategic Prioritization & Discussion Note: DCCE Roadmap for Next Year

**Date**: 2026-05-27
**Context**: Climate Resilience Data Board (CRDB) - Pillar 2
**Prepared for**: Department of Climate Change and Environment (DCCE)

---

## 1. Discussion Note: User Needs and Demand Analysis

Based on the National Climate Adaptation Information Framework (NCAIF) interviews and the subsequent inter-agency consultation workshop, the demand for climate resilience data has fundamentally shifted. The analysis of 26 validated service concepts and stakeholder voting momentum reveals three defining trends in user needs:

### 1.1 The Shift from "Dashboards" to "Data Utilities"
Historically, climate platforms have focused on providing public-facing dashboards. However, the workshop evidence (particularly the high momentum in **Cluster A - Authoritative Baselines** and **Cluster C - Sectoral Standards**) indicates that power users—such as the Thai Bankers' Association (TBA), National Economic and Social Development Council (NESDC), and infrastructure planners (DPT)—require **machine-readable data (APIs) over visual dashboards**. They need raw, probabilistic data to feed their internal financial risk models and engineering design software.

### 1.2 The Demand for "Certified" Single Sources of Truth (SSOT)
The most critical bottleneck identified by agencies is not a lack of data, but a lack of *authoritative* data. Agencies (e.g., ONWR, LDD) reported instances of conflicting climate baselines leading to incompatible adaptation plans and rejected budget requests. The highest workshop momentum was directed toward **UC-01 (Authoritative Baseline & Projection Registry)**. Users are explicitly demanding that DCCE act as a certifier—stamping specific datasets (e.g., 50-year CMIP6 projections) as the "Official National Baseline" to provide a procurement-safe shield for their investment justifications.

### 1.3 The Necessity of "Tambon-Level" Granularity
For local operations and vulnerable group protection, provincial-level data is insufficient. Demand from the Ministry of Social Development and Human Security (MSDHS) and local authorities heavily favored **UC-02 (Localized Vulnerability & Risk Mapping Service)**. The requirement is to overlay high-resolution hazard maps with micro-level socio-economic data at the sub-district (Tambon) scale to effectively target early warning and relief efforts.

---

## 2. Strategic Analysis: Global Best Practices & External Alignment

To validate the internal demand signals and guide DCCE's prioritization, a strategic analysis was conducted drawing on global best practices for National Adaptation Plan (NAP) platforms, UNFCCC guidelines, and international resilience frameworks.

### 2.1 SSOT Governance is a Legal and Institutional Challenge, Not Just Technical
Global best practices indicate that a Single Source of Truth requires robust institutional anchoring.
*   **Best Practice**: The platform must be mandated by national climate laws or executive decrees to ensure cross-sectoral compliance and data sharing [1][5]. Establishing a single "Data Custodian" with a technical mandate is critical for maintaining the integrity of the SSOT [1].
*   **Implication for DCCE**: Implementing UC-01 (Authoritative Baseline) requires DCCE to establish a **federated governance model** [3][8]. DCCE should act as the central convening authority (the Data Custodian) while relying on sectoral stewards (e.g., TMD, HII) for data generation. Standardized Data Sharing Agreements (DSAs) and a formal "certification" protocol are required to establish trust [1][8].

### 2.2 APIs are the Global Standard for Resilience Integration
International platforms (such as UNEP/GRID Geneva and the U.S. Climate Mapping for Resilience and Adaptation - CMRA) have proven that while dashboards are necessary for public communication, **APIs are essential for systemic integration** [3][5].
*   **Best Practice**: Platforms must provide open, well-documented APIs (REST/JSON, OGC WMS/WFS) to allow private sector (insurance, finance) and local government integration [3][7].
*   **Implication for DCCE**: Prioritizing **UC-07 (Machine-Readable Access / API Service)** aligns Thailand with global standards. This ensures the CRDB acts as an infrastructure backbone rather than a siloed web portal, enabling banks to automate climate risk screening in loan approvals [5].

### 2.3 Localized Risk Mapping Must Connect to Finance and Planning
Global evidence underscores that local risk maps are only effective if they directly inform resource allocation and project appraisal [5][8].
*   **Best Practice**: The IFRC and global NAP reviews emphasize that localized mapping must define clear triggers for early action and be integrated into municipal budgeting cycles [1][4].
*   **Implication for DCCE**: **UC-02 (Localized Risk Mapping)** must be developed in tandem with **UC-03 (Exportable Policy/Budget Briefing Pack Generator)**. Generating a Tambon-level map is step one; automatically translating that map into a standardized, evidence-backed budget request for local authorities is the ultimate strategic goal [8].

---

## 3. Prioritized Focus for DCCE (Next Year Roadmap)

Based on the intersection of strong internal agency demand and validated global best practices [5][8], DCCE should prioritize the following core modules for the upcoming year's development cycle:

### 🏆 Tier 1: The "Trust & Infrastructure" Foundation (Immediate Focus)
DCCE must establish the legal and technical backbone of the system before building specialized applications.

1.  **UC-01: Authoritative Baseline & Projection Registry**
    *   *Why*: It is the highest-voted requirement internally and aligns with the global necessity for a mandated SSOT [1][8]. Without this, downstream analysis lacks legal standing.
2.  **UC-07: Machine-Readable Access / API Service**
    *   *Why*: Enables immediate value delivery to high-capacity agencies and the financial sector, fulfilling the shift from dashboards to data utilities [3].
3.  **UC-10: Governance and Contactability Workflow**
    *   *Why*: Global SSOT models fail without clear data stewardship [1][3]. This ensures accountability for the data published in UC-01.


### 🥈 Tier 2: The "Local Action" Enablers (Secondary Focus)
Once the authoritative baselines (Tier 1) are established, DCCE should focus on translating those baselines into local action.

1.  **UC-02: Localized Vulnerability & Risk Mapping Service**
    *   *Why*: Directly answers the heavy demand for Tambon-level planning from MSDHS and LAOs.
2.  **UC-03: Exportable Policy/Budget Briefing Pack Generator**
    *   *Why*: Bridges the gap between technical risk data and the bureaucratic requirements of the Budget Bureau.
3.  **UC-05: Urban Resilience & Land-Use Planning Support**
    *   *Why*: Essential for long-term infrastructure and "Sponge City" design (DPT, BMA), aligning with global emphasis on climate-smart infrastructure investments.

### ⏳ Tier 3: Deferred or Long-Term Capabilities
Complex sectoral models (**UC-06**) and broad navigation portals (**UC-09**) should be deferred until the core infrastructure and localized mapping capabilities are stable and widely adopted.



## 4. References

[1] Open North. (2024). *Best Practices for National Adaptation Plan Data Governance and SSOT Frameworks*.  
[2] U.S. Global Change Research Program. (2023). *Fifth National Climate Assessment (NCA5)*. toolkit.climate.gov/NCA5  
[3] UNEP/GRID-Geneva. (2024). *Environmental Data Platforms and Federated Governance Models*. unepgrid.ch  
[4] UNFCCC. (2024). *Adaptation and Resilience Guidance: Institutional Arrangements for Information Sharing*.  
[5] The White House. (2023). *National Climate Resilience Framework*. bidenwhitehouse.archives.gov  
[6] NOAA National Centers for Environmental Information (NCEI). (2024). *Climate Metrics for Architecture and Engineering*.  
[7] CMRA. (2024). *Climate Mapping for Resilience and Adaptation Portal*. resilience.climate.gov  
[8] NAP Global Network. (2023). *Identifying Good Practices in National Adaptation Plans: A Global Review*. greenpolicyplatform.org  