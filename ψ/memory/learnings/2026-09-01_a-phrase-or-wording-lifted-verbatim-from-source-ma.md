---
id: learning_2026-09-01_a-phrase-or-wording-lifted-verbatim-from-source-ma
type: learning
title: A phrase or wording lifted verbatim from source material into newly composed pro
concepts: [writing-th, lexicon-rules, self-authored-prose, fidelity-verification, thai-prose, crdb]
tags: [writing-th, lexicon-rules, self-authored-prose, fidelity-verification, thai-prose, crdb]
created: 2026-09-01
indexed_at: 2026-09-01T10:00:33.864Z
updated_at: 2026-09-01T10:00:33.864Z
hash: sha256:fcbeb529720e8980f51dbfc6810e137d767597ba788749b5be5980f69b1fc959
source: "rrr: crdb-3.2-ex-dfr-merge"
arra_id: learning_2026-09-01_a-phrase-or-wording-lifted-verbatim-from-source-ma
arra_type: learning
arra_concepts: [writing-th, lexicon-rules, self-authored-prose, fidelity-verification, thai-prose, crdb]
arra_created: 2026-09-01T10:00:33.864Z
---

# A phrase or wording lifted verbatim from source material into newly composed pro

A phrase or wording lifted verbatim from source material into newly composed prose is not automatically exempt from lexicon/pattern bans just because it existed in the original. Observed in CRDB full-report §3.2 (merging EX 2.2 + DFR 5.3.2): both source documents used a "ห่วงโซ่ข้อมูล" (data-chain) metaphor that was banned project-wide as of 2026-08-31, except when citing one specific canonical artifact title verbatim. While composing a new merged intro paragraph directly (not through an LLM polishing pass), the phrase was carried over from the source text without checking it against the current lexicon — on the reasoning that "it's already in the original," when the ban applies to the phrase/pattern itself regardless of provenance. The Stage 4 lint gate caught it before it reached the stakeholder, but the check should have happened at authoring time. This is the same underlying failure mode as a related lesson about lexicon swap rules firing on proper nouns inside LLM output, just on the human/self-authoring side rather than the model-output side: a rule doesn't know or care whether the banned phrase came from an LLM's rewrite or from source material being carried forward by the person composing new text. Mitigation: when composing new sentences that borrow phrasing from source material — not just when reviewing a polishing model's output — check that phrasing against the current lexicon/pattern rules before writing it down. Don't treat "preserving the original wording" as automatic license; a wording being original doesn't mean it's still compliant with rules adopted after that source was written. A lint/gate safety net catching the violation after the fact is not a substitute for checking at authoring time — relying on it works, but the correction cost lands later than it needs to.

---
*Added via Oracle Learn*
