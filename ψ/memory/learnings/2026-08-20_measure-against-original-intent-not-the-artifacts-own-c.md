# Lesson: Measure a document against original intent, not just its own internal consistency

**Date**: 2026-08-20
**Context**: NCAIF sitemap v8→v9 practicality pass, CRDB project

## The pattern

When auditing whether a document's claims hold up (e.g. "these two sections share one build"), it's natural to check that claim against the most authoritative *downstream* artifact available — in this case, the sealed DRD. That's a real and useful check, but it only catches drift *within* the current document's own lineage. It can't catch the case where the current document itself has drifted from an earlier, more authoritative statement of intent, because nothing in the downstream chain remembers that earlier intent — the downstream artifacts were built *from* the current (already-drifted) document.

This session, a clean and well-evidenced "the DRD already knows the right answer, the mockups just didn't check" story explained one real problem (build duplication) but missed a second, independent one (A-BTR compliance-tag-driven scope creep against the human's original v6 intent) entirely, because that second problem lived in the gap between v6 and v8 — a gap invisible to any audit that only looks at v8 and its own descendants.

## Why it matters

An audit that only checks internal consistency will always converge on "the system is consistent with itself," even when the system has consistently drifted from what it was originally supposed to be. The fix isn't more rigor within the existing chain — it's asking, before starting, whether there's an earlier baseline outside the current document's lineage that represents the real original intent, and if so, diffing against that too.

## How to apply

Before auditing a document (sitemap, spec, requirements list) for internal consistency or claim-accuracy, ask: is there a prior version, a founding brief, or a stated original intent that predates this document's current lineage? If so, that's a required second baseline, not an optional extra pass — the two audits (internal consistency vs. drift-from-origin) catch structurally different classes of problem and neither substitutes for the other.

Related: [[2026-08-20_when-building-executive-ready-national-platform-we]] (same project, same day — asset-discovery-before-synthesis pattern, a different but complementary lesson from the mockup-building work that fed into this session's trigger).
