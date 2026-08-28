---
id: learning_2026-08-28_check-lexicon-vs-plan-style-rule-conflicts-before
type: learning
title: "Check lexicon-vs-plan style-rule conflicts before drafting, not after the mechan"
concepts: [writing-th, lexicon, style-rules, governance-conflict, mechanical-gate]
tags: [writing-th, lexicon, style-rules, governance-conflict, mechanical-gate]
created: 2026-08-28
indexed_at: 2026-08-28T13:54:16.388Z
updated_at: 2026-08-28T13:54:16.388Z
hash: sha256:9d03826b2563342db34e896f8dfa00b1b9ad1cb1854ea37e2ec3820dc841c95e
source: "rrr: chapter4-fact-check-and-exec-summary-drafting"
arra_id: learning_2026-08-28_check-lexicon-vs-plan-style-rule-conflicts-before
arra_type: learning
arra_concepts: [writing-th, lexicon, style-rules, governance-conflict, mechanical-gate]
arra_created: 2026-08-28T13:54:16.388Z
---

# Check lexicon-vs-plan style-rule conflicts before drafting, not after the mechan

Check lexicon-vs-plan style-rule conflicts before drafting, not after the mechanical gate fails.

Context: Drafting CRDB exec-summary §4.1 via /writing-th. The chapter-4 writing plan's own style section (integrating real committee feedback) explicitly overrode the project's default department shorthand: use "กรม สส." only, never "กรมฯ". I drafted accordingly. The mechanical lint then failed on [LEXICON] 'DCCE' -> use 'กรมฯ' — the global LEXICON_TH.json still had the older, more general rule and had never been reconciled with the newer, more specific plan-level override. This forced a mid-draft stop to ask Boss how to resolve the conflict rather than catching it during contract-building.

Pattern: When a governing document (a writing plan, a style section, a contract) introduces a rule that is newer and more specific than a project-wide default (a shared lexicon, a style pack), the two are not automatically reconciled just because the newer rule exists. A mechanical gate checking against the older, unreconciled source will fail — not because the draft is wrong, but because two authorities disagree and nobody has decided which wins. Discovering this after drafting (via a gate failure) costs a full round-trip; discovering it before drafting costs nothing.

Fix that worked: When a section-specific style rule contradicts or narrows a project-wide convention, check the actual enforcement artifact (lexicon file, linter config) for the conflicting rule before drafting — not just the prose style guide. If a conflict exists, surface it as an explicit decision point up front (override for this draft with documented disposition, update the shared lexicon now, or revert the newer rule) rather than letting the mechanical gate discover it. Document whichever resolution is chosen directly in the mechanical_reviews/dispositions, not as a silent workaround.

Generalizes to: Any workflow with layered governance — a global style guide plus a per-document override, a base config plus a project-specific one, a team-wide lint rule plus a file-level exception. Before producing output that will be mechanically checked, diff the specific rule you're about to follow against the general rule the checker actually enforces.

---
*Added via Oracle Learn*
