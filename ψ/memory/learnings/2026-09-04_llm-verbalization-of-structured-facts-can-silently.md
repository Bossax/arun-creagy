---
id: learning_2026-09-04_llm-verbalization-of-structured-facts-can-silently
type: learning
title: "LLM verbalization of structured facts can silently drift, even under explicit an"
concepts: [llm-verbalization, fidelity-drift, typhoon, writing-th, editorial-review, max-tokens]
tags: [llm-verbalization, fidelity-drift, typhoon, writing-th, editorial-review, max-tokens]
created: 2026-09-04
indexed_at: 2026-09-04T10:38:17.842Z
updated_at: 2026-09-04T10:38:17.842Z
hash: sha256:a81e8d321516f2ceb2f2e8b11bbb6d10be4a4214db0041d5b0772b988fdf31d4
source: "rrr: REPO"
arra_id: learning_2026-09-04_llm-verbalization-of-structured-facts-can-silently
arra_type: learning
arra_concepts: [llm-verbalization, fidelity-drift, typhoon, writing-th, editorial-review, max-tokens]
arra_created: 2026-09-04T10:38:17.842Z
---

# LLM verbalization of structured facts can silently drift, even under explicit an

LLM verbalization of structured facts can silently drift, even under explicit anti-drift instructions.

Tested typhoon-v2.5-30b-a3b-instruct by asking it to write CRDB report prose strictly from one node (Home-page unit) of an approved argument-map.json, then compared against source and old drafts.

First call: silently dropped an entire argument unit (no error/truncation signal), and silently reordered/relabeled a named category -- "international, domestic" funding sources became "private sector, international" -- inventing a category not in the source. Second call, with an explicit "do not alter given wording" instruction and higher max_tokens, fixed both but still dropped one word from a section name.

This is a controlled-vocabulary-preservation failure, not generic hallucination -- the model wasn't asked to add facts, it was asked to not change facts handed to it verbatim, and still drifted on the first unconstrained attempt, with zero signal to the caller.

How to apply: treat any LLM verbalization step over structured/approved source data as needing an independent fidelity check against the source regardless of output fluency. On a first-time call to an unfamiliar model for multi-unit generation, always set an explicit generous max_tokens rather than trusting provider defaults -- silent truncation looks identical to a complete answer. This is exactly the failure class an independent editorial-review pass against source is designed to catch.

---
*Added via Oracle Learn*
