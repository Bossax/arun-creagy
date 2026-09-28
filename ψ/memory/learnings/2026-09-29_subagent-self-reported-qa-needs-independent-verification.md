---
date: 2026-09-29
type: learning
status: raw
tags: [subagents, qa, lint, thai-writer, writing-th, verification]
source: "rrr: Arun_Creagy"
---

# Learning: a subagent's self-reported QA is not evidence it happened correctly

**Pattern**: When a subagent's own tooling is degraded or unavailable in its execution environment, it will honestly report that degradation ("lint couldn't run, I checked by hand instead") — but the fallback self-check is not reliable just because it's honestly reported. `thai-writer`, dispatched via the `.agents/skills/writing-th` path, has no working Python venv there (excluded by design from that sync mirror), so its own "run lint" step silently degrades to a manual pattern check every time. Across two dispatches in the same session, independently re-running the real linter afterward found violations the manual check missed — including, in one case, a violation the rewrite itself introduced inside text the agent had just described as checked and clean.

**Why this generalizes**: Any time a subagent is asked to both produce work and self-verify that work, the two roles compete under the same context and the same blind spots. An honest "I did X" report describes intent and effort, not ground truth. This is distinct from a subagent lying — it wasn't; it accurately reported that it fell back to a manual check. The gap is that "reported the fallback honestly" and "the fallback caught what it needed to catch" are separate claims, and only the first was actually verified.

**Practical rule**: When a subagent's task includes a verification step (lint, tests, a build), and there's any reason to suspect its environment might not support that step cleanly, independently re-run the real verification yourself afterward rather than trusting the subagent's self-report — even when it reports success, and especially when it reports a fallback. This cost about 15 minutes across two dispatches in this session and caught real, mergeable-report-affecting errors both times.

**Related, same session**: a lexicon rule intended to catch "bare verb directly after รับผิดชอบ" turned out to match any non-"การ" text following it — including prepositions and nouns — producing false positives in the very document being edited. This is the same underlying lesson at the rule-design level: a check that looks correct in isolation needs to be run against real material before being trusted, not just reasoned about.
