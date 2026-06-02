# Pillar 2 Deliverable: Use Case Inventory & Functional Specifications

**Status**: Seal Candidate
**Date**: 2026-05-27
**Target Pillar**: Pillar 2 (CRDB Use Cases)

---

## 1. Executive Boundary Statement
This deliverable specifies the functional requirements for the Climate Resilience Data Board (CRDB). It defines "what" the system must do to support Thailand's National Adaptation Plan (NAP) and sectoral resilience. 
- **In-Scope**: Functional flows, actors, data inputs/outputs, and testable acceptance criteria.
- **Out-of-Scope**: Physical database architecture, specific UI/UX design, and vendor-specific integration code.

---

## 2. Evidence Base
This deliverable is grounded in the following validated evidence:
1. **Stakeholder Demand Analysis**: Summaries of operational friction and data needs from over 12 national agencies and associations.
2. **Service Concept Inventory**: 26 discrete service proposals generated during the multi-agency consultation workshop.
3. **Normalization & Clustering Matrix**: Mapping used to group raw stakeholder requests into canonical functional clusters.

---

## 3. Synthesis Methodology
The functional specifications in this document are derived from a systematic three-stage synthesis of cross-agency demand:

1.  **Strategic Demand Discovery**: Analysis of operational pain points, data gaps, and decision triggers captured during comprehensive stakeholder interviews. This established the "baseline friction" the system must resolve.
2.  **Collaborative Service Ideation**: Collection and documentation of 26 discrete "Service Concepts" proposed by participants during the CRDB Consultation Workshop. Each concept represents a specific institutional or technical need identified by potential users.
3.  **Normalization & Canonical Clustering**: A forensic mapping process that clustered the 26 raw concepts and interview signals into 10 high-leverage "Canonical Use Cases." This normalization prevents redundant system development by grouping similar functional needs (e.g., various mapping requests) into unified modules while preserving unique domain-specific requirements.

This methodology ensures that the final specifications represent a "Zero-Discovery" baseline, where functional demand is grounded in verified institutional evidence rather than speculative design.

---

## 4. Use Case Inventory Table
- **Inventory File**: [`Pillar_02_UseCases_FunctionalSpecs_Inventory.csv`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Inventory.csv)
- **Data Dictionary**: [`Pillar_02_UseCases_FunctionalSpecs_Inventory_Dictionary.csv`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Inventory_Dictionary.csv)

---

## 5. Per-Use-Case Functional Specifications

### UC-01: Authoritative Baseline & Projection Registry
- **Problem Statement**: Agencies use conflicting climate baselines, leading to incompatible adaptation plans and budget disputes.
- **Actors & Permissions**: 
  - *Data Steward (Pillar 7)*: Approve/Publish certified baselines.
  - *Agency User*: View/Download/API access to baselines.
- **Preconditions**: Climate projections (CMIP6) and historical data (HII/TMD) have been ingested into Pillar 3.
- **Main Flow**:
	1. Steward selects a dataset in the catalog.
	2. Steward assigns "Certified National Baseline" status and version number.
	3. System publishes dataset to the SSOT registry.
	4. Agencies access the dataset via the CRDB portal or API for their planning documents.
- **Data Inputs**: CMIP6 GeoTIFFs, Historical Station Data (CSV/Excel).
- **Data Outputs**: Certified Baseline Registry entry, Downloadable GeoPackage.
- **Acceptance Criteria**: 
	- Must support versioning (e.g., v2024.1).
	- Must include a "Seal of Authority" metadata tag visible in the UI.

### UC-02: Localized Vulnerability & Risk Mapping Service
- **Problem Statement**: Local authorities lack the high-resolution spatial data needed for sub-district (Tambon) adaptation planning.
- **Actors & Permissions**: 
  - *Local Planning Officer*: Create/View sub-district maps.
  - *DCCE Analyst*: Upload vulnerability indices.
- **Preconditions**: Hazard layers (Pillar 3) and Socio-economic data (NSO) are available.
- **Main Flow**:
	1. User selects a target Sub-district (Tambon).
	2. User selects Hazard layer (e.g., 2050 Flood Projection).
	3. System overlays Hazard with Vulnerability data (e.g., Elderly population density).
	4. System generates a localized risk map with statistics for that sub-district.
- **Data Inputs**: Hazard SHP files, NSO Population micro-data.
- **Data Outputs**: Sub-district Risk Map (Web/PDF), Statistics Table (CSV).
- **Acceptance Criteria**: 
	- Mapping must be accurate at the 1:50,000 scale or better.
	- Must allow filtering by at least 3 vulnerability categories (Age, Income, Disability).

### UC-03: Exportable Policy/Budget Briefing Pack Generator
- **Problem Statement**: Climate data is difficult to package into the specific formats required by the Budget Bureau and NESDC.
- **Actors & Permissions**: 
  - *Policy Analyst*: Generate reports.
  - *Agency Executive*: Review/Export briefings.
- **Preconditions**: Validated risk analysis exists in the system.
- **Main Flow**:
  1. User selects a policy theme (e.g., Urban Water Resilience).
  2. System aggregates relevant risk indicators and loss estimates.
  3. User adds qualitative justification text.
  4. System generates a formatted PDF "Budget Briefing Pack" citing CRDB baselines.
- **Data Inputs**: Aggregated loss stats, risk indices.
- **Data Outputs**: PDF Briefing Document, Executive Summary (DOCX).
- **Acceptance Criteria**: 
  - Reports must automatically include "Authoritative Source" citations.
  - Generation must take less than 30 seconds for standard templates.

### UC-04: Disaster Impact + Loss & Damage Intake Gateway
- **Problem Statement**: Loss and damage data is fragmented across agencies with non-standard schemas, preventing national aggregation.
- **Actors & Permissions**: 
  - *Field Officer*: Upload damage reports.
  - *DCCE Validator*: Approve/Verify data.
- **Preconditions**: Standardized L&D schema is defined in the system.
- **Main Flow**:
	1. Field officer inputs event details, coordinates, and damage type.
	2. System validates data against the schema (Pillar 3).
	3. Validator reviews evidence (e.g., photos).
	4. Data is committed to the National L&D Ledger.
- **Data Inputs**: JSON/CSV damage records, Image uploads.
- **Data Outputs**: Validated L&D Record, Aggregated Damage Dashboard entry.
- **Acceptance Criteria**: 
	- Must support mobile-friendly input forms.
	- Must enforce mandatory fields per Sendai Framework requirements.

### UC-05: Urban Resilience & Land-Use Planning Support
- **Problem Statement**: City planners do not have actionable climate parameters (e.g., 1-in-100 year flood levels) to update building codes and land-use plans.
- **Actors & Permissions**: 
  - *Urban Planner*: Query parameters.
  - *Technical Expert*: Update parameters.
- **Preconditions**: Projections for SLR, Heat, and Flood are available.
- **Main Flow**:
	1. User selects a planning zone on the map.
	2. System retrieves projected climate extremes for that zone.
	3. System provides suggested engineering parameters (e.g., "Design for +0.5m SLR").
	4. User exports parameters for inclusion in land-use regulations.
- **Data Inputs**: Projections (SLR, Rainfall intensity), Urban zoning SHP.
- **Data Outputs**: Design Parameter Report, Hazard Overlay Map.
- **Acceptance Criteria**: 
	- Parameters must be provided in standard engineering units.
	- Must support "Return Period" selection (10, 50, 100 years).

### UC-06: Sectoral Impact & Recovery Modules
- **Problem Statement**: Sectors like Biodiversity and Marine ecosystems have unique data needs and impact thresholds not covered by generic risk maps.
- **Actors & Permissions**: 
  - *Sectoral Scientist*: Upload research data.
  - *Policy Maker*: View sectoral impact alerts.
- **Preconditions**: Domain-specific monitoring data (e.g., Coral temperature) is available.
- **Main Flow**:
	1. Scientist uploads impact threshold data (e.g., "Coral bleaching starts at X degrees").
	2. System monitors relevant climate feeds.
	3. System flags areas exceeding thresholds.
	4. Policy makers receive "Impact Alert" with recovery action suggestions.
- **Data Inputs**: Domain-specific sensor data (GeoTIFF/CSV), Threshold definitions.
- **Data Outputs**: Sectoral Impact Alerts, Biodiversity Risk Maps.
- **Acceptance Criteria**: 
	- Must support at least 3 initial sectors: Marine, Agriculture, and Health.
	- Alerts must be exportable in mobile-notification formats.

### UC-07: Machine-Readable Access / API Service
- **Problem Statement**: Power users and external systems (e.g., bank risk models) need direct data streams, not just dashboards.
- **Actors & Permissions**: 
  - *System Developer*: Register for API access.
  - *External System*: Request data via API.
- **Preconditions**: Data layers are registered in the Pillar 4 API gateway.
- **Main Flow**:
	1. Developer requests an API key.
	2. External system sends a spatial query to the API (e.g., "Get flood risk for Coordinate X,Y").
	3. System validates credentials and rate limits.
	4. System returns data in JSON or OGC format.
- **Data Inputs**: Query parameters (BBOX, coordinates, filters).
- **Data Outputs**: JSON/GeoJSON streams, WMS/WFS capabilities.
- **Acceptance Criteria**: 
	- API must support standard OGC (Open Geospatial Consortium) protocols.
	- Response time for single-point queries must be < 500ms.

### UC-08: Uncertainty + Safe-Use Guidance Service
- **Problem Statement**: Users often misinterpret climate projections (e.g., treating them as weather forecasts), leading to poor policy decisions.
- **Actors & Permissions**: 
  - *DCCE Communication Officer*: Publish guidance.
  - *End User*: Read guidance.
- **Preconditions**: Uncertainty reports from modelers are available.
- **Main Flow**:
	1. User selects a dataset.
	2. System displays a "Safe-Use" banner with limitations (e.g., "Do not use for site-level engineering").
	3. User clicks "Learn More" to view full uncertainty metadata.
	4. User acknowledges limitations before high-resolution download.
- **Data Inputs**: Metadata, Model validation reports.
- **Data Outputs**: "Safe-Use" summaries, Cautionary metadata tags.
- **Acceptance Criteria**: 
	- Limitations must be displayed *before* data download for high-resolution layers.
	- Guidance must be written in non-technical language.

### UC-09: Clearinghouse / Integrated Adaptation Platform Navigation
- **Problem Statement**: Users are overwhelmed by fragmented portals and cannot find related resources (e.g., matching a hazard map to a sectoral guide).
- **Actors & Permissions**: 
  - *Public User*: Search/Discover resources.
  - *Admin*: Maintain resource links.
- **Preconditions**: External links and agency metadata are curated in the catalog.
- **Main Flow**:
	1. User enters a keyword (e.g., "Mangrove") or theme.
	2. System returns links to relevant hazard maps, sectoral guides, and project registries.
	3. System provides a "Navigation Map" showing how resources connect.
	4. User follows links to external agency portals.
- **Data Inputs**: External Resource Registry, Thematic Tags.
- **Data Outputs**: Search results, Resource Connection Map.
- **Acceptance Criteria**: 
	- Search results must include at least 5 sectoral themes.
	- Links must include "Last Verified" date.

### UC-10: Governance and Contactability Workflow
- **Problem Statement**: Users cannot find who "owns" a dataset or who to contact for technical clarification, causing bottlenecks.
- **Actors & Permissions**: 
  - *Data Steward*: Manage ownership.
  - *End User*: Request clarification.
- **Preconditions**: Agency contact registry (Pillar 7) is populated.
- **Main Flow**:
	1. User views a dataset in the catalog.
	2. User clicks "Contact Owner".
	3. System routes inquiry to the registered Data Steward/Owner.
	4. Steward tracks inquiry status in the Governance Ledger.
- **Data Inputs**: Inquiry text, User contact info.
- **Data Outputs**: Tracked Inquiry, Contact Registry entry.
- **Acceptance Criteria**: 
	- Inquiries must be logged in a central "Decision & Inquiry Ledger".
	- System must automatically notify owners of pending inquiries.

---

## 6. Traceability Matrix
(See [`Pillar_02_UseCases_FunctionalSpecs_Traceability_Matrix.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Traceability_Matrix.md))

---

## 7. Phase 1 vs Deferred Boundary
- **Phase 1 (MVP)**: UC-01, UC-02, UC-03, UC-04, UC-05, UC-07, UC-08, UC-10.
- **Deferred (Phase 2+)**:
  - **UC-06**: Complex sectoral modeling requiring real-time sensor integration (e.g., Sinkholes).
  - **UC-09**: Full integrated adaptation platform (requires broader agency linkage).

---

## 8. Change Control Note
Any modifications to these use cases must be logged in the **CRDB Change Ledger**. Major scope changes require approval from the DCCE Governance Committee.

