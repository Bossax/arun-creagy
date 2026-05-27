# Pillar 2 Deliverable: Use Case Inventory & Functional Specs

## 1. Executive Boundary Statement

Pillar 2 defines *what the system must do* (user intent, triggers, inputs/outputs, and acceptance criteria). It serves as the logical sovereignty for the CRDB project, ensuring that contractors and implementers adhere to the validated functional requirements. It does not prescribe physical architecture or UI design.

## 2. Evidence List

- [NCAIF_Use_Cases.md](NCAIF_Use_Cases.md)
- [activity2_master_analysis.md](../consultation_workshop/activity2_master_analysis.md)
- [activity2_clustering_synthesis.md](../consultation_workshop/activity2_clustering_synthesis.md)
- [activity2_discourse_implications.md](../consultation_workshop/activity2_discourse_implications.md)

## 3. Canonical Use Case Inventory Table

| Use_Case_ID | Use_Case_Name | Primary_Actors | Trigger_Event | Goal_Outcome | Priority | Status | Evidence_Anchor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| UC-01 | Authoritative Baseline & Projection Registry | DCCE, TBA, NESDC | National planning cycle / Bank risk assessment | SSOT for certified climate baselines | High | Validated | CL-A, G2-C6 |
| UC-02 | Localized Vulnerability & Risk Mapping Service | DCCE, MSDHS, LAO | Local adaptation planning | Sub-district resolution hazard/vulnerability overlays | High | Validated | CL-B, G2-C4 |
| UC-03 | Exportable Policy/Budget Briefing Pack Generator | Provincial planners, DLA | Budget justification cycle | Decision-ready evidence packages for fund allocation | High | Validated | UC-03b (NCAIF) |
| UC-04 | Disaster Impact + Loss & Damage Intake Gateway | DDPM, LAO | Disaster event occurrence | Validated post-event impact data for recovery | High | Validated | CL-C, UC-01 (NCAIF) |
| UC-05 | Urban Resilience & Land-Use Planning Support | DPT, BMA, UDDC | Urban master plan revision | Climate-resilient design parameters for land-use | Medium | Validated | CL-D, G78-C8 |
| UC-06 | Sectoral Impact & Recovery Modules | Tourism, Ag, Transport | Sectoral adaptation planning | Quantification of sectoral L&D and resilient standards | Medium | Validated | CL-C, G1-C3 |
| UC-07 | Machine-Readable Access / API Service | Data Analysts, Researchers | External system integration | Direct data feeds for high-maturity power users | High | Validated | Discourse 1.2, API demand |
| UC-08 | Uncertainty & Safe-Use Guidance Service | Policy makers, Analysts | Data interpretation request | Standardized uncertainty communication & usage guides | Medium | Validated | 4.2, NXPO |
| UC-09 | Clearinghouse / Integrated Adaptation Platform | Multi-agency, Public | General adaptation discovery | Unified navigation across fragmented agency portals | Medium | Validated | G78-C5, CL-E |
| UC-10 | Governance and Contactability Workflow | DCCE, Data Owners | Data update / inquiry | Clear ownership, contact pathways, and review cycles | High | Validated | FTI, FGD1 |

## 4. Per-Use-Case Functional Specifications

### UC-01: Authoritative Baseline & Projection Registry
- **Problem Statement**: Fragmentation of climate data sources leads to inconsistent planning and lack of legal/budgetary defensibility.
- **Actors & Permissions**: DCCE (Registry Admin), Agencies/Banks (Consumers).
- **Preconditions**: DCCE has endorsed at least one historical baseline and one CMIP6 projection set.
- **Main Flow**: 
  1. User searches for \"National Baseline\".
  2. System displays certified datasets with metadata and DCCE verification seal.
  3. User downloads or accesses via API.
- **Acceptance Criteria**: 
  - Every dataset must have a \"DCCE Verified\" status.
  - Metadata must include versioning and update cadence.

### UC-02: Localized Vulnerability & Risk Mapping Service
- **Problem Statement**: Province-level data is too coarse for sub-district (Tambon) operational planning.
- **Actors & Permissions**: LAO Planners, MSDHS, DCCE.
- **Preconditions**: High-resolution hazard layers and DOPA-compliant administrative boundaries exist.
- **Main Flow**: 
  1. User selects a specific Tambon.
  2. System overlays hazard maps with socio-economic vulnerability data (e.g., disabled population concentrations).
  3. User views results on an interactive map or exports as GIS file.
- **Acceptance Criteria**: 
  - Must support Tambon-level granularity.
  - Overlays must align with DOPA administrative codes.

### UC-04: Disaster Impact + Loss & Damage Intake Gateway
- **Problem Statement**: Loss & Damage reporting is often limited to relief payouts rather than true economic impact.
- **Actors & Permissions**: DDPM (Data Owner), DCCE (Integrator).
- **Preconditions**: Disaster event has been declared.
- **Main Flow**: 
  1. Post-event impact data is uploaded/ingested from LAO/DDPM.
  2. System validates data against standard event-impact schema.
  3. Impact is mapped to economic baseline for L&D estimation.
- **Acceptance Criteria**: 
  - Support for a staging/review state before data is marked \"Sealed\".
  - Automated validation against the agreed schema.

### UC-07: Machine-Readable Access / API Service
- **Problem Statement**: High-maturity users (Banks, NESDC) need direct system-to-system integration rather than manual dashboard downloads.
- **Actors & Permissions**: API Users (Power users), System Integrators.
- **Preconditions**: Data is indexed in the CRDB data lake with appropriate access controls.
- **Main Flow**: 
  1. Developer requests API credentials.
  2. System provides API documentation and endpoints.
  3. User queries data via REST/GraphQL API using DOPA codes.
- **Acceptance Criteria**: 
  - API response must include technical metadata (provenance, confidence).
  - Response time meets minimum utility-grade performance standards.

### UC-10: Governance and Contactability Workflow
- **Problem Statement**: Knowledge loss from staff turnover and broken contact points degrade trust in government climate services.
- **Actors & Permissions**: Data Stewards, Public Users.
- **Preconditions**: Each dataset has an assigned steward role.
- **Main Flow**: 
  1. User encounters an issue or inquiry regarding a dataset.
  2. User clicks \"Contact Steward\".
  3. System routes inquiry to the current role-holder/department.
- **Acceptance Criteria**: 
  - Every catalog entry must have a valid \"Data Steward\" contact path.
  - Inquiry history is logged for audit purposes.

## 5. Phase 1 vs Deferred Boundary

### Phase 1 (MVP) Focus
- SSOT Baselines (UC-01)
- Tambon-level Risk Context (UC-02)
- API-first delivery for key partners (UC-07)
- Basic Governance/Contactability (UC-10)

### Deferred / Roadmap
- Real-time sensor-based monitoring (Advanced UC-05 patterns)
- Automated Macro-Economic L&D modeling (UC-09 complexity)
- Full \"Urban Digital Twin\" integration

## 6. Quality Control & Finality

- **ID Integrity**: Every spec matches an inventory ID.
- **Traceability**: All use cases anchored in workshop/interview evidence.
- **Logical Sovereignty**: This document constitutes the functional boundary for CRDB Pillar 2. Changes must be logged in the project trigger log.

---
*Sealed: 2026-05-27*
*Status: SEAL CANDIDATE*
