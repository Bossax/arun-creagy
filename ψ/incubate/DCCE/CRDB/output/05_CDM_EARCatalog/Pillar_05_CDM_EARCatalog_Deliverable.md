# Deliverable: Pillar 5 — Climate Data Model (CDM) & EAR Catalog

**Date**: 2026-05-28
**Version**: 2.1 (Hardened & Symmetrically Aligned)
**Status**: Seal Candidate (Aligned with P02 Use Cases, P04 Glossary v4, & Canonical CDM Design)
**Project**: CRDB (Climate Resilience Data Base)


## 0. Executive Summary
This Entity-Attribute-Relationship (EAR) Catalog serves as the logical backbone for the CRDB data system. It implements the "Sovereign Logic" required to bridge scientific rigor (IPCC, ISO 14091) with policy implementation (NCAIF, ISO 14090). It is designed to be platform-agnostic, providing a stable schema for any vendor implementing the physical database.

---

## 1. Domain Architecture (Logical Subject Areas)

| Domain_ID | Domain Name               | Owner (Subdivision)             | Core Logic / Focus                                                                 |
| :-------- | :------------------------ | :------------------------------ | :--------------------------------------------------------------------------------- |
| **DOM_01** | **Physical Climate**      | Climate Science / Modeling      | From raw observations to Drivers and Hazardous Events (The "Cause").               |
| **DOM_02** | **Risk & Impact**         | Risk Assessment                 | The core engine combining Hazard, Exposure, and Vulnerability (The "Calculation"). |
| **DOM_03** | **Resilience Assessment** | Policy & Planning               | Hierarchical scoring of adaptive capacity (The "Capacity").                        |
| **DOM_04** | **Adaptation Planning**   | Implementation & Monitoring     | ISO 14090 Adaptation Cycle and iterative decision support (The "Action").          |

---

## 2. Entity Catalog (Logical Entities)

| Domain_ID | Entity Name                   | Primary Key Type | Business Definition (Pillar 4 Alignment)                                   | P4 Term_ID |
| :-------- | :---------------------------- | :--------------- | :------------------------------------------------------------------------- | :--------- |
| **DOM_01** | **CLIMATE_SCENARIO**          | UUID             | Hypothetical future pathways (e.g., SSP5-8.5) used for projections.        | `TERM_015` |
| **DOM_01** | **CLIMATE_DRIVER**            | UUID             | Continuous physical states (e.g., Sea Level Rise, Temperature).            | `TERM_002` |
| **DOM_01** | **HAZARDOUS_EVENT**           | WMO-CHE UUID     | Discrete occurrences of disasters (e.g., "Typhoon Yagi").                  | `TERM_001` |
| **DOM_01** | **SATELLITE_OBSERVATION**     | UUID             | Remote sensing data capturing hazard extent and supporting maps.           | `TERM_028` |
| **DOM_01** | **METEOROLOGICAL_OBSERVATION**| UUID             | Measured weather data from stations used as dynamic inputs.                | `TERM_029` |
| **DOM_02** | **HAZARD_MODELS**             | UUID             | Computational engines that simulate hazards from drivers and static data.   | `TERM_022` |
| **DOM_02** | **HAZARD_MAP**                | UUID             | Spatial representation of hazard intensity (Modeled or Observed).           | `TERM_043` |
| **DOM_02** | **SPATIAL_UNIT**              | UUID             | The geometric foundation (Admin Level 3, DGGS Cell, Watershed).            | `TERM_013` |
| **DOM_02** | **EXPOSED_ASSET**             | UUID             | People, buildings, or crops located in hazard-prone areas.                 | `TERM_010` |
| **DOM_02** | **VULNERABILITY_FRAMEWORK**   | UUID             | The abstract strategy used to define vulnerability (Math vs. Index).       | `TERM_038` |
| **DOM_02** | **VULNERABILITY_DIMENSION**   | UUID             | Thematic pillars of vulnerability (e.g., Sensitivity, Capacity).           | `TERM_041` |
| **DOM_02** | **VULNERABILITY_STRUCTURE**   | UUID             | The mapping of specific variables to vulnerability framework dimensions.   | `TERM_042` |
| **DOM_02** | **IMPACT_FUNCTION**           | UUID             | Mathematical curves relating hazard intensity to damage percentage.        | `TERM_012` |
| **DOM_02** | **VULNERABILITY_DETERMINANT** | UUID             | Neutral social/economic indicators used as model variables.                | `TERM_011` |
| **DOM_02** | **RISK_ASSESSMENT**           | UUID             | An instance of a risk calculation (Probabilistic or Composite).            | `TERM_030` |
| **DOM_02** | **RISK_METRIC**               | UUID             | Quantitative outcomes (e.g., Expected Annual Loss).                        | `TERM_031` |
| **DOM_02** | **COMPOSITE_INDEX**           | UUID             | Qualitative or normalized resilience/vulnerability scores (Recursive).     | `TERM_036` |
| **DOM_02** | **DISASTER_EVENT**            | UUID             | The realized outcome of a hazard interacting with exposure.                | `TERM_044` |
| **DOM_02** | **DISASTER_RECORD**           | UUID             | A single observed occurrence of a disaster with summary statistics.        | `TERM_045` |
| **DOM_02** | **LOSS_DAMAGE_RECORD**        | UUID             | Historical impact data categorized by Sendai Targets A-D.                  | `TERM_046` |
| **DOM_02** | **ATTRIBUTION_LINK**          | UUID             | The formal logical link asserting cause between Loss and Hazard/Driver.    | `TERM_007` |
| **DOM_03** | **RESILIENCE_FRAMEWORK**      | UUID             | The governing methodology for resilience assessment.                       | `TERM_033` |
| **DOM_03** | **RESILIENCE_DIMENSION**      | UUID             | Thematic pillars (e.g., Social, Economic, Institutional).                  | `TERM_034` |
| **DOM_03** | **RESILIENCE_STRUCTURE**      | UUID             | Defines the weighting and aggregation logic for specific determinants.     | `TERM_035` |
| **DOM_03** | **RESILIENCE_ASSESSMENT**     | UUID             | Application of a framework to a spatial unit to generate an index.         | `TERM_037` |
| **DOM_04** | **ADAPTATION_OPTION**         | UUID             | Standardized solutions from the Adaptation Options Library.                | `TERM_020` |
| **DOM_04** | **ADAPTATION_PROJECT**        | UUID             | Specific implementation instances of an adaptation action.                 | `TERM_049` |
| **DOM_04** | **ADAPTATION_PROCESS**        | UUID             | The National Adaptation Plan (NAP) iterative process (Modules A-D).        | `TERM_053` |

---

## 3. Relationship Matrix (Cardinality & Integrity)

| Parent Entity | Child Entity | Cardinality | Business Rule / Integrity Requirement |
| :--- | :--- | :--- | :--- |
| `CLIMATE_SCENARIO` | `CLIMATE_DRIVER` | 1 : N | Scenarios simulate multiple physical drivers. |
| `CLIMATE_DRIVER` | `HAZARDOUS_EVENT`| 1 : N | Drivers (Stress) manifest as specific Events (Shocks). |
| `HAZARD_MODELS` | `HAZARD_MAP` | 1 : N | Models simulate intensity; Maps store spatial results. |
| `SATELLITE_OBSERVATION`| `HAZARD_MAP` | 1 : N | Observations produce historical observed maps. |
| `SPATIAL_UNIT` | `EXPOSED_ASSET` | 1 : N | Assets are contained within spatial units. |
| `EXPOSED_ASSET` | `VULNERABILITY_FRWK`| N : 1 | Assets share a vulnerability framework taxonomy. |
| `VULNERABILITY_FRWK` | `IMPACT_FUNCTION` | 1 : N | Polymorphic: implements Math-path implementation. |
| `VULNERABILITY_FRWK` | `VULN_DIMENSION` | 1 : N | Frameworks are composed of multiple dimensions. |
| `VULN_DIMENSION` | `VULN_STRUCTURE` | 1 : N | Dimensions define the logic of the structure. |
| `VULN_STRUCTURE` | `VULN_DETERMINANT`| N : 1 | Determinant Neutrality: Indicators are neutral. |
| `RISK_ASSESSMENT` | `HAZARD_MAP` | N : 1 | Assessment uses physical intensity maps. |
| `RISK_ASSESSMENT` | `CLIMATE_DRIVER` | N : 1 | Assessment uses climate indices (index-based). |
| `RISK_ASSESSMENT` | `RISK_METRIC` | 1 : N | Produces quantitative, probabilistic metrics. |
| `RISK_ASSESSMENT` | `COMPOSITE_INDEX` | 1 : N | Produces normalized policy scores. |
| `RESILIENCE_FRWK` | `RESILIENCE_DIM` | 1 : N | Resilience frameworks define thematic pillars. |
| `RESILIENCE_DIM` | `RESILIENCE_STRUC`| 1 : N | Dimensions define the weighting/aggregation logic. |
| `RESILIENCE_STRUC` | `VULN_DETERMINANT`| N : 1 | Determinant Neutrality: Reuses neutral indicators. |
| `RESILIENCE_ASSESS` | `COMPOSITE_INDEX` | 1 : N | Generates resilience scores (Recursive). |
| `LOSS_DAMAGE_REC` | `ATTRIBUTION_LINK`| 1 : N | Attribution must be anchored to realized loss evidence. |
| `ADAPTATION_PROJ` | `RISK_ASSESSMENT` | N : 1 | Projects are justified by a risk assessment baseline. |

---

## 4. CDM Domain Architecture (Narrative Explanation)

The CRDB Conceptual Data Model is organized into four distinct Domains that mirror the operational lifecycle of climate adaptation.

### Domain 1: Physical Climate (The Cause)
This domain manages the "Forcing" data. It captures everything from long-term **Climate Scenarios** (SSP/RCP) and **Climate Drivers** (e.g., Sea Level Rise, Temperature Trends) to discrete **Hazardous Events** (Shocks) and the raw observations (**Satellite/Meteorological**) that ground them.

### Domain 2: Risk & Impact Assessment (The Calculation)
This is the core computational engine. It implements the **Sovereignty Logic** of the CRDB:
*   **Polymorphic Vulnerability**: By separating `VULNERABILITY_FRAMEWORK` from its implementations, the system can support both insurance-grade actuarial modeling (`IMPACT_FUNCTION`) and policy-grade social assessments (`VULNERABILITY_DIMENSION`) within the same architecture.
*   **Determinant Neutrality**: Socio-economic indicators (e.g., "Poverty Rate") are stored as neutral `VULNERABILITY_DETERMINANT` facts. This ensures that the same data can be reused for both Vulnerability and Resilience assessments without duplication.

### Domain 3 & 4: Resilience & Adaptation (Capacity & Action)
These domains shift focus from the "Problem" (Risk) to the "Solution":
*   **Domain 3 (Resilience Assessment)** provides a capacity-based view, evaluating the strength of systems to absorb shocks. It follows a symmetrical structure to Vulnerability (Framework -> Dimension -> Structure).
*   **Domain 4 (Adaptation Planning)** tracks the National Adaptation Plan (NAP) lifecycle. It manages **Adaptation Options**, real-world **Adaptation Projects**, and the overarching **Adaptation Process** (Modules A-D).

---

## 5. Sovereignty Audit (Final Validation)
*   **V4 Alignment**: Verified. Entity names and Term IDs match the hardened Pillar 04 Business Glossary v4.
*   **3NF Compliance**: Verified. Separated Domain metadata from Entity records.
*   **Determinant Neutrality**: Verified. Both Vulnerability and Resilience clusters pull from the same `VULNERABILITY_DETERMINANT` library.
*   **Symmetry**: Verified. Both Vulnerability and Resilience use the (Framework -> Dimension -> Structure) hierarchy.
