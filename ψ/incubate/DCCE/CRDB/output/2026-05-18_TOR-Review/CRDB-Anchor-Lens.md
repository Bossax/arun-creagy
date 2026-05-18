# CRDB Anchor Lens: Audit Criteria for TOR Review (v2 - Stakeholder Driven)

**Purpose**: This document defines the non-negotiable strategic and technical requirements from the CRDB project. Every item in the new TOR (Section 5) must be evaluated against these anchors. Following sponsor feedback, this lens prioritizes **Validated Stakeholder Needs** as the primary functional requirements for the new national platform.

## 1. Validated Stakeholder Needs (Primary Functional Requirements)
The new platform must partially or fully satisfy these 5 core demand clusters identified through 39+ agency interviews:
*   **Trusted Baselines (Endorsement)**: The system must not just "store" data; it must provide a mechanism to **Endorse** and **Verify** specific hazard datasets as "Gold Standards" to resolve inter-agency conflicts.
*   **Planning & Operations Granularity**: Technical requirements must move beyond provincial summaries to support **Sub-Provincial scales** (Tambon, Neighborhood, Asset-level) as required by agencies like BMA, DPT, and UDDC.
*   **Machine-Readable & GIS-Ready Access**: APIs (REST/GraphQL) and processable spatial formats (GeoJSON/Shapefile) are mandatory. Manual downloads of PDFs or "Paper-like" maps are rejected as non-compliant.
*   **Tiered Service Design**: The UI must explicitly provide differentiated "entry points" for:
    *   **Executives**: Strategic dashboards and impact summaries (Economic/Budget justification).
    *   **Technical Analysts**: Raw data access and GIS integration.
    *   **Operational Staff**: Near-real-time or recurring monitoring feeds.
*   **Decision-Translation Support**: The system must provide tools (e.g., templates, automated calculation logic) that help users translate climate hazards into **Budget Justification, Business Continuity, and Engineering Design** arguments.

## 2. Conceptual Architecture (CDM) - The Semantic Engine
*   **Semantic Authority**: The system must enforce established definitions for core entities: *Hazard, Exposure, Vulnerability, Impact, and Adaptation Measure*.
*   **Interoperability (Entity Linkage)**: Data must not be "siloed." Every dataset must be logically linked through the CDM schema to enable cross-sectoral analysis.
*   **Boundary Management**: Support for four data handling modes: *Host, Mirror, Link, and Interpret-only*.

## 3. Service Architecture (NCAIF v4) - The User Journey
*   **NCAIF Narrative**: UI navigation must prioritize the "Storytelling" sequence: *National Situation* (Orientation) -> *Thematic Summaries* (Insight) -> *Actionable Resources* (Execution).
*   **Friction-Reduction**: Interface design must address the "Portal Fatigue" reported by stakeholders by providing *Information Scent* (previews) and clear *Owner/Steward pathways*.

## 4. Operational Governance (G1-G5) - The Publishing Rails
*   **The 5 Governance Gates**: System workflows must automate: *G1 Registration, G2 Metadata Enrichment, G3 Endorsement, G4 Crosswalk (CDM Linkage), and G5 Publishing/Archival*.
*   **The 3 Publishing Rails**: Automated access control for *Open (Public), G2G (Agency), and Internal (DCCE)* streams.

## 5. Enterprise Sustainability (Technical Baseline)
*   **API-First**: All data must be accessible via machine-to-machine (M2M) interfaces.
*   **Automated Ingestion (ETL/ELT)**: Preference for automated "Harvesting" (e.g., from TMD, GISTDA, DGA) over manual file uploads.
*   **Metadata Stewardship**: Full compliance with national metadata standards (DGA/NSO) to ensure cross-platform discoverability.
