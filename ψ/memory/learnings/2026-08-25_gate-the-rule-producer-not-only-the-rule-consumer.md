---
id: learning_2026-08-25_gate-the-rule-producer-not-only-the-rule-consumer
type: learning
title: "Gate the rule producer, not only the rule consumer."
concepts: [harness-engineering, writing-th, style-capture, validation, determinism, lexicon-schema, over-claiming]
tags: [harness-engineering, writing-th, style-capture, validation, determinism, lexicon-schema, over-claiming]
created: 2026-08-25
indexed_at: 2026-08-25T12:25:22.409Z
updated_at: 2026-08-25T12:25:22.409Z
hash: sha256:6d979347cbd58a3e0da4d76b174074be93d39a7e5abd58d38a8b82b311e0883e
source: "rrr: Arun_Creagy"
project: github.com/bossax/arun_creagy
arra_id: learning_2026-08-25_gate-the-rule-producer-not-only-the-rule-consumer
arra_type: learning
arra_concepts: [harness-engineering, writing-th, style-capture, validation, determinism, lexicon-schema, over-claiming]
arra_created: 2026-08-25T12:25:22.409Z
---

# Gate the rule producer, not only the rule consumer.

Gate the rule producer, not only the rule consumer.

In a learning loop where one skill writes rules and another enforces them, an ungated producer is where silent failure lives. In writing-th, style-capture writes LEXICON_*.json and lint_thai_writing.py enforces it. The enforcer had hard exit-code gates; the producer had no validation at all.

Consequence, verified by running the code: the 2026-08-05 capture round added five rules and three could never fire. They were structural rules ("no quoted English codename", "ปิด is not a completion verb") whose English descriptions were written into a `banned` field the linter compiles as regex. `ปิด[ผลงาน/deliverable]` compiled the brackets as a character class and matched nothing. A fourth rule's prescribed replacement contained its own banned string, making the skill's rerun-until-exit-0 instruction non-terminating.

Root cause was the data model, not carelessness. The schema had exactly one rule kind (literal string). style-capture kept discovering structural rules, had nowhere to put them, and wrote descriptions into the literal field.

Fix: every entry declares `kind` (literal | regex | structural) and `scope` (universal | report | article | letter); regex entries carry an explicit `pattern`. validate_lexicon.py runs on the producing side and rejects a literal containing regex metacharacters or an ellipsis, a rule whose `preferred` contains its own `banned` string, and duplicates. Against the pre-fix lexicon it flags seven malformed entries. Rules no pattern can express become kind:structural, reported for review and never blocking, which states coverage honestly instead of implying enforcement.

Transferable rule: whenever skill A writes data that skill B enforces, put a validator on A. The consumer being strict is not protection — it is what makes a malformed rule invisible, because a rule that can never match is silently accepted. Prefer regex where a sound pattern exists; reserve structural for rules no pattern can express, since marking a rule structural removes it from script enforcement.

This is the 2026-04-02 over-claiming failure in a new form: a stage named "Deterministic Validation" enforcing roughly a tenth of the style pack.


## Related

- [[2026-04-02_writing-th-foresight-style-pack-governance]] — never overstate condensation
- [[2026-06-27_crdb-writing-workflow-best-practice]] — promote a pattern after it fails twice
- [[2026-07-01_style-pack-compliance-workflow-running-drafts-t]] — scripted sweep plus manual polish

---
*Added via Oracle Learn*
