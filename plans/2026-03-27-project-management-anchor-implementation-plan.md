# Plan: Project management anchor implementation

## Background

This plan freezes the implementation anchor after the architecture and review process recorded in:

- [`plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md`](plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md)
- [`ψ/inbox/handoff/2026-03-27_12-03_project-management-architecture-decision-freeze.md`](ψ/inbox/handoff/2026-03-27_12-03_project-management-architecture-decision-freeze.md)

## Frozen implementation stance

Implement project management in this order:

1. **Artifacts first**
2. **Explicit modules second**
3. **Thin facade later if still needed**

Do **not** begin with a powerful singleton manager.

## Pending from last session

- Create the first implementation anchor files for CRDB project-management ledgers.
- Define the initial explicit modules for project management.
- Decide whether first implementation uses only artifacts or includes a very thin facade.
- If a facade is included, constrain it to transparent dispatch and low-risk delegation only.

## Next session goals

### Goal 1 — Create CRDB anchor ledgers

Create these canonical files under [`ψ/incubate/DCCE/CRDB/output/`](ψ/incubate/DCCE/CRDB/output/):

- `CRDB-Trigger-Log.md`
- `CRDB-Deliverable-Map.md`
- `CRDB-Claim-Register.md`
- `CRDB-Submission-Log.md`
- `CRDB-Change-Log.md`

### Goal 2 — Define the first explicit modules

Write lightweight module specs for:

- state sensing
- trigger capture
- deliverable trace

These should remain explicit and callable even if a facade is added later.

### Goal 3 — Preserve the low-agency boundary

If a thin facade is introduced, keep these rules:

- it must declare inferred state
- it must disclose the module it invokes or recommends
- it may auto-invoke only low-risk orientation actions
- it must ask before higher-agency changes
- it must emit an operation receipt

## Proposed implementation options for next session

### Option A — Conservative

Implement only the anchor ledgers and module specs.

### Option B — Controlled facade

Implement the anchor ledgers, module specs, and a dry-run style `project-manager` facade that only recommends or transparently dispatches low-risk actions.

## Recommended next-session scope

Use **Option A** unless there is a strong reason to validate the facade immediately.

## Reference

- Architecture: [`plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md`](plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md)
- Handoff: [`ψ/inbox/handoff/2026-03-27_12-03_project-management-architecture-decision-freeze.md`](ψ/inbox/handoff/2026-03-27_12-03_project-management-architecture-decision-freeze.md)
