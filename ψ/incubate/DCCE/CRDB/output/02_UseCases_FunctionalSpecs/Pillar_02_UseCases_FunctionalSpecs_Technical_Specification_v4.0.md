# Technical Specification: Forensic Service Synthesis & Intelligence Design (v4.0)

**Status**: Definitive Design Basis
**Version**: 4.0 (Forensic Restoration & Technical Enrichment)
**Project Component**: Pillar 2 — Use Cases & Functional Specifications
**Date**: 2026-06-05

---

## 1. Objective
This specification defines the authoritative methodology for synthesizing 32+ granular agency demands into the **7 National Climate Service Platforms**. The objective is to move beyond generic "Data Management" and establish an **Intelligence Value Chain** that provides legal and technical "Authoritative Seals" for national climate decisions.

---

## 2. Methodology: The Intelligence Value Chain
To prevent "Contractor Logic" (building systems without utility), every service must be designed using the **Decision-First** methodology:
1.  **The Decision Moment**: Identify the specific institutional action (e.g., "Approving a 100-year flood-proof bridge budget") that requires data.
2.  **The Intelligence Product**: Define the *processed* output (e.g., "Certified KM-marker Hazard Advisory") that satisfies the decision.
3.  **The Authority Seal**: Define why the **DCCE** must certify this transaction to provide the user with a liability shield (Article 15 Compliance).

---

## 3. Forensic Guardrails (Anti-Sanitization & Narrative Enrichment)
Version 4.0 introduces strict rules to avoid the "Sanitization Pitfalls" and ensure the conceptual design feels "alive" and institutionally grounded:

*   **Narrative-Rich Institutional Scenarios**: Agency-specific needs MUST be documented as professional scenarios that capture the specific institutional context and regulatory requirements behind the demand:
    *   *Example (DLA)*: "Local administrators require standardized economic justification that meets the regulatory requirements of the State Audit Office (OAG) for the utilization of local accumulated funds (เงินสะสม) for climate adaptation projects. This ensures that proactive investments are supported by officially recognized ROI assessments."
    *   *Example (UDDC)*: "Urban planners require a standardized data repository to resolve existing data inconsistencies between municipal and national agencies. This ensures that neighborhood-scale climate plans are based on officially verified baselines, allowing urban interventions to move from conceptual design to formal implementation."
*   **Institutional Lineage**: Foundational concepts MUST be anchored to their originators (e.g., **UDDC** for "Single Source of Truth/Neighborhood Data Management," **DLA** for "Accumulated Funds Justification").
*   **Language Fidelity**: Strictly avoid hyperbolic consultancy jargon and informal terms. Use formal, professional nomenclature throughout all deliverables.
*   **Granularity Demotion**: Specific variables (e.g., "Agricultural Debt," "KM-markers," "Sinkholes") must be woven into the narratives of the **Functional Module Specifications**, not left as floating bullet points.
*   **Grounded Enrichment**: Use international benchmarks (World Bank, IMF, PIANC) only to *complete* the story, ensuring external specs serve the stakeholder's narrative rather than overriding it. Explicitly cite as `[Technical Enrichment]`.

---

## 4. Source Manifest (The Full Evidence Base)
The synthesis MUST process the following **17-source inventory** without skimming:

### 4.1 Workshop Evidence (Activity 2)
*   `activity2_master_analysis.md` (Normalized Concepts)
*   `activity2_raw_extraction.md` (Stakeholder Language)
*   `user_use_case_raw.md` (The 32 core demands)

### 4.2 Stakeholder Interview Evidence (The "Why")
The following 13 interview summaries MUST be audited for granular institutional pain points and decision moments:
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

### 4.3 Strategic Alignment
*   `NCAIF_Detailed_Sitemap_v6.md`
*   `Communication strategy (FGD2 internal).md`

---

## 5. Operational Plan: The 3-Phase Workflow

### Phase 1: High-Fidelity Forensic Extraction
*   **Agent**: `codebase_investigator`
*   **Operational Detail**: Audit the full 17-source inventory. For each of the 32 use cases, extract:
    1.  **Originating Agencies**: (List ALL requesting agencies).
    2.  **Decision Moment**: (The specific trigger/action).
    3.  **Institutional Pain Point**: (The specific fear/blocker/regulatory need).
    4.  **Hard Technical Specs**: (Resolutions, return periods, latencies, specific indicators).
    5.  **Originator Tag**: (Strict citation of the source file/section).
*   **Artifacts**: 
    - `Pillar_02_v4_Intermediate_Extraction_Matrix.md` (Human-readable table).
    - `P2_Traceable_Dependencies.json` (Structured machine-readable inventory).

### Phase 2: Canonical Synthesis & Grounded Expansion
*   **Agent**: `generalist` (with Google/Brave Search access)
*   **Operational Detail**: Blend the inventory into 7 Services while expanding technical depth.
    *   **Rule A (Institutional Anchor)**: Service 01 (Centralized Data Catalog) MUST be the foundation for agencies demanding "Authoritative Data" or "SSOT" (e.g., UDDC).
    *   **Rule B (Contextual Modules)**: Create specific modules for unique agency needs (e.g., DLA Accumulated Funds), maintaining strict `[Originator Tags]`.
    *   **Rule C (Grounded Enrichment)**: Use web search to identify industry benchmarks (World Bank, IMF, PIANC, ISO) where stakeholder specs are underspecified.
    *   **Rule D (Explicit Citation)**: Label online sources as `[Technical Enrichment: URL]` to distinguish them from `[Stakeholder Grounding]`.
*   **Artifact**: `Pillar_02_v4_Intermediate_Clustering_Synthesis.md` (The Logic Memo).

### Phase 3: Final Productization & Intelligence Hardening
*   **Agent**: `generalist` & `codebase_investigator`
*   **Operational Detail**: Compile the findings into the definitive Service Intelligence Report.
    *   **Consolidation**: Ensure all 32 use cases are elegantly mapped into the 7 Service Platforms.
    *   **Institutional Alignment**: Verify that every module addresses a specific "Institutional Pain Point" or "Decision Moment" identified in Phase 1.
    *   **Technical Rigor**: Ensure all `[Technical Enrichment]` benchmarks are accurately integrated and cited to make the conceptual design robust and complete.
*   **Artifact**: `NCAIF_Service_Intelligence_Report_v4.md` (The Final Deliverable).

---

## 6. Service Definition Template
Every service in the final report must adhere to this structure:
*   **Service Platform Name**: (Formal & Functional).
*   **Common Core**: (The baseline capability shared by all users).
*   **Contextual Modules**: (Agency-specific intelligence products with `[Originator Tags]`).
*   **Technical Standardization**: (Parameters derived from stakeholders and `[Technical Enrichment]`).

---
*Oracle Technical Specification — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification_v4.0.md*
