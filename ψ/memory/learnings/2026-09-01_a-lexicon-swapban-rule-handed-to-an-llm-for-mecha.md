---
id: learning_2026-09-01_a-lexicon-swapban-rule-handed-to-an-llm-for-mecha
type: learning
title: A lexicon swap/ban rule handed to an LLM for mechanical text polishing fires whe
concepts: [writing-th, lexicon-rules, llm-polishing, fidelity-verification, thai-prose, crdb]
tags: [writing-th, lexicon-rules, llm-polishing, fidelity-verification, thai-prose, crdb]
created: 2026-09-01
indexed_at: 2026-09-01T08:45:38.402Z
updated_at: 2026-09-01T08:45:38.402Z
hash: sha256:6774a32a1c6703bc5bcdbb0007cb915d22bf58132abcfa462dce980628f2698b
source: "rrr: crdb-3.1-pure-p-polish"
arra_id: learning_2026-09-01_a-lexicon-swapban-rule-handed-to-an-llm-for-mecha
arra_type: learning
arra_concepts: [writing-th, lexicon-rules, llm-polishing, fidelity-verification, thai-prose, crdb]
arra_created: 2026-09-01T08:45:38.402Z
---

# A lexicon swap/ban rule handed to an LLM for mechanical text polishing fires whe

A lexicon swap/ban rule handed to an LLM for mechanical text polishing fires wherever it pattern-matches, not just where its author intended. Two concrete failure modes observed in the same polish pass (CRDB report §3.1, qwen3.6-plus): (1) a swap rule meant for one narrow purpose (a counting classifier "ฉบับ→รายการ" for deliverable items) also matched the same word inside an unrelated fixed document name ("รายงานฉบับกลาง", the Interim Report), corrupting it into a wrong-but-plausible term ("รายงานระหว่างกลาง"); (2) a banned rhetorical pattern ("ไม่ใช่เพียง...แต่") was over-generalized by the model to a structurally similar "not X, but Y" sentence that didn't contain the literal banned string, causing it to silently drop the qualifying clause entirely. Mitigation: before handing a swap/ban list to a polishing model, scan the source for every occurrence of each target word/pattern and carve out any instance that's a proper noun or fixed term. More fundamentally: never trust a lint-clean or rule-compliant output as proof of fidelity — diff every paragraph against the source regardless of how strict the prompt was. Strict instructions reduce but do not eliminate drift; paragraph-by-paragraph verification is the actual fidelity control, not the prompt's strictness. This generalizes the earlier lesson that a pipeline stage compressing evidence (e.g. an argument map's grounds field) loses fidelity that downstream stages can't recover just because an earlier stage "read" the source.

---
*Added via Oracle Learn*
