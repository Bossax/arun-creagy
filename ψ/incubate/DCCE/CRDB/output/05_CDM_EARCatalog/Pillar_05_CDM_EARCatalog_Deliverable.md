# Deliverable: Pillar 5 — Climate Data Model (CDM) & EAR Catalog

**Update plan (28 May 2025 16:45)**
 - need  to update to reflect the changes in entity name per glossary v4 
 - the entity must be specified domains/areas it is in. It could be separate tables to make the tables 3rd normal form 
 - create csv files

---
**Date**: 2026-05-27
**Status**: Seal Candidate (Aligned with P02 Use Cases & P04 Glossary)
**Project**: CRDB (Climate Resilience Data Base)


## 0. Executive Summary
This Entity-Attribute-Relationship (EAR) Catalog serves as the logical backbone for the CRDB data system. It implements the "Sovereign Logic" required to bridge scientific rigor (IPCC, ISO 14091) with policy implementation (NCAIF, ISO 14090). It is designed to be platform-agnostic, providing a stable schema for any vendor implementing the physical database.

---

## 1. Entity Catalog (Logical Domains)

| Entity Name                   | Primary Key Type | Business Definition (Pillar 4 Alignment)                             | P4 Term_ID |
| :---------------------------- | :--------------- | :------------------------------------------------------------------- | :--------- |
| **CLIMATE_SCENARIO**          | UUID             | Hypothetical future pathways (e.g., SSP5-8.5) used for projections.  | `TERM_001` |
| **CLIMATE_DRIVER**            | UUID             | Continuous physical states (e.g., Sea Level Rise, Temperature).      | `TERM_002` |
| **HAZARDOUS_EVENT**           | WMO-CHE UUID     | Discrete occurrences of disasters (e.g., "Typhoon Yagi").            | `TERM_001` |
| **SPATIAL_UNIT**              | UUID             | The common geographic boundary (Admin Level 3, DGGS Cell).           | `TERM_013` |
| **EXPOSED_ASSET**             | UUID             | People, buildings, or crops located in hazard-prone areas.           | `TERM_010` |
| **VULNERABILITY_DEFINITION**  | UUID             | The abstract strategy used to define vulnerability (Math vs. Index). | `TERM_004` |
| **IMPACT_FUNCTION**           | UUID             | Mathematical curves relating hazard intensity to damage percentage.  | `TERM_012` |
| **VULNERABILITY_FRAMEWORK**   | UUID             | Theoretical structures for indicator-based vulnerability scoring.    | `TERM_004` |
| **FRAMEWORK_STRUCTURE**       | UUID             | The mapping of specific variables to framework dimensions.           | `TERM_019` |
| **VULNERABILITY_DETERMINANT** | UUID             | Neutral social/economic indicators used as model variables.          | `TERM_011` |
| **RISK_ASSESSMENT**           | UUID             | An instance of a risk calculation (Probabilistic or Composite).      | `TERM_005` |
| **RISK_METRIC**               | UUID             | Quantitative outcomes (e.g., Expected Annual Loss).                  | `TERM_005` |
| **COMPOSITE_INDEX**           | UUID             | Qualitative or normalized resilience/vulnerability scores.           | `TERM_009` |
| **LOSS_DAMAGE_RECORD**        | UUID             | Historical impact data categorized by Sendai Targets A-D.            | `TERM_006` |
| **ATTRIBUTION_LINK**          | UUID             | The formal logical link asserting cause between Loss and Hazard.     | `TERM_007` |
| **ADAPTATION_OPTION**         | UUID             | Standardized solutions from the Adaptation Options Library.          | `TERM_020` |
| **ADAPTATION_PROJECT**        | UUID             | Specific implementation instances of an adaptation action.           | `TERM_008` |

---


## 2. Relationship Matrix (Cardinality & Integrity)

| Parent Entity | Child Entity | Cardinality | Business Rule / Integrity Requirement |
| :--- | :--- | :--- | :--- |
| `CLIMATE_SCENARIO` | `CLIMATE_DRIVER` | 1 : N | Scenarios simulate multiple physical drivers. |
| `CLIMATE_DRIVER` | `HAZARDOUS_EVENT`| 1 : N | Drivers (Stress) manifest as specific Events (Shocks). |
| `SPATIAL_UNIT` | `EXPOSED_ASSET` | 1 : N | Assets are contained within spatial units. |
| `EXPOSED_ASSET` | `VULNERABILITY_DEF`| N : 1 | Multiple assets can share a vulnerability definition. |
| `VULNERABILITY_DEF` | `IMPACT_FUNCTION` | 1 : N | Math-path implementation (e.g., CLIMADA). |
| `VULNERABILITY_DEF` | `VULN_FRAMEWORK` | 1 : N | Index-path implementation (e.g., National CRI). |
| `FRAMEWORK_STRUC` | `VULN_DETERMINANT`| N : 1 | Indicators are neutral; mapped to roles in frameworks. |
| `RISK_ASSESSMENT` | `CLIMATE_DRIVER` | N : 1 | Assessment analyzes specific climate drivers. |
| `RISK_ASSESSMENT` | `RISK_METRIC` | 1 : N | Produces probabilistic metrics. |
| `RISK_ASSESSMENT` | `COMPOSITE_INDEX` | 1 : N | Produces normalized scores. |
| `LOSS_DAMAGE_REC` | `ATTRIBUTION_LINK`| 1 : N | Every loss record must have ≥1 attribution link. |
| `ATTRIBUTION_LINK` | `HAZARDOUS_EVENT`| N : 1 | Attribution to a specific shock (Mandatory if Shock). |
| `ATTRIBUTION_LINK` | `CLIMATE_DRIVER` | N : 1 | Attribution to a slow-onset driver (Mandatory if Stress).|
| `ADAPTATION_PROJ` | `RISK_ASSESSMENT` | N : 1 | Projects are justified by a risk assessment. |

---

## 3. Attribute Registry (Mandatory Schema)

| Entity | Attribute | Data Nature | Standard / Format |
| :--- | :--- | :--- | :--- |
| `CLIMATE_DRIVER` | `Variable_Name` | Static | CF Conventions / IPCC |
| `CLIMATE_DRIVER` | `Spatiotemporal_Cube`| Temporal | NetCDF4 / OPeNDAP |
| `HAZARDOUS_EVENT` | `Event_UUID` | Static | WMO-CHE UUID |
| `SPATIAL_UNIT` | `Geometry` | Spatial | GeoJSON / WKT / DGGS |
| `EXPOSED_ASSET` | `Asset_Type` | Static | GED4ALL Taxonomy |
| `LOSS_DAMAGE_REC` | `Sendai_Target_ID` | Static | Sendai Framework A-D |
| `LOSS_DAMAGE_REC` | `Mortality_Count` | Static | Integer |
| `LOSS_DAMAGE_REC` | `Economic_Loss_LCU` | Static | Float (THB) |
| `ATTRIBUTION_LINK` | `Confidence_Level` | Static | IPCC Uncertainty Scale |
| `ADAPTATION_PROJ` | `Status` | Static | ISO 14090 (Planned/Active) |

---

## 4. Sovereignty Audit (Final Validation)
*   **Determinant Neutrality**: Verified. Socio-economic indicators are stored in `VULNERABILITY_DETERMINANT` and mapped to roles via `FRAMEWORK_STRUCTURE`.
*   **Slow-Onset Compatibility**: Verified. `ATTRIBUTION_LINK` allows linking loss to `CLIMATE_DRIVER` without requiring a fake event.
*   **Use Case Coverage**: Verified. 100% of Pillar 02 Canonical Use Cases (UC-01 to UC-10) are supported by these entities and relationships.
*   **Sitemap Coverage**: Verified. All data products in NCAIF Sitemap v4 map to ≥1 entity in this catalog.
