---
id: learning_2026-09-28_a-subagents-self-reported-qa-is-not-evidence-it-h
type: learning
title: "A subagent's self-reported QA is not evidence it happened correctly. When a suba"
concepts: [subagents, qa, verification, lint, thai-writer, writing-th, trust]
tags: [subagents, qa, verification, lint, thai-writer, writing-th, trust]
created: 2026-09-28
indexed_at: 2026-09-28T17:33:35.373Z
updated_at: 2026-09-28T17:33:35.373Z
hash: sha256:0735970387f4c888bcf2b5825f2cad8ff556dc7ec6455c66d64ee7c8ace6b1be
source: "rrr: Arun_Creagy"
arra_id: learning_2026-09-28_a-subagents-self-reported-qa-is-not-evidence-it-h
arra_type: learning
arra_concepts: [subagents, qa, verification, lint, thai-writer, writing-th, trust]
arra_created: 2026-09-28T17:33:35.373Z
---

# A subagent's self-reported QA is not evidence it happened correctly. When a suba

A subagent's self-reported QA is not evidence it happened correctly. When a subagent's own tooling is degraded in its execution environment (e.g. no working Python venv in its skill mirror), it will honestly report the degradation ("lint couldn't run, checked by hand instead") — but the fallback self-check is not reliable just because it's honestly reported. Across two dispatches of a thai-writer agent in one session, independently re-running the real linter afterward found violations the manual check missed, including one violation the rewrite itself introduced inside text the agent had just described as checked and clean. Practical rule: when a subagent's task includes a verification step (lint, tests, a build) and there's any reason its environment might not support that step cleanly, independently re-run the real verification yourself afterward rather than trusting the subagent's self-report — even when it reports success, and especially when it reports a fallback. Related: a lexicon regex rule intended to catch "bare verb after รับผิดชอบ" actually matched any non-"การ" text following it, producing false positives in the document being edited — the same lesson at the rule-design level: a check that looks correct in isolation needs to be run against real material before being trusted.

---
*Added via Oracle Learn*
