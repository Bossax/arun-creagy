# Lesson Learned: Check existing lexicon/pack rules for a matching principle before treating an edit as a novel rationale-gate candidate

**Date**: 2026-08-30
**Context**: `/style-capture section 4.3` on CRDB Exec-Summary §4.3, working-copy diff.

## What happened

A cluster of edits dropping deliverable version tags and abbreviation codenames — "DRD v2" → "DRD", "CDM/DMF" → dropped, "Node Content Storyboard...v2" → dropped — was flagged as an ambiguous new lexical candidate and put to Boss via `AskUserQuestion`, framed as a choice between "these tags were unverified/inaccurate" and "one-off correction for this document." His actual answer: "do you remember that the rule bans leaking internal code, logic, artifact names!" — pointing straight at an existing `LEXICON_TH.json` entry (the internal-artifact-locator rule, previously scoped only to slide/page locators in narrative prose). The edit wasn't a new pattern; it was that existing principle extending to a second surface (deliverable version tags/codenames) that the rule's narrow regex pattern hadn't been written to catch.

A second question in the same batch had a related but distinct miss: I hypothesized the roles-paragraph reframe ("requires clear role division" → "can help provide clearer direction") as a generic instance of the pack's own "Passive/Defeatist Syntax Elimination" category. Close, but Boss's actual point was narrower — don't restate a self-evident premise as filler before the substantive point, not a general dependency→benefit reframe.

## Why it matters

`check_lexicon_conflict.py` only does exact substring matching on the *banned/preferred term text* — it will never surface a match on the underlying *principle* behind a rule. Both misses here came from relying on that tool's silence as if it meant "no related rule exists," when what it actually means is "no rule uses this exact string." A style pack accumulates rules precisely so they don't need to be re-derived on every diff; skipping the "does this match a principle I already have?" step defeats that purpose and costs the user's attention re-explaining something already on record.

## The fix

Before drafting an `AskUserQuestion` for a non-mechanical candidate in style-capture step 4c: read through `STYLE_PACK_TH.md`'s categorized sections and skim `LEXICON_TH.json` reasons (not just banned/preferred strings) for an underlying principle the new edit might instantiate — "internal metadata leaking into reader prose," "restating the obvious," etc. — not just an exact-term match. If found, treat the new edit as broadening that existing rule's scope/pattern and cite it in the reason, rather than opening a fresh rationale-gate question.

Also: when a rationale-gate answer corrects the hypothesis rather than picking one of the offered options, write the *corrected* framing into the capture-history log, not the original guess — otherwise the next capture round inherits the wrong generalization.
