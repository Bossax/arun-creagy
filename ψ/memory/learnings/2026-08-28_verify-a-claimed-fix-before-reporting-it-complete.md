---
id: learning_2026-08-28_verify-a-claimed-fix-before-reporting-it-complete
type: learning
title: "Verify a claimed fix before reporting it complete — a tool call returning succes"
concepts: [verification, self-correction, editorial-review, writing-th, multi-round-revision]
tags: [verification, self-correction, editorial-review, writing-th, multi-round-revision]
created: 2026-08-28
indexed_at: 2026-08-28T01:59:02.372Z
updated_at: 2026-08-28T01:59:02.372Z
hash: sha256:223eb6e2bd1450a7531f24f5f0d3d007515990d5a23736b0395cd30723806a83
source: "rrr: exec-summary-1.2-four-pass-review"
arra_id: learning_2026-08-28_verify-a-claimed-fix-before-reporting-it-complete
arra_type: learning
arra_concepts: [verification, self-correction, editorial-review, writing-th, multi-round-revision]
arra_created: 2026-08-28T01:59:02.372Z
---

# Verify a claimed fix before reporting it complete — a tool call returning succes

Verify a claimed fix before reporting it complete — a tool call returning success is not evidence the intended semantic change landed everywhere it needed to.

Context: drafting CRDB exec-summary §1.2 through /writing-th's independent-review gate. Told the reviewer a term-consistency fix was applied across all 4 occurrences in the section; only 2 of 4 had actually been changed. In the same revision round, "fixed" a flagged false superlative by substituting a comparison without tracing what the comparison's reference class contained, producing a circular claim (comparing two items to a class consisting only of those same two items).

Fix that worked: for multi-site text changes, do a global/all-occurrences replace rather than editing by hand at each site, then immediately grep for the old pattern with a boundary check and confirm zero matches — only then report the fix as done. For substitutions that add a new comparison or qualifier (not just renaming), explicitly re-derive what the comparison's reference class contains before asserting an extremum/superlative against it.

Generalizes to any multi-round correction loop (code review fixes, lint cleanup, find-and-replace across a document) where a reviewer checks the claim against actual state rather than the report. Reusing the same reviewer/agent across revision rounds (rather than a fresh one each time) helps here — it can track which of its own prior findings were resolved vs. only partially addressed, catching an incomplete "fixed" claim that a fresh reviewer might not notice as a regression.

---
*Added via Oracle Learn*
