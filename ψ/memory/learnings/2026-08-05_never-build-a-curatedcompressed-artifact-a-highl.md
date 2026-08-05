---
id: learning_2026-08-05_never-build-a-curatedcompressed-artifact-a-highl
type: learning
title: "Never build a curated/compressed artifact (a highlight-reel selection, a \"top N\""
concepts: [curation, context-memory, selection-bias, matching-heuristics, timeline-th]
tags: [curation, context-memory, selection-bias, matching-heuristics, timeline-th]
created: 2026-08-05
indexed_at: 2026-08-05T10:06:08.572Z
updated_at: 2026-08-05T10:06:08.572Z
hash: sha256:85b3a9282a9d2129f9371e74cfe93e45ff2d66323d4abace79978140ab8aafcb
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-05_never-build-a-curatedcompressed-artifact-a-highl
arra_type: learning
arra_concepts: [curation, context-memory, selection-bias, matching-heuristics, timeline-th]
arra_created: 2026-08-05T10:06:08.572Z
---

# Never build a curated/compressed artifact (a highlight-reel selection, a \"top N\"

Never build a curated/compressed artifact (a highlight-reel selection, a "top N" summary) from memory of an earlier read in the same conversation — re-read the source fresh. A full-detail render can survive an incomplete memory undetected (the reader still sees everything); a "pick the important subset" pass cannot — it systematically misses whatever category wasn't salient in memory at write time, with no signal that anything is missing. Concrete instance: building a curated ~27-event project timeline from memory of a 35-row Change-Log table instead of re-reading the full 72-entry manifest + 85-row Deliverable-Map silently dropped an entire evidence-gathering layer (compliance work, interviews, workshops) because the implicit selection criterion ("has a matching decision row") structurally couldn't see deliverables sealed without a dated decision. Related: a single-exact-heading match ("Files Modified") missed a real session using a different heading ("Verified Shipped Assets") for the same content — same root cause, treating an author-chosen label or a remembered subset as a stable schema. Fix: before any compression/selection step, re-read source fresh rather than reasoning from context memory; if delegating to a subagent, say "re-read X" explicitly in the briefing rather than assuming inherited memory suffices.

---
*Added via Oracle Learn*
