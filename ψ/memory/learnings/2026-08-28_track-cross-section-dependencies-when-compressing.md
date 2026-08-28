---
id: learning_2026-08-28_track-cross-section-dependencies-when-compressing
type: learning
title: Track cross-section dependencies when compressing a multi-section document for e
concepts: [writing, multi-section-documents, coherence-review, compression, cross-section-dependencies, CRDB]
tags: [writing, multi-section-documents, coherence-review, compression, cross-section-dependencies, CRDB]
created: 2026-08-28
indexed_at: 2026-08-28T17:11:15.265Z
updated_at: 2026-08-28T17:11:15.265Z
hash: sha256:9e73dcf1143689c587c2143baf3a6bc38f52b0bf0bc780a20bfa91b82dc4f144
source: "rrr: REPO"
arra_id: learning_2026-08-28_track-cross-section-dependencies-when-compressing
arra_type: learning
arra_concepts: [writing, multi-section-documents, coherence-review, compression, cross-section-dependencies, CRDB]
arra_created: 2026-08-28T17:11:15.265Z
---

# Track cross-section dependencies when compressing a multi-section document for e

Track cross-section dependencies when compressing a multi-section document for executive-summary altitude. Per-section correctness (mechanical lint, evidence traceability, editorial review) does not guarantee whole-document coherence — a claim cut from one section for length can silently orphan a downstream section's claim that depended on it, and neither section's own review catches it because each is checked against its own contract/source, not against sibling sections. Concrete case: CRDB chapter 3 exec-summary section 3.3 (pilot-test results) compressed 5 systemic gaps down to 2 for length; section 3.4 (recommendations) drafted afterward included a recommendation addressing one of the 3 dropped gaps, which was accurate and traceable to the source document but no longer supported by anything the reader had seen in 3.3's compressed version. Fix: after drafting a batch of sections in sequence, run an explicit full-document coherence read-through before considering the batch done — check whether every later section's claim has a textual anchor earlier in the document, not just in the source material. When compressing a section a later section will build on, either keep the dependency's supporting sentence or flag the cut explicitly so the coherence pass catches it. Generalizes to any drafting-in-sequence workflow: report chapters, multi-part specs, sequential PR descriptions.

---
*Added via Oracle Learn*
