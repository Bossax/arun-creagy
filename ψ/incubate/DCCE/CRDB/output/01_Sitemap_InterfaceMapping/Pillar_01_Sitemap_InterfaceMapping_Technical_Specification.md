# Technical Specification: Pillar 1 — Sitemap & Navigation Architecture

## 0. Purpose & Scope (Sitemap as a Governed Knowledge Network)

**Decision:** Pillar 1 defines the **Information Architecture (IA)** and **Navigation Structure** of the NCAIF. It is not merely a "menu," but a **Governed Knowledge Network** that bridges technical science with administrative action.

**The "Linguistic Bridge" Mandate:** To ensure adoption by local authorities (อปท.), the Sitemap must translate academic taxonomies into **Functional Mandates (ภารกิจ)** and **Service Systems** (e.g., "Water Defense," "Public Health Resilience") rather than purely scientific categories.

**The Three-Tier Traceability Model:**
1.  **Tier 1: Sitemap (Pillar 1)** — Defines the **Services** and **Governed Content Assets**.
2.  **Tier 2: Use Cases (Pillar 2)** — The **Functional Logic** linking Services to their required **Datasets**.
3.  **Tier 3: Inventory (Pillar 3)** — The **Raw Data Warehouse** (260+ datasets).

## 1. Information Architecture (IA) & Content Standards
*   **Artifact Format**: Hierarchical Sitemap (3 Levels) & Service-to-Use-Case Crosswalk.
*   **Canonical Synthesis Sources**:
    - [NCAIF Sitemap v5 Design Decisions](ψ/incubate/DCCE/CRDB/output/01_Sitemap_InterfaceMapping/2026-06-04-NCAIF-Sitemap-v5-Design-Decisions.md) — Current architectural baseline.
    - [NCAIF Sitemap Presentation (May 12)](ψ/incubate/DCCE/CRDB/output/01_Sitemap_InterfaceMapping/2026-05-12-NCAIF-Sitemap-Presentation.md) — Approved UI/UX layouts.
*   **Architecture Mandate: "Mandate-First" IA**:
    - The structural backbone is anchored in the **National Adaptation Plan (NAP) Cycle**.
    - User-specific "hooks" (e.g., Private Sector Disclosure) are supported via secondary service cards and the technical data layer (Pillar 2 APIs), NOT through top-level sitemap silos.
*   **Content Strategy: "Transparency with Armor"**:
    - High-impact risk data (e.g., Future Flood Maps) must be structurally bundled with **Scientific Armor** (Methodology/Limitations) and **Action Armor** (Adaptation Guidance).
    - This ensures risk disclosure promotes resilience planning rather than market panic.
*   **Sitemap v5 Navigation Structure**:
    1.  **Home** (The Hero: National Situation, My Area, Planning Support).
    2.  **National Decision Support Center** (Policy Briefings, Indicators, National Status).
    3.  **Adaptation Information by Cycle** (The Scientific/Mandate Backbone).
    4.  **Risk and Area Profiles** (Provincial & Sector Context).
    5.  **Adaptation Guidance & Exemplars** (The Action Library).
    6.  **Knowledge, Tools, and Data Services** (The Technical Utility: Catalog, APIs, Standards).
    7.  **News, Updates, and About** (Institutional Transparency).
*   **Access & Sensitivity (The Download Gate)**:
    - **Visualizations (Dashboards)**: Open/Public access to ensure transparency.
    - **Raw Data Downloads**: Restricted (Tier 2/Registered) to prevent un-governed data re-processing and maintain audit trails.

## 2. Quality Assurance & Verification Criteria
*   **Navigation Integrity**: 100% of the services promised in the **TOR (Section 5.3.3)** must be explicitly placed within the v5 hierarchy.
*   **Functional Grounding**: 
    - Interactive nodes MUST map to a **Pillar 2 Use Case (UC-ID)**.
    - Narrative nodes (Explainers) MUST map to a registered **Evidence Anchor (E-ID)** from Pillar 3.
*   **Retention via Utility**: Verification that the "Private Sector Hook" (Disclosure Use Case) is discoverable via the Homepage Hub and Node 6 (APIs).
*   **UI/UX Guardrails**: Alignment with "Steps to Resilience" (Explore -> Assess -> Investigate -> Plan -> Take Action).

## 3. Implementation Constraints
*   **"Zero-Discovery" Handoff**: The contractor for Project B must treat the Sitemap and its **Mandate Mapping** as a fixed contract.
*   **Separation of Concerns**:
    - Pillar 1 defines **Where** it goes (Sitemap) and **What it says** (Governed Content).
    - Pillar 2 defines **How** it works (Use Case).
    - Pillar 3 defines **What** is inside (Data Inventory).
*   **Handoff to Project B**: The contractor must implement the **Governed Content Hub** pattern, ensuring static pages are metadata-linked consumers of the central data catalog.
