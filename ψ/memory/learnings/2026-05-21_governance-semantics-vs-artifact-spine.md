# Learning — Separate governance semantics from artifact spines (to avoid stale governance)

When hardening specification artifacts under tight timelines (TOR-first), avoid the common failure mode where every artifact tries to embed its own governance model or where governance is centralized so far away that artifacts become non-executable.

Use a three-layer split:

1) **Artifact spine (per pillar/artifact)**
- Keep the minimum row/entity-level fields required for auditability and joinability (e.g., provenance anchors, honesty posture flags, authority source pointers).

2) **Governance semantics (centralized)**
- Define what shared governance fields mean (allowed values, definitions, what “validated vs assumed” means, what “maturity” labels mean).

3) **Decision rights + operating model (centralized)**
- Define who decides, on what cadence, with what escalation rules, and how decisions are logged and versioned.

This prevents “stale shelfware governance” by ensuring:
- artifacts remain operationally usable,
- semantics remain consistent across artifacts,
- decision-making is executable with limited staffing.

Applied mapping in CRDB:
- Pillar 4/7 hold minimal audit spine; Pillar 5 defines semantics (G1–G5); Pillar 6 defines buy-in execution plan (cadence + escalation + decision log).
