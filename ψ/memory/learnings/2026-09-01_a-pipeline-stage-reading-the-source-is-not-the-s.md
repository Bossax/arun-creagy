---
id: learning_2026-09-01_a-pipeline-stage-reading-the-source-is-not-the-s
type: learning
title: "A pipeline stage \"reading the source\" is not the same claim as \"detail survived"
concepts: [pipeline-design, fidelity, compression, drafting-workflow, writing-th, lint-false-positive]
tags: [pipeline-design, fidelity, compression, drafting-workflow, writing-th, lint-false-positive]
created: 2026-09-01
indexed_at: 2026-09-01T01:33:14.405Z
updated_at: 2026-09-01T01:33:14.405Z
hash: sha256:555d54104acfdcba6d70e659d5163f47012a8b5707038b7e59404ea4cc2f1c50
source: "rrr: CRDB full-report §2.2 R-reclassification and lane-split drafting session"
arra_id: learning_2026-09-01_a-pipeline-stage-reading-the-source-is-not-the-s
arra_type: learning
arra_concepts: [pipeline-design, fidelity, compression, drafting-workflow, writing-th, lint-false-positive]
arra_created: 2026-09-01T01:33:14.405Z
---

# A pipeline stage \"reading the source\" is not the same claim as \"detail survived

A pipeline stage "reading the source" is not the same claim as "detail survived to the output." When a stage compresses evidence into a structured intermediate (e.g. an argument map's `grounds` field), downstream stages working only from that intermediate inherit the compression, not the original document's fidelity -- no matter how thoroughly the earlier stage read the source. Fix: split drafting into two lanes rather than one compress-then-regenerate pass -- Lane A polishes existing full-report-altitude prose whole, word-level only (no resynthesis); Lane B verbalizes genuinely new content from the approved intermediate. Merge the two lanes manually (human), never with a second AI stitching pass -- a stitching pass would need to re-read both lanes' raw sources to reconcile them, which reopens exactly the raw-source access the intermediate's approval boundary exists to prevent (excluded content could leak back in via the lane touching raw sources). Secondary: keep review/verification annotations in a separate file from actual content -- embedded meta-commentary like "paragraph N flagged" can false-trigger content-scoped lint rules (e.g. an internal-document-locator ban matching "para N" patterns).

---
*Added via Oracle Learn*
