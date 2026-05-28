# Deliverable: Pillar 4 — Business Glossary (Core Seeding)

**Date**: 2026-05-27
**Status**: Seeded (Draft for Pillar 5 Alignment)
**Project**: CRDB (Climate Resilience Data Base)

## 0. Executive Summary
This glossary establishes the **Universal Semantic Layer** for the CRDB project. It bridges the gap between international scientific standards (IPCC, Sendai, ISO) and local policy requirements. Every term defined here is mapped to a corresponding entity in the Pillar 5 Conceptual Data Model (CDM) to ensure technical integrity.

---

## 1. Core Terms & Definitions

| Term_ID      | Canonical Name (EN/TH)                                            | Business Definition (Tier 1)                                                                                 | Technical Definition (Tier 2)                                                                                      | Source Anchor        | CDM Entity Link             |
| :----------- | :---------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- | :------------------- | :-------------------------- |
| **TERM_001** | **Hazardous Event** (เหตุการณ์อันตราย)                       | A specific, discrete occurrence of a natural disaster that causes harm.                                     | “เหตุการณ์อันตราย” หมายถึง การเกิดขึ้นจริงของภัยที่มีศักยภาพก่อให้เกิดความเสียหาย พื้นที่ได้รับผลกระทบ และความถี่ที่บันทึกได้อย่างเป็นระบบ | Sendai / ISO 14091   | `HAZARDOUS_EVENT`           |
| **TERM_002** | **Climate Driver** (ปัจจัยขับเคลื่อนสภาพภูมิอากาศ)                | Long-term changes or states in climate patterns (e.g., mean temperature increase, sea level rise).           | Continuous physical fields or Climatic Impact-Drivers (CID) as defined by IPCC AR6.                                | IPCC AR6 / ISO 14091 | `CLIMATE_DRIVER`            |
| **TERM_003** | **Exposure** (การเปิดรับภัย)                                         | The presence of people, livelihoods, or assets in places that could be adversely affected.          | The spatial intersection of a hazard's intensity/extent with an asset inventory.                                   | ISO 14091 / IPCC     | (Spatial Relation)          |
| **TERM_004** | **Vulnerability** (ความเปราะบาง)                                  | The internal characteristics that make them susceptible to harm.                                            | The intrinsic predisposition to be adversely affected; a function of Sensitivity and Adaptive Capacity.            | ISO 14091            | `VULNERABILITY_DEFINITION`  |
| **TERM_005** | **Risk** (ความเสี่ยง)                                             | The potential for adverse consequences resulting from the interaction of hazards and vulnerability.          | Calculated potential consequences ($Risk = f(Hazard, Exposure, Vulnerability)$).                                   | ISO 14091 / IPCC     | `RISK_ASSESSMENT`           |
| **TERM_006** | **Loss & Damage** (ความสูญเสียและความเสียหาย)                     | Realized negative impacts that have already occurred.                                                       | Deterministic outcome records categorized by Sendai Targets A-D.                                                   | Sendai Framework     | `LOSS_DAMAGE_RECORD`        |
| **TERM_007** | **Attribution** (การระบุสาเหตุ)                                   | The process of linking a specific impact or trend to climate change.                                         | The formal logical link (`ATTRIBUTION_LINK`) between a Loss Record and its Cause (Event or Driver).                | IPCC / CRDB          | `ATTRIBUTION_LINK`          |
| **TERM_008** | **Adaptation** (การปรับตัว)                                       | The process of adjustment to actual or expected climate to minimize harm.                                    | Iterative organizational process (Establish > Plan > Implement > M&E) per ISO 14090.                               | ISO 14090            | `ADAPTATION_PROJECT`        |
| **TERM_010** | **Exposed Asset** (สินทรัพย์ที่เปิดรับภัย)                           | Physical or social elements located in hazard-prone areas.                                                   | Entities in the exposure inventory, ideally aligned to GED4ALL/TGEIS taxonomies.                                   | GED4ALL / TGEIS      | `EXPOSED_ASSET`             |
| **TERM_011** | **Vulnerability Determinant** (ปัจจัยกำหนดความเปราะบาง)           | Individual variables or indicators that influence vulnerability.                                            | Neutral socio-economic indicators used as variables in a vulnerability framework.                                  | ISO 14091            | `VULNERABILITY_DETERMINANT` |
| **TERM_012** | **Impact Function** (ฟังก์ชันความเสียหาย)                         | A mathematical formula used to calculate damage based on hazard intensity.                                   | Quantitative "Damage Functions" used in actuarial modeling (e.g., CLIMADA).                                        | CLIMADA / P5 Anchor  | `IMPACT_FUNCTION`           |
| **TERM_013** | **Spatial Unit** (หน่วยพื้นที่)                                   | The common geographic boundary used for data analysis.                                                       | The geometric foundation (Admin Level 3, DGGS, or Catchment) used for spatial joins.                               | CRDB / ISO 19115     | `SPATIAL_UNIT`              |
| **TERM_014** | **Baseline** (กรณีฐาน)                                  | The historical state used to compare against future changes.                                                 | Reference data or time-period (e.g., 1981-2010) used for model calibration.                                        | IPCC / P2 UC-01      | (Metadata Attribute)        |
| **TERM_015** | **Projection** (การคาดการณ์อนาคต)                                 | A potential future evolution often based on scenarios.                                                       | Future climate model outputs based on SSP/RCP scenarios.                                                           | IPCC / P2 UC-01      | `CLIMATE_SCENARIO`          |
| **TERM_016** | **LAO** (องค์กรปกครองส่วนท้องถิ่น)                         | Local Administrative Organizations responsible for sub-district adaptation.                                 | Level-3 administrative units with specific mandates for local planning and budget.                                 | Thai Governance      | `SPATIAL_UNIT`              |
| **TERM_017** | **DDPM** (กรมป้องกันและบรรเทาสาธารณภัย)                     | The primary authority for disaster data in Thailand.                                                        | The source agency for `DISASTER_RECORD` and `LOSS_DAMAGE_RECORD`.                                                  | Thai Governance      | (Data Steward)              |
| **TERM_018** | **Residual Risk** (ความเสี่ยงที่ยังคงอยู่)                        | The risk that remains even after adaptation measures have been implemented.                                  | Calculated risk outcome where $Risk = f(H, E, V)$ and $V$ reflects current adaptation.                              | ISO 14091            | `RISK_METRIC`               |
| **TERM_019** | **Impact Chain** (ห่วงโซ่ผลกระทบ)                                 | A visual representation of how a hazard cascades through a system to cause impacts.                          | A directed acyclic graph (DAG) mapping cause-effect relationships per ISO 14091.                                   | ISO 14091            | `FRAMEWORK_STRUCTURE`       |
| **TERM_020** | **Nature-based Solutions** (การแก้ปัญหาโดยใช้ธรรมชาติเป็นฐาน) | Actions that protect ecosystems to address climate challenges.                                               | A specific category of `ADAPTATION_OPTION` focused on ecological restoration.                                      | IUCN / ISO 14090     | `ADAPTATION_OPTION`         |
| **TERM_021** | **Resilience** (การมีภูมิคุ้มกัน)                                        | The capacity of systems to cope with a hazardous event and recover.                                          | “ความสามารถในการฟื้นตัวจากภัยพิบัติ” หมายถึง ขีดความสามารถในการคาดการณ์ เตรียมพร้อม และฟื้นฟูจากผลกระทบของภัยได้อย่างทันท่วงที | DCCE M&E Platform | `RESILIENCE_ASSESSMENT`               |
| **TERM_022** | **Decision Readiness** (ระดับความพร้อมสำหรับการตัดสินใจ)          | A label that tells a user if a dataset is reliable for decisions.                                            | A metadata quality seal (MVP-4) based on uncertainty and data confidence scores.                                   | CRDB / MVP-4         | (Metadata Attribute)        |


---

## 2. Usage Guidelines
1.  **Term IDs are Mandatory**: All technical specifications (Pillar 5, 6, 8) must reference these IDs to prevent semantic drift.
2.  **Tiered Logic**: Use **Tier 1** for executive briefings and UI labels; use **Tier 2** for database schema design and API documentation.
3.  **Governance**: Changes to "Core" terms require review by the DCCE Semantic Steward to ensure alignment with the Climate Change Act and international reporting (Sendai/UNFCCC).

---

## 3. Extended Terms (V2 Research Batch)
refer to csv files

---

## 4. Revision History & V4 Summary

This deliverable has undergone significant technical hardening in **Versions 3 and 4** to support database implementation.

### Key Changes in V4:
1.  **100% Data Completion**: All 56 terms now have full Thai names, Business Definitions, and Technical (Tier 2) Definitions.
2.  **Structural Alignment**: Restored user-preferred terms and updated **Vulnerability Dimensions/Frameworks** to mirror **Resilience** entities, ensuring analytical consistency across both concepts.
3.  **Expanded Vocabulary**: Added **TERM_043–056** covering operational disaster management, loss & damage records, climate finance (Government Advance Fund), Climate Scenarios, and NAP Process Modules A-D.
4.  **Database Integration**: Technical definitions now explicitly reference **CDM Entities** (e.g., `HAZARD_MAP`, `ADAPTATION_PROCESS`, `RESILIENCE_ASSESSMENT`) to serve as a direct spec for developers.
5.  **Source Synchronization**: Aligned definitions with the **DCCE M&E Platform** official source and recent research on **Hazard Modification** taxonomy.

---

## 5. Implementation Nuances & Semantic Uncertainty Zones

During the consolidation of the V2 research batch, several "Uncertainty Zones" were identified. Implementers (Database Architects and Policy Analysts) should note the following nuances:

### 5.1 Project-Specific Definitions (Resilience Cluster)
*   **Terms**: `TERM_034` (Resilience Dimension) and `TERM_035` (Resilience Structure).
*   **Nuance**: In international literature (IPCC/UNDRR), these are often interchangeable. In CRDB, we use **Dimension** as a *categorical* tag (Coping/Adaptive) and **Structure** as a *logical* mapping (weightings/joins) in the database schema. This distinction is project-specific to support the CDM's flexibility.

### 5.2 Probabilistic vs. Deterministic Functions
*   **Terms**: `TERM_012/039` (Impact Function) and `TERM_040` (Damage Function).
*   **Nuance**: While often synonyms in policy briefings (Tier 1), in technical modeling (Tier 2):
    *   **Impact Function**: Refers to probabilistic curves (e.g., depth-damage curves used in CLIMADA).
    *   **Damage Function**: Refers to deterministic actuarial calculations of realized or specific physical loss.

### 5.3 Grounding Status (Vulnerability Batch)
*   **Terms**: `TERM_037` to `TERM_042`.
*   **Nuance**: These definitions are currently derived **100% from internal CDM drafts**. While they ensure internal technical consistency, they have not yet been fully cross-referenced with the final IPCC AR6 "Climatic Impact-Drivers" (CID) technical papers.

### 5.4 Thai Translation & Legal Alignment
*   **Term**: `TERM_026` (Climate Impact Driver).
*   **Nuance**: The Thai term used (*ปัจจัยขับเคลื่อนผลกระทบทางภูมิอากาศ*) is a scientific translation. This should be reviewed against the final language in the **Thailand Climate Change Act** once enacted to ensure legal alignment.

### 5.5 Risk vs. Resilience Assessment Hierarchy
*   **Nuance**: There is a potential overlap between `TERM_030` (Risk Assessment) and `TERM_037` (Resilience Assessment). Current logic treats **Risk Assessment** as the primary umbrella for calculating potential loss, while **Resilience Assessment** evaluates the system's capacity to absorb that loss.


oss, while **Resilience Assessment** evaluates the system's capacity to absorb that loss.


