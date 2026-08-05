# Research Objective — CRDB Lifecycle Grounding

**Date**: 2026-08-05
**Owner**: Boss (Claude + agy joint research)

## Objective

Ground CRDB's 8-item deliverable set — data inventory, data product inventory, sitemap, data
management framework, use case & demand analysis, gap analysis, recommendations, and LDM (Loss &
Damage data model) — against authoritative requirements-engineering and enterprise-data-architecture
practice, in order to determine, with evidence rather than assumption, which of CRDB's existing
pillar outputs can be rearranged, enriched, and reprocessed into industry-shaped deliverables at a
coherent-draft (not production-ready) quality bar, within the 2 weeks remaining before the
dissemination event.

## Background

CRDB's team self-imposed a 9-pillar physical directory taxonomy that does not map 1:1 onto what DCCE
actually asked for. RTM and NFR artifacts (standard for a system-design engagement) are **out of
scope** — CRDB is a pre-system-design blueprint/analysis engagement, not TOR70's system build. A
first-pass mapping (done from general knowledge, not grounded in authoritative practice) suggested
CDM, Glossary, Governance, and RefData are legitimately sub-parts of one "Data Management Framework"
deliverable rather than four independent pillars — this research exists to verify or correct that
hypothesis against real sources, and to establish what "coherent-draft, not production-ready" should
concretely mean for each of the 8 deliverables.

## Sources

- **"Business requirement for SW development"** notebook — `5133ef48-564c-40df-bdd1-142bb7e5bdf3` (9 sources) — requirements-engineering / SRS practice.
- **"Enterprise Data Architecture"** notebook — `3adf8897-245c-43c6-aec9-8977f2aab2fb` (25 sources) — data governance / data management framework practice.

## Output

A final redirection plan (`99_FINAL_crdb-redirection-plan.md`) — concrete, evidence-traced, executable
within 2 weeks — produced after 3 iterations of Claude-generated queries, agy-executed notebook
retrieval, Claude synthesis, and agy second-opinion feedback.
