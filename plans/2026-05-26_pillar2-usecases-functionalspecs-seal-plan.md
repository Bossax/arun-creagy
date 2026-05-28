# Plan — Produce and Seal Pillar 2 (Use Case Inventory & Functional Specs)

**Date**: 2026-05-26 (Asia/Bangkok)

**Scope**: Produce the sealable Pillar 2 deliverable package (canonical use-case inventory + per-use-case functional specifications) based on interview findings and workshop analysis artifacts.

**Acceptance gate** is defined in [`Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md:15).

---

## 1) Objective

Create a **procurement-safe, testable, evidence-traceable** Pillar 2 deliverable that specifies *what the system must do* (functional intent + acceptance criteria), without prescribing implementation architecture, consistent with the boundary in [`Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md:7).

---

## 2) Inputs (frozen evidence set)

Use only the following as the authoritative evidence base for Pillar 2 compilation:

### 2.1 Interview-derived use cases and patterns

- [`canoncial_use_cases.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/canoncial_use_cases.md)
- [`NCAIF — Workflow patterns + MVP v3.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF%20—%20Workflow%20patterns%20+%20MVP%20v3.md)

### 2.2 Workshop validation + expansion artifacts

- [`activity2_raw_extraction.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_raw_extraction.md)
- [`activity2_master_analysis.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_master_analysis.md)
- [`activity2_clustering_synthesis.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_clustering_synthesis.md)
- [`activity2_discourse_implications.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_discourse_implications.md)

### 2.3 Pillar 2 acceptance criteria and schema requirements

- [`Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md)

---

## 3) Outputs to produce (Pillar 2 deliverable package)

### 3.1 Canonical deliverable file (compiled)

Create a single compiled deliverable as the sealing target:

- `ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Deliverable.csv

This file will include:

1. Executive boundary statement (what Pillar 2 is / is not)
2. Evidence list (inputs above)
3. **Canonical Use Case Inventory Table** (required)
4. **Per-Use-Case Functional Specifications** (required)
5. Traceability matrix (interviews + workshop concepts + clusters)
6. “Phase 1 vs Deferred” boundary section
7. Change control note (future scope edits must be logged in ledgers)

### 3.2 Optional supporting artifacts (only if needed)

- `Pillar_02_UseCases_FunctionalSpecs_Codebook.md` (only if coding categories are needed to explain consolidation)
- `Pillar_02_UseCases_FunctionalSpecs_Traceability_Matrix.md` (only if the matrix is too large for the compiled file)

---

## 4) Method: how to convert evidence into sealable specs

### 4.1 Consolidation principle (avoid “26 use cases”)

Treat the workshop’s 26 normalized concepts as **validation signals**, not 1:1 final use cases.

Anchor consolidation on:

- interview intent and workflow patterns in [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Use_Cases.md:175)
- demand clusters in [`activity2_clustering_synthesis.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_clustering_synthesis.md:7)
- implementation implications in [`activity2_discourse_implications.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_discourse_implications.md:22)

Target: **8–10 canonical use cases** that are procurement-safe and testable.

### 4.2 Inventory table schema (must satisfy Pillar 2 spec)

The canonical inventory table must include fields required by [`Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md:21):

- `Use_Case_ID`
- `Use_Case_Name`
- `Primary_Actors`
- `Trigger_Event`
- `Goal_Outcome`
- `Inputs`
- `Outputs`
- `Dependencies`
- `Priority`
- `Status`
- `Evidence_Anchor`

### 4.3 Per-use-case functional spec template

Each use case spec must include the required schema from [`Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md:37):

- `Use_Case_ID`
- Problem statement / user intent
- Actors & permissions
- Preconditions
- Main flow (step-by-step)
- Alternate / exception flows
- Data inputs (explicit)
- Data outputs (explicit)
- Non-functional constraints (TOR-relevant only)
- Acceptance criteria (testable)

### 4.4 Traceability requirement (procurement shield)

For each canonical use case, include:

- pointers to relevant interview entries (from [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Use_Cases.md))
- pointers to workshop concept IDs (from [`activity2_master_analysis.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_master_analysis.md:7))
- mapping to workshop clusters (from [`activity2_clustering_synthesis.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_clustering_synthesis.md:7))

---

## 5) Proposed canonical use case set (draft)

This is the working consolidation target (final names/IDs can be adjusted during compilation):

1. **UC-01 — Authoritative Baseline & Projection Registry** (SSOT + endorsement + versioning)
2. **UC-02 — Localized Vulnerability & Risk Mapping Service** (sub-district/LAO-ready overlays)
3. **UC-03 — Exportable Policy/Budget Briefing Pack Generator** (Tier-1 decision packaging)
4. **UC-04 — Disaster Impact + Loss & Damage Intake Gateway** (schema + validation + revision history)
5. **UC-05 — Urban Resilience & Land-Use / Infrastructure Planning Support**
6. **UC-06 — Sectoral Impact & Recovery Modules (extensible pattern)**
7. **UC-07 — Machine-Readable Access / API Service for Priority Layers**
8. **UC-08 — Uncertainty + Limitations + Safe-Use Guidance Service**
9. **UC-09 — Clearinghouse / Integrated Adaptation Platform Navigation (link-first)**
10. **UC-10 — Governance and Contactability Workflow (owner/contact + review/publish)**

Each of these must be tied to evidence and acceptance criteria; if a use case cannot be made testable, it must be re-scoped or marked Deferred.

---

## 6) Quality controls (non-negotiable)

1. **ID integrity**: no orphan specs; every spec ID must exist in the inventory (per [`Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md:54)).
2. **Evidence traceability**: every use case must have an `Evidence_Anchor` (per [`Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md:55)).
3. **No invention**: unknown dependencies must be recorded as `Unknown/TBD` (per [`Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md:57)).
4. **Do not collapse demand signals**: keep separate signals where relevant (e.g., cluster membership vs workshop vote momentum) and explain the consolidation logic.
5. **Scope protection**: explicitly state exclusions (no architecture mandate, no guaranteed automation, no sensitive personal data exposure without governance approval).

---

## 7) Execution steps (work order)

1. Build a draft canonical inventory table (8–10 use cases) and assign stable IDs.
2. For each canonical use case, draft the functional spec using the template in Section 4.3.
3. Build traceability matrix linking each canonical use case to:
   - relevant interview UCs in [`NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Use_Cases.md)
   - workshop concept IDs in [`activity2_master_analysis.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_master_analysis.md)
   - workshop clusters in [`activity2_clustering_synthesis.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/activity2_clustering_synthesis.md)
4. Add explicit Phase 1 vs Deferred decisions and boundaries.
5. Run the quality controls in Section 6.
6. Mark Pillar 2 as “seal candidate” once the compiled deliverable satisfies the acceptance gate.

---

## 8) Definition of “sealed”

Pillar 2 is sealable when:

- the inventory table exists and meets the schema
- every inventory row has a corresponding spec
- each spec contains testable acceptance criteria
- each use case includes evidence anchors (interview/workshop)
- phase boundaries and exclusions are explicit

This matches the “logical sovereignty” stance in [`Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/Pillar_02_UseCases_FunctionalSpecs_Technical_Specification.md:61).

