# DRAFT TECHNICAL TOR REQUIREMENT: National Climate Adaptation Database (CRDB)
**Document Purpose**: Technical Translation Document for Vendor Communication (e.g., Ditto PCL) and DCCE Management Alignment.
**Status**: DRAFT FOR DISCUSSION
**Context**: This document translates the policy goals of the original TOR into precise Data Engineering and System Architecture requirements to ensure the delivery of a sustainable "Data Space" rather than a static "Web Portal."

---

## 1. System Paradigm & Core Architecture
The proposed system must not be a monolithic Document Management System (DMS) or a standard Content Management System (CMS). It must be implemented as a **Decoupled Data Space** comprising three distinct planes to support an evolutionary roadmap.

### 1.1 Decoupled Architecture Requirements
*   **Data Plane (Backend)**: An API-first data repository (Data Lake/Warehouse hybrid) capable of handling structured (tabular, geospatial vector/raster) and unstructured data.
*   **Control/Governance Plane (Middleware)**: A rules engine implementing the Department's 5-Gate Governance workflow (G1-G5) managing registration, metadata enrichment, endorsement, and access control (Open, G2G, Internal).
*   **Consumer Plane (Frontend)**: A Headless CMS and visualization layer that consumes data exclusively via the Data Plane APIs. 

### 1.2 "Guided Synthesis" Content Engine
*   The system must support **Dynamic Content Modeling**. Reports and articles must be treated as "Data Entities" linked to the underlying spatial and statistical datasets, not as static PDF or HTML pages.
*   Automated generation of "Briefing Packs" (e.g., Provincial Risk Summaries) pulling real-time values from the Data Plane.

---

## 2. Ingestion & Interoperability (ETL/ELT)
Manual data entry must be a secondary fallback. The primary data ingestion strategy must be automated interoperability.

### 2.1 Automated Harvester Nodes
*   The system must include Harvester/ETL services capable of scheduled data extraction from external APIs (REST, GraphQL, OGC WFS/WMS) from primary node agencies (e.g., TMD, GISTDA, DDPM, ONEP).
*   Must support "Source-to-Target Mapping" to align external schemas with the Department's central model.

### 2.2 Metadata & Standards Compliance
*   Metadata management must strictly comply with **DCAT-AP 3.0** and **ISO 19115** (Geospatial Metadata).
*   Every dataset must technically support custom "Trust & Guardrail" metadata tags (e.g., Confidence Level, Appropriate Use Case).

---

## 3. Boundary of Implementation: CRDB Project vs. System Integrator (SI)
To accelerate development and ensure domain accuracy, the Department (via the CRDB consultation project) will provide the foundational "Business Logic." The SI is responsible for the "Technical Implementation" of this logic.

### 3.1 Provided by the Department (Input Logic):
1.  **Conceptual Data Model (CDM)**: The relational map defining Climate Hazards, Exposure, Vulnerability, and Adaptation Measures.
2.  **Service Architecture (NCAIF v4)**: The required user journeys and navigational structures ("Question-First" taxonomy).
3.  **Governance Workflows (G1-G5)**: The step-by-step approval matrices for data publication.
4.  **Baseline Dataset Registry**: The prioritized list of 10-20 critical initial datasets and their source APIs.

### 3.2 Responsibility of the SI (Technical Delivery):
1.  Translate the provided CDM into a physical **Logical Database Schema** (e.g., PostgreSQL/PostGIS).
2.  Build the **ETL pipelines** to connect to the sources identified in the Baseline Registry.
3.  Develop the **RBAC (Role-Based Access Control) matrix** that physically enforces the G1-G5 workflows.
4.  Build the **Frontend interfaces and D3.js/Mapbox visualizations** that map to the NCAIF v4 journeys.

---

## 4. Specific System Features (Replacing Legacy Requirements)

| Original TOR Concept | Required Technical Implementation |
| :--- | :--- |
| "Collect and Survey Data" | Develop API Harvesters and execute Source-to-Target mapping based on the provided Registry. |
| "Write Articles for Public" | Implement a Headless CMS linked to the Data Plane to generate dynamic "Action Cards" and "Briefing Packs." |
| "Interactive Website" | Develop Intent-Driven dashboards (React/Angular) utilizing OGC APIs for geospatial rendering. |
| "Database Design" | Implement the provided Conceptual Data Model (CDM) as a relational spatial database. |

---

## 5. Personnel & Competency Requirements (Section 11 Modification)
The complexity of translating climate science into a technical architecture requires specific domain capabilities from the bidding consortium.

*   **Geospatial Data Architect (Mandatory)**: Must possess proven experience in designing multi-agency Data Spaces, OGC API implementation, and DCAT-AP metadata structuring.
*   **Climate Knowledge Broker / Domain Lead (Mandatory)**: Must possess a Master’s degree or higher in Climate Science, Environmental Economics, or a related field. Responsible for ensuring the SI's technical models accurately reflect climate risk downscaling and adaptation logic.
*   **Data Engineer (ETL Specialist)**: Responsible for building the automated Harvester nodes and API integrations.