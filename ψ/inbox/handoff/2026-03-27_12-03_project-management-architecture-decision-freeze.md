# Handoff: Project management architecture decision freeze

**Date**: 2026-03-27 12:03 ICT
**Context**: Decision freeze after architecture review, second-opinion checks, and Nat-brain mentality review.

## Decision Frozen

The chosen direction is:

- **artifact-first project management** as the foundation
- **explicit modular capabilities** as the operating core
- optional **thin, transparent `project-manager` facade** only after the artifacts and module boundaries are stable
- **no strong singleton manager** and no hidden orchestration

This decision is grounded in:

- [`plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md`](plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md)
- [`CLAUDE.md`](CLAUDE.md)

## What We Did

- Designed a CRDB-first Oracle-aligned project work-cycle architecture.
- Added trigger, evidence, claim, decision, deliverable, and learning layers.
- Added a non-linear session model to fit fragmented and iterative work.
- Tested the skill layer against mental overhead using hypothetical sessions.
- Evaluated a singleton `project-manager` pattern against Oracle principles.
- Ran independent and proxy Nat-brain style reviews to stress-test the singleton approach.
- Revised the plan to include four implementation alternatives and an updated recommendation.
- Clarified the invocation model for a disorientation-oriented [`/project-manager`](plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md).

## Pending

- [ ] Create the first implementation anchor files for CRDB project-management ledgers.
- [ ] Define the initial explicit modules for project management.
- [ ] Decide whether first implementation uses only artifacts or includes a very thin facade.
- [ ] If a facade is included, constrain it to transparent dispatch and low-risk delegation only.

## Next Session

- [ ] Implement the anchor artifact skeleton for CRDB:
  - trigger log
  - deliverable map
  - claim register
  - submission log
  - change log
- [ ] Draft the first explicit module specs:
  - state sensing
  - trigger capture
  - deliverable trace
- [ ] Only after artifact stability, decide whether to add the thin `project-manager` facade.

## Key Files

- [`plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md`](plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md)
- [`ψ/inbox/handoff/2026-03-27_12-03_project-management-architecture-decision-freeze.md`](ψ/inbox/handoff/2026-03-27_12-03_project-management-architecture-decision-freeze.md)
- [`plans/2026-03-27-project-management-anchor-implementation-plan.md`](plans/2026-03-27-project-management-anchor-implementation-plan.md)
