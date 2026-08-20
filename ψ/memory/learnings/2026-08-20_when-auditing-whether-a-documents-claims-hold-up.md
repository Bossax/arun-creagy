---
id: learning_2026-08-20_when-auditing-whether-a-documents-claims-hold-up
type: learning
title: "When auditing whether a document's claims hold up (e.g. \"these two sections shar"
concepts: [audit-methodology, documentation-drift, requirements-baseline, scope-creep]
tags: [audit-methodology, documentation-drift, requirements-baseline, scope-creep]
created: 2026-08-20
indexed_at: 2026-08-20T08:18:24.112Z
updated_at: 2026-08-20T08:18:24.112Z
hash: sha256:93095dcecfbbe9d2e3192afcca3e47543b8392bc07bf651d6e38e25f962c696d
source: "rrr: Arun_Creagy"
arra_id: learning_2026-08-20_when-auditing-whether-a-documents-claims-hold-up
arra_type: learning
arra_concepts: [audit-methodology, documentation-drift, requirements-baseline, scope-creep]
arra_created: 2026-08-20T08:18:24.112Z
---

# When auditing whether a document's claims hold up (e.g. \"these two sections shar

When auditing whether a document's claims hold up (e.g. "these two sections share one build"), checking against the most authoritative downstream artifact (like a sealed DRD) only catches drift within the current document's own lineage — it can't catch the case where the current document itself has drifted from an earlier, more authoritative statement of original intent, because the downstream artifacts were built FROM the already-drifted document. In the NCAIF sitemap v8→v9 audit, a clean "the DRD already knows the right answer, the mockups just didn't check" story explained build duplication but missed a second, independent problem entirely: A-BTR compliance-tag-driven scope creep against the human's original v6 intent, invisible to any audit that only looks at v8 and its descendants. Fix: before auditing a document for internal consistency, ask whether a prior version or founding brief exists outside the current document's lineage, and treat diffing against it as a required second baseline, not an optional extra pass — internal-consistency audits and drift-from-origin audits catch structurally different problem classes.

---
*Added via Oracle Learn*
