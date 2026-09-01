# Lesson: A pipeline stage "reading the source" isn't the same claim as "detail survived to the output"

## Context

CRDB full-report §2.2 was reclassified from P+ to R (Boss's call, 2026-09-01) because it needed synthesis from multiple new WP artifacts. The writing-th skill's Stage 1 (argument recovery) read the full 65KB `5.2.2` source and packed relevant detail into each argument unit's `grounds` field. Stage 3 (verbalization) then worked *only* from the approved argument map — by design, blind to raw sources, so it can't reargue or reintroduce excluded content.

## The problem

Boss pointed out that when Stage 3 verbalizes purely from `grounds`, the actual source prose — with its full nuance, specific phrasing, and detail beyond what got condensed into `grounds` — never reaches the final draft. Stage 1 "read" the source, but that's a claim about Stage 1's process, not about what survived into the eventual output. The two are easy to conflate, especially when the whole point of the map/verbalize separation is designed to feel airtight.

## The resolution

Split Stage 3 into two lanes instead of one verbalization pass:
- **Lane A**: for content that already has full-report-altitude prose in an existing source document, polish that document *whole*, word-level only (qwen default model, strict no-rewrite prompt), never re-synthesizing from a compressed intermediate.
- **Lane B**: for content with no existing full-report-level prose anywhere, verbalize fresh from the approved argument map (qwen3.7-plus) — this lane's isolation from raw sources is fine, since there's no prior prose to lose fidelity from.
- **Merge is manual, by the human**, not by another AI pass — because a second AI stitching step would need to re-read both lanes' sources to reconcile them coherently, which reopens exactly the raw-source access the argument-map boundary exists to prevent (excluded content could sneak back in via Lane A's untouched source prose).

## Why to apply this again

Whenever a pipeline has a lossy intermediate representation (a summary, an extracted-argument structure, a compressed grounds field), check explicitly whether downstream stages are working from the intermediate or the original — "stage X already looked at this" is not evidence that stage X's output preserved what mattered. When in doubt, route unmodified source content through a separate "polish, don't resynthesize" lane rather than trusting a single compress-then-regenerate pass to be lossless.

## Secondary lesson: keep meta-commentary out of content files

Embedding review notes/annotations (e.g., "[paragraph 3 — flagged]") directly in a report-content file risks tripping content-scoped lint rules meant for actual prose (an internal-document-locator ban pattern matched "ย่อหน้าที่ N" as if it were "หน้า N"). Write verification/review notes to a fully separate file from the start.
