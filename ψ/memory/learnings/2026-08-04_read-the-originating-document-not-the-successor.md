# Lesson: When sealing a T-E-D-A chain, cite the originating document, not just its successor

**Type**: learning
**Created**: 2026-08-04
**Tags**: seal, ledger, causality, evidence

## The pattern

While proposing a T-E-D-A chain for the CRDB 9-pillar folder restructure, the first draft cited only `D-032` (the 9-Pillar Inception Package Anchor) as the evidence behind the physical folder rename. The user asked: "isn't this file [`2026-05-20_CRDB-Blueprint-Handoff-and-Procurement-Shield-Strategy.md`, E-038, the *original* 8-Pillar table] important enough to be mentioned in this chain?" It was — E-038 is where the pillar concept and names actually originate; D-032 is a same-week successor that reordered and expanded it.

A related error surfaced right after: folder numbers were assumed to mirror E-038's pillar order, when they actually mirror D-032's *reordered* sequence (D-032 flipped from architecture-first/CDM=P1 to deliverable-first/Sitemap=P1, and added a new Use-Case pillar not present in E-038 at all). This was only caught by going back and reading D-032's actual Section 3 table rather than reasoning from what had already been summarized in context.

## Why it happens

When a lineage has a "final" or "most complete" version, it's natural to cite that one — it's cleaner, and it's usually still linked to the earlier evidence in the ledger. But a T-E-D-A chain's whole purpose is preserving *why* a decision happened, and the "why" often lives in the earlier, rougher document, not its polished successor. Citing only the latest link in a chain silently erases the causal step that mattered most.

## How to apply

When building an Evidence/Decision chain for `/seal`, trace back to the *first* document that introduced the concept being hardened, not just the version that's easiest to point to. If a successor document changed something structural (reordering, renaming, adding/removing units), that change itself deserves its own note in the ledger — don't let the newer document's numbering silently overwrite the reader's understanding of the older one. When in doubt about what an older document actually said, re-read it rather than trusting a paraphrase already sitting in context.

Related: [[trace-deep-is-not-done-until-the-log-is-written]], the same session's other lesson about not stopping at the "interesting" part of a skill and skipping its mechanical completion step.
