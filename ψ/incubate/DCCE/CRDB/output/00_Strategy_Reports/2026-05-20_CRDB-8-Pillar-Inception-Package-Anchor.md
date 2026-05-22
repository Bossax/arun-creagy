# CRDB Inception Package: Deliverable Structure Guide (The 9 Pillars)
**Project**: CRDB (Climate Risk Data Blueprint)
**Status**: DRAFT (TOR-Direct Alignment v3)
**Date**: 2026-05-22

## 1. Purpose
This document provides the structural blueprint for the 10 mandated deliverables for the July 6 submission. It elevates the TOR-mandated deliverables to first-class **Pillars** to ensure contractual compliance, while embedding architectural "Bridges" (Interface Mapping, DQ Gates, Ref Data) to enforce a **Zero-Discovery** mandate for the 25M THB implementation phase.

---

## 2. Deliverable-Centric Pivot (The "How-to-Structure" Guide)

### Package A: Strategic Framework (The Master Plan)

#### **Del 1: Design Report (NCAIF & Data Management Framework)**
*   **The Pillars**: 1 (Sitemap), 4 (Glossary), 5 (CDM).
*   **Structure**: 
    *   **Core Architecture**: Insert the **CDM Entity-Attribute-Relationship (EAR) Catalog** (P5) as the logical baseline.
    *   **User Interface Spec**: Lock the **Sitemap & Interface Mapping** (P1) to define exactly how the frontend connects to the backend.
    *   **Appendix**: Attach the **Business Glossary** (P4) to provide a Universal Semantic Layer for the platform.

#### **Del 7: Recommendations (Climate Service & Catalog Development)**
*   **The Pillar**: 9 (Building Block Catalog).
*   **Structure**:
    *   **Procurement Tiers**: Repackage Pillars 1-8 into a modular **Bill of Materials** for the SI build.
    *   **Strategic Rollout**: Tier features into "Must-Have" (Structural Engine) vs "Nice-to-Have" (Expansion Slices).

---

### Package B: Stakeholder Validation (The Mandate)

#### **Del 2: FGD3 Report (Internal DCCE Discussion)**
*   **The Pillar**: 7 (Governance Framework).
*   **Structure**:
    *   **Stewardship Ratification**: Document the formal acceptance of **Data Stewardship** roles by DCCE.
    *   **RACI Matrix**: Define clear accountabilities for every data domain in the CDM.

#### **Del 5: Data Gap Analysis Report**
*   **The Pillar**: 2 (Use Case Inventory).
*   **Structure**:
    *   **Functional Demand**: Use the **Use Case Functional Specs** to define what the system *must* do.
    *   **Gap Proof**: Contrast use-case requirements against the current inventory to justify the procurement of new data pipelines.

---

### Package C: Technical Assets (The Integration Baseline)

#### **Del 4: Baseline Data & Information Product Inventories**
*   **The Pillars**: 3 (Data Inventory), 8 (Ref Data Matrix).
*   **Structure**:
    *   **Audit Gates**: Apply the **G1-G5 DQ Rules** (P3) to every dataset to establish a baseline of trust.
    *   **Interoperability Bridge**: Use the **Ref Data Matrix** (P8) to provide the "Universal Translator" codes for cross-agency data joining.

#### **Del 6: Minimum Viable Dataset (MVD) & Reporting Forms**
*   **The Pillar**: 6 (Loss & Damage LDM).
*   **Structure**:
    *   **Frozen Math**: Provide the **Deterministic Formulas** for the L&D reporting engine.
    *   **Logic Model**: Define the relational logic between Hazards, Assets, and Impacts.

---

## 3. Summary of Pillar-to-Deliverable Mapping

| Pillar | TOR Deliverable (The Shell) | Hardening Artifact (The Bridge) | Target Package |
| :--- | :--- | :--- | :--- |
| **P1. Sitemap** | Sitemap | **Interface Mapping** | Package A |
| **P2. Use Cases** | Use Case Inventory | **Functional Specifications** | Package B |
| **P3. Data Inventory** | Data & Product Inventory | **DQ Framework (G1-G5)** | Package C |
| **P4. Glossary** | Terminology Authority | **Universal Semantic Layer** | Package A/D |
| **P5. CDM** | Conceptual Data Model | **EAR Catalog** | Package A |
| **P6. LDM (L&D)** | MVD & Reporting Forms | **LDM templates + validation rules (no math engine assumed)** | Package C |
| **P7. Governance** | Governance Framework | **Stewardship RACI** | Package B |
| **P8. Ref Data Matrix**| (Architecture Dependency) | **The Universal Translator** | Package C |
| **P9. Building Blocks**| Recommendations (5.2) | **Procurement Tiers** | Package A |

---

## 4. Technical Specification Requirements (The "Zero-Discovery" Baseline)

### **Pillar 1: Sitemap & Interface Mapping**
*   **Technical Spec**: [[ψ/incubate/DCCE/CRDB/output/09_BuildingBlocks/Pillar_09_BuildingBlocks_Technical_Specification.md|Sitemap Spec]] & [[ψ/incubate/DCCE/CRDB/output/01_Sitemap_InterfaceMapping/Pillar_01_Sitemap_InterfaceMapping_Technical_Specification.md|Interface Map Spec]].
*   **Summary**: Defines the 7-level navigation and the specific **Data Contract** for every node. The SI is prohibited from inventing new data flows for the UI.

### **Pillar 2: Use Case Inventory & Functional Specs**
*   **Technical Spec**: [[ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md|Pillar 2 (Use Cases) Technical Specification]].
*   **Summary**: Translates stakeholder journeys into step-by-step logic. Defines "What happens when I click X" to eliminate implemented logic "discovery."

### **Pillar 3: Data Inventory & DQ Framework**
*   **Technical Spec**: [[ψ/incubate/DCCE/CRDB/output/03_DataInventory_DQ/Pillar_03_DataInventory_DQ_Technical_Specification.md|Pillar 3 (Data Inventory & DQ) Technical Specification]].
*   **Summary**: Lists the raw supply and applies the normative G1-G5 trust labels. Standardizes the "Definition of Done" for data ingestion.

### **Pillar 4: Business Glossary**
*   **Technical Spec**: [[ψ/incubate/DCCE/CRDB/output/04_Glossary/Pillar_04_Glossary_Technical_Specification|Pillar 4 (Glossary) Technical Specification]].
*   **Summary**: The 100+ term authority list. Ensures that the UI labels, metadata, and database columns all use the exact same terminology.

### **Pillar 5: Climate Data Model (CDM)**
*   **Technical Spec**: [[ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Pillar_05_CDM_EARCatalog_Technical_Specification.md|Pillar 5 (CDM) Technical Specification]].
*   **Summary**: The frozen relational structure of the domain. SI must implement the Physical Schema as a 100% faithful realization of this CDM.

### **Pillar 6: Loss & Damage LDM (Data Model)**
*   **Technical Spec**: [[ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md|Pillar 6 (LDM) Technical Specification]].
*   **Summary**: Defines the logical data model (entities + relationships) for Loss & Damage reporting. Computation formulas are treated as separate, explicit artifacts when needed (do not assume they are embedded in the LDM).

### **Pillar 7: Governance (RACI & Workflow)**
*   **Technical Spec**: [[ψ/incubate/DCCE/CRDB/output/07_Governance_RACI/Pillar_07_Governance_RACI_Technical_Specification.md|Pillar 7 (Governance) Technical Specification]].
*   **Summary**: Defines the humans in the loop. The SI must build the digital gates (G1-G5) that enforce these DCCE approval roles.

### **Pillar 8: Reference Data Matrix**
*   **Technical Spec**: [[ψ/incubate/DCCE/CRDB/output/08_RefData_Matrix/Pillar_08_RefData_Matrix_Technical_Specification.md|Pillar 8 (Ref Data) Technical Specification]].
*   **Summary**: The interoperability key. Provides the crosswalks for Provinces, Sectors, and Hazards to enable multi-agency data joining.

### **Pillar 9: Building Block Catalog**
*   **Technical Spec**: [[ψ/incubate/DCCE/CRDB/output/09_BuildingBlocks/Pillar_09_BuildingBlocks_Technical_Specification.md|Pillar 9 (Building Blocks) Technical Specification]].
*   **Summary**: The modular procurement menu. Tiers the other 8 pillars into a 3-year rollout strategy (Tier 1: Core Engine, Tier 2: Services, Tier 3: Expansion).

---
*Synthesized by the [BA+DA+IA] Team for the July 6th CRDB Handover.*
