---
id: learning_2026-08-30_verify-diff-provenance-before-running-style-captur
type: learning
title: "Verify diff provenance before running style-capture's zero-drop lexical audit. A"
concepts: [style-capture, writing-th, diff-provenance, rationale-gate, CRDB]
tags: [style-capture, writing-th, diff-provenance, rationale-gate, CRDB]
created: 2026-08-30
indexed_at: 2026-08-30T11:45:18.934Z
updated_at: 2026-08-30T11:45:18.934Z
hash: sha256:b1b72ee974290e7b2f66b2af35815314e34377119a4fa2a626f84e92e7b72586
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-30_verify-diff-provenance-before-running-style-captur
arra_type: learning
arra_concepts: [style-capture, writing-th, diff-provenance, rationale-gate, CRDB]
arra_created: 2026-08-30T11:45:18.934Z
---

# Verify diff provenance before running style-capture's zero-drop lexical audit. A

Verify diff provenance before running style-capture's zero-drop lexical audit. A non-empty `git diff` on a report-section file is necessary but not sufficient evidence of a human style-correction pass — three distinct causes produce a non-empty diff: (1) an outline reshuffle moving unrelated content under a reused filename (no real edit), (2) a pipeline re-verbalization of the same argument map (AI output vs AI output, no human in the loop), (3) an actual human edit. Before running diff_word_table.py's output through the zero-drop audit, check the diff's shape: word/sentence-level substitutions with no new facts/figures/restructured sections = proceed; whole new paragraphs, added numbers, cut/added sections, or renumbered lists = stop and confirm provenance with the user first. This generalizes the earlier "ask rationale before promoting" lesson from rationale to provenance itself.

Secondary finding: a rationale-gate answer can surface a rule bigger than the candidate being asked about. In one case, "why did you drop these specific timeline figures" revealed an actual writing-plan scope boundary (don't presume detail about a not-yet-decided next TOR) rather than a style preference — that belongs in the writing-th contract-validation logic, not the style lexicon or a generic content_correction log entry. When an answer names a rule outside the current skill's remit, surface it as a distinct follow-up instead of silently filing it away.

---
*Added via Oracle Learn*
