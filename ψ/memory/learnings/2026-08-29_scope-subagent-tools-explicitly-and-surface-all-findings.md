# Lesson: Scope Subagent Tools Explicitly, and Surface All Findings Evenly

**Date**: 2026-08-29
**Context**: CRDB executive-summary citation audit and citation insertion (8 read-only
audit subagents, then 4 writer subagents)

## The pattern

Two related mistakes in one session:

1. Four subagents were told (in prose) to search only project files
   (`inbox_source/` etc.) for citation sources, as part of a plan that explicitly
   deferred web search to a later step ("log them and we'll use web search later"). One
   subagent (chapter 1) used WebFetch to independently verify URLs and pull citations —
   including some (Nielsen Norman Group, an academic CHI paper) that don't trace back to
   any project file at all. This wasn't caught until I reviewed the subagent's own report
   and had to flag it to Boss after the fact, rather than before it happened.
2. After the first audit pass (8 subagents, one master report), the closing chat summary
   led with "priority actions" framed around the chapter Boss had originally flagged
   (Chapter 3 — DesInventar/DaLA). Genuinely strong findings that already existed in the
   same report for Chapter 1 (UX/IA citations: information scent, progressive disclosure,
   Climate Resilience Toolkit) and Chapter 4 (TOGAF/IBM/GDS/NESDC) went unmentioned in the
   summary. Boss read this as the audit having missed them entirely — "severe flaw in the
   plan" — when the actual defect was that a complete finding wasn't surfaced.

## The general lesson

**Scoping a subagent's method in prose is not the same as constraining its tools.**
General-purpose subagents default to full tool access; if a task must stay within one
data source (project files only, no live web), that needs to be an actual tool
restriction, not just an instruction the agent might not follow byte-for-byte.

**A closing summary after multi-agent work must inventory every result evenly**, not lead
with whichever finding matches the user's original framing. A "quick wins" or "priority"
section is fine as one part of the report, but it cannot substitute for a complete
inventory — the reader has no way to know solid findings exist elsewhere in the report if
the summary doesn't mention them, and will reasonably conclude the work is incomplete.

## How it changed the output

For (1): future multi-source-restricted subagent tasks should explicitly withhold
WebFetch/WebSearch when the task says "project files only," not just describe the scope.

For (2): the corrected summary listed every chapter's findings with equal structure
(SOURCED / PARTIAL / GAP per chapter) rather than a single "here's what to do first" list.

## Related

A third, related standard surfaced later in the same session: this project's citation
discipline treats an undated ("ม.ป.ป." / "n.d.") citation as equivalent to no citation —
Boss rejected all 10 inserted undated citations and had them moved to gap logs instead of
staying in the drafts. See [[citation-style-th]] (memory) — undated sources should be
gap-logged from the start, not inserted speculatively.

---
*Added via /rrr*
