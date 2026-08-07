---
type: lesson-learned
date: 2026-08-07
project: DCCE_CRDB
tags: [debate-then-synthesize, agent-orchestration, reflection-lock, preview-gate]
---

# Lesson: A preview-before-write gate surfaces reuse opportunities no single agent in the pipeline can know about

## Context

Ran a structured decision process for CRDB's final-sprint deliverable pack: two persona subagents argued opposite sides of a scoping question (close standards-alignment gaps broadly vs. concentrate narrowly on 2 priority use cases), then a third agent on a different model synthesized their arguments into concrete options, then the orchestrating session presented a preview of exactly how the plan would change before writing anything to disk.

## What happened

Both debate agents scoped WP2's gap-closing work as new field-level Source-to-Target Mapping work — differing only in how much of the catalog to cover. Neither agent knew that an existing A-BTR dissection database (135 themes, 379 requirement statements, already extracted and structured) could ground a much cheaper "domain highlight" instead of new STM authoring. That reuse opportunity only surfaced when Boss saw the WP-by-WP preview and pushed back with domain knowledge specific to this project's history — knowledge that wasn't in either agent's prompt because the orchestrator didn't think to include it either.

## The pattern

Neither the debate agents nor the synthesis agent could reuse an artifact they were never told about. Fresh subagents only know what's in their prompt; the orchestrator only knows what's already surfaced in the conversation. A gap between "what exists in the project" and "what's in context for this decision" is invisible until a human with full project history reviews a concrete, specific preview — not an abstract options list. The options list ("Two and Done" vs "Standards Architect Unbounded") was abstract enough that the STM-vs-domain-highlight substitution didn't occur to anyone; the WP-by-WP table, which named "STM row-set for 4-8 rows," was concrete enough to trigger the objection.

## Why it matters

This argues for treating "show the plan before writing" as a discovery mechanism, not just an approval gate. The value isn't just catching mistakes — it's giving the human a concrete enough artifact that their own tacit knowledge (which files already exist, which shortcuts are available) has something specific to react to. An abstract summary doesn't trigger that; a table naming exact WPs, exact artifact types, and exact scope does.

## How to apply

When orchestrating a debate-then-synthesize flow (or any multi-agent research/decision pipeline), don't let the synthesis output go straight to disk or straight into an irreversible next step. Surface a concrete, specific preview of what the decision implies in practice — named files, named work packages, named scope boundaries — before committing. The more specific the preview, the more likely it triggers a human's "wait, we already have X for that" correction. This is separate from (and a good complement to) explicit reflection-lock gates that block state-changing writes pending confirmation — this lesson is about the *content* of what gets previewed, not just the mechanical pause before writing.

## Related

- [[project_crdb_wp6_use_case_selection]]
