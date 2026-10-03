# Statutory Audit: Database Authority Boundary Between DCCE and TMD

**Document Reference**: 2026-10-02_tmd-authority-test.md  
**Author**: Keth (Public Administration & Environmental Governance Specialist)  
**Target Repository**: [Arun_Creagy](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy)  
**Primary Sources**:
- [bureaucrazy.sqlite](file:///C:/Users/sitth/OracleWorkspace/Keth-goverment-agent/src/data/bureaucrazy.sqlite) (Statutory duties and ministerial decrees)
- [CC-Act-Chapter12-link-to-NFCS.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/lab/Sub-law_TOR/CC-Act-Chapter12-link-to-NFCS.md) (Draft Climate Change Act Chapter 12 statutory mapping)
- [1013_dcce-tmd-nfcs-relationship.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/traces/2026-09-26/1013_dcce-tmd-nfcs-relationship.md) (NFCS institutional trace)
- [250113_TMD_NFCS_Law-Baseline Review_V3- Legal Mandate & Governance Framework.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/WMO-NFCS/inbox_source/250113_TMD_NFCS_Law-Baseline%20Review_V3-%20Legal%20Mandate%20&%20Governance%20Framework.md)

---

## 1. Executive Summary

This statutory audit analyzes the database authority division between the Department of Climate Change and Environment (DCCE, Ministry of Natural Resources and Environment) and the Thai Meteorological Department (TMD, Ministry of Digital Economy and Society).

The draft Climate Change Act (Chapter 12, Sections 158 to 166) creates a clear two-part boundary:
1. **Physical and Meteorological Base Data (Section 160)** belongs under TMD custodianship. TMD collects, maintains, and supplies observed weather records, operational monitoring data, short and medium forecasts, and raw long-term climate projection scenarios.
2. **Climate Risk, Impact, and Adaptation Data (Sections 158 and 161)** belongs under DCCE custodianship. DCCE aggregates sectoral records, assesses spatial and socioeconomic vulnerability, links municipal datasets, and runs the public National Climate Information Center.

```
[TMD: Meteorological Science Layer]
  - Historical weather observations
  - Real-time station monitoring
  - Short/medium-term forecasts
  - Raw climate projections
           │
           ▼ (Statutory data linkage: Section 163)
[DCCE: Integration & Risk Layer]
  - National Climate Information Center (Section 158)
  - Sectoral risk and impact modeling (Section 161)
  - Inter-agency data collection powers (Section 159 & 164)
  - National Adaptation Plan (NAP) tracking
```

---

## 2. Statutory Authority Analysis: Draft Climate Change Act Chapter 12

Chapter 12 of the draft Climate Change Act governs **Climate Information and Risk Assessment** (Sections 158 to 166).

### Section 158: National Climate Information Center Mandate
Section 158 establishes the national obligation for DCCE to maintain and publish the national climate information database. The law mandates five core content areas:
1. Climate data (ข้อมูลภูมิอากาศ)
2. Risk and impact assessment data (ข้อมูลการประเมินความเสี่ยงและผลกระทบ)
3. Adaptation pathways and case studies (แนวทางและตัวอย่างการปรับตัว)
4. Adaptation implementation progress (ผลการดำเนินงานด้านการปรับตัว)
5. Additional categories specified by DCCE ministerial announcements

### Section 160: TMD Custodianship over Base Climate Data
Section 160 designates TMD as the lead owner for Section 158(1) base climate datasets:
- **Historical Observations**: Ground station observations, synoptic historical series, radar, and satellite archives.
- **Monitoring Data**: Active weather monitoring feeds across terrestrial and maritime stations.
- **Forecasts**: Short-term and medium-range weather predictions.
- **Climate Projections**: Long-term baseline projection scenarios across national time horizons.

### Section 161: DCCE Custodianship over Risk and Vulnerability
Section 161 assigns DCCE statutory authority over Section 158(2) risk datasets:
- Combining national projection data with socioeconomic assets, land use records, and public infrastructure.
- Area-based and sector-based vulnerability assessments (water, agriculture, tourism, public health, human settlements).
- Quantifying adverse impacts on vulnerable demographic groups.

### Sections 159, 163, 164, and 166: Integration Authority and Coercive Power
- **Section 159 (Access Authority)**: Empowers DCCE to inspect and request relevant data holdings across public entities.
- **Section 163 (Mandatory Linkage)**: Compels government agencies to connect their databases and deliver necessary climate feeds directly into DCCE central infrastructure.
- **Section 164 (Data Production Orders)**: Permits DCCE to instruct partner agencies to conduct surveys, compile datasets, and submit new records when existing coverage remains insufficient.
- **Section 166 (Escalation Pathway)**: Establishes formal Cabinet dispute escalation for inter-agency jurisdictional deadlocks.

---

## 3. Current Administrative Baseline: Ministerial Regulations (bureaucrazy.sqlite)

Records in [bureaucrazy.sqlite](file:///C:/Users/sitth/OracleWorkspace/Keth-goverment-agent/src/data/bureaucrazy.sqlite) identify the existing administrative baseline established by separate ministerial regulations.

### Thai Meteorological Department (TMD, Ministry of Digital Economy and Society)
*Source: Ministerial Regulation on the Division of the Thai Meteorological Department B.E. 2560*
- **Duty 1**: Monitor, observe, track, and report weather conditions, aeronautical meteorology, and natural phenomena.
- **Duty 2**: Weather forecasting and early hazard warnings.
- **Duty 3**: Development and management of meteorological, earthquake, and geophysical databases and thematic mapping services.
- **Duty 4**: Technical standardization and maintenance for meteorological equipment, sensors, and telemetry systems.
- **Duty 6**: Official liaison and data compliance with the World Meteorological Organization (WMO).
- **Core Technical Assets**: Over 120 automated synoptic stations, regional radar networks, upper-air sounding systems, and earthquake monitoring arrays.

### Department of Climate Change and Environment (DCCE, Ministry of Natural Resources and Environment)
*Source: Ministerial Regulation on the Division of the Department of Climate Change and Environment B.E. 2566*
- **Duty 1**: Propose and formulate national climate policy, greenhouse gas mitigation plans, and national adaptation strategies.
- **Duty 2**: Track, inspect, and evaluate policy implementation; conduct climate risk and impact appraisals; publish national climate status reports.
- **Duty 5**: Collect, prepare, and operate information service platforms covering national climate change and environment data.
- **Duty 8**: Research and develop climate management technology and operate as an environmental reference hub.
- **Core Policy Assets**: National Adaptation Plan (NAP) registry, Biennial Transparency Reports (BTR), Thailand Greenhouse Gas Management accounts, and the Thailand Climate Change Adaptation Information Platform (T-PLAT).

---

## 4. Operational Comparison: Stated Law versus Documented Practice

A review of actual project operations reveals significant friction points where administrative practice departs from statutory design:

| Operational Dimension | Statutory Mandate (De Jure) | Documented Implementation (De Facto) | Source Evidence |
| :--- | :--- | :--- | :--- |
| **Climate Downscaling** | Section 160 gives TMD exclusive ownership of long-term projections. | DCCE commissions external universities to generate localized 1km x 1km downscaled models because TMD historical runs focused on regional synoptic scales. | [250113_TMD_NFCS_Law-Baseline Review_V3-Stakeholder Capacity & Baseline Matrix.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/WMO-NFCS/inbox_source/250113_TMD_NFCS_Law-Baseline%20Review_V3-Stakeholder%20Capacity%20&%20Baseline%20Matrix.md) |
| **National Framework (NFCS)** | TMD acts as the WMO-designated lead agency for climate services. | TMD and DCCE co-lead the NFCS Steering Committee under a delicate two-tier structure, deliberately avoiding unilateral ownership claims. | [1013_dcce-tmd-nfcs-relationship.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/traces/2026-09-26/1013_dcce-tmd-nfcs-relationship.md) |
| **Database Architecture** | Section 163 mandates line agencies to stream data directly into DCCE. | Agencies maintain isolated databases; data integration currently relies on bilateral MOUs and project-specific consultant data pipelines rather than automated API streams. | [cluster-infrastructure-transport-and-environment.md](file:///C:/Users/sitth/OracleWorkspace/Keth-goverment-agent/ψ/memory/knowledge/bureaucrazy-lab/cluster-infrastructure-transport-and-environment.md) |
| **Data Granularity** | National statutory aggregation. | Urban planning and local budgets require hyper-local exposure data that neither TMD observation stations nor DCCE policy indicators provide independently. | [2026-06-29_data-governance-in-climate-risk-projects-must-not.md](file:///C:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/memory/learnings/2026-06-29_data-governance-in-climate-risk-projects-must-not.md) |

---

## 5. Structural Boundary Synthesis

The statutory boundary between DCCE and TMD represents a functional division between physical atmospheric science and socioeconomic policy translation:

1. **Upstream Physical Data Authority (TMD)**:
   - Owns observational infrastructure, real-time sensing, historical meteorology, and baseline climatological modeling.
   - Operates under Ministry of Digital Economy and Society (MDES) budget lines and WMO technical protocols.
   - Serves as the primary provider of atmospheric hazard triggers (rainfall intensity, wind speed, heat index, drought anomalies).

2. **Downstream Impact and Synthesis Authority (DCCE)**:
   - Owns vulnerability assessments, spatial exposure layers, adaptation planning, and international reporting.
   - Operates under Ministry of Natural Resources and Environment (MNRE) policy mandates.
   - Converts TMD hazard inputs into sectoral loss projections, local adaptation spending justifications, and engineering guidelines.

3. **Core Institutional Friction Point**:
   - The boundary blurs at **dynamical climate downscaling** and **impact-based forecasting**. Both departments possess legitimate claims to downscaled modeling (TMD through meteorological science mandates, and DCCE through adaptation risk requirements). 
   - A formal Data Sovereignty Agreement between MNRE and MDES remains necessary to prevent redundant supercomputing expenditures and maintain a single source of truth for national planning.
