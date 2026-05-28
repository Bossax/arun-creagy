# Plan — Produce and Seal Pillar 5 (CDM & EAR Catalog)

**Date**: 2026-05-27 (Asia/Bangkok)

**Scope**: Produce the sealable Pillar 5 deliverable package (Entity-Attribute-Relationship Catalog) that serves as the logical backbone for the CRDB system, directly answering the functional requirements in Pillar 02 and the architectural requirements of the NCAIF Sitemap.

---

## 1) Objective

Create a **logically sovereign, procurement-ready** Pillar 5 deliverable. The CDM must not only be scientifically sound (Climate Science/Disaster Risk) but must be **functionally mapped** to ensure it can support every use case in Pillar 02 and every interface requirement in the NCAIF Sitemap.

---

## 2) Inputs (The Grounding Evidence)

### 2.1 Functional & Architectural Drivers (The "What")
- **Pillar 02 Use Cases**: [`Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md) (The 10 canonical UCs).
- **NCAIF Sitemap**: [`ψ/incubate/DCCE/CRDB/output/01_Sitemap_InterfaceMapping/`](ψ/incubate/DCCE/CRDB/output/01_Sitemap_InterfaceMapping/) (The structural design of the target system).

### 2.2 Technical & Semantic Baselines (The "How")
- **CDM Anchor**: [`Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md)
- **Glossary Spec (Pillar 04)**: [`Pillar_04_Glossary_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/04_Glossary/Pillar_04_Glossary_Technical_Specification.md)

---

## 3) Execution Steps

### Step 1: Requirements Audit (NCAIF + P02 Alignment) [COMPLETE]
- [x] **Sitemap Mapping**: Audit every module/page in the NCAIF Sitemap. Identify which CDM entity provides the underlying *data*.
- [x] **Use Case Stress-Test**: For each of the 10 Canonical Use Cases (UC-01 to UC-10), verify that the entity relationships allow for the required data flow.

### Step 2: Semantic Integrity Check (Pillar 04 Alignment) [COMPLETE]
- [x] **Term Sync**: Cross-reference all Entity Business Definitions with the Pillar 04 Glossary. Ensure every entity name has a corresponding `Term_ID`.

### Step 3: Entity-Attribute-Relationship (EAR) Compilation [COMPLETE]
- [x] **Entity Catalog**: Finalize the list of entities.
- [x] **EXCLUSION**: Content-management entities handled in Pillar 01.
- [x] **Attribute Registry**: Define data nature and align with standards.
- [x] **Relationship Matrix**: Define Cardinality and mandatory constraints.

### Step 4: Verification against Core Mandates [COMPLETE]
- [x] **Determinant Neutrality**: Confirmed.
- [x] **Slow-Onset Attribution**: Confirmed.

---

## 4) Deliverable Package (Output)

The final product will be:
`ψ/incubate/DCCE/CRDB/output/05_CDM_EARCatalog/Pillar_05_CDM_EARCatalog_Deliverable.md`

Including:
1. **Logical Domain Map** (Physical, Attribution, Receptor, Vulnerability, Outcomes).
2. **The EAR Catalog** (Entity List, Attribute Registry, Relationship Matrix).
3. **Traceability Matrix**: Mapping Entities → Pillar 02 Use Cases → NCAIF Sitemap Modules.
4. **Implementation Constraints** (Sovereignty rules for vendors).

---

## 5) Definition of "Sealed"

Pillar 5 is sealed when the EAR Catalog is verified to support:
- **100% of Pillar 02 Use Cases.**
- **100% of the NCAIF Sitemap requirements.**
- **All non-negotiable logic** (Driver/Hazard separation, Determinant Neutrality).
