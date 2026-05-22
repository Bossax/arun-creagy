# Technical Specification: Pillar 2 — Use Case Inventory & Functional Specs

## 0. Purpose (TOR-direct, time-bounded)

This pillar specifies the **minimum functional specification package** required to make the CRDB blueprint implementable under procurement constraints.

**Boundary:** Pillar 2 defines *what the system must do* (user intent, triggers, inputs/outputs, click paths, and acceptance criteria). It does **not** prescribe:

- physical implementation architecture,
- UI design systems,
- detailed integration/ETL designs (those remain implementation choices, constrained by the blueprint).

## 1. Data Structural Requirements

### 1.1 Mandatory artifact set (minimum viable)

1. **Use Case Inventory Table** (single canonical registry)
2. **Per-Use-Case Functional Specification** (one spec per use case; may be separate files or a single compiled document)
3. **Workflow pattern drafts / MVP variants** may exist as supporting artifacts, but the inventory table + per-use-case specs are the acceptance gate.

### 1.2 Mandatory schema — Use Case Inventory Table

The inventory table must include (at minimum):

- `Use_Case_ID` (stable identifier; never re-used)
- `Use_Case_Name`
- `Primary_Actors` (roles, not people)
- `Trigger_Event`
- `Goal_Outcome` (what is achieved)
- `Inputs` (data/products required)
- `Outputs` (data/products produced)
- `Dependencies` (pillars and/or external systems)
- `Priority` (e.g., `High` / `Medium` / `Low`)
- `Status` (e.g., `Draft` / `Validated` / `Deferred`)
- `Evidence_Anchor` (pointer to interview note / workshop note / TOR clause)

### 1.3 Mandatory schema — Per-Use-Case Functional Specification

Each use case spec must include:

- `Use_Case_ID` (matches the inventory)
- `Problem statement` / `User intent`
- `Actors & permissions` (role-level)
- `Preconditions`
- `Main flow` (step-by-step; click path narrative is acceptable)
- `Alternate flows` / `exception flows`
- `Data inputs` (explicit references to inventory/datasets)
- `Data outputs` (explicit references to products/forms/catalog entries)
- `Non-functional constraints` (only when TOR-relevant)
- `Acceptance criteria` (testable statements)

## 2. Quality Assurance & Verification Criteria

- **ID integrity:** every referenced use case must exist in the inventory; no orphan specs.
- **Evidence traceability:** every use case must have an `Evidence_Anchor`.
- **Cross-pillar alignment:** dependencies must reference the correct pillar folder names under [`ψ/incubate/DCCE/CRDB/output/`](ψ/incubate/DCCE/CRDB/output:1).
- **No invention:** if a data dependency is unknown, it must be recorded as `Unknown/TBD` with an evidence note; do not fabricate datasets.

## 3. Implementation Constraints

- This pillar is **logical sovereignty**: contractors may optimize physical implementation, but must not change the defined use case intent, IDs, or acceptance criteria without a logged governance decision.
- Any changes to use case scope must be recorded in the CRDB ledgers (change log + trigger log) with a rationale and evidence link.

