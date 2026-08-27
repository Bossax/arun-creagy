# Lesson: Gates Check Mechanics, Not Quality — and a Correction Applies to the Whole Document

**Source**: CRDB exec-summary multi-agent writing pipeline pilot (บทนำ + 1.1), 2026-08-27–28. Full narrative: `ψ/memory/retrospectives/2026-08/28/00.48_exec-summary-sourcing-and-multiagent-pilot.md`.

## The pattern

A three-stage writing pipeline (English content draft → Thai style rewrite → structural benchmark) was piloted on two sections of a Thai executive summary. Every automated gate passed (`lint_thai_writing.py`, `check_density.py`) at every stage, and the work was still rated 2/10 by the human reviewer. Across five separate correction rounds, the human caught defects the gates structurally could not detect:

1. Scope drift into full-report depth despite an explicit exclusion in the brief.
2. Internal process artifacts (slide citations, an arrow-chain diagram rendered as prose, section-roadmap meta-commentary) leaking into reader-facing text.
3. A bare English acronym the human had already eliminated in their own edit of a different section of the same document — not generalized by the agent.
4. Reflexive avoidance of list formatting, from over-applying a benchmark note about a different problem (numbered-enumeration-as-rhetorical-hook).
5. Substance lost during a scope-trim (whole paragraphs cut to remove one bad phrase).

Only after the fifth round did the fix change shape: instead of patching each symptom, two of the recurring corrections were converted into real `LEXICON_TH.json` entries (`kind: literal`/`kind: regex`) that block mechanically at Stage 5, and the judgment-call corrections were written into a `## 10` requirements section added directly to the project's writing-plan document, which `/writing-th` Stage 0 reads before drafting.

## Why this matters generally

- **Lexicon/lint gates check narrow mechanical things** (banned terms, character-count ratios) — they cannot detect scope-appropriateness, structural completeness, citation-type appropriateness, or formatting choices. Treating "gates passed" as "this is done" is a category error every time a quality bar includes dimensions outside what the gate measures.
- **A correction made in one section of a document is evidence about the whole document, not just the spot it was caught.** When a human eliminates a pattern in their own edit, the correct next action is checking the rest of the document immediately (a grep is nearly free), not waiting for the same correction to be repeated elsewhere.
- **A lesson learned from one failure mode can be over-applied to suppress an unrelated, legitimate pattern** if the underlying mechanism isn't understood — "reduce numbered-enumeration-as-rhetorical-hook" and "avoid list formatting" are different instructions that got conflated.
- **The strongest fix for a recurring correction is one that doesn't rely on remembering it** — convert pattern-matchable lessons into `kind: literal`/`kind: regex` gate rules; reserve prose-only capture-log entries and brief-document additions for genuine judgment calls a script cannot make.

## Concepts

writing-pipeline, quality-gates, style-capture, generalization, self-review, CRDB
