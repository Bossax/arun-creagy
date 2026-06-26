# Stage 2 Judgment Notes — CRDB Loss & Damage Data Model

## Purpose

Intermediate trace notes for design points that require human judgment before Stage 3 final specification. This file follows the working rule in [`plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md`](../../../../../../plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md:118).

## Judgment register

### J01 — What counts as the minimum mandatory core?

- **Evidence tension:** DDPM’s current operational reporting is narrow and reimbursement-oriented, while international standards and PDNA forms carry much broader sectoral and valuation detail. See [`2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md`](../../inbox_source/2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md:7), [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:71), and [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:68).
- **Decision needed:** Should the MVD minimum core stay close to immediately collectable DDPM fields, or should it include some higher-order sector and valuation fields as mandatory from day one?
- **Analyst leaning:** Keep the mandatory core narrow and operational; push valuation-heavy and sector-specific fields into later-completion modules.
- **Risk if decided poorly:** Overly ambitious mandatory fields will make the draft form unrealistic for field adoption and fail the “test with real events” logic in [`TOR 5.3.7`](../../inbox_source/CRDB%20-%20TOR.md:192).

### J02 — One integrated form vs staged form family

- **Evidence tension:** PDNA evidence is explicitly phase-based, while the TOR wording asks for “a” draft MVD and “a” reporting form. See [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:55), [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:68), and [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:91).
- **Decision needed:** Should the deliverable be presented as one logical form with staged sections, or as a form family aligned to phase 1 / phase 2 / phase 3-4 workflows?
- **Analyst leaning:** Use one logical data model and reporting envelope, but explicitly partition fields by collection phase.
- **Risk if decided poorly:** A single undifferentiated form will confuse timing and data availability; multiple disconnected forms could fragment identifiers and provenance.

### J03 — Which sector taxonomy should dominate the logical model?

- **Evidence tension:** NESDC proposes five Thai-facing sectors, while DaLA/PDNA and other standards use different sector structures and unit-of-analysis assumptions. See [`NESDC-Loss-and-damage-database-presentation-slide.md`](../../inbox_source/NESDC-Loss-and-damage-database-presentation-slide.md:182) and [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:68).
- **Decision needed:** Should the MVD hard-code the NESDC five-sector structure, or define a broader sector registry that can map NESDC sectors as one view?
- **Analyst leaning:** Use a broader sector registry with NESDC-aligned reporting categories as a mapped presentation layer.
- **Risk if decided poorly:** Hard-coding the presentation taxonomy may limit interoperability and future extension.

### J04 — Administrative compensation values vs full damage/loss estimates

- **Evidence tension:** DDPM’s operational values are reimbursement-linked and may understate actual losses, while standards-based approaches seek fuller economic estimation. See [`2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md`](../../inbox_source/2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md:7), [`2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md`](../../inbox_source/2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md:8), and [`NESDC-Loss-and-damage-database-presentation-slide.md`](../../inbox_source/NESDC-Loss-and-damage-database-presentation-slide.md:128).
- **Decision needed:** Should the draft schema store these as separate value types, or leave a single generic monetary field for simplicity?
- **Analyst leaning:** Separate them explicitly: observed/admin compensation value, direct damage estimate, and economic loss estimate.
- **Risk if decided poorly:** A merged value field would corrupt traceability and create false comparability across methods.

### J05 — How far to go on macroeconomic and indirect effects in Stage 3

- **Evidence tension:** NESDC’s framing includes economic impact and policy response, but DDPM practice does not collect GDP-level impacts. See [`NESDC-Loss-and-damage-database-presentation-slide.md`](../../inbox_source/NESDC-Loss-and-damage-database-presentation-slide.md:76), [`NESDC-Loss-and-damage-database-presentation-slide.md`](../../inbox_source/NESDC-Loss-and-damage-database-presentation-slide.md:85), and [`2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md`](../../inbox_source/2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md:9).
- **Decision needed:** Should macroeconomic and indirect-effect fields be represented in the Stage 3 draft spec, or deferred outside the MVP scope?
- **Analyst leaning:** Defer them from the minimum operational schema; mention them as future analytical extensions.
- **Risk if decided poorly:** Pulling macro indicators into the MVP may break the minimum viable boundary.

### J06 — Event testing method for [`TOR 5.3.7`](../../inbox_source/CRDB%20-%20TOR.md:192)

- **Evidence tension:** The TOR requires testing with at least three past events, but the controlling plan prohibits turning this into full historical excavation. See [`CRDB - TOR.md`](../../inbox_source/CRDB%20-%20TOR.md:192) and [`plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md`](../../../../../../plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md:39).
- **Decision needed:** What constitutes “testing” — field availability mapping, mock backfill, partial sample application, or complete event reconstruction?
- **Analyst leaning:** Define testing as a structured field-availability and mapping exercise on selected events, not full reconstruction.
- **Risk if decided poorly:** The workstream could expand uncontrollably into data excavation and delay the data-model deliverable.

## Current analytical stance

At this stage, the evidence supports a conservative MVP posture:

1. minimum mandatory fields should reflect what can plausibly be collected in rapid DDPM-style practice;
2. richer sectoral, valuation, and recovery fields should remain attachable modules;
3. provenance, phase, and revision metadata are not optional extras but control mechanisms required to reconcile current DDPM practice with standards-oriented expansion.
