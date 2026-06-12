# Technical Specification: Service-Centric Use Case Extraction Plan (Pillar 2)

**Status**: Active / Methodological Plan
**Version**: 2.2 (Formalized Technical Revision)
**Date**: 2026-06-05

---

## 1. Objective
This specification defines the methodology and source inventory for identifying and defining **Climate Information Service Use Cases** for the DCCE National Climate Change Adaptation Information Framework (NCAIF). This document serves as the **Operational Plan** for the refactoring of Pillar 2.

---

## 2. Core Definitions: Service vs. System
To ensure "Service-First" alignment, the following definitions must be strictly applied:

*   **Information Service Use Case**: A specific information product or advisory that provides **Observable Value** to a decision-maker (e.g., "A National Risk Certification for Budget Defense").
*   **Technical Requirement (Mandate)**: The backend infrastructure, data pipelines, or standards required to support a service (e.g., "Metadata ingestion," "API gateways," "Data ownership ledgers"). These are **NOT** use cases.
*   **The Decision-First Principle**: A use case is only valid if it starts with a specific user decision (User-Pull) rather than a pre-existing dataset (Data-Push).

---

## 3. The Extraction Methodology 
The analysis will process each source concept through the following "Triple Filter":

1.  **The Decision Context**: What specific action/policy does the user need to justify or execute?
2.  **The Intelligence Product**: What is the *processed* output (not raw data) that the DCCE delivers to solve the problem?
3.  **The Authority Requirement**: Why does the user need the *DCCE* to provide this, rather than a generic vendor? (e.g., "Certification," "Official Baseline," "National Audit").

---

## 4. Source Inventory (The Evidence Base)
The following sources MUST be processed to extract the final service list. These represent the "Grounded Memory" of the project.

### 4.1 Workshop Evidence (Activity 2)
*   `ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_master_analysis.md` (Normalized Concepts)
*   `ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_raw_extraction.md` (Original Stakeholder Language)
*   `ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_clustering_synthesis.md` (Thematic Clusters)

### 4.2 Stakeholder Interview Evidence
1.   `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - BMA.md`
2.   `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DLA.md`
3.   `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DPT.md`
4.   `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - MSDHS.md`
5.   `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NESDC.md`
6.   `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NSO.md`
7.   `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NXPO.md`
8.   `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - OTP.md`
9.   `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - Thai Bankers' Association.md`
10.   `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - UDDC.md`
11.   `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary DDPM.md`
12. [ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - FTI](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - FTI)
13. [ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DGA](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DGA)

---

## 5. Operational Plan: The Transparent Extraction Workflow
To ensure maximum transparency, traceability, and context management, the extraction process will follow a staged workflow using **intermediate artifacts** stored within this directory.

### Phase 1: Forensic Extraction (Evidence Audit)
*   **Method**: Utilize three specialized sub-agents to process the 17+ sources in parallel clusters (Workshop, Infrastructure, Policy/Social).
*   **Artifact**: `Pillar_02_Intermediate_Extraction_Matrix.md`
*   **Content**: A raw, un-filtered table mapping every "Decision Moment" to a Source ID, Decision Context, and Intelligence Product.

### Phase 2: Canonical Clustering (Service Synthesis)
*   **Method**: Horizontal analysis of the Extraction Matrix to identify service patterns and technical overlaps.
*   **Artifact**: `Pillar_02_Intermediate_Clustering_Synthesis.md`
*   **Content**: A "Logic Memo" explaining the clustering of raw needs into the final 7-8 National Services, including the re-classification of technical requirements as "Infrastructure Products."

### Phase 3: Final Productization & Hardening
*   **Method**: Drafting the final report and traceability matrix.
*   **Artifact**: `NCAIF_Service_Intelligence_Report.md` (Final Deliverable)

---

## 6. Output Format: The "Service Intelligence" Profile
Every extracted use case must be documented using this "Service-First" template:

| Field | Description |
| :--- | :--- |
| **Service Name** | A value-oriented title (e.g., "National Risk Certification Service"). |
| **User Persona** | The specific decision-maker (e.g., "Provincial Planner," "Bank Risk Officer"). |
| **Decision Trigger** | The real-world event/need that initiates the service. |
| **Intelligence Product** | The specific "Authoritative Package" delivered (Advisory, Report, Map). |
| **Outcome / Value** | The "So What?" (e.g., "Budget approved," "Infrastructure hardened"). |
| **Underlying Standard** | The technical "Standard-as-Product" that makes it authoritative (The "Pipes"). |

---

## 7. Execution Mandate
1.  **Purge**: Remove all references to "Intake Gateways," "Repositories," and "Registries" as top-level use cases.
2.  **Broaden**: Re-frame "Climate Baselines" (UC-01) as a comprehensive "National Risk Certification" encompassing Hazard, Exposure, and Vulnerability.
3.  **Consolidate**: Group the 26 raw workshop concepts into **6-8 High-Impact Intelligence Services**.
4.  **Traceability**: Maintain 1:1 traceability from the final report back to the `Pillar_02_Intermediate_Extraction_Matrix.md`.

---
*Oracle Technical Specification — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md*
