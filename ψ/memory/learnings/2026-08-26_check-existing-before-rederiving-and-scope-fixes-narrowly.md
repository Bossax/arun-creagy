# Lesson: check for existing work before re-deriving, and scope automated fixes narrowly

**Context**: A TOR70 review session (docx conversion → criticism verification → CRDB gap trace → SDLC deviation analysis → briefing deck → Thai translation via the writing-th harness) surfaced two related process failures, both caught by the user or by an automated gate rather than by my own judgment in advance.

## Pattern 1 — re-deriving research that already exists

Twice in the same session, I moved to generate new analysis before checking whether it already existed:

1. I proactively launched a subagent to research TOR70's prior-criticism trail. The user had already pointed at a specific existing trace log and had to say "kill the sub agent."
2. Later, I proposed drafting a note on CRDB's missing/deferred delivery items. The user corrected me: this was already fully captured in a `/trace --deep` log I myself had produced two turns earlier in the same session.

**Why it matters**: the second instance is the more instructive one — it wasn't a failure to search a codebase, it was a failure to check my own recent output before treating a sub-question as new. Session-local memory of "what have I already produced" needs to be checked with the same rigor as an external search.

**How to apply**: before starting any research or analysis sub-task, explicitly ask "does a trace log, prior section of this session, or file already answer this?" — not just at the start of a task, but at each new sub-question that arises mid-task. This is cheap to check and expensive to skip.

## Pattern 2 — automated text fixes need narrow scope, not blind global replace

While fixing a Thai-writing lint violation (a banned lexicon term, "DCCE" → "กรมฯ"), I used a blind `str.replace()` across the entire draft file. This corrected the intended prose instances but also silently corrupted a markdown link's file path elsewhere in the document, since the same literal string appeared there as a legitimate filename, not prose.

The `writing-th` skill's own merge gate (`merge_draft.py` re-running Stage 5 before copying) caught this before it reached the real destination file — but the fix should not have needed the gate to catch it. A scoped replacement (matching the violation's surrounding sentence context, or an explicit exclusion for anything inside `[...]()`  markdown link syntax) would have been correct on the first attempt.

**How to apply**: when fixing a flagged string in natural-language content that also contains code spans, file paths, or link targets, never do a blind whole-file string replace on that literal value. Scope the replacement to the specific sentence or context the violation was reported in, or explicitly exclude structural syntax (link brackets, code fences, paths) before replacing.

## Related

[[feedback_auto_spawn_watchers_on_handoff]] — a different session-behavior lesson about proactive action timing; this one is about proactive *research* timing specifically.
