---
id: learning_2026-08-22_when-building-a-deliverable-from-a-written-plan-a
type: learning
title: "When building a deliverable from a written plan (a slide deck plan, a spec, a co"
concepts: [verification, deck-building, self-review, frontend-slides, plan-adherence]
tags: [verification, deck-building, self-review, frontend-slides, plan-adherence]
created: 2026-08-22
indexed_at: 2026-08-22T15:17:08.069Z
updated_at: 2026-08-22T15:17:08.069Z
hash: sha256:bdd9ffd1bdea1d03b646cc8276c5cd8d3dc51ec1c14ae4171d425e2b09192fe0
source: "rrr: dcce-merl-open-issues-synthesis-and-deck"
arra_id: learning_2026-08-22_when-building-a-deliverable-from-a-written-plan-a
arra_type: learning
arra_concepts: [verification, deck-building, self-review, frontend-slides, plan-adherence]
arra_created: 2026-08-22T15:17:08.069Z
---

# When building a deliverable from a written plan (a slide deck plan, a spec, a co

When building a deliverable from a written plan (a slide deck plan, a spec, a content outline), checking the built output for general quality — overflow, contrast, readability, no broken layout — is necessary but not sufficient. A slide can pass every visual quality check and still be missing content the plan itself called for, because visual QA and content-completeness QA are different checks. Concretely: a deck slide was planned to carry three colored cards, each with a term name plus a one-line definition. The built slide implemented only the term names — three centered labels, no definitions. This rendered cleanly (no overflow, good contrast) and passed visual review. It was still wrong, and the user caught it, not the builder. After building any deliverable from a written plan, do a second pass that is not visual: open the plan document and the built output side by side, and confirm each planned content element actually appears. This generalizes beyond decks to any build preceded by a written plan or spec.

---
*Added via Oracle Learn*
