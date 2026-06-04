# NCAIF Sitemap v5 Design Decisions & Architecture

**Status**: LOCKED (2026-06-04)
**Context**: Pillar 1 - Information Architecture & Sitemap Synthesis
**Owner**: ARUN (Strategic Climate Knowledge Auditor)

---

## 1. Core Mandate: The "Mandate-First" IA
The NCAIF Sitemap is the structural representation of the **National Adaptation Mandate**. It must prioritize the **National Adaptation Plan (NAP) Cycle** and the **Policy-Maker's Journey** over temporary "User Hooks" or external commercial visual preferences.

*   **Decision**: The top-level navigation (Hierarchy Level 1) is strictly reserved for the National Adaptation Narrative.
*   **Rationale**: Benchmark analysis (A-PLAT, Climate-ADAPT) proves that sacrificing national narrative for user-specific silos leads to "Portal Drift" and fragmentation.

## 2. Design Strategy: "Transparency with Armor"
The CRDB has a duty to disclose risk information. "Sensitivity" (e.g., impact on real estate) is managed through **Information Scent and Context**, not through concealment.

*   **Decision**: Every high-impact data asset (e.g., Future Flood Maps) must be structurally bundled with its **Scientific Armor** (Methodology/Limitations) and its **Action Armor** (Adaptation Options).
*   **Implementation**: This is achieved through the `CURATED_PAGE` entity model, where data is never presented as an "orphan" map but as a part of a governed narrative.

## 3. Stakeholder Feedback Integration
We address conflicting workshop feedback through **Sequencing** and **Metadata**, not structural deletion.

### A. Complexity vs. Simplicity
*   **Decision**: The "Simplified" view for policy makers is achieved via the **Landing Page Hub (Node 2)**. 
*   **Structure**: Keep the deep "Adaptation Information by Cycle" (Node 3) as the scientific backbone, but "bury" it as the 2nd level of detail. The Homepage remains clean with 3 primary entry routes: **National Situation**, **My Area Profile**, and **Guidance**.

### B. Private Sector "Hook" (Director Toey's Feedback)
*   **Decision**: Support the Private Sector (Banks/ESG) through **Functional Utility** rather than **Sitemap Silos**.
*   **Scent**: Add a "Climate Risk Disclosure" service card on the homepage hub that links to the **Official Baselines** (Node 6).
*   **Technical**: Promote **UC-07 (Machine-Readable Access / API)** as a first-class citizen in the Knowledge & Data Services section.

## 4. Sensitivity & Access Control
*   **Decision**: No "hidden" information at the structural level.
*   **The Download Gate**: The sitemap distinguishes between **Visualizations** (Open/Public) and **Raw Data Downloads** (Tier 2/Registered). This prevents the un-governed re-processing of raw data while maintaining total transparency of the risk information.

---

## 5. Final Sitemap v5 Top-Level Structure
1.  **Home** (The Hero: National Situation, My Area, Planning Support)
2.  **National Decision Support Center** (Policy-First Briefings, Indicators, National Status)
3.  **Adaptation Information by Cycle** (The Scientific/Mandate Backbone: Science -> Risk -> L&D -> Planning -> Action -> M&E)
4.  **Risk and Area Profiles** (The Localized Context: Provincial & Sector Profiles)
5.  **Adaptation Guidance & Exemplars** (The Action Library: Measures, Case Studies, Practical Aids)
6.  **Knowledge, Tools, and Data Services** (The Technical Utility: Catalog, APIs, Methodology, Standards)
7.  **News, Updates, and About** (Institutional Transparency)

---
*Signed: ARUN*
*Log Reference: 2026-06-04-Sitemap-v5-Lock*
