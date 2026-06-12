# Technical Specification: Service-Centric Use Case Synthesis (Pillar 2)

**Status**: Draft for Approval
**Version**: 3.0 (Hardened Operational Plan)
**Date**: 2026-06-05

---

## 1. Objective
This specification defines the rigorous methodology and source inventory for identifying and defining **Climate Information Service Use Cases** for the DCCE National Climate Change Adaptation Information Framework (NCAIF). This version hardens the v2.0 plan by incorporating lessons learned from the first analysis round to ensure institutional value and technical rigor.

---

## 2. Core Definitions: Service vs. System
To ensure "Service-First" alignment and prevent "Contractor Logic," the following definitions apply:
*   **Information Service Use Case**: A specific information product or advisory providing **Observable Value** to a decision-maker (e.g., "National Risk Certification").
*   **Technical Requirement (Mandate)**: Infrastructure components (e.g., "Metadata ingestion," "API gateways"). These are **NOT** use cases but **Supporting Infrastructure**.
*   **The Decision-First Principle**: A use case is only valid if it starts with a specific user decision (User-Pull) rather than a pre-existing dataset (Data-Push).

---

## 3. Lessons Learned & Guardrails (Round 1)
The synthesis must explicitly avoid the following identified failure modes:
1.  **Avoid "Data-Push" Bias**: Analysis must include "Institutional Data" (policy, budget, status) which carries equal decision-value to physical science data.
2.  **Re-frame Chores as Services**: "Monitoring & Evaluation" and "Reporting" are not chores; they are automated **Tracking Services** that reduce administrative burden.
3.  **Prevent Jargon Leak**: Terms like "API" and "Database" must be replaced with institutional outcomes (e.g., "Exchange Service," "Authoritative Registry").
4.  **No Monolithic Designs**: Use cases must align with the **Copernicus CDS Decoupled Architecture** (Metadata Layer vs. Payload Delivery).

---

## 4. The Extraction Methodology (The Triple Filter)
Every concept from the sources must pass through the following filters:
1.  **The Decision Context**: What specific action/policy does the user need to justify or execute?
2.  **The Intelligence Product**: What is the *processed* output (not raw data) that the DCCE delivers to solve the problem?
3.  **The Authority Requirement**: Why is the *DCCE Official Seal* required for this transaction?

---

## 5. Source Inventory (The Evidence Base)
The following **17 sources** represent the "Grounded Memory" and MUST be processed:

### 5.1 Workshop Evidence (Activity 2)
*   `ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_master_analysis.md` (Normalized Concepts)
*   `ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_raw_extraction.md` (Stakeholder Language)
*   `ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_clustering_synthesis.md` (Thematic Clusters)

### 5.2 Stakeholder Interview Evidence
1.  `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - BMA.md`
2.  `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DLA.md`
3.  `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DPT.md`
4.  `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - MSDHS.md`
5.  `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NESDC.md`
6.  `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NSO.md`
7.  `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NXPO.md`
8.  `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - OTP.md`
9.  `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - Thai Bankers' Association.md`
10. `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - UDDC.md`
11. `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary DDPM.md`
12. `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - FTI.md`
13. `ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DGA.md`

### 5.3 Strategic Alignment Sources
*   `ψ/incubate/DCCE/CRDB/output/01_Sitemap_InterfaceMapping/NCAIF_Detailed_Sitemap_v6.md`
*   `ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/Communication strategy - Selling NCAIF and CDM (FGD2 internal).md`

---

## 6. Operational Plan: The Staged Workflow
The process will follow a staged workflow using **intermediate artifacts** stored in the Pillar 2 directory.

### Phase 1: Forensic Extraction (Evidence Audit)
*   **Method**: Utilize three specialized sub-agents to process the sources in parallel clusters.
*   **Artifact**: `Pillar_02_v3_Intermediate_Extraction_Matrix.md`
*   **Content**: A raw table mapping "Decision Moments" to Source IDs, Decision Context, and Intelligence Products.

### Phase 2: Canonical Synthesis (Service Synthesis)
*   **Method**: Horizontal analysis of the Matrix to identify service patterns and technical overlaps.
*   **Artifact**: `Pillar_02_v3_Intermediate_Clustering_Synthesis.md`
*   **Content**: A "Logic Memo" explaining the clustering of raw needs into 7-8 National Services.

### Phase 3: Final Productization & Hardening
*   **Method**: Drafting the final report and traceability matrix.
*   **Artifact**: `NCAIF_Service_Intelligence_Report_v3.md` (Final Deliverable)

---

## 7. Output Format: The "Service Intelligence" Profile
Every extracted use case must be documented using this template:

| Field | Description |
| :--- | :--- |
| **Service Name** | Institutional title (e.g., "National Risk Certification Service"). |
| **User Persona** | Specific role (e.g., "Provincial Planner," "Bank Risk Officer"). |
| **Decision Trigger** | The real-world event/need initiating the service. |
| **Intelligence Product** | The specific output (Advisory, Report, Map). |
| **Outcome / Value** | The institutional result (e.g., "Budget approved"). |
| **Underlying Standard** | The technical "Standard-as-Product" (The "Pipes"). |

---

## 8. Execution Mandate
1.  **Purge**: Remove all references to "Intake Gateways" or "Database Systems" as services.
2.  **Tracking Service**: Explicitly include "National Adaptation Compliance & Tracking" as a core service.
3.  **Traceability**: Maintain 1:1 traceability from the final report to the Extraction Matrix.
4.  **Language**: Strictly neutral, institutional Thai/English. No sales-oriented hyperbole.

---
*Oracle Technical Specification — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification_v3.md*
