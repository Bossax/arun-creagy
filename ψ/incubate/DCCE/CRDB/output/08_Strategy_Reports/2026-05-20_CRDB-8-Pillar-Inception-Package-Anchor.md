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
    *   **Core Architecture**: Insert the **CDM Entity-Attribute-Relationship (EAR) Catalog** as the non-negotiable logical baseline.
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
    *   **Logical Data Model (LDM)**: Define the **"Disaster Card"** entity structure and its relational logic (Hazard-Asset-Impact).
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

| Pillar | Delivering Package | Target Deliverable | Format |
| :--- | :--- | :--- | :--- |
| **1. CDM (Logical Baseline)** | Package A | **Del 1** (Design Report) | **EAR Catalog** (Excel/CSV) |
| **2. Business Glossary** | Package A / D | **Del 1** (Appendix) / **Del 9** (Tagging) | **Normalized CSV** |
| **3. LDM Logic (MVD)** | Package C | **Del 6** (MVD Spec) | **Functional Excel Model** |
| **4. Interface Map** | Package C | **Del 4** (Inventory Mapping) | **Mapping CSV** |
| **5. DQ Framework (G1-G5)** | Package A / D | **Del 1** (Rules) / **Del 8-10** (Audits) | **Audit Ruleset (JSON/CSV)** |
| **6. Governance (RACI)** | Package B | **Del 2** (FGD3 Report) | **RACI Matrix** |
| **7. Ref Data Matrix** | Package C | **Del 4** (Dependencies) | **Master Data CSV** |
| **8. Building Block Catalog** | Package A | **Del 7** (Procurement Tiers) | **Tiered Feature List** |

---

## 4. Technical Specification Requirements

This section defines the mandatory technical standards, verification criteria, and implementation constraints for each of the 8 Pillars. These requirements constitute the "Definition of Done" for the CRDB hardening phase.

### **Pillar 1: Climate Data Model (CDM) - Logical Baseline**
*   **Detailed Requirements**: Refer to [[ψ/incubate/DCCE/CRDB/output/01_CDM_Architecture/Pillar_01_CDM_Technical_Specification.md|Pillar 1 Technical Specification]].
*   **Summary**: Defines the logical Entity-Attribute-Relationship (EAR) structure for all climate risk and adaptation data subject areas. It serves as the mandatory logical baseline for the physical database implementation.

### **Pillar 2: Business Glossary**
*   **Detailed Requirements**: Refer to [[ψ/incubate/DCCE/CRDB/output/02_Glossary_Semantics/Pillar_02_Glossary_Technical_Specification.md|Pillar 2 Technical Specification]].
*   **Summary**: A controlled list of 100+ terms providing the Universal Semantic Layer (USL) for the entire platform. It ensures consistent labeling and discoverability across all data products.

### **Pillar 3: Logic Rules (MVD)**
*   **Detailed Requirements**: Refer to [[ψ/incubate/DCCE/CRDB/output/03_Logic_MVD_MVP/Pillar_03_LDM_Logic_Technical_Specification.md|Pillar 3 Technical Specification]].
*   **Summary**: Defines the TOR-required **Minimum Viable Dataset (MVD)** and **Loss & Damage reporting form** as a Logical Data Model (LDM) specification, including validation/revision requirements and a ≥3 historical-event pilot evidence pack. Computation/estimation logic is not assumed unless explicitly mandated.

### **Pillar 4: Interface Map**
*   **Detailed Requirements**: Refer to [[ψ/incubate/DCCE/CRDB/output/04_Inventory_Mapping/Pillar_04_Interface_Map_Technical_Specification.md|Pillar 4 Technical Specification]].
*   **Summary**: A TOR-supporting **source-to-CDM crosswalk** that makes the inventories joinable and records integration posture + unknowns explicitly (not a validated ETL design in this project). It includes row-level `Feasibility_Posture` and `Provenance_Anchor` so Project B can implement harvesters later without vendor-led rediscovery.

### **Pillar 5: DQ Framework (G1-G5)**
*   **Detailed Requirements**: Refer to [[ψ/incubate/DCCE/CRDB/output/05_Quality_Standards/Pillar_05_DQ_Framework_Technical_Specification.md|Pillar 5 Technical Specification]].
*   **Summary**: The **normative semantics** of the 5 governance gates (G1–G5) for Phase 1 execution (manual/procedural now; automatable later). It standardizes meanings of classification rails, container metadata minima, endorsement/authority labels, denominators/crosswalk governance, and revision/maturity labels.

### **Pillar 6: Governance (RACI)**
*   **Detailed Requirements**: Refer to [[ψ/incubate/DCCE/CRDB/output/06_Governance_RACI/Pillar_06_Governance_Technical_Specification.md|Pillar 6 Technical Specification]].
*   **Summary**: A Stewardship RACI **plus a governance buy-in execution plan** (cadence, onboarding, escalation, decision log) to prevent stale shelfware. It defines who decides and how division-wide governance runs with limited resources, and acts as a procurement shield for Project B.

### **Pillar 7: Ref Data Matrix**
*   **Detailed Requirements**: Refer to [[ψ/incubate/DCCE/CRDB/output/04_Inventory_Mapping/Pillar_07_Ref_Data_Technical_Specification.md|Pillar 7 Technical Specification]].
*   **Summary**: A TOR-supporting **reference data dependency matrix + authority/source map** (not a fully reconciled master data package in this project). It identifies required reference sets, who the authority is, what depends on what, and records `Reference_Status` (Agreed/Contested/Unknown) and crosswalk needs for downstream resolution.

### **Pillar 8: Building Block Catalog**
*   **Detailed Requirements**: Refer to [[ψ/incubate/DCCE/CRDB/output/07_Sitemap_BuildingBlocks/Pillar_08_Building_Block_Technical_Specification.md|Pillar 8 Technical Specification]].
*   **Summary**: A TOR-5.2-first inventory of **NCAIF building blocks** with **budgeting/strategy-oriented presentation as primary** and catalog/link-out as secondary. Each Tier-1 (TOR-critical) block must map to NCAIF sections, deliverables, dependencies, and project evidence anchors (to avoid invented features and preserve consultation-derived grounding).
