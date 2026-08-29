---
id: learning_2026-08-29_before-proposing-to-fix-an-enforcement-gap-by-addi
type: learning
title: "Before proposing to fix an enforcement gap by adding a rule to a config file, ch"
concepts: [verification, code-review, false-assumption, writing-th, lexicon, gate-enforcement]
tags: [verification, code-review, false-assumption, writing-th, lexicon, gate-enforcement]
created: 2026-08-29
indexed_at: 2026-08-29T08:07:02.776Z
updated_at: 2026-08-29T08:07:02.776Z
hash: sha256:f8fd7cae812008e80945b85375c002f43f8a73efd99047ecaa897613388dbb89
source: "rrr: writing-th-v6-build-and-verification"
arra_id: learning_2026-08-29_before-proposing-to-fix-an-enforcement-gap-by-addi
arra_type: learning
arra_concepts: [verification, code-review, false-assumption, writing-th, lexicon, gate-enforcement]
arra_created: 2026-08-29T08:07:02.776Z
---

# Before proposing to fix an enforcement gap by adding a rule to a config file, ch

Before proposing to fix an enforcement gap by adding a rule to a config file, check what the enforcing code itself actually matches -- not just what its configuration declares. During the writing-th v6.0 build, a plan named two lexicon patterns to promote based on reading LEXICON_TH.json and STYLE_PACK_TH.md's capture log, which discussed the patterns extensively without them appearing as lexicon entries. Testing before shipping revealed a hardcoded regex in lint_thai_writing.py's matcher had been catching exactly this pattern family all along (tracked in the miss register under a different label, 4 historical hits) -- the lexicon addition was pure duplication, reverted once discovered. Absence from a config file is not proof of absence from enforcement; a rule-based system often has bootstrapped, pre-configuration logic for its earliest or most important rules.

---
*Added via Oracle Learn*
