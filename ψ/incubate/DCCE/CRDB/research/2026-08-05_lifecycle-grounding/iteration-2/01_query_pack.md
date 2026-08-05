# Iteration 2 — Query Pack (deeper, topic-specific)

See `../AGY_INSTRUCTIONS.md` for command syntax, guardrails, and output conventions.

Context: iteration-1 corrected the working hypothesis — Glossary/CDM/Governance/RefData are four
separate disciplines that should stay visibly distinct under one "Data Management Framework"
narrative heading, not one merged document (source: DAMA-DMBOK discipline table + "boiling-the-ocean"
anti-pattern warning). These questions dig into the specific gaps iteration-1 left open. Note on Q1
for both notebooks: the exact phrase "Loss & Damage data model" returned zero hits last round —
these questions deliberately use generic modeling terminology instead.

## Notebook: Business requirement for SW development (`5133ef48-564c-40df-bdd1-142bb7e5bdf3`)

1. In requirements-engineering practice, how does a domain-specific data/requirements model (e.g. for one business area or risk domain) typically relate to an organization-wide conceptual data model referenced in a BRD/SRS — is it a bounded specialization, an extension, or an independently governed artifact?
2. Should a data-domain gap analysis for an early-stage blueprint use a dimension-scored requirements-conformance matrix, a phased maturity-roadmap format, or a hybrid — what does standard SRS/BRD practice recommend when the subject is data infrastructure maturity rather than a software feature set?
3. How is "data management framework" typically scoped within a business-requirements deliverable set — as an operational capability (data ops/pipelines) or a governance-and-standards artifact (policies, glossary, stewardship)?
4. For a 2-week-scoped requirements/analysis engagement, what concrete checklist distinguishes a "draft" deliverable that is still credible from one that is merely a placeholder — is there a standard minimum-content bar cited in the sources?
5. Do any of the sources treat "sitemap" or information-architecture artifacts as part of a business-requirements deliverable set, or is this consistently treated as outside BRD/SRS scope?

## Notebook: Enterprise Data Architecture (`3adf8897-245c-43c6-aec9-8977f2aab2fb`)

1. In DAMA-DMBOK or comparable enterprise data modeling practice, how does a subject-area or domain-specific logical data model (e.g. a specialized model scoped to one risk or loss domain) typically relate to an organization's central conceptual data model — is it a bounded-context specialization, an extension, or an independently governed artifact?
2. What is the standard scope and definition of a "Data Management Framework" as a named deliverable — does it refer to DAMA's operational "data management" discipline (day-to-day pipelines, storage, quality processes), or the broader governance + architecture + metadata + MDM program bundle? Which usage is more common in blueprint / pre-system-design engagements specifically?
3. What should a Master/Reference Data Management deliverable structurally contain at draft stage — e.g. what does a minimal reference-data matrix or code-list register look like before full production implementation?
4. What change-management or governance workflow does standard practice recommend for keeping a business glossary synchronized when the underlying conceptual/logical data model changes over time?
5. What is a minimal, achievable version of a "data product inventory" or "data management framework" deliverable for a 2-week, pre-system-design analysis engagement — which components can be represented as placeholders/scaffolding vs. must be substantively populated?
