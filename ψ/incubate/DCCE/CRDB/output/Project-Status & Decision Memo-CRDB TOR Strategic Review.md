# Final Strategic Audit Report: CRDB TOR Hardening
**Target**: DCCE National Climate Adaptation Database (25M THB)
**Audit Date**: 2026-05-19
**Status**: Finalized & Grounded (Verified against Corrected Transcript)

---

## 1. AI Content Governance: "Automated ETL Logic"
*   **The Nuance**: The DCCE Project Lead (Toey) has mandated an AI integration layer to facilitate public accessibility and summarize international research.
*   **The Principle**: AI-generated content is not "magic"; it is a dynamic form of data processing. Just as traditional ETL scripts are governed by explicit logic and logs, the AI layer must be governed by **Grounding Logic**.
*   **Decision Required**: Redline the TOR to treat AI generation as a **New Category of ETL**. The contractor (Ditto) must study and implement a governance framework where AI-generated outputs are auditable. This includes a **Grounding UI** where every AI claim is explicitly linked to the foundational data or legacy reports provided by DCCE.

## 2. Personnel & Scope: Integration vs. Invention
*   **The Nuance**: The contractor (Ditto) is a technical integrator, not a climate research institute.
*   **Strategic Risk**: Over-scoping the contractor to "create" risk assessment methodologies is a mistake. Methodology development is a separate, complex scientific task.
*   **Decision Required**: Redline **Section 11 (Personnel)**. The contractor's personnel must be experts in **Platform Integration**, **API Orchestration (WIS 2.0/OGC)**, and **Data Visualization**. They are **not** required to develop new risk methodologies. Instead, their scope is strictly the **Integration of Existing Analytical Products**, such as the *Spatial Climate Risk Map DCCE v2* and the upcoming *BTR project* outputs.

## 3. Product Ownership: Boss’s Blueprint
*   **The Nuance**: There is a risk of the contractor "guessing" appropriate dashboard designs.
*   **Correction**: DCCE (through the Architect, Boss) retains absolute product ownership. The Architect has already drafted the sitemap, conceptual data models, and user journeys.
*   **Decision Required**: Redline **Section 5 (Technical Requirements)** to mandate that the contractor’s deliverables must strictly conform to the **Service Blueprint** and **Layout Structure** provided by the Architect (Boss). The contractor provides the technical execution to realize these specific requirements.

## 4. Strategic Data Gating: Use-Case Prioritization
*   **The Nuance**: DCCE possesses a massive volume of data (internal, cross-agency, international).
*   **Correction**: We will not implement a "data firehose" approach. Data ingestion will be selective and strategic.
*   **Decision Required**: Implement a **"Use-Case Gating"** clause. Use-case prioritization is the sole responsibility of the **Architect (Boss)**. The contractor is prohibited from building ingestion pipelines for data sources that have not been vetted and prioritized against the Architect's use-case roadmap.

## 5. Knowledge Foundations: Legacy Reports
*   **The Nuance**: Existing assets (PDFs, CSVs, research reports) are the department's intellectual core.
*   **Correction**: These are not "legacy files" to be migrated; they are the **Foundational Outputs** that define the platform’s authority.
*   **Decision Required**: The platform must be architected *around* these documents. The TOR must mandate that the contractor uses these **Legacy Reports as the Core Baseline Content**. The database must serve to make this foundational knowledge interoperable and accessible through modern standards (APIs/WIS 2.0).

---
**Auditor Signature**: Arun Creagy, Strategic Auditor
**Approval**: Boss, Project Architecture Specialist
