# CRDB Deliverable Redirection Plan — v2

**Date:** 2026-08-06
**Supersedes:** `99_FINAL_crdb-redirection-plan.md` (v1, 2026-08-05). v1 is retained, not deleted, as the record of Phase A. This document does not repeat v1's content by reference alone — every finding v1 got right is restated here in corrected and deepened form, so this file stands on its own as the operative plan.

**Why a v2 was needed.** Boss rated v1 6/10 and flagged four specific defects: (1) it asked the wrong question about the LDM — treating it as a pending architecture-paradigm choice when it is a delivered artifact for a single sub-domain, of low importance to which package it sits in; (2) it never answered the actual bridging question this project needs — what a business-requirements handoff package to TOR70 should contain, and how CRDB's outputs map onto it; (3) it did not identify which stage of the software/data development lifecycle CRDB is actually at; (4) its redirection plan for the eight deliverables "looks good but lacks depth" because it was never checked against an ideal business-requirements package. This v2 corrects all four, using three primary sources read directly (not sourced from the two research notebooks) plus a fifth iteration of grounded literature research (Phase B, iterations 4–5) that Phase A did not have.

---

## 0. What Changed From v1

- **Dropped entirely:** v1's "Decision A — which LDM-to-CDM paradigm to adopt" and the three-paradigm (centralized/federated/semantic) framing built around it. This framing was an error in Phase A. The LDM is a delivered logical data model for the Loss & Damage sub-domain; no paradigm decision is pending for it, and which package it is filed under is a low-importance housekeeping question, not a research question. See Settled Finding 1 below.
- **Dropped:** v1's "Decision B — whether CRDB's 'Data Management Framework' usage matches DCCE's wording." This is now settled, not open: CRDB's phase placement (Planning + Requirement Analysis + Design, with no physical system yet built) makes the broad sense the only sense that could apply — there is no day-to-day operational data management to speak of yet.
- **Added:** an explicit lifecycle placement of CRDB within the Database System Development Lifecycle (DSDLC), grounded in a primary source read directly rather than in the two general-literature notebooks (Section 1).
- **Added:** a full grounding of what a business-requirements handoff package for an enterprise data platform contains, and how CRDB's eight deliverables map onto it (Sections 2–3) — the question v1 never asked.
- **Deepened:** the eight-item redirection plan (Section 4) now incorporates Business-NFR content, Functional Specification structure, use-case prioritization mechanics scaled to DCCE's actual size, and a Data Contract / Assumption Log — none of which existed in v1's version of this section.

---

## 1. Where CRDB Sits in the Lifecycle

Source: `ψ/incubate/DCCE/CRDB/inbox_source/The Enterprise Data System Development Lifecycle.md`, cross-checked against DCCE's own accepted framing in the 2026-06-11 Strategic Alignment Deck and Director Toey meeting reflection.

The governing model is a **7-phase Database System Development Lifecycle (DSDLC)**: Planning, Requirement Analysis, Design, Development, Testing, Deployment, Maintenance. This is confirmed as fixed (Settled Finding 3, `SCOPE_LEDGER.md`).

- **CRDB = Planning + Requirement Analysis + Design.** Its role is data architect, information architect, and business analyst — not system architect, not software engineer (Settled Finding 4). Concretely: CRDB stock-takes datasets, information products/services, use cases and needs; designs a conceptual data model for key domains and a logical data model (the LDM) for the Loss & Damage sub-domain; produces a glossary; and introduces a metadata standard for the discovery layer.
- **TOR70 = Development + Testing + Deployment + Maintenance.** This is the downstream contractor's scope: physical/system design, co-designed with CRDB's data architect to ensure the built system serves the business requirements CRDB defines, but built and tested by TOR70.

This phase boundary affects how CRDB's remaining work should be scoped. The primary source frames CRDB's phase as an early requirements-gathering stage that produces a contractual baseline — the standard approach in IT procurement for reducing uncertainty (which is highest at the start of a project and narrows only as concrete decisions are made) before a fixed-price build begins. Without a frozen baseline, a common failure occurs: an enterprise launches a fixed-price build with unresolved requirements, and the vendor, protecting its margin against work it did not price in, responds by cutting corners (skipping tests, refactoring, and documentation), inflating its bid with a 20–50% risk buffer, or shipping code with incomplete business logic (a defect category tracked as CWE-840) because no domain expert had defined the rule before a developer had to invent one under deadline pressure.

The practical implication for CRDB: the remaining two weeks of work should freeze enough domain logic, in a form TOR70 can be held to at fixed price, that this failure mode does not occur. Each item in Section 4 below can be checked against that test: does this artifact reduce the number of things TOR70 would otherwise have to invent mid-build?

This also fixes DCCE's own accepted role split (from the Strategic Alignment Deck, presented to and accepted by Director Toey): DCCE is to be **product owner, data owner, and data steward** of its own platform — the authoritative data custodian in the climate-change field — while CRDB, in this project, builds the requirements and models that let DCCE occupy that role, and TOR70, in the next project, builds the system to serve it. DCCE's own accepted 3-step handoff process (Settled Finding 5) is: (a) prioritize use cases and produce Functional Specifications for TOR70 to build; (b) define minimum website content scope for TOR70; (c) review and certify the governance framework for adoption. Sections 3–4 below are organized to serve exactly these three steps.

---

## 2. What a Business-Requirements Package for an Enterprise Data Platform Contains

Grounded in Phase B, iterations 4–5 (requirements-engineering literature and enterprise-data-architecture literature, queried in parallel and cross-checked against each other and against real-world practice by a second-opinion pass).

### 2.1 The component set, and who owns which half

Both literatures converge on the same functional core, though they group it differently. Combined, a well-formed package contains:

| Component | Owner | Notes |
|---|---|---|
| Business drivers & workload profiling | CRDB | Measurable business impact, not aspiration |
| Source inventory with documented caveats (per source: business impact, semantic meaning, origin, refresh frequency, retention, caveats, access pattern, QA rules, output schema) | CRDB | This is CRDB's Data Inventory, made complete |
| Business glossary / governed semantic layer | CRDB | Non-negotiable in both literatures; CRDB's existing Glossary pillar |
| Data-quality & ingestion-validation rules (numeric, testable) | CRDB | "Data must be clean" is a named anti-pattern in both literatures |
| RBAC / access mapped to personas | CRDB | Not a flat policy — per-persona |
| Prioritized data-product inventory | CRDB | CRDB's Data Product Inventory pillar |
| Business NFRs (see 2.2) | **CRDB** | Corrected from Phase A — see below |
| Functional Specification per prioritized use case (see 2.3) | CRDB | The core handoff artifact for step (a) |
| Data Contract + Assumption Log (see 2.4) | CRDB | Standard mitigation for the "ambiguous adjectives" failure mode |
| Governance/RACI model, sign-off gate | CRDB | Standalone deliverable, not folded into the narrative — corroborates DCCE's step (c) |
| System NFRs (index strategy, node sizing) | TOR70 | Not CRDB's job |
| Bidirectional Requirements Traceability Matrix (RTM) | TOR70 | Confirmed out of scope for CRDB (Settled Finding, Phase A) |
| Procurement terms: cost, schedule, staffing, acceptance procedure | DCCE's procurement instrument | Kept structurally separate — see 2.5 |

**Structure of the whole package:** one coherent, cross-referenced content baseline — requirements, data design, and governance context living together, not scattered across disconnected documents, so TOR70 does not have to reconcile them — but with contractual/procurement mechanics kept in a separate instrument that references the baseline (see 2.5), not merged into it.

### 2.2 Business NFRs vs. System NFRs

Phase A treated NFRs as entirely out of scope for CRDB, deferring them wholesale to TOR70. This was corrected in Phase B, iteration 4, and reinforced with concrete content in iteration 5: **NFRs split into two kinds**, and only one of them is TOR70's.

- **System NFRs** (index strategy, node sizing, infrastructure-level SLI/SLO/SLA percentile targets, formal Configuration Control Board) — TOR70's job. Adopting this heavier apparatus in CRDB's blueprint would over-engineer a coherent-draft deliverable.
- **Business NFRs** (data-freshness/refresh-cadence targets, regulatory and compliance thresholds relevant to DCCE's own regulatory context, numeric data-quality divergence thresholds, access-pattern latency expectations by persona, retention/lifecycle rules, and — worth naming explicitly — semantic/metric consistency, i.e., one governed definition per metric, which maps directly onto CRDB's glossary work) — **CRDB's job**, to be captured directly in the blueprint, not deferred as "raw material" for TOR70 to build an NFR document from later.

**Capture form:** a lightweight thresholds table (requirement ID, description, quantified target, priority, owner) plus supporting narrative. Not the full SLI/SLO/SLA/percentile apparatus or the ISO/IEC 25010 system-NFR taxonomy — that belongs to TOR70.

**Note for DCCE's domain specifically:** the literature's business-NFR examples are drawn from generic commercial data-warehouse and modern-platform contexts (FinOps ceilings, EU AI Act lineage requirements), not from a Thai public-sector climate-data platform. CRDB should select from this list the categories that actually apply to DCCE's context (freshness, compliance thresholds, access latency by persona, retention, semantic consistency) and treat categories like FinOps cost ceilings or AI Act-style lineage as probably not applicable rather than importing them uncritically.

### 2.3 Functional Specification structure for a single prioritized use case

Both literatures agree on the governing rule: freeze the logical "what" and "why" (outcomes, inputs, constraints, success criteria); leave physical implementation choices to TOR70. Both independently ban subjective adjectives ("fast," "clean," "secure") and both exclude project-management content (cost, schedule, methodology) from this document entirely.

**Content (data-pipeline half, most directly reusable by CRDB):**
1. Business context and persona/access-pattern detail
2. Inbound source and pipeline parameters
3. Logical transformation rules
4. Known-caveats/risk log
5. Verifiable data-quality rules and success metrics
6. End-user-validated sample data with a recorded sign-off, before any backend work begins

**Discipline (formal SRS half, layered on top):** unique requirement identifiers; Event-Condition-Action (ECA) style behavior statements; a four-part external-interface taxonomy (user, hardware, software, communications); complete input-response coverage, not just the happy path; and a rule against unresolved "TBD" placeholders — each one that cannot be avoided must carry a named owner and a resolution deadline, not be left silently blank.

Given the two-week timeline, some fields may legitimately remain TBD — but logged against an owner and deadline, not silently omitted. This reconciles the coherent-draft quality bar with contract-ready discipline rather than treating the two as in tension.

**Explicit exclusion list** (leave to TOR70): physical server specs, index-tuning strategy, storage layout.

### 2.4 Data Contract + Assumption Log

A **Data Contract** formalizes the schema and quality agreement between a data producer and consumer to prevent uncontrolled schema drift. Structure, directly reusable from CRDB's existing data-inventory and glossary work: schema and semantic-mapping definitions (tied to the governed glossary), data-quality rules and thresholds, operational parameters (ingestion frequency, retention/versioning), access modalities and latency expectations, and a known-caveats section. CRDB should mark, in narrative form, which fields are intended to be machine-enforced later (e.g., a JSON Schema validation at ingestion) — that automation is TOR70's implementation concern, not something CRDB builds, but naming it tells TOR70 what to automate.

An **Assumption Log** exists to bound liability by making explicit what the requirements process assumed rather than verified — a living risk register ("if this assumption changes, these requirements must be revisited"), not a one-time disclaimer. Given CRDB is a fixed, time-boxed blueprint engagement rather than an ongoing Agile program, the right format is the **formal, point-in-time SRS-style "Assumptions and Dependencies" section** (ID, category, stated assumption, the responsibility it bounds), not a continuously-edited Agile wiki page.

Both artifacts are the standard, literature-attested mitigation for the single most common fixed-price failure mode both literatures name: ambiguous, unmeasurable adjectives that cannot be tested at acceptance and therefore cannot bound a vendor's liability.

### 2.5 The technical/business content boundary vs. the procurement boundary

Both literatures agree, independently: the technical/business side covers everything about **what** the platform must do and how well (business drivers, logical architecture, source/interface inventory, transformation rules, quality rules, security/access constraints, validated sample data, quantified Business NFRs). The procurement side covers everything about **how the engagement is run and paid for** (cost, delivery schedule, staffing, reporting, formal acceptance procedures) — and, separately, **development methodology and tooling** (Agile ceremonies, CI/CD pipeline choices, Git workflow) belongs on the procurement/process side too: CRDB should not pre-decide how TOR70's team works, only what it must deliver.

**The connective mechanism:** CRDB's prioritized Functional Specification functions as a technical appendix that DCCE's Statement of Work formally references by name — the SOW states the vendor agrees to deliver a system satisfying the prioritized requirements in the appendix, for a fixed price, connecting the commercial contract to the technical baseline without merging the two documents into one. CRDB does not draft that reference itself, but its priority ratings and use-case identifiers must be stable and unambiguous enough to be cited that way. (How Thai government procurement documents specifically structure this kind of reference is outside what the literature can answer — an open question for Boss's judgment, not a research question, and adjacent enough to the out-of-scope line-agency topic that it should only be pursued with explicit sign-off that it's a distinct question.)

### 2.6 Use-case prioritization, scaled to DCCE's actual size

Both literatures frame prioritization the same way at the top: narrow a broad candidate list to a small, well-justified initial priority group using multiple scoring criteria, weighting feasibility/readiness as heavily as business impact.

**Mechanics, combined:**
1. Score DCCE's 8 candidate products against selection criteria: low cost to deliver, small in scale, high impact, useful across multiple teams, easy to deliver, and backed by a sponsor with adequate funding.
2. Apply a five-point Critical / High / Medium / Low / Future scale to rank the shortlisted use cases (and their associated Business NFRs).
3. Resolve stakeholder disagreement via one-on-one interviews (not group workshops, so no single voice dominates), forcing ambiguous goals into quantified targets, documenting assumptions explicitly.
4. A final review milestone freezes the prioritized baseline; ad-hoc changes are blocked afterward.

**Scale correction:** the enterprise-data-architecture literature's own numeric anchor for an initial priority group is 10–20 critical data assets — a figure from large enterprise data-mesh programs, not transferable to DCCE's much smaller candidate set of 8 named products. For DCCE, a realistic initial group for the TOR70 handoff is **one or two use cases**, not ten to twenty. This is the number Functional Specifications (Section 2.3) should actually be written for in the two weeks available — attempting more than that repeats the same scope failure both literatures separately warn produces fixed-price contract breakdowns: trying to cover the full candidate list at once instead of a manageable subset.

---

## 3. Mapping CRDB's Nine Categories, and DCCE's Eight Requested Items, onto the Package Above

CRDB's nine self-organized categories (Sitemap, Use Cases, Data Inventory, Glossary, CDM, LDM, Governance, Reference Data, Building Blocks) do not map 1:1 onto DCCE's eight requested items (data inventory, data product inventory, sitemap, data management framework, use case & demand analysis, gap analysis, recommendations, LDM). This mapping was not produced in Phase A; it is below.

| Business-requirements package component (Section 2)                             | CRDB category that supplies it | DCCE deliverable item it lands in                   |
| ------------------------------------------------------------------------------- | ------------------------------ | --------------------------------------------------- |
| Source inventory with caveats                                                   | Data Inventory                 | Item 1 (Data Inventory)                             |
| Prioritized data-product inventory + Data Contracts                             | Data Inventory + Use Cases     | Item 2 (Data Product Inventory)                     |
| Business glossary / semantic layer                                              | Glossary                       | Item 4 (Data Management Framework)                  |
| Conceptual data model + architecture principles                                 | CDM                            | Item 4 (Data Management Framework)                  |
| Governance/RACI + sign-off gate                                                 | Governance                     | Item 4 (Data Management Framework)                  |
| Reference/master data (8-column structure)                                      | Reference Data                 | Item 4 (Data Management Framework)                  |
| Functional Specifications, Business NFRs, Assumption Log, prioritization        | Use Cases (+ new work)         | Item 5 (Use Case and Demand Analysis)               |
| Dimension-scored gap matrix + roadmap                                           | Gap analysis (new synthesis)   | Item 6 (Gap Analysis)                               |
| Strategic recommendations + phased roadmap                                      | (new synthesis)                | Item 7 (Recommendations)                            |
| LDM + shared metric register                                                    | LDM                            | Item 8 (LDM)                                        |
| — (UX/information-architecture artifact, not a package component per Section 2) | Sitemap                        | Item 3 (Sitemap) — stands outside the DMF narrative |
| — (not part of this package; not researched here, out of scope)                 | Building Blocks                | No direct item — see Section 6                      |

This map is what makes CRDB's output "directly usable as TOR70's input" per DCCE's step (a) and (b): every package component in Section 2 has a named home in one of DCCE's eight items, and every one of CRDB's nine internal categories is accounted for (including the two — Reference Data Matrix, Building Blocks — that need an explicit housekeeping decision rather than more content work; see Section 6).

---

## 4. Redirection Plan: The Eight Deliverable Items

1. **Data Inventory.** Cover approximately eighty percent of current systems, owners, and consumers, with detailed capture (the nine-field source profile from Section 2.1) scoped to the ten most business-critical assets rather than the full estate. CRDB's existing data catalog is a starting point; not updated since early June, it needs re-scoring against the top-ten criterion.

2. **Data Product Inventory.** For the same assets, add business metadata (definitions, metric logic), a governance responsibility assignment using five named roles (Data Owner, Data Steward, Data Architect, Data Engineer, Governance Council) mapped to five decision types (quality thresholds, new-source approval, access policy, definition-conflict resolution, architecture-change approval), a compliance classification, and — new in this version — a Data Contract per priority asset (Section 2.4). Automated quality scoring and enforcement tooling remain out of scope at this stage.

3. **Sitemap.** Confirmed outside the Data Management Framework narrative (Section 2.1, 3). CRDB's existing sitemap, organized around the stages of the climate-adaptation cycle, already satisfies this item on its own terms. No further content work is proposed here; DCCE's own note on treating info pages as governed digital assets (from the Director Toey meeting) is a matter for the governance work in item 4, not a sitemap redesign.

4. **Data Management Framework.** One narrative heading, four separately identifiable components:
   - **Glossary** — business glossary + metric register (calculation logic, responsible domain team, cross-domain interoperability standard per term). Directly addresses the drift already identified: the glossary, frozen at fifty-six terms since late May, was not updated when the CDM expanded in July.
   - **Conceptual Data Model** — six to ten stated architecture principles plus the logical entity map. Resolve first the fact that two final, sealed deliverable records currently exist for it with no record of which one supersedes the other — the earlier, smaller version should be marked superseded.
   - **Governance** — the five-role responsibility matrix from item 2, plus a stewardship model and the sign-off gate that corroborates DCCE's step (c). CRDB's existing governance material is a starting point to check against this structure, not rebuild.
   - **Reference Data** — the eight-column structure (business definition + calculation logic, technical schema + valid ranges, system of record, owner/steward, compliance classification, validation rules) populated for three to five top-priority code lists, selected against four criteria: ties to a specific business objective, covers an entity shared across functions, has a reliable-enough source to document now, and any deferred elements marked deferred (not silently omitted) using a standard priority scale. CRDB's existing reference-data material is a specification only, with no data populated — this is the substantive work required here.

5. **Use Case and Demand Analysis.** This item changes the most from v1. It should now contain, per Section 2.6, one or two use cases (not the full candidate set) selected via the quick-win + five-point-scale process, each with a full Functional Specification (Section 2.3: context/persona, source/pipeline parameters, transformation rules, caveats, quality rules, validated sample data with sign-off — under the formal discipline of unique IDs, ECA statements, external-interface taxonomy, and owner-and-deadline-logged TBDs), its Business NFRs captured in the lightweight thresholds table (Section 2.2), and an Assumption Log entry (Section 2.4). CRDB's existing service-dossier material, produced during an earlier pivot away from a use-case inventory, can be reused as raw content but must be checked against this fuller structure, since the pivot itself was never validated against it.

6. **Gap Analysis.** A dimension-scored matrix covering dimensions 1–6 of the nine-dimension DATER framework (Hoseini, Quix & Decker, arXiv:2606.08811v1) — Control/Governance/Trust (1–3) and Data Modeling/Understanding (4–6) — with dimensions 7–9 (system integration, data virtualization, analytics/ML support) explicitly noted as deferred to a later, build-stage assessment. Feeds into a phased roadmap.

7. **Recommendations.** The prioritized use-case selection called for in Section 2.6 already has a concrete answer, proposed in CRDB's own TOR70 communication deck rather than invented here: three already-existing analytical products should form the project's main focus — the spatial risk database, the hazard/exposure map, and the Climate Risk Index — plus two new use cases with clearly demonstrated demand to take up after those: the A-BTR reporting system and disaster-loss-statistics analysis. This recommendation carries a paired budget note from the same deck: reallocate funds from support staffing and IT tooling toward product research/design and content-synthesis expertise, since that is where the actual constraint on delivering the second group sits. Strategic recommendations and an implementation roadmap with cost and benefit framing should be built around this concrete list, using the same phase structure as item 6 for consistency across the deliverable set. Where recommendations touch DCCE's own procurement instrument (e.g., referencing the Functional Specifications as a technical appendix — Section 2.5), state the mechanism but do not draft DCCE's procurement language.

   The redirected deliverables above are also the direct answer to specific, already-validated flaws in TOR70 itself: a Functional Specification with a recorded sign-off gate (Section 2.3) and the Requirements Traceability Matrix it feeds (item 5) directly close the "no use-case-first requirements gathering" gap that the TOR70 literature validation confirmed as its most strongly supported failure mode; the Business-NFR thresholds table (Section 2.2) replaces the TOR's ungoverned "not less than 100 datasets" quantity target with a testable quality bar, closing the data-quantity/KPI-trap failure mode; and the same Functional Specification's ban on subjective adjectives closes the failure mode around unmeasurable dashboard and content-quality language ("accurate," "concise," "easy to understand"). Where TOR70 itself still needs amendment rather than being fixable by a CRDB deliverable — the CMS scope-overreach failure mode (one system asked to do content management, GIS processing, dashboarding, and identity management at once) chief among them — that is a redline for TOR70's text directly, not something CRDB's deliverables can compensate for.

8. **Loss & Damage Data Model.** The LDM is a delivered artifact for a single sub-domain — not a pending architecture-paradigm decision (Settled Finding 1; this corrects the framing error in v1). The remaining work is: (a) add a missing deliverable record for it — it currently has no entry in the project's deliverable records despite being the most developed of CRDB's nine original categories, and (b) if useful, connect it to the shared glossary/metric-register artifact from item 4, since a shared register of Loss & Damage metric definitions is useful regardless of how the LDM ultimately sits relative to the CDM. Which package (this item vs. folded into item 4) it is filed under is a low-importance housekeeping call, not a research question.

---

## 5. The Bridge to TOR70: What It Still Needs to Do, and How It Should Work

Sections 1–4 describe what CRDB hands off. This section describes what happens on the other side of that handoff: what TOR70 still has to do beyond what is currently written in its terms of reference, and how its own development process should be organized so it actually uses what CRDB provides instead of rediscovering the same ground.

### 5.1 What CRDB hands off

By the end of the two weeks described in Section 7, CRDB's package for TOR70 consists of: a Functional Specification for each of the one or two priority use cases (Section 2.3), each carrying its own Business NFR thresholds table and Assumption Log entry; a Data Contract for each priority data product; the glossary and metric register; the conceptual data model and the Loss & Damage logical data model; a governance responsibility matrix with a sign-off gate; and the gap analysis and recommendations. All of it is referenced as a technical appendix in DCCE's Statement of Work for TOR70, so the fixed-price contract is anchored to a specific, named baseline rather than a general description of intent.

### 5.2 What TOR70 still needs to do, beyond what the current TOR draft asks for

CRDB's package resolves the requirements side of the handoff, but several things remain squarely TOR70's own work, and a few of them are not adequately covered by the TOR text as it currently stands:

1. **Physical and system design.** TOR70 designs the database schema, server architecture, and data pipelines to satisfy CRDB's conceptual and logical models — co-designed with CRDB's data architect, not invented independently from a blank page.
2. **System-level non-functional requirements.** CRDB defines the business-level thresholds (Section 2.2); TOR70 is responsible for the infrastructure-level implementation of those thresholds — server sizing, index strategy, and a formal process for tracking and approving any change to them once the system is built.
3. **Splitting the single content-management component into separately scoped services.** The current TOR asks one system to handle content management, spatial data processing, dashboard building, metadata cataloging, identity and access management, and audit logging all at once. This should be split into distinct services, each with its own acceptance criteria, rather than one component implicitly expected to do all of it — this is a change to the TOR text itself, not something CRDB's deliverables can compensate for.
4. **Automated processing of long-form documents.** The current TOR expects consultants to manually rewrite academic reports into summary articles and infographics with no stated tooling or review-round limit. Automated text-extraction and search indexing should be the primary mechanism for making these documents usable, with manual human writing reserved for a small, explicitly bounded set of flagship publications.
5. **Building the actual requirements traceability matrix.** CRDB provides the Functional Specifications the matrix must trace back to; TOR70 builds and maintains the matrix itself, connecting each build task and test case to a specific requirement.
6. **Automated enforcement of the Data Contracts.** CRDB defines the contract content; TOR70 implements the machine checks (for example, schema validation run at ingestion and in the build pipeline) that enforce it.
7. **Choosing storage and table formats.** TOR70 should commit to open, non-proprietary formats rather than a single named technology stack decided before requirements were validated, to avoid a costly migration later.
8. **Acceptance testing tied to CRDB's quantified targets.** The current TOR already lists several testing categories (function, sub-system integration, data quality, display, security, performance and availability, user acceptance). Each of these should be scored against the specific numeric targets in CRDB's Business NFR tables and Functional Specification success metrics, not against general descriptions such as "accurate" or "easy to understand."

### 5.3 How TOR70's development process should be organized

1. Start from CRDB's Functional Specifications as the frozen technical baseline; do not reopen requirements discovery once the build begins.
2. Validate the system design against one priority use case first, before extending the same architecture to the second, rather than committing to one full architecture for all use cases and future growth at once.
3. Validate each build milestone with DCCE through working prototypes, not a single end-of-phase demonstration — the same iterative validation principle CRDB itself should be following during the two weeks described in Section 7.
4. Hold a formal review and sign-off at each phase transition (for example, before moving from design into build, and before moving from build into deployment), consistent with the change-control discipline described in Section 2.
5. Keep technical documentation generated from the actual codebase where possible (for example, automatically generated data lineage and metadata), rather than maintaining separate static diagrams that go out of date.
6. Carry the Assumption Log forward through the build. If an assumption changes, revisit the requirement it supports rather than reinterpreting it without a recorded decision.
7. Keep DCCE acting as product owner and data owner throughout the build, with its own staff functioning as data stewards day to day — the governance structure CRDB defines should be the way the project actually runs, not a document filed away after sign-off.

---

## 6. Governance Housekeeping (inexpensive, alongside the content work)

- Resolve the Conceptual Data Model's two conflicting sealed records (item 4).
- Add a deliverable record for the LDM (item 8).
- Record an explicit decision on **Reference Data Matrix** and **Building Blocks** — both dormant since late May: either continue Reference Data Matrix under item 4 as scoped above, or record explicitly that it and Building Blocks are being retired, rather than leaving their status undocumented. Building Blocks in particular has no home in the package map in Section 3 and should be either mapped or formally closed.

---

## 7. Suggested Schedule

| Days | Focus |
|---|---|
| 1–2 | Resolve the CDM's two conflicting sealed records; select the 1–2 priority use cases (Section 2.6) and the 3–5 reference-data elements; decide whether to continue or retire Reference Data Matrix / Building Blocks. |
| 3–7 | Build the glossary/metric register; draft the Functional Specification(s) for the selected use case(s) including Business NFR table and Assumption Log entries; populate the reference-data structure; draft Data Contracts for the top-priority data products. |
| 8–11 | Score the gap-analysis matrix across DATER dimensions 1–6; draft the phased roadmap and recommendations; add the LDM deliverable record; note in the recommendations how the requirements document should be referenced by the procurement contract. |
| 12–14 | Cross-check terminology and phase language across all eight items; verify every Functional Specification's TBDs carry an owner and deadline; prepare materials for the dissemination event. |

---

## Sources

**Phase A (iterations 1–3):** requirements-engineering literature ("Business requirement for SW development" notebook) and enterprise-data-architecture literature ("Enterprise Data Architecture" notebook), including Hoseini, S., Quix, C., & Decker, S., arXiv:2606.08811v1 (DATER framework). Full record in `iteration-1`, `iteration-2`, `iteration-3`.

**Phase B (iterations 4–5):** the same two notebooks, re-queried on the CRDB→TOR70 bridge-package question specifically. Full record, including raw extracts and agy's second-opinion feedback, in `iteration-4`, `iteration-5`.

**Primary sources, read directly (grounding Section 1 and the Settled Findings this document relies on):**
- `ψ/incubate/DCCE/CRDB/inbox_source/The Enterprise Data System Development Lifecycle.md`
- `ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/2026-06-11-Strategic-Alignment-Deck-Final.md` (presented to and accepted by Director Toey)
- `ψ/incubate/DCCE/CRDB/inbox_note/2026-06-11-Meeting-with-Director-Toey-Reflection.md`
- `ψ/incubate/DCCE/CRDB/output/2026-05-18_TOR-Review/Slide-Deck-โครงการพัฒนาระบบฐานข้อมูลด้านการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศของประเทศ.md` — source of the concrete three-plus-two use-case prioritization in item 7
- `ψ/incubate/DCCE/CRDB/output/2026-05-18_TOR-Review/TOR70_failure-modes-literature-validation.md` — source of the failure-mode crosswalk in item 7

`SCOPE_LEDGER.md` in this same folder is the operational record of what was settled and what remained open at each point in Phase B, and should be consulted alongside this document for the reasoning trail behind any given finding.
