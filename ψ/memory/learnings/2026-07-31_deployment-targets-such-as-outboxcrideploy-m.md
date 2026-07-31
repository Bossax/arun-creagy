---
id: learning_2026-07-31_deployment-targets-such-as-outboxcrideploy-m
type: learning
title: Deployment targets (such as ψ/outbox/cri_deploy) must NEVER be auto-synchronized
concepts: [deployment_guardrail, score_normalization, streamlit_rendering, oracle_governance]
tags: [deployment_guardrail, score_normalization, streamlit_rendering, oracle_governance]
created: 2026-07-31
indexed_at: 2026-07-31T05:09:44.751Z
updated_at: 2026-07-31T05:09:44.751Z
hash: sha256:37b18657854d8a0bbcf6de3c7f073af70778d4645b3672ed4f8dcd0d7045731c
source: Retrospective v4.4
project: github.com/bossax/arun_creagy
arra_id: learning_2026-07-31_deployment-targets-such-as-outboxcrideploy-m
arra_type: learning
arra_concepts: [deployment_guardrail, score_normalization, streamlit_rendering, oracle_governance]
arra_created: 2026-07-31T05:09:44.751Z
---

# Deployment targets (such as ψ/outbox/cri_deploy) must NEVER be auto-synchronized

Deployment targets (such as ψ/outbox/cri_deploy) must NEVER be auto-synchronized or mutated by an AI agent during local development or troubleshooting without explicit, turn-level command from the human. Precomputed JSON summary arrays (like rankings.top_10) must be cross-checked against primary records arrays to ensure score fields like normalized_score are present and bound correctly in Streamlit UI helpers.

---
*Added via Oracle Learn*
