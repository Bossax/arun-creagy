---
id: learning_2026-08-29_in-multi-stage-llm-writing-pipelines-like-writing
type: learning
title: "In multi-stage LLM writing pipelines (like writing-th), strict content isolation"
concepts: [rrr, writing-th, linguistic-layers, subagent-isolation, thai-institutional-writing, context-grounding]
tags: [rrr, writing-th, linguistic-layers, subagent-isolation, thai-institutional-writing, context-grounding]
created: 2026-08-29
indexed_at: 2026-08-29T18:08:26.674Z
updated_at: 2026-08-29T18:08:26.674Z
hash: sha256:a333b7a177c55b27abc3b8c7125448cebb79c11420def9b835e7ac17c6a0d08e
source: rrr on 01.07_crdb-ch4-reverbalization-with-thai-source-grounding
project: github.com/bossax/arun_creagy
arra_id: learning_2026-08-29_in-multi-stage-llm-writing-pipelines-like-writing
arra_type: learning
arra_concepts: [rrr, writing-th, linguistic-layers, subagent-isolation, thai-institutional-writing, context-grounding]
arra_created: 2026-08-29T18:08:26.674Z
---

# In multi-stage LLM writing pipelines (like writing-th), strict content isolation

In multi-stage LLM writing pipelines (like writing-th), strict content isolation at the verbalization stage prevents argument drift but starves idiomatic language generation when the upstream argument map is in English. 

The essential distinction is Content Authority vs. Language Anchor:
1. The English argument map (argument-map.json) remains the SOLE AUTHORITY on facts, claims, warrants, and numbers.
2. Domain source documents (source_paths) and reference style exemplars must be provided to the verbalizer as a LANGUAGE ANCHOR to absorb authentic Thai institutional cadence, administrative terminology, and sentence rhythm.
3. Verification pipelines must include an explicit Syntactic Fluency check (L2/L3) at Stage 5 rather than relying solely on L1 regex linters or high-level Toulmin coverage checks.

---
*Added via Oracle Learn*
