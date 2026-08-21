---
query: "what are the design principles of NCAIF IA in terms of the content structure? what are the core references"
target: "Arun_Creagy"
mode: smart
timestamp: 2026-08-21 12:36
---

# Trace: NCAIF IA design principles and core references

**Target**: Arun_Creagy (CRDB project)
**Mode**: smart (Oracle first, <3 relevant hits → direct file dig)
**Time**: 2026-08-21 12:36

## Oracle Results
10 hits, all low-confidence retro snippets (FTS-only, vector search unavailable this session) — mentioned NCAIF sitemap work happened but none stated the actual design principles or references. Treated as insufficient; escalated to direct file reads instead of 5-agent --deep (target files were already known from prior session context).

## Files Found
- `ψ/incubate/DCCE/CRDB/output/04_Sitemap/Pillar_01_Sitemap_InterfaceMapping_Technical_Specification.md` — canonical IA design-principle spec (Mandate-First IA, Transparency with Armor, Three-Tier Traceability Model, Download Gate, Governed Content Hub)
- `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-06-04-NCAIF-Sitemap-v5-Design-Decisions.md` — LOCKED decision doc, same principles with rationale (benchmarked against A-PLAT, Climate-ADAPT)
- `ψ/incubate/DCCE/CRDB/output/04_Sitemap/2026-05-12-NCAIF-Sitemap-Presentation.md` — the DCCE-approved slide-by-slide layout (E-046 in Evidence Registry): "the authoritative source for scientific sub-bullets and node naming"
- `ψ/incubate/DCCE/CRDB/CRDB-Evidence-Registry.md` (E-046) — names the May 12 Strategic Presentation as Project Sponsor (DCCE) mandate
- `ψ/incubate/DCCE/CRDB/output/04_Sitemap/NCAIF_Detailed_Sitemap_v9.md` — current sealed baseline (D-075), content structure itself, references v6 as Boss's original intent and the practicality-pass annotations (shared build / pending DCCE decision)
- **(added in Addendum below)** `ψ/incubate/DCCE/CRDB/output/archive/National Climate Adaptation Information Framework.md` — the founding design-lock doc, missed on first pass
- **(added in Addendum below)** `ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12 - User Experience Design Principles for National Climate Change Adaptation Information Services.md` — the research-grounded UX brief underlying Pack C, missed on first pass

## Git History
Not searched — direct file dig covered the question fully.

## GitHub Issues/PRs
None (no remote search performed; not relevant to this doc-based question).

## Cross-Repo Matches
None — question is scoped entirely to this repo's CRDB project.

## Oracle Memory
See Oracle Results above — retros confirm sitemap v4/v5 evolution timeline but don't carry the principle statements themselves; the technical spec and design-decisions docs are the primary source.

## Summary
Two design principles anchor NCAIF's IA: **Mandate-First IA** (top-level nav reserved for the National Adaptation Plan cycle and policy-maker journey, not user-hook silos — benchmarked against A-PLAT and Climate-ADAPT to avoid "Portal Drift") and **Transparency with Armor** (every high-impact risk asset ships bundled with Scientific Armor + Action Armor rather than being concealed or shown as an orphan map). Supporting structural rules: a Three-Tier Traceability Model (Sitemap → Use Cases → Data Inventory), the Download Gate (open visualizations, gated raw downloads), and "Zero-Discovery Handoff" (sitemap + mandate mapping is a fixed contract for the downstream TOR70 contractor).

Core references: the **2026-05-12 NCAIF Sitemap Presentation** (DCCE Project Sponsor mandate, E-046 — approved UI/UX layout, authoritative for node naming) and the **2026-06-04 Sitemap v5 Design Decisions** doc (LOCKED, the canonical synthesis of those principles). The current sealed baseline is v9 (D-075, supersedes v8/D-050), which keeps this same DNA while stripping v8's inline BTR compliance tags in favor of `(shared build)` / `(pending DCCE decision)` annotations.

## Addendum (2026-08-21, same session — user flagged a missed source)

The initial dig above missed the actual **founding design-lock document**, which predates and grounds everything found in the first pass:

- `ψ/incubate/DCCE/CRDB/output/archive/National Climate Adaptation Information Framework.md` (status: In Progress, last_updated 2026-03-06) — locks the **preliminary NCAIF design for FGD2**. Introduces the workflow-pattern/MVP framing (P1–P4 → MVP-1–4), three sitemap alternatives, the March 2026 "vNext" sitemap, a formal **standards-alignment check against IPCC/WMO/UNFCCC/ISO 14090-14091**, the **Pack A/B/C decision matrix** (Pack A = product constraints, Pack B = TOR scope/Task 5.5, Pack C = usability guidance), the **landing-page access model**, and the **2026-03-13 locked stable-vs-flexible backbone rules** plus a three-tier sitemap change-approval process (minor → section owner; structural → CRDB/NCAIF coordination review; backbone → DCCE leadership review).

That document's Pack C usability basis points to a second missed file, the actual theoretical bedrock under "Mandate-First IA" and "Transparency with Armor":

- `ψ/incubate/DCCE/CRDB/inbox_source/2026-03-12 - User Experience Design Principles for National Climate Change Adaptation Information Services.md` — a research-grounded UX brief (information foraging/scent theory, matrix taxonomies, front-end tool/catalog separation, progressive disclosure, Fogg Behavior Model, GFCS co-production, case studies of US Climate Resilience Toolkit and World Bank CCKP). Its "Synthesizing the Benchmark Framework" section (lines 220–230) states **5 Core UX Design Principles for CIS (Climate Information Services)**:
  1. **Iterative Agility and Sustained Co-Production** — no launch-and-abandon; continuous structured user engagement as science evolves.
  2. **Equitable Accessibility (5 dimensions)** — Approachability, Acceptability, Availability, Affordability, Appropriateness; low-bandwidth design, multi-language, WCAG compliance.
  3. **Algorithmic and Informational Transparency** — document provenance, metadata, error margins, methodology, managed through progressive disclosure to avoid cognitive overload. (Direct ancestor of "Transparency with Armor.")
  4. **Decoupled Architecture with Integrated Discoverability** — backend data catalog fully separate from task-oriented front-end tools, bridged contextually. (Direct ancestor of the v5 spec's Governed Content Hub / catalog-tools separation.)
  5. **Narrative-Driven Information Architecture** — structure the sitemap around actionable pathways and user mental models ("Assess Risk," "Find Funding"), not scientific ontologies; uses information scent and storytelling for non-technical onboarding. (Direct ancestor of "Mandate-First IA.")

**Revised summary**: the "Mandate-First IA" / "Transparency with Armor" principles documented in the v5-era Pillar 1 spec are not first-order — they're CRDB's own applied restatement of these 5 research-grounded UX principles, filtered through the Pack A/B/C decision process and the IPCC/WMO/UNFCCC/ISO standards-alignment check, all locked in the March 2026 founding document before the May 12 workshop presentation or the June 2026 v5 lock existed. The full core-reference chain, in dependency order: **UX Design Principles brief (2026-03-12) → NCAIF founding design-lock doc (Jan–Mar 2026, Pack A/B/C + standards check) → May 12 Workshop Presentation (E-046) → Sitemap v5 Design Decisions (2026-06-04, LOCKED) → Pillar 1 Technical Spec → v9 sealed baseline (D-075, current)**.
