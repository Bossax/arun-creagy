---
id: learning_2026-08-14_audience-facing-documents-must-not-narrate-the-pro
type: learning
title: "Audience-facing documents must not narrate the project's own discovery process."
concepts: [technical-writing, audience-awareness, documentation-voice, internal-codes, repeat-feedback, deliverable-quality]
tags: [technical-writing, audience-awareness, documentation-voice, internal-codes, repeat-feedback, deliverable-quality]
created: 2026-08-14
indexed_at: 2026-08-14T14:57:42.913Z
updated_at: 2026-08-14T14:57:42.913Z
hash: sha256:af4a65024294b311bccba5d5f6469344ff16ab368bc2ee5286019e8719fd85c5
source: "rrr: Arun_Creagy (CRDB WP6)"
arra_id: learning_2026-08-14_audience-facing-documents-must-not-narrate-the-pro
arra_type: learning
arra_concepts: [technical-writing, audience-awareness, documentation-voice, internal-codes, repeat-feedback, deliverable-quality]
arra_created: 2026-08-14T14:57:42.913Z
---

# Audience-facing documents must not narrate the project's own discovery process.

Audience-facing documents must not narrate the project's own discovery process.

FAILURE MODE: writing a deliverable whose sections close with "WP4's build-phase work found...", "REQ-069 is recorded as covered...", "Brief E-4 confirms...", "the Enrichment Roadmap suggests...". Content accurate, voice wrong — the document narrates WHICH work package discovered WHAT, in WHICH artifact, at WHICH stage, rather than describing the subject itself.

WHY WRONG: external readers (client leadership, downstream contractors) do not care which internal work package found a finding, what a requirement's internal ID is, or what an internal document is named. Internal codes FEEL like precision but function as noise, obscuring the actual argument behind project bookkeeping.

THE FIX — state findings as facts about the subject, not as reports on who discovered them when:
- "WP4's work found the composite index can't be disaggregated" -> "DCCE's existing risk index can't be broken down below the province level"
- "REQ-008, 014, 015 are marked ready to build" -> "much of its content is ready to build"
- "Brief E-4 confirms this is a future-project workstream" -> "This work is explicitly being deferred, not attempted in the current phase"
- Plain-language technical shorthand too: STAC/ISO -> "international metadata conventions"; CMIP6 -> "global climate projections"; PDPA -> "a privacy review"

Keep the honest current-state assessment (omitting blockers would mislead), but frame it as the subject's real standing, not as an audit result.

PRE-DRAFT CHECK: who reads this, and would they recognize a single internal code in it? If no, none should appear.

NOTE: this is a REPEAT correction across three separate sessions. The underlying instinct is "showing my work" — which serves the author, not the reader.

---
*Added via Oracle Learn*
