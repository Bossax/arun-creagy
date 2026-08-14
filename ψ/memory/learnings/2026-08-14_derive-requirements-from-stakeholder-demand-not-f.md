---
id: learning_2026-08-14_derive-requirements-from-stakeholder-demand-not-f
type: learning
title: "Derive requirements from stakeholder demand, not from an abstract category check"
concepts: [requirements-engineering, business-analysis, derivation-direction, NFR, stakeholder-demand, category-error, domain-modeling]
tags: [requirements-engineering, business-analysis, derivation-direction, NFR, stakeholder-demand, category-error, domain-modeling]
created: 2026-08-14
indexed_at: 2026-08-14T14:57:28.397Z
updated_at: 2026-08-14T14:57:28.397Z
hash: sha256:20b8ba2b10066edccfa21d448284e5a43e8de50b13e1350b1944a89c35642bd3
source: "rrr: Arun_Creagy (CRDB WP6)"
arra_id: learning_2026-08-14_derive-requirements-from-stakeholder-demand-not-f
arra_type: learning
arra_concepts: [requirements-engineering, business-analysis, derivation-direction, NFR, stakeholder-demand, category-error, domain-modeling]
arra_created: 2026-08-14T14:57:28.397Z
---

# Derive requirements from stakeholder demand, not from an abstract category check

Derive requirements from stakeholder demand, not from an abstract category checklist.

WRONG DIRECTION: abstract requirement taxonomy (freshness, latency, compliance, retention...) -> invent one plausible instance per service. Produces documents that look complete and are useless.

RIGHT DIRECTION: stated stakeholder demand -> what the service must actually answer -> then thresholds attached to those answers.

DETECTION SIGNAL: if a service has N stated use cases in the source material and your requirements table has far fewer than N rows, the table is wrong regardless of how well-formed each row is. Count the source's own enumerated demands and compare. Large asymmetry means you generated rather than derived.

The conceptual layer must exist before the requirement layer can be authored. "Without a clear picture of what these services should answer, how could you derive NFRs?"

RELATED CATEGORY ERROR (same artifact): a cross-domain analytic product does not map to one data domain. A risk product consumes hazard + exposure/vulnerability + impact together. Matching it to the domain whose NAME matches ("Exposure & Vulnerability") is a category error. When attributing a derived/analytic product to a category, check what it CONSUMES, not what it is CALLED.

---
*Added via Oracle Learn*
