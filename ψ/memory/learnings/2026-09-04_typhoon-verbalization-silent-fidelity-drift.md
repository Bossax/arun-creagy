# Lesson: LLM verbalization of structured facts can silently drift, even under explicit anti-drift instructions

**Context**: Tested `typhoon-v2.5-30b-a3b-instruct` (via a new global MCP server) by asking it to write CRDB report prose strictly from one node (arg-03/03a/03b, the Home-page unit) of the approved `crdb-full-report-2.6/argument-map.json`, then compared the result against the source and against two old human/consultant drafts.

**What happened**:
1. First call: silently dropped an entire argument unit (the two role-based portals) with no error or truncation signal visible to the caller — just stopped short, producing a coherent-looking but incomplete paragraph.
2. Same first call: silently reordered/relabeled a named category — "international, domestic" funding sources became "private sector, international" — inventing a category not present in the source.
3. Second call, with an explicit "do not alter the given wording" instruction and a higher `max_tokens`, fixed both of those but still dropped one word ("และแผน" / "and planners") from a section name.

**Why this matters**: This is a controlled-vocabulary-preservation failure, not a generic hallucination — the model wasn't asked to add facts, it was asked to *not change* facts already handed to it verbatim, and still drifted on the first, unconstrained attempt. It happened with zero signal to the caller (no warning, no flagged uncertainty, no truncation notice) — the only way to catch it was already knowing the source cold and diffing by hand.

**How to apply**:
- Treat any LLM verbalization step over structured/approved source data (argument maps, spec extracts, ledger content) as needing an independent fidelity check against the source, regardless of how fluent the output reads — fluency is not evidence of fidelity.
- On a first-time call to an unfamiliar model/provider for a multi-unit generation task, always set an explicit, generous `max_tokens` rather than trusting provider defaults — a silent truncation can look identical to a complete answer.
- This is exactly the class of error the `writing-th` pipeline's Tier 1/2 editorial review (independent clean-context review against the argument map) exists to catch — don't treat a fluent raw draft from any model, including this one, as safe to skip that review.

Related: [[feedback_ai_writing_tells_in_thai_prose]] (verify named-framework attributions before writing them — same discipline, different failure surface).
