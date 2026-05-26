---
title: Learning: Pillar readiness ≠ sealability (CRDB Pillar 2 example)
tags: [crdb, pillar, governance, specification, procurement, workflow]
created: 2026-05-26
source: rrr: Arun_Creagy
---

# Learning: Pillar readiness ≠ sealability (CRDB Pillar 2 example)

Learning: Pillar readiness ≠ sealability (CRDB Pillar 2 example)

In CRDB, having strong evidence/analysis (“ready”) is not the same as being able to seal a pillar (“sealable”). A pillar is sealable only when it satisfies its explicit acceptance-gate artifacts.

Example: Pillar 2 acceptance gate requires:
- a canonical Use Case Inventory Table (single registry)
- per-use-case functional specifications with testable acceptance criteria

Operational rule: When a pillar is claimed “ready”, immediately check the pillar’s Technical Specification for the mandatory artifact set, then produce the missing gate artifacts before calling it “sealed”.

Tooling/process add-on: Standardize on apply_patch for file creation/edits to avoid write-method ambiguity; keep handoffs separate from pillar-sealing outputs.

---
*Added via Oracle Learn*
