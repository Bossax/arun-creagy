# A green mechanical gate certifies governed patterns, not correctness

**Date**: 2026-09-11
**Source**: GGA targets Thai translation, writing-th harness
**Concepts**: quality-gates, linting, review-design, thai-writing, false-assurance

## What happened

`lint_thai_writing.py` passed the GGA translation twice while target 9(g) contained
`ความรู้ของชนพื้นเผ่าเมือง` — a syllable transposition of the contract-locked term
`ชนเผ่าพื้นเมือง`. The independent Stage 5 reviewer caught it on a clause-by-clause
read against the English source.

The linter was not broken. It governs terms listed in `LEXICON_TH.json` plus
structural patterns. `ชนเผ่าพื้นเมือง` is not a lexicon entry, so no rule was
watching it, and a transposed Thai compound is not a pattern the tokenizer treats
as anomalous.

The typo also falsified its own documentation: that was the only occurrence of the
term in actual target text, and translator's note 4 asserted the document used
that spelling throughout.

## The lesson

"Stage 4 passed" means *no governed rule was violated*. It does not mean the prose
is correct. Two consequences:

1. **Report mechanical results with their scope attached.** Saying "lint green" and
   stopping invites the reader — and the next session — to hear "verified."
2. **Do not let a mechanical pass reduce attention on the editorial pass.** The
   inverse is true: the narrower the mechanical coverage, the more the clean-context
   human-or-agent read is carrying.

A sharpening detail: the miss happened in the same turn as confident reasoning
about a linter *false positive* (`ฉบับ → รายการ` misfiring on non-counting uses).
Attention was on what the linter wrongly flags, not on what it cannot see. Thinking
carefully about a tool's false positives is not the same as thinking about its
blind spots, and the first can crowd out the second.

## Related

- A human edit landing on disk mid-session invalidates your reading of the whole
  surrounding clause, not just the token that changed. The transposition entered
  with an edit whose diff showed the correct spelling; the corruption appeared
  after. Re-read the full sentence after any external edit.
- See `[[feedback_ask_rationale_before_style_merge]]` — holding the review to ask
  why the edit was made was correct, but the question narrowed attention to the
  term being asked about.

## How to apply

- When reporting a passing mechanical gate, name what it covers.
- After any external edit to a draft under review, re-read the affected clause in
  full before advancing a stage.
- Verify a reviewer's finding against the file before acting on it — done correctly
  here, and worth keeping as habit.
