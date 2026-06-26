# Stage 2 Technical Synthesis Skeleton — CRDB Loss & Damage Data Model

## Status boundary

This is a skeleton only for Stage 2 under [`plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md`](../../../../../../plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md:60). It is not the final technical specification and it does not draft final prose sections.

## 1. Framing statement

- The integrated workflow joins [`TOR 5.3.6`](../../inbox_source/CRDB%20-%20TOR.md:190) data-model/reporting-form design with [`TOR 5.3.7`](../../inbox_source/CRDB%20-%20TOR.md:192) event-application methodology.
- The central architectural rule is to keep **database design** distinct from **assessment methodology**, per [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:6).
- The minimum viable posture should remain compatible with present DDPM reporting reality while keeping clear extension paths toward standards-based loss-and-damage analysis.

## 2. Evidence-backed design premises

### 2.1 Confirmed premises

- DDPM current reporting is centralized, hierarchical, and not PDNA-based. See [`2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md`](../../inbox_source/2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md:6) and [`2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md`](../../inbox_source/2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md:7).
- Rapid assessment fields already cover event identity, casualties, affected population, damaged housing, utility disruption, and urgent needs. See [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:71).
- International standards expect structured metadata, spatial hierarchy, hazard typology, human impacts, asset impacts, and workflow status. See [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:20) and [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:68).
- NESDC signals the policy need for a standardized Thai loss-and-damage database and a move toward prevention/risk management. See [`NESDC-Loss-and-damage-database-presentation-slide.md`](../../inbox_source/NESDC-Loss-and-damage-database-presentation-slide.md:32) and [`extracts/NESDC_Loss_and_Damage_comparison.csv`](extracts/NESDC_Loss_and_Damage_comparison.csv:2).

### 2.2 Proposed premises

- The data system should be modernized for web/mobile field collection and data sharing. See [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:27), [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:28), and [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:31).
- New forms should maximize use of existing databases rather than replace them wholesale. See [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:33).

### 2.3 Inferred premises

- The MVD likely requires separate logical treatment for event records, impact observations, baseline references, valuation references, and provenance/revision metadata.
- The 5.3.7 testing method should evaluate staged field collectability, not full historical reconstruction.

## 3. Core synthesis structure for Stage 3 drafting

### 3.1 Problem statement

- Thailand has multiple relevant loss/damage evidence streams but no single standardized and interoperable loss-and-damage database structure.
- DDPM current operational records are useful but narrower than PDNA- or standards-oriented loss-and-damage needs.
- The draft MVD must therefore bridge current operational feasibility with future analytical extensibility.

### 3.2 Scope boundary

- **Inside scope:** logical data model for minimum viable event and loss/damage reporting; phased completeness logic; provenance and revision controls; event-application method.
- **Outside scope:** full national historical reconstruction; full loss-estimation engine; full macroeconomic modeling; complete software implementation design.

## 4. Candidate logical architecture

### 4.1 Anchor record family A — disaster event record

Purpose:

- represent one disaster occurrence as the top-level reporting object.

Likely content blocks:

- event identifier and source-system identifiers;
- hazard type and cause;
- event dates / duration;
- location hierarchy;
- disaster severity / management level;
- collection phase;
- workflow status and revision status.

Evidence anchors:

- [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:73)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:22)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:27)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:31)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:35)

### 4.2 Anchor record family B — human and household impact summary

Purpose:

- capture rapid counts that are operationally central and consistently referenced across DDPM and standards sources.

Likely content blocks:

- deaths, injured, missing;
- affected population, evacuees, homeless, vulnerable groups;
- affected households / damaged housing counts.

Evidence anchors:

- [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:74)
- [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:76)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:39)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:46)

### 4.3 Anchor record family C — sector / asset / livelihood impact observation

Purpose:

- store repeated observations for sector-specific impacts linked back to one event.

Likely content blocks:

- sector and subsector;
- asset/livelihood type;
- ownership/public-private flag;
- baseline quantity and damaged/destroyed quantity;
- unit of measure;
- observation notes and evidence source.

Evidence anchors:

- [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:81)
- [`NESDC-Loss-and-damage-database-presentation-slide.md`](../../inbox_source/NESDC-Loss-and-damage-database-presentation-slide.md:184)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:70)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:74)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:78)

### 4.4 Support record family D — valuation reference and loss calculation support

Purpose:

- preserve the separation between observed physical counts and valuation references/calculation inputs.

Likely content blocks:

- unit cost / unit value source;
- replacement cost;
- repair cost;
- projected revenue baseline;
- actual revenue;
- compensation-rule value;
- valuation method tag.

Evidence anchors:

- [`NESDC-Loss-and-damage-database-presentation-slide.md`](../../inbox_source/NESDC-Loss-and-damage-database-presentation-slide.md:202)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:76)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:81)
- [`2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md`](../../inbox_source/2025-05-10-additional-note-about-loss-and-damage-from-ddpm.md:7)

### 4.5 Support record family E — provenance, workflow, and revision control

Purpose:

- make multi-stage and multi-source updates traceable.

Likely content blocks:

- source organization;
- source document / form type;
- collection phase;
- reporter / reviewer;
- record status;
- revision number;
- created / updated timestamps;
- verification note.

Evidence anchors:

- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:24)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:25)
- [`Disaster_Loss_Standards_Analysis.md`](../../inbox_source/Disaster_Loss_Standards_Analysis.md:26)
- [`Post Disaster Needs Assessment report by DDPM.md`](../../inbox_source/Post%20Disaster%20Needs%20Assessment%20report%20by%20DDPM.md:105)

## 5. Field-completeness logic skeleton

### 5.1 Required-now candidate group

- event identification;
- event timing;
- location hierarchy;
- hazard type;
- management/severity level;
- basic human impacts;
- basic housing impacts;
- utility disruption summary;
- urgent needs summary;
- initial provenance metadata.

### 5.2 Later-completion candidate group

- detailed sectoral asset inventories;
- repair/replacement cost inputs;
- revenue loss and operating-cost fields;
- baseline production and livelihood fields;
- verified recovery-needs estimates;
- macroeconomic aggregation links.

### 5.3 Explicitly non-core / future-extension candidate group

- GDP/GRP/GPP impact calculations as mandatory fields;
- full psychosocial or environmental valuation modules unless separately justified;
- complete prevention-investment planning layer.

## 6. Skeleton for [`TOR 5.3.7`](../../inbox_source/CRDB%20-%20TOR.md:192) event-application method

### 6.1 Objective

- test whether the draft MVD can be meaningfully applied to selected past events without full retrospective excavation.

### 6.2 Candidate method sequence

1. select a small set of representative past events;
2. map available source documents for each event;
3. score each MVD field as:
   - directly available;
   - derivable with reasonable transformation;
   - unavailable / not currently collected;
4. record provenance and gaps for each mapped field;
5. summarize whether the event can support rapid-only, partial loss/damage, or extended assessment use.

### 6.3 Expected outputs from testing

- field availability matrix;
- gap categories by event and sector;
- identification of fields that are too ambitious for the minimum mandatory core;
- recommendations for revision of required vs later-completion logic.

## 7. Human-review checkpoints carried into Stage 3

- confirm the minimum mandatory core boundary;
- confirm whether one logical form or a phase-partitioned form family is preferred;
- confirm the sector taxonomy approach;
- confirm treatment of compensation values versus broader damage/loss estimates;
- confirm how far Stage 3 should represent macroeconomic effects.

## 8. Draft conclusion frame

- The evidence supports a conservative but extensible loss-and-damage data model: operationally feasible at the event-reporting core, modular at the sector/valuation layer, and controlled through provenance, phase, and revision metadata.
- This conclusion remains provisional until the Stage 3 specification resolves the human-judgment points recorded in [`Stage2_Judgment_Notes.md`](Stage2_Judgment_Notes.md).
