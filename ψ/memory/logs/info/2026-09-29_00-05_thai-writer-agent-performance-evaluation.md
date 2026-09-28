---
date: 2026-09-29 00:05
type: info
status: raw
significance: neutral
---

# thai-writer agent performance evaluation (2026-09-28)

Compared thai-writer's first revise pass (commit `9ce382f`) against Boss's manual edits on top of it (commit `2d18225`), plus two dispatches from the same day: the 68-item table application and the §5.1.5 regrounding restricted to WP6/WP7 sources only.

## What Boss had to fix after thai-writer's rewrite

- Most of the post-rewrite diff was Boss's own new authoring — added subheadings, restructured framing — not corrections to thai-writer's output.
- Real attributable miss #1: terminology consistency. Boss swapped "ขีดความสามารถ" → "ศักยภาพ" by hand in 4+ separate spots; thai-writer didn't catch this as a standing preference and propagate it document-wide.
- Real attributable miss #2: one over-assertion left standing (a claim that ปภ. data "hasn't been verified centrally, which is a precondition for using it" — a causal claim the source didn't support; Boss cut it by hand). This is exactly the certainty-ladder discipline thai-writer is supposed to enforce.
- All the `%%`/`==`/`~~` annotations in the draft were added BY Boss during his own manual restructuring pass, not marks on thai-writer's work — including Boss flagging his own rewritten paragraph as confusing.
- Conclusion: thai-writer's sentence-level voice/fabrication work held up well under review. What needed fixing was standard editorial follow-through, not AI-voice or fact problems.

## Procedural efficiency gaps found

- thai-writer's built-in lint step is silently broken: `.agents/skills/writing-th` has no `.venv` (excluded by design from that sync mirror), so every dispatch falls back to a manual/by-hand style check and reports it as such. Independent lint runs (from the working `.oracle-shared-skills` venv) found violations the manual check missed both times — 5 on the first dispatch, 3 on the second, one of which (`นอกจากนี้`) was a NEW violation the rewrite itself introduced inside text it claimed to have checked by hand. Its self-reported checks aren't reliable without independent verification. Fix: create the `.venv` once at `.agents/skills/writing-th/.venv`.
- The rewrite work surfaced 6 pre-existing `LEXICON_TH.json` false-positive rules this session (ฉบับ scope, ห่วงโซ่ผลกระทบ/อุปทาน exceptions, Governance bilingual-label exception, จุดตัด regex, and a รับผิดชอบ regex that's still too broad — matches any text after รับผิดชอบ that isn't literally "การ", not just bare verbs — produced 4 false positives in one document alone and needs narrowing).
- Grounding discipline was good: the §5.1.5 regrounding (strict two-source-only constraint) made a small surgical diff rather than a wholesale rewrite, correctly removed unsupported facts (CCIC, InVEST) without inventing replacements, and flagged 4 real cross-section conflicts instead of silently resolving them.
- Cost/time asymmetry: the broader 68-item revise pass finished in ~15 min; the narrower, more strictly-grounded §5.1.5 pass took ~80 min for less token volume. Stricter grounding constraints seem to slow deliberation more than scope size does — worth watching if this pattern scales to larger grounded rewrites.

## Action items still open

1. Create the missing `.venv` so lint actually runs in dispatches.
2. Narrow the รับผิดชอบ regex in `LEXICON_TH.json`.
3. Consider whether thai-writer's prompt should include an explicit "apply document-wide terminology consistency" pass step.

Logged via /fyi
