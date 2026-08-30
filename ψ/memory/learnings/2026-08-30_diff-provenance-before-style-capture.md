# Lesson: Verify diff provenance before running style-capture's zero-drop audit

**Context**: Two `/style-capture` runs today (CRDB §4.4, §4.5) each started
with a non-empty diff that looked, at first glance, like a human editorial
correction ready for the Zero-Drop Lexical Scan.

**What actually happened**:
- §4.4's working-copy diff was comparing two *unrelated* sections that
  happened to share a filename after a report-outline renumbering (old §4.4
  content had moved to become the new §4.3). Zero style signal in that diff.
- §4.5's first diff was real but was Boss revising content and structure
  (cutting two whole sections, re-phasing a 7-item list into 8 items across
  ระยะสั้น/ระยะกลาง timeline buckets) — not correcting AI prose style.
- §4.5's *second* pass, after Boss explicitly said "I edited it," was a
  genuine human edit — and even then, only 1 of 73 diff rows was a real
  lexical candidate (หมุนรอบ → ยึด); the rest were still legitimately
  structural/content and got dispositioned that way rather than forced into
  a lexical bucket.

**The generalizable rule**: a non-empty `git diff` on a report-section file
is necessary but not sufficient evidence of a style-correction pass. At
least three distinct causes produce a non-empty diff on these files:
1. An outline reshuffle that moves unrelated content under a reused filename
   (no edit at all — just a naming collision).
2. A pipeline re-verbalization of the same argument map (AI output vs. AI
   output, no human in the loop).
3. An actual human edit (the only case the diff's face value suggests).

**How to apply**: before running `diff_word_table.py`'s output through the
zero-drop lexical audit, look at the diff's *shape*. Word/sentence-level
substitutions with no new facts, figures, or restructured sections =
proceed. Whole new paragraphs, added numbers/facts, cut/added sections, or
renumbered lists = stop and ask the user to confirm this is actually their
edit before treating any of it as corrective style signal. This is cheap
insurance against exactly the kind of bad promotion the 2026-08-30 morning
postmortem (three patterns promoted on inference alone, two had to be
reverted) was written to prevent — the failure mode generalizes from "guessed
the rationale" to "guessed the provenance."

**Secondary finding**: a rationale-gate answer can surface a rule bigger than
the candidate being asked about. Boss's answer to "why drop the 270-day/
day-210 timeline figures" wasn't a style preference at all — it named an
actual writing-plan scope boundary (don't write in specifics about a
next-TOR that hasn't been decided yet). That belongs in `writing-th`'s
contract-validation logic, not in `LEXICON_TH.json` or the miss register's
`content_correction` bucket where it's currently sitting. When an answer
names a rule outside style-capture's remit, surface it as a distinct
follow-up instead of just logging it and moving on.

**Related**: [[feedback_ask_rationale_before_style_merge]],
[[feedback_check_existing_rules_before_treating_edit_as_novel]]
