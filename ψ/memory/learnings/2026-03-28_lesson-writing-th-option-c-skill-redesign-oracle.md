# Lesson — writing-th Option C skill redesign (Oracle-aligned)

## Pattern

When the user wants Thai drafting that can closely mimic a specific “example report” style **without losing** the Oracle’s stable voice and safety rules, use a layered style system:

1) Example report (session reference) is PRIMARY for terminology + section flow.
2) Write a timestamped Session Style Pack Summary into the writing plan (append-only).
3) Apply resonance as safety rails (citations, hedging, no hallucinated sources).
4) Store evolving improvements as learnings; promote stable rules to resonance only after repetition or explicit approval.

## Execution / learning separation

- [`/writing-th`](.roo/skills/writing-th/SKILL.md) handles MCP-first retrieval, session style-pack summary, outline-stop, drafting.
- [`/writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md) handles draft-vs-edited pattern extraction and durable learning notes.

## Operational guardrail

`oracle_learn()` may report success but the file can be missing on disk.

- Verify and materialize per: [`ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md`](ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md)

