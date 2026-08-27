---
id: learning_2026-08-27_a-writing-quality-harness-must-separate-mechanical
type: learning
title: A writing-quality harness must separate mechanical assurance from editorial assu
concepts: [rrr, writing-th, editorial-quality, semantic-gates, hash-bound-review, source-fidelity, executive-summary, skill-engineering, independent-review]
tags: [rrr, writing-th, editorial-quality, semantic-gates, hash-bound-review, source-fidelity, executive-summary, skill-engineering, independent-review]
created: 2026-08-27
indexed_at: 2026-08-27T18:26:33.676Z
updated_at: 2026-08-27T18:26:33.676Z
hash: sha256:6d5f7882fb9eca2a4fb7ebd0a76bac157906203a150cb522e74f878fc7bbb7c8
source: rrr on 01.25_writing-th-v5-semantic-harness
arra_id: learning_2026-08-27_a-writing-quality-harness-must-separate-mechanical
arra_type: learning
arra_concepts: [rrr, writing-th, editorial-quality, semantic-gates, hash-bound-review, source-fidelity, executive-summary, skill-engineering, independent-review]
arra_created: 2026-08-27T18:26:33.676Z
---

# A writing-quality harness must separate mechanical assurance from editorial assu

A writing-quality harness must separate mechanical assurance from editorial assurance. Literal/regex lint and character-ratio checks can pass drafts that are wrong in scope, unsupported by evidence, overly process-centered, or unsuitable for the reader.

Use this control pattern:
1. Approve a content contract that fixes audience, decision use, section job, altitude, inclusions, exclusions, evidence policy, terminology, and required structures.
2. Classify the transformation as rewrite, synthesis, or new. Apply size heuristics only to comparable rewrites; use semantic preservation review for synthesis.
3. Run mechanical checks and label their verdict honestly.
4. Require independent clean-context editorial review against core and deliverable-specific dimensions. Permit self-review only as visibly degraded assurance.
5. Bind the review receipt to SHA-256 hashes of the exact draft and contract. Any edit invalidates the receipt.
6. Refuse merge for missing/stale receipts, failed dimensions, unresolved critical or major findings, or undisposed mechanical review warnings.
7. Treat a routed skill as a package: synchronize and drift-check every referenced runtime resource, not only SKILL.md.

Validated behavior: an executive-summary draft passed all encoded mechanical rules but an independent reviewer rejected an unsupported institutional conclusion. After revision, the stale receipt failed its hash check; a fresh independent review passed and the merged artifact matched the reviewed draft hash.

---
*Added via Oracle Learn*
