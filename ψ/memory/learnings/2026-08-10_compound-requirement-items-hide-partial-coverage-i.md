---
id: learning_2026-08-10_compound-requirement-items-hide-partial-coverage-i
type: learning
title: Compound requirement items hide partial coverage in binary match/gap evidence-ma
concepts: [evidence-matching, requirement-analysis, gap-analysis, validation, compound-items]
tags: [evidence-matching, requirement-analysis, gap-analysis, validation, compound-items]
created: 2026-08-10
indexed_at: 2026-08-10T16:31:01.568Z
updated_at: 2026-08-10T16:31:01.568Z
hash: sha256:3b83ec109b0d66cfaa9f8123c2577d217bbbd6b7e2a96c67ec11e7dae7f1256d
source: "rrr: wp4-content-report-and-forward"
arra_id: learning_2026-08-10_compound-requirement-items-hide-partial-coverage-i
arra_type: learning
arra_concepts: [evidence-matching, requirement-analysis, gap-analysis, validation, compound-items]
arra_created: 2026-08-10T16:31:01.568Z
---

# Compound requirement items hide partial coverage in binary match/gap evidence-ma

Compound requirement items hide partial coverage in binary match/gap evidence-matching pipelines. When a requirement item bundles multiple distinct named sub-topics into one line (e.g. "non-economic losses: mental health, biodiversity, cultural heritage"), a matching pass that marks the whole item "matched" the moment any one sub-topic finds a source will badly overstate real coverage. In one case, binary matching reported 39/73 (53%) requirements "matched," but decomposing compound items and re-checking each named sub-topic against its matched asset(s) revealed the true figure was only 20 fully covered (27%), with 19 more only partially covered. This was caught by a human spot-checking individual results against literal requirement text, not by the pipeline itself. Fix: decompose compound/enumerated requirement items into separate matchable sub-units before running the matching pass, not as a follow-up audit after someone catches it by hand. Sibling lesson to "grounding criteria must be independent of what's being scored" — same failure family: a pipeline's aggregate output looks rigorous while a structural blind spot in how items are defined quietly inflates the numbers.

---
*Added via Oracle Learn*
