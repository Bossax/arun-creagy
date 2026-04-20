---
date: 2026-03-27T16:01:00+07:00
type: info
status: raw
significance: important
---

## Issue (Serious)
There was a workflow integrity failure where an `oracle_learn()` call was referenced as having created a local learning file (example referenced name: `ψ/memory/learnings/2026-03-27_crdb-pm-history-reconstruction-pattern-treat-crd.md`), but that file did **not** exist on disk.

### Why this is serious
- Violates the system expectation of *durable capture*: learnings and retrospectives are the “Nothing is Deleted” memory substrate.
- Creates false confidence: downstream references (handoffs, plans, commits) may point to non-existent artifacts.
- Repeats a known pattern: the user reported this happened “again”.

### Required guardrail (future fix)
- After every `oracle_learn()` call, verify the returned file path exists on disk.
- If missing, immediately materialize the referenced learning file and commit it, and also log the incident.

Logged via /fyi

