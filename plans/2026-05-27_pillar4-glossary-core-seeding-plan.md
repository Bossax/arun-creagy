# Plan — Pillar 4 Glossary Core Seeding (Unblocking P5)

**Date**: 2026-05-27 (Asia/Bangkok)

**Scope**: Rapidly harvest and define the ~30 core terms used in Pillar 02 (Use Cases) and Pillar 05 (CDM) to provide the mandatory `Term_IDs` required for the EAR Catalog.

---

## 1) Objective
Establish a **controlled semantic baseline** for the CRDB project. This glossary ensures that policy makers (Tier 1) and data engineers (Tier 2) are using the same language for the same concepts, specifically those anchored in international standards (IPCC, Sendai, ISO 14090/14091).

---

## 2) Execution Steps

### Step 1: Term Harvesting (Evidence-Based)
Extract terms from the following "Authority" sources:
- [ ] **Pillar 02 (Use Cases)**: Actors (e.g., LAO, Policy Maker) and data requirements (e.g., Sub-district vulnerability map).
- [ ] **Pillar 05 (CDM Anchor)**: Core entities (e.g., `CLIMATE_DRIVER`, `HAZARDOUS_EVENT`, `ATTRIBUTION_LINK`).
- [ ] **ISO 14091**: *Vulnerability*, *Exposure*, *Sensitivity*, *Adaptive Capacity*, *Risk*.
- [ ] **ISO 14090**: *Adaptation Action*, *Adaptation Option*, *Resilience*.
- [ ] **Sendai Framework**: *Loss*, *Damage*, *Disaster*.

### Step 2: Definition Hardening & Normalization
- [ ] **De-duplication**: Merge similar concepts (e.g., "Climate Stressor" vs "Climate Driver").
- [ ] **Tiered Definitions**:
    - **Tier 1 (Policy)**: Short, non-technical explanation.
    - **Tier 2 (Technical)**: Implementation-specific explanation (e.g., mapping to a specific NetCDF variable or UUID).
- [ ] **Authority Linking**: Attach a `Source_Anchor` to every term.

### Step 3: Deliverable Generation
- [ ] Create `ψ/incubate/DCCE/CRDB/output/04_Glossary/Pillar_04_Glossary_Deliverable.md`
- [ ] Assign stable `TERM_XXX` IDs.
- [ ] Include the `CDM_Entity_Link` as required by the P4 Tech Spec.

---

## 3) Definition of "Seeded"
Pillar 4 is "seeded" when:
- All core entities in Pillar 5 have a corresponding `Term_ID`.
- All actors and primary data products in Pillar 2 have a corresponding `Term_ID`.
- Definitions are verified against the referenced ISO/IPCC/Sendai standards.
