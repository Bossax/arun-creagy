---
id: learning_2026-07-01_rule-compliance-alignment-in-text-generation-wh
type: learning
title: # Rule compliance alignment in text generation
concepts: [rules, compliance, style-pack, translation, LLM-forgetfulness]
tags: [rules, compliance, style-pack, translation, LLM-forgetfulness]
created: 2026-07-01
indexed_at: 2026-07-01T09:08:21.550Z
updated_at: 2026-07-01T09:08:21.550Z
hash: sha256:f95d38585caa14455b62c00714266f1121e747a4933787122e4faffc82e1cc80
source: Oracle Learn
project: bossax/arun_creagy
arra_id: learning_2026-07-01_rule-compliance-alignment-in-text-generation-wh
arra_type: learning
arra_concepts: [rules, compliance, style-pack, translation, LLM-forgetfulness]
arra_created: 2026-07-01T09:08:21.550Z
---

# # Rule compliance alignment in text generation

# Rule compliance alignment in text generation

When merging or composing draft sections into a document, LLMs are highly prone to recency bias or default template usage, which reintroduces forbidden terms (e.g. DCCE, CRDB, use cases, API) violating the style pack constraints.
To resolve this, a dual-pass compliance workflow must be established:
1. Automated Batch replacement using string mapping scripts to catch 100% of simple occurrences.
2. Manual contextual cleanup to restore sentence flow, fix spacing, and adjust grammatical structures in Thai.

---
*Added via Oracle Learn*
