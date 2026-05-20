# CRDB Inception Package: Deliverable Structure Guide (The 8 Pillars)
**Project**: CRDB (Climate Risk Data Blueprint)
**Status**: DRAFT (Deliverable-Centric v2)
**Date**: 2026-05-20

## 1. Purpose
This document provides the structural blueprint for the 10 mandated deliverables for the July 6 submission. It uses the **Deliverable** as the primary pivot to show how the "8 Pillars of Success" are tucked into the existing reporting requirements to create a hardened Procurement Shield.

---

## 2. Deliverable-Centric Pivot (The "How-to-Structure" Guide)

### Package A: Strategic Framework (The Master Plan)

#### **Del 1: Design Report (NCAIF & Data Management Framework)**
*   **The Pillars**: 1 (CDM), 2 (Glossary), 5 (DQ Framework).
*   **Structure**: 
    *   **Core Architecture**: Insert the **CDM Physical Schema (ERD)** as the non-negotiable system of record.
    *   **Data Quality Section**: Insert the **G1-G5 Audit Rules** as mandatory system acceptance criteria.
    *   **Appendix**: Attach the **Business Glossary** (100+ terms) to prevent semantic drift during software development.

#### **Del 7: Recommendations (Climate Service & Catalog Development)**
*   **The Pillar**: 8 (Building Block Catalog).
*   **Structure**:
    *   **Procurement Tiers**: Tier the **NCAIF Sitemap v4** features into "Must-Have" (Core Engine) vs "Nice-to-Have" (Data Slices).
    *   **Use Case Prescription**: Translate High-Priority Use Cases into **Functional Requirements** (e.g., "The system *must* support BTR sectoral drill-downs as defined in the CDM").

---

### Package B: Stakeholder Validation (The Mandate)

#### **Del 2: FGD3 Report (Internal DCCE Discussion)**
*   **The Pillar**: 6 (Governance Operating Model).
*   **Structure**:
    *   **Stewardship Ratification**: Use this report to document the formal acceptance of **Data Stewardship** roles by DCCE Sub-divisions.
    *   **RACI Matrix**: Define who approves, authors, and maintains each CDM data domain.

#### **Del 5: Data Gap Analysis Report**
*   **The Aspect**: **Theoretical Demand vs. Empirical Supply**.
*   **Structure**:
    *   **Target Baseline**: Define the data requirements (entities/attributes) needed for **High-Priority Use Cases** (CRI v2, BTR, MVD).
    *   **Gap Matrix**: Compare the "Demand" (from CDM) against the "Supply" (from Del 4 Inventories) to prove why the contractor cannot rely on current data alone.

---

### Package C: Technical Assets (The Integration Baseline)

#### **Del 4: Baseline Data & Information Product Inventories**
*   **The Pillars**: 4 (Interface Map), 7 (Ref Data Matrix).
*   **Structure**:
    *   **Integration Boundary**: Map major external sources (ThaiWater, BTR, etc.) to **CDM Subject Areas** (Subject-Area Interface Map).
    *   **Architectural Dependencies**: List the entities (Admin Units, Agency Codes) that require **Reference Data S-O-T** implementation (Reference Data Matrix).

#### **Del 6: Minimum Viable Dataset (MVD) & Reporting Forms**
*   **The Pillar**: 3 (LDM Logic Rules).
*   **Structure**:
    *   **Logical Data Model (LDM)**: Define the **"Disaster Card"** fact table and its relational logic (Hazard-Asset-Impact).
    *   **Deterministic Formulas**: Provide the logic for entity relationships within the Loss & Damage domain.

---

### Package D: Public Content (Governed Assets)

#### **Del 8, 9, 10: Media, Articles, and Infographics**
*   **The Alignment**: Pillars 2 (Glossary) and 5 (DQ Framework).
*   **Structure**:
    *   **Semantic Metadata**: Tag all content with terms from the **Business Glossary**.
    *   **Quality Audit**: Ensure all infographics and articles cite sources according to **G1-G2 DQ Rules**.

---

## 3. Summary of Pillar-to-Deliverable Mapping

| Pillar | Delivering Package | Target Deliverable |
| :--- | :--- | :--- |
| **1. CDM (Physical ERD)** | Package A | **Del 1** (Design Report) |
| **2. Business Glossary** | Package A / D | **Del 1** (Appendix) / **Del 9** (Tagging) |
| **3. LDM Logic (MVD)** | Package C | **Del 6** (MVD Spec) |
| **4. Interface Map** | Package C | **Del 4** (Inventory Mapping) |
| **5. DQ Framework (G1-G5)** | Package A / D | **Del 1** (Rules) / **Del 8-10** (Audits) |
| **6. Governance (RACI)** | Package B | **Del 2** (FGD3 Report) |
| **7. Ref Data Matrix** | Package C | **Del 4** (Dependencies) |
| **8. Building Block Catalog** | Package A | **Del 7** (Procurement Tiers) |
