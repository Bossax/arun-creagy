---
id: learning_2026-09-11_a-green-mechanical-gate-certifies-governed-pattern
type: learning
title: "A green mechanical gate certifies governed patterns, not correctness."
concepts: [quality-gates, linting, review-design, thai-writing, false-assurance, writing-th, attention-blind-spots]
tags: [quality-gates, linting, review-design, thai-writing, false-assurance, writing-th, attention-blind-spots]
created: 2026-09-11
indexed_at: 2026-09-11T08:53:04.183Z
updated_at: 2026-09-11T08:53:04.183Z
hash: sha256:6a85be54c6a1107794d167a6b45255ece774df4853232094b4fe96835647a1a4
source: "rrr: Arun_Creagy"
arra_id: learning_2026-09-11_a-green-mechanical-gate-certifies-governed-pattern
arra_type: learning
arra_concepts: [quality-gates, linting, review-design, thai-writing, false-assurance, writing-th, attention-blind-spots]
arra_created: 2026-09-11T08:53:04.183Z
---

# A green mechanical gate certifies governed patterns, not correctness.

A green mechanical gate certifies governed patterns, not correctness.

During the GGA targets Thai translation (writing-th harness, 2026-09-11), `lint_thai_writing.py` passed the draft twice while target 9(g) contained `ความรู้ของชนพื้นเผ่าเมือง` — a syllable transposition of the contract-locked term `ชนเผ่าพื้นเมือง`. The independent Stage 5 reviewer caught it on a clause-by-clause read against the English source.

The linter was not broken. It governs terms listed in LEXICON_TH.json plus structural patterns. The term was not a lexicon entry, so no rule watched it, and a transposed Thai compound is not something the tokenizer treats as anomalous. The typo also falsified its own documentation — it was the only occurrence in actual target text, while translator's note 4 asserted the document used that spelling throughout.

Lesson: "Stage 4 passed" means no governed rule was violated, not that the prose is correct. Report mechanical results with their scope attached; saying "lint green" and stopping invites the reader to hear "verified." And do not let a mechanical pass reduce attention on the editorial pass — the narrower the mechanical coverage, the more the clean-context read is carrying.

Sharpening detail: the miss happened in the same turn as confident reasoning about a linter FALSE POSITIVE (`ฉบับ → รายการ` misfiring on non-counting uses like `ฉบับเต็ม`). Attention was on what the linter wrongly flags, not on what it cannot see. Thinking about a tool's false positives is not the same as thinking about its blind spots, and the first can crowd out the second.

Related: a human edit landing on disk mid-session invalidates your reading of the whole surrounding clause, not just the token that changed. The transposition entered with an edit whose diff showed the correct spelling; the corruption appeared after. Re-read the full sentence after any external edit, and verify a reviewer's finding against the file before acting on it.

---
*Added via Oracle Learn*
