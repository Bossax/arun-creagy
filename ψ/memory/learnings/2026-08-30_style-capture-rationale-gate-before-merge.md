---
date: 2026-08-30
type: lesson
topic: style-capture-architecture
---

# Lesson: ask why before merging, and don't trust prose "MANDATORY" as enforcement

## What happened

Running `/style-capture` on a real human edit (CRDB §4.1) exposed two
distinct failure modes in the same session, at two different scopes:

1. **Scan skipped despite being labeled mandatory.** SKILL.md step 4 says
   "CRITICAL DIRECTIVE: ZERO-DROP LEXICAL SCAN" in bold. It was still
   skipped on the first pass — only paragraph-level structural cuts were
   caught; every word-level swap inside a rewritten sentence was missed
   until the user asked "did you capture the lexicon level styles?"

2. **Rationale inferred instead of asked, three times, including once
   immediately after being corrected for #1.** Three patterns were promoted
   into `STYLE_PACK_TH.md` purely on inference. One was the user filling in
   a domain fact he happened to know (adding "API," a specific request
   mechanism) — not a style habit. Generalizing it would have taught future
   drafts to invent mechanism detail not grounded in sources, which directly
   violates `writing-th`'s no-fabricated-sources rule. Another was a scope
   decision ("it does not fit the report's objective"), not a reusable
   pattern. Both had to be reverted and re-asked. This repeated a third time
   *during the planning phase for the fix to #2* — i.e., correcting the
   behavior in the moment did not stop the same default (act on inference,
   don't pause to ask) from reasserting itself minutes later.

## Root cause

A prose instruction, even one marked "MANDATORY" or "CRITICAL," is not a
forcing function. It competes with everything else in a long context and
loses under load — this is the same failure mode a prior architecture
analysis (`ψ/inbox/2026-08-29_writing-harness-skill-architecture-analysis.md`
line 325) already named for a different pattern: "Prose instructions get
skipped under load... Hooks cannot be skipped." Inferring rationale from a
diff is a related but separate risk: even a careful re-read of the diff
doesn't reveal *why* a human made a change, only *what* changed — tone,
domain knowledge, and scope decisions can produce visually similar diffs.

## Fix (implemented, 2026-08-30)

- `diff_word_table.py`: a computed word-level diff table the agent must work
  from row-by-row, replacing "scan by eye" with "classify what's already on
  the table." Converts a skippable instruction into a mechanical artifact.
- `register.py` rationale gate: a `status` column
  (`unconfirmed`/`mechanical`/`confirmed_generalizable`/`one_off`/`content_correction`)
  that `ready` filters on independently of sighting count. `mechanical`
  (pure token swaps) can promote on the first sighting; everything else is
  blocked from `ready` until confirmed via a required `AskUserQuestion` step
  (`SKILL.md` new step 4c) — asking about tone vs. content-accuracy vs.
  domain-fact vs. scope-decision vs. general-preference, not inferring it.
- `check_lexicon_conflict.py` / `check_term_propagation.py`: a related,
  smaller instance of the same root cause — a new lexicon entry
  (`เมทะดาตา → ข้อมูลอภิพันธ์`) silently coexisted with a pre-existing
  conflicting mapping until caught by chance. Now checked before writing.

## Generalizable takeaway

Any skill step whose failure mode is "the agent skips/guesses under load"
needs a script producing something concrete to react to — a table, a gate,
a required tool call — not stronger wording. And "I inferred the reason and
it turned out plausible" is not the same risk class as "I inferred the
reason and it was wrong" — the fix has to make asking cheaper/required, not
just make inferring more careful, because careful inference from a diff
alone cannot recover information (intent) that was never in the diff.
