---
title: Iteration boundaries and micro-query discipline for semantic groundtruthing
tags: [notebooklm, semantic-governance, workflow, source-fidelity, architecture, crdb]
created: 2026-07-10
source: /rrr retrospective
---

# Iteration boundaries and micro-query discipline for semantic groundtruthing

When grounding an architecture proposal with NotebookLM, the correct unit of work is an **iteration**, not a single query. One iteration may require several tightly scoped source-bound queries, as long as they all serve one synthesis objective. The mistake is to collapse multiple distinct analytical questions into one broad prompt, because that weakens source fidelity and makes later synthesis harder to audit.

For semantic-governance work specifically, two disciplines matter:

1. **Micro-query discipline**
   - Ask one question per query.
   - Keep the query tied to one evidence objective (e.g. mapping model, metadata mechanism, governance layering, content-change boundary).
   - Save each raw response separately and name it according to the iteration objective.

2. **Vocabulary discipline**
   - Define “iteration” as one round of research ending in synthesis.
   - Define “phase” only for implementation roadmap stages.
   - Keep these terms stable across notes, filenames, and decision logs.

This matters because semantic-groundtruth work is not just about finding supporting quotes. It is about producing an evidence chain that remains understandable when design decisions are later converted into technical specifications, governance notes, or procurement-facing artifacts.

