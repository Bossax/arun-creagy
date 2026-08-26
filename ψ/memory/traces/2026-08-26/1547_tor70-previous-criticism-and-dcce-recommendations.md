---
type: trace
traceId: 8256f89e-b405-479b-91cf-9ee5cdffeb07
date: 2026-08-26
query: "Criticisms of previous TOR70 and recommendations to improve the DCCE climate adaptation web and data platform TOR"
target: "TOR70 national climate adaptation database TOR"
mode: deep
timestamp: 2026-08-26 15:47
friction_score: 1.00
coverage: [oracle, files, git, cross-repo, session-history-unavailable]
confidence: high
---

# Trace: TOR70 previous criticism and DCCE recommendations

**Target**: TOR70 national climate adaptation database TOR  
**Mode**: deep | **Friction**: 0.70 | **Confidence**: high

## Sources

- Current source: `ψ/incubate/DCCE/CRDB/output/2026-05-18_TOR-Review/TOR70_การพัฒนาระบบฐานข้อมูลด้านการปรับตัว_2569-08-01.docx`
- Previous version: `ψ/incubate/DCCE/CRDB/output/2026-05-18_TOR-Review/TOR70_original-พัฒนาระบบฐานข้อมูล_9-July-2026.md`
- Detailed critique: `ψ/incubate/DCCE/CRDB/output/2026-05-18_TOR-Review/TOR70-development-of-climate-adaptation-databse-comments.md`
- Validated failure modes: `ψ/incubate/DCCE/CRDB/output/2026-05-18_TOR-Review/TOR70_failure-modes-literature-validation.md`
- Strategic recommendations: `ψ/incubate/DCCE/CRDB/output/2026-05-18_TOR-Review/2026-05-19_TOR-Strategic-Redlines-Memo.md`
- Procurement/NFR learning: `ψ/memory/learnings/2026-08-05_in-two-stage-enterprise-data-platform-procurement.md`

## Criticisms of previous TOR

1. **Workshop substituted for requirements discovery.** One workshop with 20 people was insufficient to validate personas, business questions, service priorities, and acceptance requirements.
2. **Data collection was not use-case-led.** The TOR risked data hoarding and dashboard construction without a traceable decision or user need.
3. **Dataset quantity was gameable.** The previous ≥100-dataset target rewarded volume, including low-value or duplicated material, without freshness, quality, lineage, or usability thresholds.
4. **Unstructured content was under-specified.** It did not clearly distinguish file storage, metadata discovery, full-text/OCR search, extraction, editorial synthesis, and copyright/permission responsibilities.
5. **Taxonomy and architecture could lock in too early.** The TOR required broad classification before requirements and architecture were sufficiently validated, with unclear ownership of evolving vocabularies and metadata.
6. **The CMS was implicitly overloaded.** CMS, data ingestion, GIS, dashboards, cataloguing, IAM, audit, and data services were treated as one broad platform responsibility, increasing monolith and vendor-lock-in risk.
7. **Dashboards and search had weak acceptance logic.** Generic requirements such as “easy,” “accurate,” or “appropriate” were not objectively testable; dashboards lacked named business questions, and “keyword search” left the expected search depth unclear.
8. **Technical and climate-domain expertise were unbalanced.** A technically capable contractor could still lack the climate knowledge-broker capacity needed to turn evidence into policy-useful content.
9. **Delivery controls were incomplete.** The previous version left schedule and payment sections effectively blank and had a major budget inconsistency: ฿25 million stated in the TOR and detailed budget.
10. **Public communication scope was disproportionate.** The 100-person launch, exhibition, media, video, ten articles, ten infographics, and 400 promotional items risked consuming budget needed for durable data pipelines and platform operations.

## Recommendations to DCCE

### A. Reframe the procurement objective

- Define the asset as a **national climate data space / guided synthesis platform**, not merely a website or document portal.
- Identify a small number of priority products and business questions first: existing risk tools, A-BTR reporting, and loss-and-damage analysis are candidates already identified in project work.
- Separate platform build from optional public communications and event production.

### B. Add a staged discovery and governance gate

- Replace the single workshop with: stakeholder interviews/workshop, use-case and service prioritisation, prototype validation, requirements traceability matrix, and formal System Requirements Review.
- Require an **Alignment Map** linking each use case to datasets, data products, functional requirements, architecture decisions, and acceptance tests.
- Assign named DCCE owners for data domains, products, metadata, security, and acceptance decisions.

### C. Replace volume KPIs with trust and usability KPIs

- Retain a minimum dataset number only as a floor; require per-dataset metadata, provenance, owner, update frequency, quality profile, access rights, disclosure level, and intended use.
- Add measurable freshness, completeness, validity, uniqueness, lineage, and ingestion-success thresholds.
- Require data contracts with source agencies and automated validation/circuit-breaker rules for failed ingestion.
- The current DOCX’s ≥30 prepared datasets is clearer than the previous target, but still needs quality and use-case acceptance criteria.

### D. Specify a modular architecture

- Separate data storage, ingestion/transformation, metadata/catalogue, GIS/spatial services, semantic/analytics services, CMS/content workflow, identity/access, audit, and presentation layers.
- Require API-first interoperability, open formats, versioned schemas, exportability, and documented migration/exit paths.
- Allow taxonomy and schema evolution through versioning and governance rather than a one-time frozen classification.
- Treat CMS as a thin content/workflow layer, not the system’s analytical or integration engine.

### E. Make content and search deliverables explicit

- Decide whether the contract includes automated OCR/full-text indexing or only metadata-based discovery of PDFs and media.
- Bound human editorial synthesis to named flagship products, with source citations, review responsibility, revision limits, and rights clearance.
- Define search acceptance: metadata search, full-text search, filters, relevance, response time, and supported file types.

### F. Make the TOR contractually testable

- Convert adjectives into measurable NFRs: uptime, response time, accessibility, browser/device support, backup frequency, RPO/RTO, security severity thresholds, and defect closure rules.
- Require test plans and evidence for functional, integration, data validation, responsive UI, UAT, penetration, backup/restore, and disaster recovery testing.
- Make source code, infrastructure-as-code/configuration, schemas, metadata, test evidence, manuals, and deployment runbooks explicit deliverables.

### G. Fix procurement and sustainability design

- Align budget, staffing months, milestones, scope, and payment gates; state what is excluded or optional.
- Distinguish business NFRs owned by DCCE/design authority from system NFRs delivered by the build contractor.
- Require a post-delivery operating model: data-owner responsibilities, update calendar, support/warranty SLA, maintenance budget, and handover competency.
- Add a climate knowledge-broker/content governance role or require a named climate-domain partner in the team.

## Current DOCX assessment

The DOCX improves the previous version by adding a 270-day schedule, four payment milestones, explicit security/testing, a 30-dataset floor, metadata fields, and clearer installation/training requirements. It also removes the large public-launch package and reduces the budget to ฿12.5 million.

The principal unresolved issue is alignment: the objectives still promise articles, infographics, multimedia, and storytelling, while the detailed scope no longer gives those outputs clear quantities, ownership, quality criteria, or budget. The reduced target audience also weakens the mandate for multi-agency adoption. These should be resolved before procurement.

## Friction analysis

**Score**: 1.00 — the evidence is physically present in the repository and indexed by Oracle, and the goal was answered with high completeness.  
**Coverage**: oracle, files, git, cross-repo; session history unavailable (`unknown-host`).  
**Goal check**: Yes. The trace identifies criticisms of the previous TOR and recommendations that can be presented to DCCE. The DOCX was inspected as the current source; no external procurement-law verification was performed.

### Potential Ledger Yields (T-E-D-A Hypothesis)

- **[T] Potential Trigger**: The previous TOR could produce a static, manually maintained portal rather than a durable, trusted climate data asset.
- **[E] Supporting Evidence**: Previous TOR, detailed clause critique, literature-validated FM1–FM7 report, strategic redlines, current DOCX.
- **[D] Potential Decision**: Re-scope around validated priority use cases, modular data architecture, measurable trust/quality criteria, and explicit operating ownership.
- **[A] Target Asset**: DCCE’s TOR70 procurement package for the national climate adaptation web and data platform.
