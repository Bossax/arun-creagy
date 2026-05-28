---
title: Immutable User Curation in Semantic Hardening
date: 2026-05-28
concepts: [Data Engineering, Automation, Semantic Consistency, Curation]
---

# Immutable User Curation in Semantic Hardening

When transitioning draft artifacts (like CSV glossaries) into database-ready formats ("hardening"), automated processes must treat manual user curation as immutable.

**The Pattern:**
1. A draft dataset is augmented by AI research.
2. A human expert manually refines specific cells (e.g., nuanced translations or architectural alignments).
3. The AI is asked to "harden" the file (e.g., apply RFC 4180 formatting or backfill missing metadata).
4. **Failure State:** The AI uses its generated data as the master template, inadvertently overwriting the human expert's edits.

**The Resolution:**
Automation must only target the *gaps*. When merging files, the user-edited file must be defined as the absolute base. AI-generated data should only be injected into explicitly empty fields or newly defined metadata columns (like `CDM_Entity_Link` or `Semantic_Owner`), never overwriting populated primary content fields.

**Secondary Insight (CSV Auditing):**
Visual inspection of raw CSV text for empty fields is prone to error ("sparse data blindness"). Validation of completeness requires structural parsing, not visual scanning, to prevent hallucinating data completion.