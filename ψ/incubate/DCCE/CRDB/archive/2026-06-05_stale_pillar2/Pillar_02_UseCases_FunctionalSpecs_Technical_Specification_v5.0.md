# Technical Specification: Forensic Service Synthesis & Intelligence Design (v5.0)

**Status**: Definitive Design Basis
**Version**: 5.0 (Methodology-Driven Synthesis & Complete Merge)
**Project Component**: Pillar 2 — Use Cases & Functional Specifications
**Date**: 2026-06-08

---

## 1. Objective
This specification defines the authoritative methodology for synthesizing 40+ granular agency demands into the **7 National Climate Service Platforms**. The objective is to move beyond generic "Data Management" and establish an **Intelligence Value Chain** that provides legal and technical "Authoritative Seals" for national climate decisions, ensuring absolute structural integrity across all evidence bases.

---

## 2. Methodology: The Intelligence Value Chain
To prevent "Contractor Logic" (building systems without utility), every service must be designed using the **Decision-First** methodology:
1.  **The Decision Moment**: Identify the specific institutional action (e.g., "Approving a 100-year flood-proof bridge budget") that requires data.
2.  **The Intelligence Product**: Define the *processed* output (e.g., "Certified KM-marker Hazard Advisory") that satisfies the decision.
3.  **The Authority Seal**: Define why the **DCCE** must certify this transaction to provide the user with a liability shield (Article 15 Compliance).

---

## 3. Forensic Guardrails (Anti-Sanitization & Structural Integrity)
Version 5.0 introduces strict rules to close the structural gaps identified in previous iterations, ensuring the conceptual design is both institutionally grounded and immune to synthesis collapse:

*   **Mandatory Comprehensive Merge**: The synthesis pipeline MUST integrate data from BOTH **Activity 1 (Stakeholder Interviews)** AND **Activity 2 (Consultation Workshop)**. Treating interview data as primary while discarding workshop data (e.g., LDD, MOTS, DMCR) is a fatal structural flaw.
*   **Methodology Over Sector (Sector-Agnostic Design)**: The 7 Core Service Platforms are defined by their **Functional Methodology** (e.g., Spatial Overlay, Cost-Benefit Analysis, Telemetry API), NOT by the institutional sector (e.g., Agriculture, Tourism, Health). 
    *   *Anti-Pattern*: Creating a new "Agriculture Platform" just because LDD provided data.
    *   *Correct Pattern*: Mapping LDD's "Plot-level Crop Impact" into the existing ` Vulnerability Analytics` platform because the underlying math (spatial intersection of hazard and asset) is identical.
*   **Narrative-Rich Institutional Scenarios**: Agency-specific needs MUST be documented as professional scenarios that capture the specific regulatory context:
    *   *Example (DLA)*: "Local administrators require standardized economic justification that meets OAG regulatory requirements for the utilization of accumulated funds (เงินสะสม)."
*   **Granularity Demotion**: Specific variables (e.g., "Agricultural Debt," "KM-markers") must be woven into the narratives of the **Functional Module Specifications**, not left as floating bullet points.

---

## 4. Source Manifest (The Full Evidence Base)
The synthesis MUST process the following inventory without skipping or structurally filtering out Activity 2 concepts:

### 4.1 Workshop Evidence (Activity 2 - The Forgotten Data)
*   `activity2_master_analysis.md` (Normalized Concepts - MUST extract all G-codes including G78-C9, G1-C10)
*   `activity2_raw_extraction.md` (Stakeholder Language)
*   `user_use_case_raw.md` (The core demands)

### 4.2 Stakeholder Interview Evidence (Activity 1 - The "Why")
The following 13 interview summaries MUST be audited:
1.  `Interview Summary - BMA.md`
2.  `Interview Summary - DLA.md`
3.  `Interview Summary - DPT.md`
4.  `Interview Summary - MSDHS.md`
5.  `Interview Summary - NESDC.md`
6.  `Interview Summary - NSO.md`
7.  `Interview Summary - NXPO.md`
8.  `Interview Summary - OTP.md`
9.  `Interview Summary - Thai Bankers' Association.md`
10. `Interview Summary - UDDC.md`
11. `Interview Summary DDPM.md`
12. `Interview Summary - FTI.md`
13. `Interview Summary - DGA.md`

---

## 5. Operational Plan: The 3-Phase Workflow

### Phase 1: High-Fidelity Forensic Extraction (No Data Left Behind)
*   **Agent**: `codebase_investigator`
*   **Operational Detail**: Audit the full source inventory. Extract ALL Use Cases (40+) spanning both Activity 1 and Activity 2. Extract:
    1.  **Originating Agencies**: (List ALL requesting agencies).
    2.  **Decision Moment**: (The specific trigger/action).
    3.  **Institutional Pain Point**: (The specific fear/blocker/regulatory need).
    4.  **Hard Technical Specs**: (Resolutions, return periods, latencies).
*   **Artifacts**: 
    - `P2_Hard_Dependencies_Inventory.json` (Structured machine-readable inventory of 40+ UCs).

### Phase 2: Sector-Agnostic Canonical Synthesis
*   **Agent**: `generalist` (with Search access)
*   **Operational Detail**: Blend the inventory into 7 Services.
    *   **Rule A (Methodology Mapping)**: Map use cases based on technical function, not agency name. (e.g., LDD -> Vulnerability Analytics; MOTS -> Loss & Damage).
    *   **Rule B (Contextual Modules)**: Create specific modules for unique agency needs, maintaining strict `[Originator Tags]`.
    *   **Rule C (Grounded Enrichment)**: Use web search to identify industry benchmarks (World Bank, IMF, PIANC) where stakeholder specs are underspecified.
*   **Artifact**: `Pillar_02_v5_Intermediate_Clustering_Synthesis.md` (The Logic Memo).

### Phase 3: Final Productization & Intelligence Hardening
*   **Agent**: `generalist` & `codebase_investigator`
*   **Operational Detail**: Compile the findings into the definitive Service Intelligence Report.
    *   **Consolidation**: Ensure all 40+ use cases are elegantly mapped into the 7 Service Platforms.
    *   **Narrative Refinement**: Ensure the Service descriptions explicitly demonstrate their cross-cutting, sector-agnostic nature.
*   **Artifact**: `NCAIF_Service_Intelligence_Report_v5.md` (The Final Deliverable).

---

## 6. Service Definition Template
Every service in the final report must adhere to this structure:
*   **Service Platform Name**: (Formal, Functional, & Sector-Agnostic).
*   **Common Core**: (The baseline methodology shared by all users).
*   **Contextual Modules**: (Agency-specific intelligence products with `[Originator Tags]`).
*   **Technical Standardization**: (Parameters derived from stakeholders and `[Technical Enrichment]`).

---
*Oracle Technical Specification — ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification_v5.0.md*
