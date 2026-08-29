# Lesson: fork vs. fresh subagent for content-isolated harness stages

A harness stage's "must never load X" rule is a boundary on **what content
enters that stage's context**, not automatically a requirement that the stage
run in a freshly-booted subagent. These are separable, and conflating them is
expensive.

Concretely, in the writing-th v6 harness: `th-argument-mapper` and
`th-verbalizer` must never load `STYLE_PACK_TH.md`, `LEXICON_TH.json`, or the
editorial rubric — but that's a content rule. If the orchestrating session's own
context never contained that material either, a `fork` (which inherits the
parent's context and shares its prompt cache, at the cost of always running on
the parent model) satisfies the rule just as well as a cold `Agent()` call, and
does so without re-reading large source files, the writing plan, and prior
drafts from scratch on every call.

`th-editorial-reviewer` is genuinely different: its independence requirement is
about not seeing *the drafting agent's own reasoning and self-justification* —
exactly what a fork inherits by design. That stage must stay a fresh, non-fork
call, always.

**Why this matters**: a session that ran eight Stage-1/Stage-3 subagent calls as
cold `Agent()` spawns — following the harness's own canonical invocation
pattern uncritically — burned an account's 5-hour usage window with Stage 5 and
Stage 6 still unrun. A same-day comparison session doing equivalent work at far
lower cost turned out to have bought its savings by running *every* stage
in-line, including Stage 5 — which broke reviewer independence, the one thing
that stage exists to guarantee. Neither the "always fresh" nor the "always
in-line" pattern is correct by default. The fork/fresh split by stage is.

**How to apply**: before treating a documented content-isolation boundary as
justification for a fresh subagent, check what the *orchestrating* context
already contains. If it's clean of the forbidden material, fork is available
and cheaper. If the orchestrator has read the forbidden material for its own
reasoning (e.g., explaining a rubric to a user), that specific run must fall
back to a fresh call and say so — the precondition is checked per-run, not
assumed to hold globally. Never extend this reasoning to a stage whose
isolation requirement is about *provenance of reasoning* rather than content
category (like an independent reviewer) — that one stays fresh unconditionally.
