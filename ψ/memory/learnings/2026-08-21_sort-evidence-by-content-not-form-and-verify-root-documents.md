---
name: sort-evidence-by-content-not-form-and-verify-root-documents
description: When tracing the origin of a design decision or categorizing source material, verify the root document and sort by what a source argues, not its surface form (citations, formatting, tone)
metadata:
  type: feedback
---

Two related failures in one trace session, same root cause: trusting surface signals over verifying substance.

**Failure 1 — stopped searching at "enough" instead of "root".** Tracing NCAIF's IA design principles, I found a plausible, complete-looking answer (a v5-era technical spec + the May 12 workshop presentation) and stopped. Boss then pointed out I'd missed the actual founding design-lock document (`National Climate Adaptation Information Framework.md`, Jan-Mar 2026) — older, and the direct ancestor of everything I'd found. The v5 spec was a restatement, not the origin.

**Failure 2 — sorted a document by its form, not its content.** A UX research brief (`2026-03-12 - User Experience Design Principles...`) has citation-heavy, lit-review formatting (footnotes, Works Cited, named studies). I filed it under "academic content" for that reason alone. But its actual argument — progressive disclosure, decoupled architecture, narrative-driven IA — is entirely about information architecture and navigation, not domain science. The real "academic content" bucket was the IPCC/WMO/UNFCCC/ISO standards-alignment section, a genuinely different part of the same source chain.

**Why:** [[trace-authority-over-plausibility]] — a complete-looking answer isn't the same as a correctly-rooted one, and citation density signals rigor, not subject-matter category.

**How to apply:** When tracing "why does X exist" or "what's the origin of Y," explicitly ask whether the found document is the root or just a downstream restatement — check what it cites as its own inputs before treating it as settled. When categorizing a source into a framework (e.g., academic vs. structural, topic vs. presentation), sort by what the document actually claims/argues, never by its formatting or tone. Especially relevant on this CRDB project, which has multiple layered document generations (v4→v5→v8→v9 sitemaps; Pack A/B/C decision chains) where an earlier, more foundational doc is easy to miss if a later doc looks sufficient on its own.
