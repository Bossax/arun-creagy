# Comprehensive data-user needs list (derived from CRDB stakeholder interviews)

Status: draft synthesis (interview-grounded)

## Purpose and scope

This document consolidates **expressed needs of data users** across CRDB stakeholder interviews into a reusable, comprehensive list.

Scope notes:

- This is **demand-side** synthesis: what users say they need to *do their work*.
- It is not a system design or implementation plan.
- Primary evidence sources for this synthesis layer:
  - Need clusters v2: [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:1)
  - Interview comparison matrix v2 (for agency roles + examples): [`2026-03-23-Chapter2-interview-comparison-matrix-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-interview-comparison-matrix-v2.md:1)
  - Baseline version for history (pre-FTI/UDDC/BMA/DPT): [`2026-03-17-Chapter2-stakeholder-needs-synthesis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-stakeholder-needs-synthesis.md:1)

---

## Reading guide (how to use this needs list)

Use this list to:

1) define **requirements** for NCAIF-facing services and CDM/governance priorities,
2) define **data product specs** (what, for whom, at what scale/cadence, with what caveats),
3) identify **gaps** (supply vs demand) without collapsing into “we need all data”.

Each need below is written in the form:

- **Need statement** (what they need)
- **Who needs it** (user groups / agencies)
- **Typical decisions / workflows** it supports
- **Implications for data products** (what a “good enough” deliverable looks like)

---

## 0) Cross-cutting meta-needs (what makes any dataset usable)

These are repeatedly implied across multiple needs; they are the “usability rails” for all data services.

### 0.1 Clear ownership, contactability, and handoff paths

- **Need statement:** Users must be able to identify who owns a dataset/service, how to contact them, and how to request clarification or access.
- **Who needs it:** Most visible in FTI (trust + broken portals), plus operators and planners who cannot wait for informal networks.
- **Implication:** “Catalog entry” is not just metadata; it must include *owner pathway* (steward / custodian / escalation).
- Evidence anchor: owner pathways and discoverability cluster in [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:13).

### 0.2 Explicit limitations, uncertainty, and appropriate-use statements

- **Need statement:** Users need to know what a dataset can and cannot support (scale, time validity, uncertainty, misuse risks).
- **Who needs it:** Especially decision-facing users, local budget-defense workflows, and private-sector intermediaries.
- **Implication:** Every “decision-facing” product must ship with a companion limitations note.
- Evidence anchor: “trustworthy communication” and tiering in [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:19).

---

## 1) Long-term projections and forward-looking scenarios

### 1.1 Authoritative forward-looking climate-risk inputs (not just historical)

- **Need statement:** Future-oriented, authoritative climate and hazard projections are needed for planning and investment decisions.
- **Who needs it:** DLA, MSDHS, NESDC, OTP, TBA, plus DPT/FTI additions in v2.
- **Typical decisions / workflows:**
  - long-term policy and investment planning,
  - macroeconomic forecasts,
  - sector plans and standards updates,
  - business continuity / industrial planning.
- **Implications for data products:**
  - “projection packs” that are stable enough to cite in budget/planning documents,
  - scenario/time-slice clarity,
  - an endorsed baseline (tie to Need cluster #2).
- Evidence anchor: projections cluster in [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:11).

### 1.2 Planning-grade rainfall inputs for drainage and infrastructure design

- **Need statement:** Climate-adjusted rainfall and extremes inputs that are engineering/planning usable.
- **Who needs it:** DPT; implied also for city operators and infrastructure resilience planning.
- **Typical decisions / workflows:**
  - drainage design,
  - flood-prone area planning,
  - zoning and building guidance updates.
- **Implications for data products:**
  - design-storm / intensity-duration-frequency (IDF)-like guidance, or a clearly defined proxy product,
  - GIS-ready delivery and documentation.
- Evidence anchor: DPT example in projections cluster: [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:26).

---

## 2) Authoritative baselines and a trusted reference point (“single source of truth”)

### 2.1 Endorsed hazard and risk baselines (verification + versioning)

- **Need statement:** Users need a trusted baseline with an endorsement mechanism, not multiple competing datasets.
- **Who needs it:** NESDC, NXPO, DGA, NSO, OTP, FTI, UDDC.
- **Typical decisions / workflows:**
  - “official dataset” selection for reporting,
  - local budget justification,
  - private-sector planning based on verified hazard layers.
- **Implications for data products:**
  - a recommended dataset registry with endorsement status + version history,
  - difference notes (what changed, what is comparable).
- Evidence anchors:
  - baseline cluster: [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:12)
  - cross-cutting observation: single source of truth becomes business + ops need: [`2026-03-23-Chapter2-interview-comparison-matrix-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-interview-comparison-matrix-v2.md:19)

### 2.2 Standardized indicators and a consistent reference frame

- **Need statement:** Users need consistent indicator definitions and reference frames so cross-agency work is comparable.
- **Who needs it:** NESDC, NSO, NXPO, OTP (and any agency that aggregates across sources).
- **Typical decisions / workflows:**
  - national-level synthesis and prioritization,
  - monitoring/progress reporting,
  - cross-sector comparisons.
- **Implications for data products:**
  - shared definitions + data dictionaries + “how computed” notes.
- Evidence anchor: baseline and metadata clusters in [`2026-03-17-Chapter2-stakeholder-needs-synthesis.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter2-stakeholder-needs-synthesis.md:10).

---

## 3) Metadata, owner pathways, and discoverability

### 3.1 Data cataloging with decision-facing metadata (not just technical fields)

- **Need statement:** Users need cataloging, definitions, owner pathways, and technical metadata to understand meaning and use.
- **Who needs it:** MSDHS, NSO, DGA, DDPM, plus FTI and DPT (usability and GIS-ready access).
- **Typical decisions / workflows:**
  - dataset discovery and selection,
  - determining suitability for a use case,
  - interpreting maps/indices correctly.
- **Implications for data products:**
  - dataset pages with: steward/owner, cadence, coverage, limitations, and access condition.
- Evidence anchor: discoverability cluster in [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:13).

### 3.2 Contactable, maintained portals (anti-“broken website”)

- **Need statement:** Users need maintained interfaces and stable links; otherwise trust collapses.
- **Who needs it:** FTI explicitly; broadly applies to multi-agency users.
- **Typical decisions / workflows:**
  - ongoing planning cycles that depend on regularly checking updates.
- **Implications for data products:**
  - link persistence policy, simple stewardship checklist, and visible update timestamps.
- Evidence anchor: FTI complaint summarized in [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:34).

---

## 4) Operationally relevant granularity (scale that matches real decisions)

### 4.1 Municipality/tambon/corridor/asset/facility scale inputs

- **Need statement:** Users need finer granularity than provincial summaries for targeting and design.
- **Who needs it:** DLA, MSDHS, OTP, TBA, NSO; plus UDDC, BMA, DPT, FTI in v2.
- **Typical decisions / workflows:**
  - local planning and budgeting,
  - targeting vulnerable groups,
  - corridor/infrastructure risk,
  - asset-level finance risk analysis,
  - city operations.
- **Implications for data products:**
  - explicit tiering by scale (province vs city vs facility),
  - clear “valid uses” per tier.
- Evidence anchor: granularity cluster in [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:14).

### 4.2 Distinguish three granularity demand tiers (communication vs planning vs operations)

- **Need statement:** Provincial-scale products are still useful for communication, but planning/operations require different scales.
- **Who needs it:** Explicit after adding FTI/UDDC/BMA/DPT.
- **Implications:** design NCAIF products as a tiered system, not one map for everyone.
- Evidence anchor: granularity-tier observation in [`2026-03-23-Chapter2-interview-comparison-matrix-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-interview-comparison-matrix-v2.md:20).

---

## 5) Machine-readable interoperability and GIS-ready access

### 5.1 APIs / structured exchange and reusable spatial formats

- **Need statement:** Users need machine-readable access (APIs) and GIS-ready formats to avoid manual scraping and PDF reformatting.
- **Who needs it:** BMA, DPT, UDDC, DGA.
- **Typical decisions / workflows:**
  - operational monitoring,
  - planning workflows,
  - running local models,
  - integrating data into municipal systems.
- **Implications for data products:**
  - minimum interoperable delivery formats,
  - standard field definitions,
  - consistent spatial referencing.
- Evidence anchor: interoperability cluster in [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:15).

### 5.2 Reduce “website checking” and “paper-like outputs”

- **Need statement:** If the access path forces manual checking or PDF extraction, it is functionally unusable for operators.
- **Who needs it:** BMA and DPT are explicit.
- **Implications:** treat this as a non-functional requirement: time-to-integrate must be reduced.
- Evidence anchor: “interoperability is not only about cataloging” in [`2026-03-23-Chapter2-interview-comparison-matrix-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-interview-comparison-matrix-v2.md:21).

---

## 6) Planning-grade and engineering-ready datasets

### 6.1 Urban planning, drainage design, and local intervention design inputs

- **Need statement:** Users need data that supports design and implementation (not only high-level maps).
- **Who needs it:** DPT, UDDC, OTP, BMA.
- **Typical decisions / workflows:**
  - infrastructure design,
  - land-use planning,
  - NbS intervention siting and design.
- **Implications for data products:**
  - “planning-grade” label must mean something operational: resolution, geometry, methods note.
- Evidence anchor: planning-grade cluster in [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:16).

---

## 7) Economic loss, business interruption, and budget justification

### 7.1 Translate hazard/risk info into defensible economic arguments

- **Need statement:** Users need methods and data to translate hazards into economic loss and investment justification.
- **Who needs it:** NESDC, DDPM, TBA, DLA, UDDC, FTI.
- **Typical decisions / workflows:**
  - macroeconomic loss estimation,
  - post-event assessment,
  - budget defense for proactive adaptation,
  - business continuity planning.
- **Implications for data products:**
  - standard reporting pack templates,
  - explicit separation of “relief payouts” vs “true loss” where relevant,
  - worked examples.
- Evidence anchor: loss/budget cluster in [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:17).

---

## 8) Vulnerability and resilience indicators (beyond hazard)

### 8.1 Social/institutional vulnerability and subgroup sensitivity

- **Need statement:** Users need vulnerability and resilience indicators that capture social/institutional drivers and subgroup sensitivity.
- **Who needs it:** MSDHS, NXPO, NSO, DDPM, UDDC.
- **Typical decisions / workflows:**
  - targeting social protection,
  - resilience planning and prioritization,
  - local planning that combines hazard and vulnerability.
- **Implications for data products:**
  - vulnerability frameworks that can be explained and audited,
  - guidance on how indicators should be interpreted.
- Evidence anchor: vulnerability cluster in [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:18).

---

## 9) Tiered service design and trustworthy communication

### 9.1 Different service layers for different audiences

- **Need statement:** Users want tiered services: raw data for analysts/operators, dashboards/packs for executives, and explainers for broad audiences.
- **Who needs it:** UDDC, BMA, FTI, plus FGD evidence.
- **Typical decisions / workflows:**
  - daily operations (operators),
  - decision meetings and budgeting (executives),
  - public communication (general users).
- **Implications for data products:**
  - explicit Tier 1 vs Tier 2 product stance,
  - clear navigation so users don’t mix “tool mode” and “catalog mode”.
- Evidence anchors:
  - tiered service cluster: [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:19)
  - tiered service observation (UDDC/BMA/FTI): [`2026-03-23-Chapter2-interview-comparison-matrix-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-interview-comparison-matrix-v2.md:22)

---

## 10) Access, publishing, and governance pathways

### 10.1 Clear access rules and routinized sharing mechanisms

- **Need statement:** Users need clarity on what can be shared, how, and under what conditions, with a safe publishing workflow.
- **Who needs it:** DGA, NXPO, NSO, MSDHS, FTI (+ FGD evidence).
- **Typical decisions / workflows:**
  - data sharing across agencies,
  - publication of decision-facing products,
  - risk management around sensitive registries.
- **Implications for data products:**
  - access-tier labels (open/internal/restricted),
  - publishing gates and review responsibilities.
- Evidence anchor: governance/access cluster in [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:20).

### 10.2 Trust erosion from weak stewardship and turnover

- **Need statement:** Even when data exist, weak stewardship and turnover can make systems unusable.
- **Who needs it:** Highlighted through FTI; implicit across multi-agency ecosystems.
- **Implications:** treat stewardship and support as part of the “data product”, not optional operations.
- Evidence anchor: expanded governance cluster note in [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:62).

---

## Appendix A — Canonical “top 5” demand backbone (as stated in v2)

The strongest drafting takeaway after adding FTI/UDDC/BMA/DPT is recorded as:

1) trusted baselines,
2) planning- and operations-ready granularity,
3) machine-readable and GIS-ready access,
4) tiered service design with credible communication,
5) translation of hazards into budget, business, and engineering decisions.

See the explicit statement in [`2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md:64).

---

## Appendix B — Coverage matrix (need clusters × interview summary notes)

Anchor note: This appendix cross-checks the need clusters in this document against the v2 interview summary notes in [`ψ/incubate/DCCE/CRDB/output/Interview summary notes/`](ψ/incubate/DCCE/CRDB/output/Interview summary notes:1).

Coverage codes used in the matrix: **Strong / Medium / Weak / Not mentioned**.

### Coverage matrix



| Need cluster                                                                             | BMA    | DGA           | DLA    | DPT    | FTI    | MSDHS         | NESDC  | NSO           | NXPO   | OTP    | Thai Bankers' Association | UDDC   | DDPM          | Evidence highlights (interview-note pointers)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------- | ------ | ------------- | ------ | ------ | ------ | ------------- | ------ | ------------- | ------ | ------ | ------------------------- | ------ | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.1 Clear ownership, contactability, and handoff paths                                   | Weak   | Medium        | Weak   | Weak   | Strong | Medium        | Weak   | Medium        | Medium | Weak   | Weak                      | Weak   | Medium        | - Broken links/contacts + turnover erodes usability: [`Interview Summary - FTI.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - FTI.md:48) <br>- “Who produces what” / dataset ownership cataloging: [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NSO.md:16) <br>- Provider/consumer roles + request workflow: [`Interview Summary - DGA.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DGA.md:33)                                                                                                                         |
| 0.2 Explicit limitations, uncertainty, and appropriate-use statements                    | Weak   | Weak          | Weak   | Weak   | Weak   | Weak          | Weak   | Weak          | Strong | Medium | Strong                    | Weak   | Weak          | - Probabilistic-map misuse / need uncertainty education: [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - Thai Bankers' Association.md:39) <br>- Liability fears block publishing forecasts (needs governance guardrails): [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NXPO.md:57) <br>- Budget skepticism driven by long-term uncertainty: [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - OTP.md:81)                                          |
| 1.1 Authoritative forward-looking climate-risk inputs (not just historical)              | Medium | Not mentioned | Strong | Strong | Medium | Strong        | Strong | Weak          | Strong | Strong | Medium                    | Strong | Not mentioned | - Need authoritative long-term forecasts/projections usable annually: [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - OTP.md:73) <br>- Climate-adjusted rainfall projections; historical rainfall no longer adequate: [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DPT.md:57) <br>- Lacks predictive forecasts; needs projections at tambon/municipality: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - MSDHS.md:32)                                               |
| 1.2 Planning-grade rainfall inputs for drainage and infrastructure design                | Strong | Not mentioned | Weak   | Strong | Weak   | Not mentioned | Weak   | Not mentioned | Weak   | Strong | Not mentioned             | Weak   | Not mentioned | - Urgent need for climate-adjusted rainfall/hydrology for drainage planning: [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DPT.md:57) <br>- Extreme rainfall exceeding older design assumptions + need better localized extreme-rain forecasting: [`Interview Summary - BMA.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - BMA.md:25) <br>- Uses 50–100-year rainfall models; needs authoritative hydrological projections: [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - OTP.md:54)           |
| 2.1 Endorsed hazard and risk baselines (verification + versioning)                       | Weak   | Weak          | Medium | Weak   | Strong | Weak          | Weak   | Weak          | Strong | Weak   | Medium                    | Strong | Weak          | - “Single source of truth” / verification gap: [`Interview Summary - FTI.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - FTI.md:46) <br>- Agencies produce different numbers; no one verifies/declares baseline: [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NXPO.md:49) <br>- Wants DCCE to sanction which baseline models/metrics to use: [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - UDDC.md:52)                                                                                       |
| 2.2 Standardized indicators and a consistent reference frame                             | Weak   | Medium        | Weak   | Weak   | Weak   | Strong        | Strong | Strong        | Medium | Strong | Weak                      | Weak   | Medium        | - Requests standardized social indicators for NAP Human Settlement: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - MSDHS.md:40) <br>- Needs standardized indicators/baselines/targets for national milestone tracking: [`Interview Summary - NESDC.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NESDC.md:51) <br>- Official statistics tiering/assignment (FDES committees): [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NSO.md:39)                                                       |
| 3.1 Data cataloging with decision-facing metadata (not just technical fields)            | Weak   | Strong        | Medium | Medium | Weak   | Strong        | Weak   | Strong        | Weak   | Weak   | Weak                      | Weak   | Strong        | - No central catalog; lacks metadata/dictionaries → calls to interpret data: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - MSDHS.md:34) <br>- CKAN agency catalogs + metadata/tagging/harvesting + GD Catalog registration: [`Interview Summary - DGA.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DGA.md:42) <br>- DDPM portal/catalog (~40 datasets) for API exchange: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary DDPM.md:34)                                                            |
| 3.2 Contactable, maintained portals (anti-“broken website”)                              | Weak   | Weak          | Weak   | Weak   | Strong | Medium        | Weak   | Weak          | Weak   | Weak   | Weak                      | Weak   | Weak          | - Broken website/contacts + turnover called out directly: [`Interview Summary - FTI.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - FTI.md:48) <br>- Staff time lost hunting across websites; wants centralized catalog to reduce friction: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - MSDHS.md:34)                                                                                                                                                                                                                                                 |
| 4.1 Municipality/tambon/corridor/asset/facility scale inputs                             | Strong | Weak          | Strong | Strong | Medium | Strong        | Medium | Strong        | Medium | Strong | Strong                    | Strong | Medium        | - Asset-level flood depth/duration + probability needed for finance: [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - Thai Bankers' Association.md:26) <br>- Needs tambon/municipality-level hazard overlays to match real relief-budget holders: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - MSDHS.md:32) <br>- Infrastructure vulnerabilities down to km markers / utility poles: [`Interview Summary - OTP.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - OTP.md:58) |
| 4.2 Distinguish three granularity demand tiers (communication vs planning vs operations) | Strong | Weak          | Medium | Strong | Medium | Strong        | Medium | Medium        | Medium | Medium | Medium                    | Strong | Weak          | - Two tiers (raw/processable data vs simplified dashboards) explicitly requested: [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - UDDC.md:56) <br>- Operators need near-real-time interoperable feeds; managers need dashboards: [`Interview Summary - BMA.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - BMA.md:79) <br>- Individual-level internal data but published dashboards aggregated to tambon: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - MSDHS.md:25)                           |
| 5.1 APIs / structured exchange and reusable spatial formats                              | Strong | Strong        | Medium | Strong | Weak   | Medium        | Weak   | Medium        | Weak   | Medium | Weak                      | Strong | Medium        | - Lack of API-based exchange; staff manually check external websites: [`Interview Summary - BMA.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - BMA.md:57) <br>- GDX as API “highway” + CKAN harvesting; machine-readable formats: [`Interview Summary - DGA.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DGA.md:37) <br>- PDF/paper outputs block planning; wants digital/GIS-ready: [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DPT.md:61)                                                                           |
| 5.2 Reduce “website checking” and “paper-like outputs”                                   | Strong | Weak          | Medium | Strong | Medium | Medium        | Weak   | Weak          | Weak   | Weak   | Weak                      | Strong | Weak          | - Manual “check websites” problem (no structured feeds): [`Interview Summary - BMA.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - BMA.md:57) <br>- Data still provided as PDFs/paper; wants digital spatially referenced data: [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DPT.md:61) <br>- Wants raw/processable data (CSV/API) alongside dashboards: [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - UDDC.md:56)                                                                            |
| 6.1 Urban planning, drainage design, and local intervention design inputs                | Strong | Not mentioned | Medium | Strong | Weak   | Weak          | Weak   | Weak          | Weak   | Strong | Weak                      | Strong | Weak          | - Engineering-detail datasets (terrain, drainage geometry, etc.) needed for planning/design: [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DPT.md:63) <br>- Intervention-level NbS design uses very fine data (1m DEM / 20cm drone): [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - UDDC.md:33) <br>- Interest in integrated drainage capacity analytics: [`Interview Summary - BMA.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - BMA.md:63)                                                  |
| 7.1 Translate hazard/risk info into defensible economic arguments                        | Weak   | Weak          | Strong | Weak   | Strong | Medium        | Strong | Weak          | Medium | Strong | Strong                    | Strong | Strong        | - “True loss vs relief fund” gap; needs standardized Loss & Damage valuation: [`Interview Summary - NESDC.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NESDC.md:45) <br>- Requests manuals translating hazards into business interruption costs: [`Interview Summary - FTI.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - FTI.md:54) <br>- Economic loss valuation gap; indirect losses hard; needs better framework: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary DDPM.md:55)                                            |
| 8.1 Social/institutional vulnerability and subgroup sensitivity                          | Weak   | Weak          | Weak   | Weak   | Weak   | Strong        | Weak   | Strong        | Strong | Weak   | Weak                      | Strong | Strong        | - Subgroup impacts (children/elderly/disabled), gender/equality requirements: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - MSDHS.md:42) <br>- Need to map resilience/carrying capacity (not just hazard exposure): [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NXPO.md:51) <br>- Adaptive capacity measurement currently impossible; wants indices/methodologies: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary DDPM.md:61)                                      |
| 9.1 Different service layers for different audiences                                     | Strong | Weak          | Medium | Medium | Strong | Strong        | Weak   | Medium        | Strong | Medium | Medium                    | Strong | Weak          | - Two tiers (raw/processable data vs simplified dashboards): [`Interview Summary - UDDC.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - UDDC.md:56) <br>- Tiered services for operators vs managers/policy teams: [`Interview Summary - BMA.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - BMA.md:79) <br>- Requests interactive portal + chatbot/community features: [`Interview Summary - FTI.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - FTI.md:48)                                                                                             |
| 10.1 Clear access rules and routinized sharing mechanisms                                | Weak   | Strong        | Weak   | Weak   | Weak   | Medium        | Weak   | Strong        | Strong | Medium | Medium                    | Weak   | Strong        | - GDX requires formal request + legal mandate; provider controls fields; API gateway: [`Interview Summary - DGA.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DGA.md:33) <br>- Statistics Act privacy constraints + MOUs needed: [`Interview Summary - NSO.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NSO.md:24) <br>- Portal/catalog with APIs for exchange via MOUs: [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary DDPM.md:34)                                                                                        |
| 10.2 Trust erosion from weak stewardship and turnover                                    | Weak   | Weak          | Weak   | Weak   | Strong | Medium        | Weak   | Weak          | Strong | Weak   | Weak                      | Weak   | Medium        | - Turnover + broken contacts cause knowledge loss; wants maintained portal: [`Interview Summary - FTI.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - FTI.md:48) <br>- Catalog/metadata gaps force time-wasting + phone calls to interpret: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - MSDHS.md:34) <br>- Fear/liability discourages publishing forecasts; needs governance protections: [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NXPO.md:57)                                        |

### Gaps / deltas (from this cross-check)

- **0.2 Limitations/uncertainty statements are under-explicit across most interviews:** only a few notes make uncertainty handling explicit (notably banking stress-testing misuse risk and NXPO accountability fears). Consider tightening 0.2 to require *standard interpretation guidance* for probabilistic layers and scenario products, not only “limitations notes.” Evidence: [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - Thai Bankers' Association.md:39), [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NXPO.md:57).

- **Distinguish “baseline endorsement/verification” vs “data access workflow” more sharply:** 2.1 (endorsement) and 10.1 (sharing mechanisms) are both present, but interviews separate them: “which dataset is *official/trusted*” (FTI/NXPO/UDDC) vs “how to legally/technically request/share” (DGA/NSO/DDPM). Consider clarifying boundaries and cross-references between 2.1 and 10.1. Evidence: [`Interview Summary - FTI.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - FTI.md:46), [`Interview Summary - DGA.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DGA.md:33).

- **Planning-grade rainfall (1.2) should explicitly cover both “design rainfall/projection inputs” and “forecasting for localized extremes”:** DPT emphasizes projection inputs for design; BMA emphasizes urban-scale localized extreme rainfall forecasting for operations. The current 1.2 wording leans to design-storm/IDF style; consider adding explicit mention of *urban localized extreme-rain forecasting gap* as part of the cluster or as a sub-need. Evidence: [`Interview Summary - DPT.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - DPT.md:57), [`Interview Summary - BMA.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - BMA.md:59).

- **Loss & Damage (7.1) needs a tighter split between (a) direct physical loss, (b) indirect/cascading business interruption, and (c) relief/compensation payouts:** NESDC and DDPM explicitly highlight the “true loss vs relief funds” mismatch; banks/FTI extend into business interruption and damage functions. Consider tightening 7.1 phrasing so those sub-components are explicit. Evidence: [`Interview Summary - NESDC.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NESDC.md:45), [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary DDPM.md:55), [`Interview Summary - Thai Bankers' Association.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - Thai Bankers' Association.md:33).

- **Vulnerability/resilience (8.1) is overloaded (social subgroup sensitivity vs institutional capacity/adaptive capacity):** MSDHS focuses on subgroup targeting and equity; NXPO/DDPM emphasize “carrying capacity” / adaptive capacity measurement. Consider clarifying whether 8.1 is one combined cluster or two sibling clusters (social vulnerability vs institutional capacity). Evidence: [`Interview Summary - MSDHS.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - MSDHS.md:42), [`Interview Summary - NXPO.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary - NXPO.md:51), [`Interview Summary DDPM.md`](ψ/incubate/DCCE/CRDB/output/Interview summary notes/Interview Summary DDPM.md:61).

