# Learning: Phase 3 and Phase 4 must be operationally explicit in article pipelines

In a multi-stage article workflow, labels like “Phase 3” and “Phase 4” cannot remain conceptual shorthand once they start guiding real execution. If the human says **execute Phase 3**, the agent must treat that as an integrated operational pass, not as a small interpretation chosen ad hoc in the moment.

The durable pattern from this session is:

1. **Phase 3 must be a delta-only pass**
   - Start from the existing extraction.
   - Check the decision log and the active draft.
   - Query only what is still missing and only what matters for the chosen article direction.

2. **Phase 3 must produce concrete artifacts**
   - updated `raw-copy.md` when new gaps exist
   - verbatim retrieval outputs under those new query blocks
   - `03_Verified_Facts.md` as the canonical verification layer
   - style capture updates when the edited draft introduces reusable voice changes

3. **Phase 4 must be the actual final drafting stage**
   - The plan should not insert a redundant pseudo-phase in front of final drafting.
   - Phase 4 should simply draft from the outputs already created by Phases 1–3.

4. **If the workflow is unclear, patch the plan immediately**
   - Conversational clarification is not enough when the ambiguity is structural.
   - The source-of-truth document must be updated so future execution stays consistent.

This session shows that workflow ambiguity creates repeated execution friction even when the underlying writing quality is strong. The fix is not more explanation. The fix is explicit deliverable definitions per phase.

