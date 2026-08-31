---
id: learning_2026-08-31_citationevidence-audits-go-stale-silently-when-th
type: learning
title: Citation/evidence audits go stale silently when their target draft is later rewr
concepts: [citation-audit, writing-th-v6, evidence-traceability, staleness-check, external-vs-internal-sourcing, pretooluse-gate]
tags: [citation-audit, writing-th-v6, evidence-traceability, staleness-check, external-vs-internal-sourcing, pretooluse-gate]
created: 2026-08-31
indexed_at: 2026-08-31T04:00:24.394Z
updated_at: 2026-08-31T04:00:24.394Z
hash: sha256:65eccc143ebe8987b4c260796c5b2e10a0f1a26109a58f0d674170e2068f9792
source: "rrr: crdb-ch1-references-chapter-and-platform-citation-trace"
arra_id: learning_2026-08-31_citationevidence-audits-go-stale-silently-when-th
arra_type: learning
arra_concepts: [citation-audit, writing-th-v6, evidence-traceability, staleness-check, external-vs-internal-sourcing, pretooluse-gate]
arra_created: 2026-08-31T04:00:24.394Z
---

# Citation/evidence audits go stale silently when their target draft is later rewr

Citation/evidence audits go stale silently when their target draft is later rewritten — compare the audit's build timestamp against the draft's last-modified timestamp before trusting it, and spot-check by grepping the audit's cited terms against the live draft text. Separately: when a claim's clearest source is an internal/unsealed working doc, use it only to precisely name what concept needs grounding, then search externally for that concept's real-world analog — internal, unsealed docs identify claims, they don't source them. And a harness write-gate failing on a missing sidecar file (e.g. no argument-map.json) is a legitimate signal that the target artifact needs an upstream step, not friction to route around — park the already-verified work product rather than forcing or dropping it.

---
*Added via Oracle Learn*
