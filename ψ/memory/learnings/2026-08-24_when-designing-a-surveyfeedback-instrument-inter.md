---
id: learning_2026-08-24_when-designing-a-surveyfeedback-instrument-inter
type: learning
title: "When designing a survey/feedback instrument, interrogate measurement validity (d"
concepts: [survey-design, measurement-validity, ceiling-effect, google-apps-script, idempotency, iterative-design]
tags: [survey-design, measurement-validity, ceiling-effect, google-apps-script, idempotency, iterative-design]
created: 2026-08-24
indexed_at: 2026-08-24T11:48:49.034Z
updated_at: 2026-08-24T11:48:49.034Z
hash: sha256:0c39c06ec7712384fa8c5109200fdef00659b830dd6a2d3df5bf4f759533ba7b
source: "rrr: crdb-dissemination-feedback-form"
arra_id: learning_2026-08-24_when-designing-a-surveyfeedback-instrument-inter
arra_type: learning
arra_concepts: [survey-design, measurement-validity, ceiling-effect, google-apps-script, idempotency, iterative-design]
arra_created: 2026-08-24T11:48:49.034Z
---

# When designing a survey/feedback instrument, interrogate measurement validity (d

When designing a survey/feedback instrument, interrogate measurement validity (does this metric discriminate between good/bad outcomes, does it map to a decision) before optimizing interaction cost (page count, tap count). A generic "relevance to your work" 1-5 scale asked of a pre-selected, already-relevant audience produces a ceiling effect (everyone rates 4-5) and no usable signal, no matter how cheap it is to answer. The fix is often not more expensive to answer — e.g. replacing single-dimension "relevance" with a paired "priority x completeness" measure (read as a quadrant) gave strictly more decision-usable data at the same tap cost.

Separately: any script whose job is to instantiate a persistent resource (FormApp.create() for a Google Form, a repo scaffold, a deployment) will predictably need an "update the existing one" mode the moment someone iterates on the design after the first successful run. Build create/update symmetry into the script from the first pass (a shared body-builder function + an ID-based open-and-rebuild path) rather than retrofitting it once the user already has IDs/URLs they depend on — retrofitting adds churn and forces the user to re-diagnose "wait, doesn't re-running this just make a duplicate?"

---
*Added via Oracle Learn*
