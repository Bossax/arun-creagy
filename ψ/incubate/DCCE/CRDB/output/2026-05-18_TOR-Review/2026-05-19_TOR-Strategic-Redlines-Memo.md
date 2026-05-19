# Strategic TOR Hardening Memo: National Climate Adaptation Database (CRDB)

**Target Artifact**: Draft TOR for "National Climate Change Adaptation Database" (25M THB)
**Strategic Anchor**: "Guided Synthesis" Platform Vision (2026-05-19)
**Reviewer**: ARUN (Strategic Knowledge Librarian)

---

## Executive Summary: Avoiding the "Portal Trap"
The current Draft TOR risks delivering a **"Portal Trap"**—a static website requiring heavy manual labor that will likely become obsolete shortly after contract completion. To prevent this, the TOR must shift from "Data Collection" to **"Automated Synthesis."** The following redlines ensure that the contractor delivers a scalable, interoperable **Data Space** rather than a monolithic document portal.

---

## 1. Redline: Section 11 — Personnel Requirements (The "Climate Brain")
*The risk identified in potential contractors (e.g., Ditto PCL) is high technical capacity but low climate domain expertise. We must mandate the following specific roles:*

### 11.1 Lead Climate Knowledge Broker (Synthesis Lead)
*   **Role**: Responsible for the "Guided Synthesis" logic (60% of the USP). They design the Automated Briefing Pack templates and the "Action Card" logic.
*   **Requirement**: Minimum Master’s degree in Climate Science, Environmental Economics, or related field. Must demonstrate experience in translating climate projections into policy-ready narratives.

### 11.2 Geospatial Data Architect (Trust & Guardrail Lead)
*   **Role**: Responsible for the "Trust & Guardrails" (40% of the USP). They design the Decoupled Data Space, DCAT-AP metadata schema, and the Data Lake architectural runway.
*   **Requirement**: Proven experience in enterprise data architecture, OGC APIs, and DCAT-AP/ISO 19115 standards. Must have designed at least one multi-agency data exchange system.

### 11.3 HCI/UX Specialist (Data Literacy focus)
*   **Role**: Responsible for the "Question-First" navigation and ensuring the platform is usable by policymakers with low data literacy.
*   **Requirement**: Portfolio demonstrating user-centric design for complex data systems or decision-support tools.

---

## 2. Redline: Section 5 — Scope of Work (The "Synthesis Engine")

### 5.3 Synthesis & Content Modeling (Revised)
*   **Old**: "Write articles and summaries for the public."
*   **New (Redline)**: "Develop a **Knowledge Modeling Engine**. The contractor shall design and implement automated templates for **Provincial Climate Briefing Packs** and a curated library of **Adaptation Action Cards**. Content must be dynamically linked to the underlying Conceptual Data Model (CDM) so that updates to datasets automatically trigger 'Stale-ness' flags in the synthesis."

### 5.6 Architecture & Database Design (Revised)
*   **Old**: "Design a relational database and system architecture."
*   **New (Redline)**: "The contractor MUST implement a **Decoupled Data Space Architecture** (separating Data, Control, and Application planes). The system must be built as an **API-First** infrastructure, compliant with **WIS 2.0 and OGC APIs**. The Logical Schema MUST strictly follow the **CRDB Conceptual Data Model (CDM)** provided by the Department."

### 5.7 Data Ingestion & Metadata (Revised)
*   **Old**: "Develop an ETL system for manual file uploads."
*   **New (Redline)**: "The contractor shall implement **Automated Ingestion (Harvester Nodes)**. The system must support scheduled harvesting from external agency APIs (TMD, GISTDA, DDPM). Manual uploads are permitted only as a fallback. **Metadata (5.7.5)** must be fully **DCAT-AP 3.0 compliant**, including mandatory 'Confidence Labels' and 'Appropriate Use' guardrails for every dataset."

---

## 3. Mandatory Milestone Addition
**Milestone 1.2: Architecture & Vision Alignment Workshop**
Before finalized Design (5.6), the contractor must present an "Alignment Map" showing how their proposed technical architecture realizes the **"Guided Synthesis" Vision** and the **G1-G5 Governance Gates**. Failure to align with these anchors is grounds for deliverable rejection.
