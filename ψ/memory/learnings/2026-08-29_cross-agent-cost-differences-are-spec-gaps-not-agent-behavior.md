---
title: Cross-agent cost differences are usually spec gaps, not agent behavior differences
date: 2026-08-29
tags: [writing-th, orchestration, subagent-cost, skill-design, harness-architecture]
concepts: [fork-vs-fresh-subagent, execution-tiering, content-isolation-vs-reasoning-isolation]
---

## The pattern

Two agents (Claude Code, Antigravity) ran the same `writing-th` skill on
comparable work and produced wildly different token costs — one burned an
entire 5-hour quota, the other used roughly half the tokens for a similar
batch. The first instinct was to explain this as a difference in how the two
agents "behave." That framing was wrong.

Reading `references/subagent-prompts.md` §3 directly showed both platforms'
documented invocation pattern was identical in kind: fresh-spawn only, for
every stage, on both platforms. Neither agent's behavior was a platform quirk —
one agent (Claude Code) followed the documented spec literally and paid its
full cost; the other (Antigravity) silently deviated from its own documented
spec to save cost, and in doing so broke the one isolation guarantee
(Stage 5 reviewer independence) the spec existed to protect.

## The generalizable lesson

When two agents running the same instructions produce very different outcomes,
check the actual instruction text before attributing the difference to agent
capability or agent judgment. A spec that never distinguishes *why* an
isolation requirement exists (content-boundary vs. reasoning-independence) will
get satisfied differently by different agents, and both satisfactions can be
individually defensible while still being wrong in different directions.

## The concrete fix pattern

Once the underlying isolation requirement was named precisely — "must never
load certain content" (Stage 1/3) vs. "must never see the drafting agent's own
reasoning" (Stage 5) — the fix followed directly: stages in the first category
can safely `fork` or even run inline in the orchestrator (a fork inherits
context and shares cache but keeps output out of the parent); the stage in the
second category can never fork or run inline, full stop, regardless of cost
pressure. This is now written into `writing-th`'s SKILL.md and
`subagent-prompts.md` as an explicit three-tier table (small/medium/large batch
→ inline/fork/fork, always-fresh for the reasoning-isolated stage).

## Where this generalizes

Any harness or skill with a documented "must never load X" restriction for a
subagent should distinguish, in the spec itself, whether X is being restricted
because it's the wrong *content* for that stage's job, or because the stage's
entire value depends on not inheriting the *reasoning* of a prior stage. Only
the second kind justifies a hard "always fresh, never fork, never inline" rule
regardless of cost. Conflating the two — as the pre-2026-08-29 `writing-th` spec
did, uniformly requiring fresh spawns everywhere — either overpays (follow it
literally) or invites an ungoverned workaround that quietly breaks the one
case that actually mattered (deviate from it under cost pressure).

See also: `ψ/memory/retrospectives/2026-08/29/22.56_crdb-ch4-revision-mode-and-quota-burn.md`
(the cost postmortem that started this), `ψ/memory/retrospectives/2026-08/29/23.44_writing-th-execution-tier-upgrade.md`
(this session's implementation), and `ψ/inbox/2026-08-29_writing-harness-skill-architecture-analysis.md`
§9 (the original "never fork for the reviewer" design note that this session
found was narrower than either agent's actual behavior).
