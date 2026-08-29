---
id: learning_2026-08-29_a-harness-stages-must-never-load-x-rule-is-a-co
type: learning
title: "A harness stage's \"must never load X\" rule is a content boundary, not automatica"
concepts: [subagent-orchestration, cost-efficiency, context-isolation, writing-th, claude-code]
tags: [subagent-orchestration, cost-efficiency, context-isolation, writing-th, claude-code]
created: 2026-08-29
indexed_at: 2026-08-29T15:58:19.098Z
updated_at: 2026-08-29T15:58:19.098Z
hash: sha256:7db326b5736e4220993dd138f8bb1339a0b6f43e723084501a9a82b5918b7d04
source: "rrr: crdb-ch4-revision-mode-and-quota-burn"
arra_id: learning_2026-08-29_a-harness-stages-must-never-load-x-rule-is-a-co
arra_type: learning
arra_concepts: [subagent-orchestration, cost-efficiency, context-isolation, writing-th, claude-code]
arra_created: 2026-08-29T15:58:19.098Z
---

# A harness stage's \"must never load X\" rule is a content boundary, not automatica

A harness stage's "must never load X" rule is a content boundary, not automatically a freshness requirement. If the orchestrating session's own context is already clean of the forbidden material (style pack, lexicon, rubric), a fork (inherits context, shares prompt cache, cheaper) satisfies the isolation rule as well as a cold subagent spawn does — reserve fresh, non-fork subagent calls for stages whose isolation is about provenance of reasoning (e.g. an independent reviewer must never see the drafting agent's self-justification), not content category. Conflating the two burned an account's 5-hour usage window running 8 cold Stage-1/Stage-3 subagent calls in the writing-th harness when several could safely have been forks.

---
*Added via Oracle Learn*
