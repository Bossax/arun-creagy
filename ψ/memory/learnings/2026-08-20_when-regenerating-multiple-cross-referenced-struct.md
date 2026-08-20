---
id: learning_2026-08-20_when-regenerating-multiple-cross-referenced-struct
type: learning
title: "When regenerating multiple cross-referenced structured documents (e.g. a set of"
concepts: [scripting, data-integrity, csv, delta-regeneration, verification, ncaif, crdb]
tags: [scripting, data-integrity, csv, delta-regeneration, verification, ncaif, crdb]
created: 2026-08-20
indexed_at: 2026-08-20T11:00:41.249Z
updated_at: 2026-08-20T11:00:41.249Z
hash: sha256:0eef081c5d3566dfa31f5c85a814bd55252732ce11b6f8e7263376c9e87a73b9
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-20_when-regenerating-multiple-cross-referenced-struct
arra_type: learning
arra_concepts: [scripting, data-integrity, csv, delta-regeneration, verification, ncaif, crdb]
arra_created: 2026-08-20T11:00:41.249Z
---

# When regenerating multiple cross-referenced structured documents (e.g. a set of

When regenerating multiple cross-referenced structured documents (e.g. a set of CSVs where rows in one file reference IDs in another — requirements -> deliverables -> data-specs -> assets-cited), write the delta as a small Python script rather than hand-editing each file. Scripting caught two real bugs a hand-edit would likely have missed: a CSV-escaping error (unquoted commas breaking column alignment) and an orphaned reference (a data-spec row pointing at a requirement that had just been removed elsewhere). It also made referential-integrity verification mechanical via an independent check script, rather than trusting careful reading alone. Distinct from prose documents (storyboards, delta notes) where hand-editing is still the right tool since there's no cross-reference integrity to check.

Related: when a plan document describes a "disagreement between two documents," read both documents' actual text before assuming the disagreement lives where the plan says it does. In this session the plan attributed a discrepancy to a DRD-vs-Storyboard disagreement, but the actual contradiction was entirely internal to the Storyboard (one section disagreed with another section of itself). Trusting the plan's framing without re-reading the source would have led to fixing the wrong thing.

---
*Added via Oracle Learn*
