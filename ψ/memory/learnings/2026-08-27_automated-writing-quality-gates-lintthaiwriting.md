---
id: learning_2026-08-27_automated-writing-quality-gates-lintthaiwriting
type: learning
title: "Automated writing-quality gates (lint_thai_writing.py, check_density.py) check n"
concepts: [writing-pipeline, quality-gates, style-capture, generalization, self-review, CRDB]
tags: [writing-pipeline, quality-gates, style-capture, generalization, self-review, CRDB]
created: 2026-08-27
indexed_at: 2026-08-27T17:50:42.245Z
updated_at: 2026-08-27T17:50:42.245Z
hash: sha256:a7626c092ec0229911f2d095221765edc780e6950df84988e65117c6355849ba
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-27_automated-writing-quality-gates-lintthaiwriting
arra_type: learning
arra_concepts: [writing-pipeline, quality-gates, style-capture, generalization, self-review, CRDB]
arra_created: 2026-08-27T17:50:42.245Z
---

# Automated writing-quality gates (lint_thai_writing.py, check_density.py) check n

Automated writing-quality gates (lint_thai_writing.py, check_density.py) check narrow mechanical things — lexicon terms, character-count ratios — not scope-appropriateness, structural completeness, internal-artifact leakage, or formatting choices. In a CRDB exec-summary multi-agent pipeline pilot (English draft → Thai rewrite → benchmark), every gate passed at every stage while the human still rated the output 2/10 across five separate correction rounds: scope drift into full-report depth, internal artifacts (slide citations, arrow-chain-as-prose) leaking into reader-facing text, a bare acronym already eliminated in one section of the document but not generalized to another section of the same document, reflexive list-avoidance from over-applying an unrelated benchmark lesson, and substance lost during trimming. The fix that actually changed the pattern: convert pattern-matchable corrections into real kind:literal/kind:regex lexicon gate rules (block mechanically every run) rather than prose-only capture-log entries, and put genuine judgment-call corrections directly into the project's writing-plan document where the writing skill's Stage 0 calibration reads them. Also: when a human corrects a pattern in one section of a document, check the whole document for the same pattern immediately rather than waiting to be told it recurred elsewhere.

---
*Added via Oracle Learn*
