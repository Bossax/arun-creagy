---
id: learning_2026-07-10_iteration-boundaries-and-micro-query-discipline-fo
type: learning
title: Iteration boundaries and micro-query discipline for semantic groundtruthing
concepts: [notebooklm, semantic-governance, workflow, source-fidelity, architecture, crdb]
tags: [notebooklm, semantic-governance, workflow, source-fidelity, architecture, crdb]
created: 2026-07-10
indexed_at: 2026-07-10T09:51:20.544Z
updated_at: 2026-07-10T09:51:20.544Z
hash: sha256:fb612389bb55e412de076312acf742a1264b83bfce675e6d9c2d1829c8911fcc
source: ψ/memory/learnings/2026-07-10_iteration-boundaries-and-micro-query-discipline-for-semantic-groundtruthing.md
project: github.com/sitth/arun_creagy
arra_id: learning_2026-07-10_iteration-boundaries-and-micro-query-discipline-fo
arra_type: learning
arra_concepts: [notebooklm, semantic-governance, workflow, source-fidelity, architecture, crdb]
arra_created: 2026-07-10T09:51:20.544Z
---

# Iteration boundaries and micro-query discipline for semantic groundtruthing

Iteration boundaries and micro-query discipline for semantic groundtruthing

When grounding an architecture proposal with NotebookLM, the correct unit of work is an iteration, not a single query. One iteration may require several tightly scoped source-bound queries, as long as they all serve one synthesis objective. The mistake is to collapse multiple distinct analytical questions into one broad prompt, because that weakens source fidelity and makes later synthesis harder to audit.

For semantic-governance work specifically, two disciplines matter:
1. Micro-query discipline: ask one question per query, keep each query tied to one evidence objective, and save each raw response separately with names aligned to the iteration objective.
2. Vocabulary discipline: define iteration as one round of research ending in synthesis, define phase only for implementation roadmap stages, and keep these terms stable across notes, filenames, and decision logs.

This matters because semantic-groundtruth work is not just about finding supporting quotes. It is about producing an evidence chain that remains understandable when design decisions are later converted into technical specifications, governance notes, or procurement-facing artifacts.

---
*Added via Oracle Learn*
