# CRDB Phase 2 Requirements: DCCE Climate Adaptation Division Data System & MERL Methodology

## 1. Executive Summary
This document outlines the core system and methodological research requirements for the Phase 2 implementation of the Climate Resilience Database (CRDB). It translates the aspirations of the DCCE MERL (Monitoring, Evaluation, Research, and Learning) Terms of Reference into enforceable architectural requirements. By embedding advanced methodological logic (Contribution Analysis, Dual-Track M&E, Semantic Governance) directly into the system's Conceptual Data Model (CDM), the platform guarantees that climate adaptation reporting becomes a standardized, research-ready, and internationally compliant automated output.

---

## 2. System Architecture Requirements (The "Platform" Reality)

### 2.1 Federated Data Integration (The Universal Translator)
*   **Requirement:** The system MUST NOT operate as a standalone repository for submitted flat forms. It must implement a federated data architecture anchored by the Pillar 5 Conceptual Data Model (CDM).
*   **Implementation:** All ingested M&E data streams must be structurally mapped using the Pillar 8 Reference Data Matrix. Every local indicator must be tagged with standardized national codes (e.g., DOPA administrative spatial codes).
*   **Justification:** This enforces a vertical integration flow (Commune $\rightarrow$ District $\rightarrow$ Province $\rightarrow$ DCCE), allowing disconnected, hyper-local adaptation metrics to be spatially joined and aggregated automatically to meet national targets.

### 2.2 Dual-Track M&E Structural Separation
*   **Requirement:** The database schema MUST enforce a structural separation between administrative process tracking and environmental outcome tracking (following the TAMD methodology).
*   **Implementation:** 
    *   **Track 1 (Process/Readiness):** The system shall automatically ingest existing provincial capacity and administrative metrics (e.g., LPA, e-LAAS) to track policy implementation and readiness without imposing new manual reporting burdens.
    *   **Track 2 (Outcomes):** The system shall map physical and economic impacts via a 3-layer Loss & Damage Model (LDM), structurally isolating immediate casualty data (`DISASTER_EVENT`) from long-term economic valuations (`LD_ECONOMIC_LOSS`).

*(Reference: TAMD framework from the UNEP DTU Partnership guidebook: [[ψ/inbox/Adaptation metrics -  Perspectives on measuring, aggregating and comparing adaptation results|Adaptation metrics -  Perspectives on measuring, aggregating and comparing adaptation results]])*

### 2.3 Decoupling of Scientific Hazard Data
*   **Requirement:** The core relational M&E tables MUST NOT be bloated with complex, raw scientific simulation parameters (e.g., LiDAR terrain models, flood depth coefficients).
*   **Implementation:** Scientific hazard variables shall be managed via a metadata-driven registry entity (`ENVIRONMENTAL_DATA`). The database will store the STAC-compliant metadata and pointers to the custodian agencies hosting the raw scientific models, rather than storing the heavy simulation data in SQL tables.

---

## 3. Methodological Research Requirements (The MERL Upgrade)

### 3.1 "Outcome Bridge" and Contribution Analysis
*   **Requirement:** The system MUST abandon the methodological requirement for strict causal attribution and instead support systemic "Contribution Analysis."
*   **Implementation:** The architecture must contain associative bridge entities (such as `ADAPTATION_PROJECT_OUTCOME_CONTRIBUTION`). This establishes explicit database relationships between local project outputs (`ADAPTATION_OUTPUT`) and macro-level spatial resilience changes (`ADAPTATION_OUTCOME`).
*   **Justification:** This allows researchers to continuously query the database to prove how specific government interventions plausibly contributed to positive resilience trends over time, fulfilling the "Research" mandate of the MERL TOR dynamically across the entire country.

### 3.2 Automated Data Quality and Semantic Governance
*   **Requirement:** The system MUST enforce cross-sector semantic consistency to solve the "Mitigation Paradox" (where diverse sectors measure adaptation differently).
*   **Implementation:** 
    *   **Horizontal Semantic Flow:** All incoming data from Line Ministries (Agriculture, Health, Water) must be mapped against the Pillar 4 Business Glossary. 
    *   **Quality Control:** Data must pass through automated Pillar 3 Data Quality Gates (G1-G5) prior to final database commitment.
*   **Justification:** This replaces the unscalable need for continuous manual field "ground-truthing" by standardizing and validating messy cross-sector data at the point of digital entry.

### 3.3 Native A-BTR Alignment for International Finance
*   **Requirement:** The system MUST natively output the required evidence base for Thailand's Biennial Transparency Report (BTR) without requiring ad-hoc manual data calls.
*   **Implementation:** The database schema must remain 100% compliant with the 147 quantitative indicators identified during the A-BTR requirement analysis. The lineage of data—from local project entry, through the DQ Gates, into the CDM entity—must remain fully traceable.
*   **Justification:** Providing a transparent, automated, and verifiable evidence base is the foundational requirement for securing international climate finance (e.g., GCF, Adaptation Fund) and fulfilling global treaty obligations.
