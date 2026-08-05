# CRDB Deliverable Redirection — Research Report and Plan

**Date:** 2026-08-05

**Scope:** This report grounds CRDB's remaining deliverable set in requirements-engineering and enterprise-data-architecture literature, and sets out a plan for the two weeks remaining before the dissemination event.

**Sources:** Two bodies of literature were reviewed for this report. The first covers business-requirements and software-requirements-specification practice (referred to below as the requirements-engineering literature). The second covers enterprise data architecture and data governance practice (referred to below as the data-governance literature). Both were reviewed across three successive rounds of inquiry, each round's findings independently checked before the next round was scoped. The full record of each round, including the underlying source material, is retained in the `iteration-1`, `iteration-2`, and `iteration-3` folders alongside this report.

---

## 1. Background

CRDB produced nine self-organized categories of output over the course of the project: Sitemap, Use Cases, Data Inventory, Glossary, Conceptual Data Model (CDM), Loss & Damage Data Model (LDM), Governance, Reference Data, and Building Blocks. This nine-category structure was set by the CRDB team; it was not specified by DCCE. DCCE's actual request comprises eight items: a data inventory, a data product inventory, a sitemap, a data management framework, a use case and demand analysis, a gap analysis, recommendations, and a Loss & Damage data model.

Requirements Traceability Matrices and Non-Functional Requirement specifications, which would ordinarily accompany a system-build engagement, are not part of this request. CRDB is a pre-system-design blueprint; those artifacts belong to the downstream TOR70 engagement.

Before this research was undertaken, an internal working assumption held that four of CRDB's nine categories — the Conceptual Data Model, the Glossary, Governance, and Reference Data — were properly components of a single "Data Management Framework" deliverable rather than four separate items. This report tests that assumption against the literature before committing the two weeks of remaining effort to a specific restructuring approach.

---

## 2. Findings

### 2.1 Should governance-related deliverables be combined or kept separate?

The working assumption was not confirmed as originally stated. Both bodies of literature describe the glossary, conceptual data modeling, governance and stewardship, and reference/master data management as related but separate disciplines, each with its own typical deliverable, rather than as parts of a single artifact. The data-governance literature specifically names the practice of scoping all four components into one simultaneous deliverable as a recognized failure mode, associated with programs that do not deliver anything usable within their first year.

The finding that is supported is narrower than the original assumption: it is standard practice to present these four items under one narrative heading, such as "Data Management Framework," provided each remains a separately identifiable deliverable rather than being merged into a single document.

### 2.2 How does a domain-specific data model relate to a central conceptual model?

Neither body of literature specifies a single formal rule governing the relationship between a domain-specific model such as the LDM and a central conceptual model such as the CDM. Both bodies of literature do, however, describe three paradigms in current use, and both arrived at the same three independently:

1. **Centralized.** The domain model is a subset of one enforced central schema.
2. **Federated (data mesh).** The domain model is designed and governed independently, with a federated governance layer standardizing only cross-domain interoperability — shared interfaces and data contracts.
3. **Semantic, ontology-mapped.** The domain model remains local, with its terms mapped to a shared ontology or glossary rather than derived from a central schema.

Both bodies of literature separately identify a "semantic layer" — a shared register of metric and term definitions, of the kind implemented by tools such as dbt's Semantic Layer — as the mechanism that keeps a federated or semantic-mapped domain model consistent with the rest of the organization without requiring a single shared schema. A later round of inquiry specified the minimum content of that artifact: a business glossary and metric register recording, for each metric, its calculation logic and the domain team responsible for it.

Which of the three paradigms CRDB should adopt for the LDM is not settled by this research and requires a decision by the CRDB team, addressed in Section 3 as Decision A.

### 2.3 What does "Data Management Framework" mean as a deliverable?

Both bodies of literature note that this term is used in two different ways: narrowly, to mean day-to-day operational data management such as pipelines, storage, and quality processes; or broadly, to mean a combined program of governance, architecture, metadata, and master-data management. Both agree that in blueprint or pre-system-design engagements specifically, the broad meaning is conventional. Neither body of literature has been checked against DCCE's original request wording, so whether DCCE's own usage matches this convention remains open, addressed in Section 3 as Decision B.

### 2.4 How does a data inventory differ from a data product inventory?

Both bodies of literature describe these as distinct deliverable types, and did so independently and consistently. A data inventory records raw or source-level data assets: technical metadata, centrally or IT-owned, catalogued but not packaged for consumption. A data product inventory records curated data products: business and technical metadata, defined consumption interfaces, service-level expectations, and domain ownership. Because this distinction was reached independently from separate material in each body of literature, it can be treated with more confidence than a finding resting on a single source.

### 2.5 What should a reference data or master data deliverable contain, and how much of it is needed in two weeks?

The data-governance literature specifies a structure for a draft-stage reference-data or master-data deliverable: for each entity or code list, record a business definition and calculation logic, technical schema and valid value ranges, system of record, data owner and steward, compliance classification, and validation rules — an eight-column structure in total.

A separate line of inquiry addressed how many entities such a deliverable should cover within a two-week, draft-only timeframe. The literature treats scoping to a small number of high-priority elements, rather than the full data estate, as standard practice at this stage, provided the selection is justified against four criteria: each selected element ties to a specific business objective; it covers an entity genuinely shared across functions; its data source is reliable enough to document now; and any deferred elements are marked as deferred, using a standard priority scale, rather than silently omitted.

### 2.6 What structure should the gap analysis follow?

The requirements-engineering literature recommends combining two formats: a dimension-scored matrix comparing current state to target state, feeding into a phased roadmap for closing the gaps identified.

The specific dimension framework referenced earlier in this project's discussions — nine named dimensions, referred to as DATER — was not found in the data-governance literature reviewed. It was subsequently located in the requirements-engineering literature, where it is attributed to a specific published source: Hoseini, Quix, and Decker (arXiv:2606.08811v1). That source specifies all nine dimensions and groups them into three sets: Control, Governance, and Trust (dimensions 1 through 3); Data Modeling and Understanding (dimensions 4 through 6); and Data Processing (dimensions 7 through 9).

A separate and independently derived list in the data-governance literature, describing what should be assessed at the discovery stage of a data blueprint as against what should be deferred to a later build stage, maps onto the first six of these nine dimensions. The remaining three — concerning system integration, data virtualization, and analytics and machine-learning support — are treated in that literature as later-phase, build-stage concerns rather than discovery-stage ones. Taken together, this supports scoring dimensions 1 through 6 at this stage of CRDB's work and explicitly deferring dimensions 7 through 9.

### 2.7 Is a sitemap a data-management or requirements-engineering deliverable?

Two separately worded lines of inquiry against the requirements-engineering literature found no reference to sitemaps or information-architecture artifacts. This consistent absence indicates that a sitemap is conventionally treated as a user-experience or information-architecture deliverable, outside the scope of requirements-engineering or data-architecture practice.

### 2.8 What can be deferred, and what is expected at draft stage?

Across both bodies of literature, a consistent pattern describes which elements of each deliverable type should be substantively developed at a draft or blueprint stage, and which can be represented as placeholders or deferred to a later, system-build stage. Expected at draft stage: a governance responsibility matrix with named roles, a business glossary with core term and metric definitions, and a small set of six to ten stated architecture principles. Treated as deferrable: selection of specific technology or vendor tooling, detailed physical database schemas, and automated data-quality monitoring code.

### 2.9 A limitation in the evidence

One question — the mechanism for keeping a business glossary synchronized as a conceptual data model changes over time — was answered in two separate rounds of inquiry using the same single source both times; rewording the question in the second round did not surface an independent second source. This should be treated as a limitation in the coverage of the literature reviewed on this specific point, not as a sign that the answer itself is incorrect, and it should be cited with that caveat if used in the final deliverable.

---

## 3. Decisions Required from the CRDB Team

Two questions could not be resolved by this research and require a decision, or a comparison against DCCE's own documents, rather than further literature review.

**Decision A — which LDM-to-CDM paradigm to adopt.** The three options are set out in Finding 2.2. The more common pattern in the literature for a situation of this kind is the federated option, supported by a business glossary and metric register — but the choice itself belongs to the CRDB team. Whichever option is chosen, the literature describes five categories of supporting justification expected to accompany it: an assessment of the actual data and workload characteristics involved, the intended users' access patterns, an inventory of source-data constraints, a scored assessment using the dimension framework described in Finding 2.6, and evidence that the organization can support the governance model the choice implies.

**Decision B — whether "Data Management Framework," as CRDB is using the term, matches DCCE's own wording.** This research confirms that the broad meaning described in Finding 2.3 is conventional for this type of engagement, but this has not been checked against DCCE's original request text, which falls outside the literature reviewed. If DCCE's wording matches, no change is needed. If it does not, a scope note within the deliverable is sufficient to resolve it.

---

## 4. Redirection Plan: The Eight Deliverable Items

The following restates DCCE's eight requested items, describing what each should contain at a draft-stage quality bar, based on the findings in Section 2. Where applicable, existing CRDB material is identified for reuse rather than being rebuilt from nothing.

1. **Data Inventory.** Cover approximately eighty percent of current systems, owners, and consumers, with detailed work scoped to the ten most business-critical assets rather than the full estate. CRDB's existing data catalog can serve as a starting point; it has not been updated since early June and will need to be re-scored against the top-ten criterion.

2. **Data Product Inventory.** For the same ten assets, add business metadata such as definitions and metric logic, a governance responsibility assignment, and a compliance classification. The responsibility assignment should use five named roles — Data Owner, Data Steward, Data Architect, Data Engineer, and a Governance Council — mapped to five specific decision types: setting quality thresholds, approving new data sources, setting access policy, resolving definition conflicts, and approving architecture changes. Service-level agreements, automated quality scoring, and enforcement tooling are not expected at this stage.

3. **Sitemap.** Treated as outside the Data Management Framework narrative, per Finding 2.7. CRDB's existing sitemap already satisfies this item on its own terms; no further work is proposed here, though it may be handed to a separate user-experience workstream if DCCE expects it presented within this package.

4. **Data Management Framework.** Present as one narrative heading covering four separately identifiable components:

   - **Glossary** — a business glossary and metric register recording, for each metric or term, its calculation logic in plain language, the domain team responsible for it, and any cross-domain interoperability standard it is subject to. This directly addresses the terminology mismatch identified in an earlier gap assessment, where the existing glossary — frozen at fifty-six terms since late May — was not updated when the conceptual data model was expanded in July.
   - **Conceptual Data Model** — six to ten stated architecture principles and a logical entity map. CRDB's existing model can be reused as the entity map, but its current dual-seal status should be resolved first: two deliverable records currently exist for it, both marked as sealed, with no supersession recorded between them; the earlier, smaller version should be marked superseded and the later, larger version treated as canonical. Once Decision A is made, the chosen paradigm should be documented and the five-part justification described in Section 3 attached to it.
   - **Governance** — a responsibility matrix using the five-role structure described under item 2, and a stewardship model. CRDB's existing governance material can be used as a starting point and checked against this structure rather than rebuilt.
   - **Reference Data** — the eight-column structure described in Finding 2.5, populated for three to five top-priority code lists selected using the four criteria set out there, with any deferred elements marked as deferred rather than omitted. CRDB's existing reference-data material is a specification only, with no data populated; this is the substantive work required for this item.

5. **Use Case and Demand Analysis.** A problem statement with measurable business impact, user personas and access patterns, current and proposed process flows, prioritized requirements, testable acceptance criteria, and sample-data validation with a recorded sign-off. CRDB's existing service-dossier material, produced during an earlier pivot away from a use-case inventory, can be reused but should be checked against this list, since the pivot itself was not previously validated against these criteria.

6. **Gap Analysis.** Use the combined format described in Finding 2.6: a dimension-scored matrix, covering dimensions 1 through 6 of the nine-dimension framework attributed to Hoseini, Quix, and Decker, with dimensions 7 through 9 explicitly noted as deferred to a later, build-stage assessment, feeding into a phased roadmap.

7. **Recommendations.** Strategic recommendations and an implementation roadmap with cost and benefit, using the same phase structure as item 6 for consistency across the deliverable set.

8. **Loss & Damage Data Model.** Pending Decision A, the recommended framing is the federated option, supported by the glossary and metric-register artifact described under item 4. That artifact can be built now regardless of which paradigm is ultimately chosen, since a shared register of Loss & Damage metric definitions is useful under any of the three options. CRDB's existing technical specification for this model is the most developed of the nine original categories, but it has no corresponding entry in the project's deliverable records; this should be corrected as part of this item.

---

## 5. Governance Items to Resolve Alongside the Content Work

These were identified in an earlier gap assessment of CRDB's records and are addressed here because they are inexpensive relative to the content work above.

- Resolve the dual-seal status of the Conceptual Data Model, as described under item 4.
- Add a deliverable record for the Loss & Damage Data Model, as described under item 8.
- Record a decision on the Reference Data Matrix and Building Blocks categories, both of which have seen no substantive activity since late May: either continue the Reference Data Matrix under item 4 as scoped above, or record explicitly that these categories are being retired, rather than leaving their status undocumented.

---

## 6. Suggested Schedule

| Days | Focus |
|---|---|
| 1–2 | Resolve Decisions A and B; resolve the Conceptual Data Model's dual-seal status; select the three to five reference-data elements. |
| 3–7 | Build the glossary and metric register; re-validate the use-case material against Finding 2.8; populate the reference-data structure. |
| 8–11 | Score the gap-analysis matrix across dimensions 1 through 6; draft the phased roadmap and recommendations; add the deliverable record for the Loss & Damage Data Model. |
| 12–14 | Check terminology and phase language for consistency across all eight items; prepare materials for the dissemination event. |

---

## Sources

Hoseini, S., Quix, C., & Decker, S. arXiv:2606.08811v1.

The full record of the literature review underlying this report — all questions posed, all material returned, and the independent check applied after each round — is retained in the `iteration-1`, `iteration-2`, and `iteration-3` folders alongside this report, for verification of any finding above.
