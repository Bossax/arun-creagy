---
title: Learning — Separate governance semantics from artifact spines (to avoid stale go
tags: [governance, dama, dmbok, procurement, scope-control, specification]
created: 2026-05-21
source: rrr: Arun_Creagy
---

# Learning — Separate governance semantics from artifact spines (to avoid stale go

Learning — Separate governance semantics from artifact spines (to avoid stale governance)

When hardening specification artifacts under tight timelines (TOR-first), avoid the failure mode where every artifact embeds its own governance model, or governance is centralized so far away that artifacts become non-executable.

Use a three-layer split:
1) Artifact spine (per pillar/artifact): keep minimum row/entity-level fields required for auditability/joinability (provenance anchors, honesty posture flags, authority source pointers).
2) Governance semantics (centralized): define shared governance field meanings (allowed values, definitions, what “validated vs assumed” means, maturity labels).
3) Decision rights + operating model (centralized): define who decides, cadence, escalation rules, and decision log/versioning.

Outcome: artifacts remain operational, semantics remain consistent, and decision-making is executable with limited staffing.

Applied mapping in CRDB: Pillar 4/7 hold minimal audit spine; Pillar 5 defines semantics (G1–G5); Pillar 6 defines buy-in execution plan (cadence + escalation + decision log).

---
*Added via Oracle Learn*
