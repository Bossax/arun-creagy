---
title: Verify built artifacts against their own plan document, not just general quality bars
date: 2026-08-22
type: learning
status: distilled
tags: [verification, deck-building, self-review, frontend-slides]
source: rrr — dcce-merl-open-issues-synthesis-and-deck
---

## Pattern

When building a deliverable from a written plan (a slide deck plan, a spec, a content outline), checking the built output for general quality — overflow, contrast, readability, no broken layout — is necessary but not sufficient. A slide can pass every visual quality check and still be missing content the plan itself called for, because visual QA and content-completeness QA are different checks.

Concretely: a deck slide was planned to carry three colored cards, each with a term name plus a one-line definition ("a one-line preview of the three functions"). The built slide implemented only the term names — three centered labels on colored bars, no definitions. This rendered cleanly in a PDF export (no overflow, good contrast, readable text) and passed visual review. It was still wrong, and the user caught it, not the builder.

## Why

Visual verification (screenshot/PDF review, overflow checks, contrast checks) answers "does this render correctly." It does not answer "does this say what the plan said it should say." Those require different checks: one against the rendered output, one against the source plan document, side by side, section by section.

## How to apply

After building any deliverable from a written plan, do a second pass that is not visual: open the plan document and the built output side by side, and confirm each planned content element actually appears — not just that the slide/section looks complete. A near-empty-but-well-formatted card is exactly the failure mode that visual QA alone will not catch, because "well-formatted" and "content-complete" are orthogonal properties.

This generalizes beyond decks — any time a written plan or spec precedes the build (a report outline, a form's field list, an API's stated contract), verify against the plan's own text, not just against the artifact's own internal consistency.
