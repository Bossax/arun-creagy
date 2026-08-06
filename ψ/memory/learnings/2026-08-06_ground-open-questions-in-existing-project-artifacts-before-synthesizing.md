---
title: Ground "it depends" answers in existing project artifacts before synthesizing new ones
tags: [crdb, research-discipline, trace-skill, oracle-search, governance, workflow]
created: 2026-08-06
source: /rrr retrospective — CRDB WP1 Groups C-E closure
---

# Ground "it depends" answers in existing project artifacts before synthesizing

When a stakeholder question resists a confident direct answer (e.g. "what governance
maturity model should we propose, given the framework is only room-accepted and the
adoption pace is DCCE's own call?"), the instinct is to synthesize a plausible-sounding
framework from first principles. That's the wrong first move on a long-running project.

**The correct order:**
1. `oracle_search` (or equivalent fast keyword/vector search) across the project's own
   memory/learnings/output first — cheap, fast, catches anything already indexed.
2. If that comes back thin, escalate to a deeper search (the `/trace` skill, or targeted
   `Grep` across the project's own output folders) — but treat the skill's prescribed
   heavy mode (e.g. 5 parallel subagents) as *one option*, not mandatory, when a cheaper
   targeted search over a known local directory tree can answer the same question. If you
   substitute a lighter method, say so explicitly rather than silently deviating.
3. Only synthesize fresh if steps 1–2 genuinely find nothing.

In this session, step 2 (a handful of targeted Greps instead of the skill's default
5-agent deep mode) found `Proposed-governance-plan-to-DCCE.md` — a 2-phase governance
roadmap CRDB had already drafted and DCCE had already partially referenced (FGD3 Slide 23).
This was strictly better than any freshly-synthesized maturity model: it was already
grounded, already partially socialized with the client, and reusing it kept the new
rationale document's citation trail honest (pointing to a real prior artifact, not an
invented framework dressed up as one).

**Why this matters beyond this one case:** on long-running consulting-style projects,
the highest-value answer to "what should we do here" is very often "here's what we
already proposed/decided, restated in this new context" — not a new synthesis. Treating
every open question as a blank-slate design problem wastes the project's own prior work
and risks producing inconsistent recommendations across different deliverables.

**How to apply:** whenever a rationale/strategy document hits an "it depends" question,
search the project's own artifact history before drafting an answer — especially in
folders explicitly named for the relevant domain (here, `Governance_RACI/`).
