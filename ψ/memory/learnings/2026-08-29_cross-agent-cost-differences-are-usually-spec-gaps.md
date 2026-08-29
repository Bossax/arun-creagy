---
id: learning_2026-08-29_cross-agent-cost-differences-are-usually-spec-gaps
type: learning
title: "Cross-agent cost differences are usually spec gaps, not agent behavior differenc"
concepts: [writing-th, subagent-orchestration, fork-vs-fresh, harness-design, token-efficiency, content-isolation-vs-reasoning-isolation]
tags: [writing-th, subagent-orchestration, fork-vs-fresh, harness-design, token-efficiency, content-isolation-vs-reasoning-isolation]
created: 2026-08-29
indexed_at: 2026-08-29T16:46:30.423Z
updated_at: 2026-08-29T16:46:30.423Z
hash: sha256:7a287d180cbc95d8c9e4da89ebd5a77fe83ad95cfd906acd98ee24450cc661e2
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-29_cross-agent-cost-differences-are-usually-spec-gaps
arra_type: learning
arra_concepts: [writing-th, subagent-orchestration, fork-vs-fresh, harness-design, token-efficiency, content-isolation-vs-reasoning-isolation]
arra_created: 2026-08-29T16:46:30.423Z
---

# Cross-agent cost differences are usually spec gaps, not agent behavior differenc

Cross-agent cost differences are usually spec gaps, not agent behavior differences. Two agents (Claude Code, Antigravity) ran the same writing-th skill and produced very different token costs — one burned an entire 5-hour quota, the other used roughly half. Reading the actual invocation spec (subagent-prompts.md) showed both agents were following/deviating-from the SAME underspecified rule: fresh-spawn-only for every stage, on both platforms, with no distinction between "must never load certain content" isolation (Stage 1/3 argument-mapper and verbalizer) and "must never see the drafting agent's own reasoning" isolation (Stage 5 editorial-reviewer). One agent followed the expensive spec literally; the other deviated from it to save cost and silently broke Stage 5 independence, the one guarantee the spec existed to protect. Fix: name the isolation requirement precisely per stage. Content-isolated stages can safely fork (inherits context, shares cache, keeps output out of parent) or even run inline in the orchestrator for small batches. Reasoning-isolated stages must always be fresh, non-fork, non-inline subagent calls, regardless of cost pressure or batch size. Implemented as a three-tier (small/medium/large batch) execution table in writing-th SKILL.md v6.2.0.

---
*Added via Oracle Learn*
