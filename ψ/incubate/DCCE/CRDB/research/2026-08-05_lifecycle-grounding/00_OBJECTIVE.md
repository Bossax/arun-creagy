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
within 2 weeks — produced after Claude-generated queries, agy-executed notebook retrieval, Claude
synthesis, and agy second-opinion feedback.

---

## Phase B Addendum (2026-08-05, later same day)

Phase A (iterations 1-3, described above) grounded CRDB's internal deliverable structure well, but
review of the resulting draft surfaced two problems: two of its "Decisions Required" were manufactured
rather than real (both now resolved — see `SCOPE_LEDGER.md`), and the research never actually answered
the bridging question this project needs — what a business-requirements handoff package to TOR70
should contain, and how CRDB's outputs map onto it.

Three primary sources, read directly (not sourced from the two notebooks), now ground this more
concretely than generic literature can, and settle several questions Phase A left open:
- `ψ/incubate/DCCE/CRDB/inbox_source/The Enterprise Data System Development Lifecycle.md`
- `ψ/incubate/DCCE/CRDB/output/00_Strategy_Reports/2026-06-11-Strategic-Alignment-Deck-Final.md`
  (presented to Director Toey; Boss confirms this is to be treated as accepted by DCCE)
- `ψ/incubate/DCCE/CRDB/inbox_note/2026-06-11-Meeting-with-Director-Toey-Reflection.md`

**New objective for Phase B**: ground the CRDB→TOR70 bridge-package question itself — what a good
business-requirements package for enterprise-data-platform software development looks like, and how
it should be organized so CRDB's output is directly usable as TOR70's input — rather than re-grounding
CRDB's internal deliverable structure a second time.

**Explicitly out of scope**: line-agency partnership / R&D data-sharing strategy. This is Boss's own
strategic judgment call, not something the two literature notebooks can meaningfully answer.

**Process change**: Phase B has no fixed iteration count. After each iteration's synthesis and agy's
second-opinion feedback are finalized, Claude proposes the next iteration's queries and pauses for
Boss's explicit approval before writing them — there is no autonomous chaining as there was across
iterations 1→2→3 in Phase A.

Full detail on settled findings, approved research areas, and out-of-scope topics: see
`SCOPE_LEDGER.md` in this same folder — that file, not this one, is the operational source of truth
for what's open and closed at any given point in Phase B.
