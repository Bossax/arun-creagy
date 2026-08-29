# Lesson: Verify a mechanism's implementation, not just its config, before promoting a rule to fix it

**Date**: 2026-08-29
**Source**: writing-th v6.0 build — lexicon promotion step (see retrospective `ψ/memory/retrospectives/2026-08/29/15.05_writing-th-v6-build-and-verification.md`)

## What happened

The v6.0 build plan (approved by the user) named two specific patterns to promote into `LEXICON_TH.json` — `ไม่ได้...แต่...` and `ไม่ควรถูกมองเป็น...แต่ควรถูกมองเป็น...` — on the premise that they were "documented style guidance that had never been mechanically enforced." That premise came from reading `LEXICON_TH.json`'s contents and `STYLE_PACK_TH.md`'s capture log, both of which discussed the pattern extensively without it appearing as a lexicon entry.

While testing the new rules against synthetic text before calling the step done, both new lexicon entries fired — and so did an existing `[CONTRAST]` finding neither of us had accounted for. Reading `lint_thai_writing.py`'s actual matching code revealed a hardcoded regex (`contrast = re.compile(r"ไม่ได้.{0,60}?แต่|ไม่ใช่.{0,60}?แต่|ไม่ควรถูกมองเป็น.{0,60}?แต่")`) that had been catching exactly this pattern family all along, tracked in the miss register under the label `contrast` with 4 historical hits. The lexicon additions were pure duplication.

## Why this happened

The planning-phase inventory read the *data* the gate consumes (`LEXICON_TH.json`) and the *validator* that checks that data's shape (`validate_lexicon.py`), but not the *matcher* that actually applies rules to text (`lint_thai_writing.py`'s body). "This pattern isn't in the lexicon" was treated as equivalent to "this pattern isn't enforced" — but a gate can enforce a rule through hardcoded logic that never touches the configuration file at all.

## The generalizable lesson

Before proposing to fix an enforcement gap by adding a rule to a config file, check what the enforcing code itself actually matches — not just what its configuration declares. A rule-based system frequently has bootstrapped, pre-configuration logic for its earliest or most important rules (this contrast regex predated the lexicon's `kind: regex` mechanism). Absence from the config is not proof of absence from enforcement.

## How to apply

- When diagnosing "X isn't caught," grep the actual matching/validation code for X's literal pattern before concluding it needs a new rule, not just the data file that's supposed to declare rules.
- When a plan is built from document review rather than code review, flag that distinction explicitly — "the docs say this is unenforced" is a weaker claim than "I read the enforcement code and confirmed no path catches this."
- If a planned fix turns out to be redundant once you actually test it, revert and say so plainly rather than adding it anyway because it was pre-approved — the approval was for the goal (close the gap), not for a specific rule text that testing later showed to be unnecessary.

## Related

[[feedback_generous_asset_matching]] — a different case of the same broader principle: verify the actual state of a system before asserting what is or isn't present in it.
