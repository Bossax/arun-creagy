---
id: learning_2026-09-01_before-creating-any-new-artifact-at-a-path-with-se
type: learning
title: "Before creating any new artifact at a path with session/batch history (e.g. a wr"
concepts: [workflow-discipline, multi-session-pipeline, drafting-workflow, writing-th, near-miss]
tags: [workflow-discipline, multi-session-pipeline, drafting-workflow, writing-th, near-miss]
created: 2026-09-01
indexed_at: 2026-09-01T03:03:27.787Z
updated_at: 2026-09-01T03:03:27.787Z
hash: sha256:8a47cdabd0edf06fb7f078cad3e3968d9402197958ebc2132c6c33a7d542f5e3
source: "rrr: CRDB full-report §2.3 Stage 0-3 session (grounds enrichment + subargument split)"
arra_id: learning_2026-09-01_before-creating-any-new-artifact-at-a-path-with-se
arra_type: learning
arra_concepts: [workflow-discipline, multi-session-pipeline, drafting-workflow, writing-th, near-miss]
arra_created: 2026-09-01T03:03:27.787Z
---

# Before creating any new artifact at a path with session/batch history (e.g. a wr

Before creating any new artifact at a path with session/batch history (e.g. a writing-contract.json in a multi-session drafting pipeline), list or check that location first, as a default habit rather than one triggered by suspicion. A planning document (spine doc, writing plan) describes intended work, not necessarily what has already executed — in a project where sessions hand off to each other, the target directory's actual file state is the authoritative record of what's done, not the plan. Composing a new artifact from requirements alone risks overwriting a human-approved file (with meaningful state like approval.status) or producing a silent duplicate the human then has to notice and reconcile. Generalizes to any "produce artifact X at path Y" task in a system with iterative/staged history at Y: inspect Y's current state first, don't compose X from requirements alone.

---
*Added via Oracle Learn*
