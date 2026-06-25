# Stage 3 Draft — LossDamage Data Model Technical Specification

## 1. Purpose and scope boundary

This draft technical specification translates the Stage 2 evidence base into a minimum viable logical data model for the CRDB Loss and Damage workflow. It is prepared as the Stage 3 artifact required by [`plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md`](../../../../../../plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md:76), using the evidence and judgment trail in [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:1), [`Stage2_Judgment_Notes.md`](Stage2_Judgment_Notes.md:1), and [`Stage2_Technical_Synthesis_Skeleton.md`](Stage2_Technical_Synthesis_Skeleton.md:1).

The draft specification is designed to support the design obligation in [`TOR 5.3.6`](../../inbox_source/CRDB%20-%20TOR.md:190) and to remain compatible with the event-application methodology boundary in [`TOR 5.3.7`](../../inbox_source/CRDB%20-%20TOR.md:192).

### 1.1 In scope

1. logical definition of the minimum viable event-level and loss/damage observation structure;
2. required-versus-later-completion field logic;
3. linkage, provenance, validation, revision, and timeliness rules;
4. explicit treatment of current DDPM operational practice versus later PDNA-oriented enrichment.

### 1.2 Out of scope

1. full historical population of the database;
2. full software implementation design;
3. macroeconomic modeling as part of the minimum operational schema;
4. a complete loss-estimation engine, including comprehensive valuation formulas, national unit-cost libraries, and automatic economic-loss computation, unless separately agreed under a later scope.

## 2. Design basis

The specification adopts five Stage 2 conclusions as controlling design premises.

1. Current DDPM reporting is hierarchical, centralized, and operationally oriented rather than PDNA-based, which means the minimum mandatory core must remain close to fields that are plausibly collectible in rapid practice; see [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:19) to [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:23).
2. PDNA evidence is explicitly phased, so the model must allow the same event record to accumulate detail over time rather than forcing one-time completion; see [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:25) to [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:29).
3. International standards expect structured event metadata, workflow controls, and asset-level observations, which justifies a two-level architecture with event records and repeated impact observations; see [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:30) to [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:31).
4. Administrative compensation values must not be conflated with broader damage and loss estimates; see [`Stage2_Judgment_Notes.md`](Stage2_Judgment_Notes.md:30) to [`Stage2_Judgment_Notes.md`](Stage2_Judgment_Notes.md:35).
5. Provenance, collection phase, and revision controls are core control fields rather than optional metadata, because the model must reconcile operational DDPM practice, PDNA recommendations, and standards-oriented extension paths; see [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:38) to [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:40).

## 3. Logical architecture

The minimum viable logical architecture consists of two anchor record families and three support structures.

### 3.1 Anchor entity A — `DISASTER_RECORD`

Purpose: represent one disaster occurrence as the top-level reporting object for intake, consolidation, and staged update.

This entity carries the event header, rapid human-impact summary, basic housing and utility disruption summary, phase marker, and workflow envelope.

### 3.2 Anchor entity B — `LOSS_DAMAGE_RECORD`

Purpose: represent one repeated sector, asset, livelihood, service, or facility impact observation linked to a single disaster event.

This entity carries sector-specific quantities and, where available, later-stage damage, loss, and compensation values without forcing those values into the minimum event header.

### 3.3 Support structure C — baseline reference snapshot

Purpose: store or link pre-disaster baseline quantities or context needed for later assessment, while remaining logically separate from post-event observations.

### 3.4 Support structure D — valuation reference

Purpose: store or link unit cost, replacement cost, repair cost, or other valuation references used in later-stage estimation.

### 3.5 Support structure E — provenance and workflow audit

Purpose: preserve source, phase, status, revision, and verification history for each event-level and observation-level record.

## 4. Entity specification

## 4.1 `DISASTER_RECORD`

### 4.1.1 Functional role

`DISASTER_RECORD` is the authoritative event header for one disaster occurrence. It provides the minimum viable structure needed for field intake, hierarchical reporting, central consolidation, and later-stage enrichment.

### 4.1.2 Required-now fields

The following fields form the minimum mandatory event core.

1. `disaster_record_id` — system-generated unique identifier for the event record.
2. `source_event_id` — identifier from the originating source system or form, if available.
3. `hazard_type_code` — standardized hazard type.
4. `event_name_or_label` — working label for the event.
5. `event_start_date` — date the event began.
6. `event_end_date` — date the event ended, or null when still ongoing.
7. `reporting_date` — date the record was submitted into the reporting chain.
8. `country_code` — country identifier.
9. `province_code` — province identifier.
10. `district_code` — district identifier where known.
11. `subdistrict_code` — subdistrict identifier where known.
12. `location_text` — free-text location descriptor where coding is incomplete.
13. `disaster_management_level` — operational severity or management level used by the reporting authority.
14. `collection_phase` — rapid, follow-up, verified, or recovery-oriented phase code.
15. `record_status` — draft, submitted, consolidated, verified, revised, or closed.
16. `deaths_count` — number of deaths known at time of reporting.
17. `injured_count` — number of injured persons known at time of reporting.
18. `missing_count` — number of missing persons known at time of reporting.
19. `affected_people_count` — affected population count.
20. `evacuated_people_count` — evacuees count, where available in rapid reporting.
21. `affected_households_count` — affected households count.
22. `houses_damaged_count` — damaged houses count.
23. `houses_destroyed_count` — destroyed houses count.
24. `utility_disruption_summary` — structured or coded summary of disrupted utilities and essential services.
25. `urgent_needs_summary` — structured or coded summary of urgent relief needs.
26. `source_system` — originating system or reporting channel.
27. `source_document_type` — originating form or document type.
28. `reporting_organization` — submitting organization.
29. `created_at` — system timestamp for record creation.
30. `updated_at` — system timestamp for last update.
31. `revision_number` — current revision sequence.

### 4.1.3 Later-completion fields

These fields should remain attachable later rather than mandatory at initial intake.

1. `hazard_cause_detail` — more detailed causal narrative.
2. `geo_coordinates` — point or geometry reference if collected digitally.
3. `utility_disruption_duration` — estimated duration of service interruption.
4. `vulnerable_group_breakdown` — disaggregation by vulnerable population groups.
5. `temporary_shelter_count` — shelter-specific detail.
6. `response_actions_summary` — immediate actions taken.
7. `baseline_snapshot_ref` — link to pre-disaster baseline reference.
8. `verification_note` — summary of field verification or review findings.
9. `closed_date` — date the record was administratively closed.

### 4.1.4 Non-core event-level fields

The following should not be mandatory in the minimum viable event header.

1. GDP, GRP, or GPP impacts;
2. comprehensive indirect economic effects;
3. full environmental valuation;
4. complete psychosocial valuation modules.

## 4.2 `LOSS_DAMAGE_RECORD`

### 4.2.1 Functional role

`LOSS_DAMAGE_RECORD` stores repeated impact observations linked to one event. It is the main structure for sectoral, asset, livelihood, and service-level loss/damage detail.

### 4.2.2 Required-now fields

The minimum operational version of `LOSS_DAMAGE_RECORD` should require only fields that support clear traceability and basic impact description.

1. `loss_damage_record_id` — unique identifier for the observation record.
2. `disaster_record_id` — foreign key linking the observation to [`DISASTER_RECORD`](Stage3_LossDamage_DataModel_Technical_Specification_Draft.md:48).
3. `sector_code` — normalized sector identifier.
4. `subsector_code` — optional finer category where available, but structurally present.
5. `impact_unit_type` — asset, facility, service, livelihood, crop area, household asset, or other defined unit.
6. `impact_item_label` — human-readable label of the affected item.
7. `ownership_type` — public, private, household, community, mixed, or unknown.
8. `location_reference` — coded or text location reference for the impact observation.
9. `damage_state` — affected, damaged, destroyed, disrupted, lost, or other controlled code.
10. `affected_quantity` — observed quantity affected.
11. `unit_of_measure` — unit attached to the affected quantity.
12. `observation_date` — date of the observation.
13. `collection_phase` — same phase logic as the event record.
14. `source_system` — source system or collection channel.
15. `source_document_type` — form or document type.
16. `reporting_organization` — reporting organization.
17. `record_status` — draft, submitted, consolidated, verified, revised, or closed.
18. `created_at` — creation timestamp.
19. `updated_at` — update timestamp.
20. `revision_number` — revision sequence.

### 4.2.3 Later-completion fields

These fields reflect PDNA-style enrichment and standards-oriented expansion and should normally be completed after the rapid phase.

1. `baseline_quantity` — pre-disaster quantity.
2. `baseline_reference_period` — date or season of the baseline.
3. `damaged_quantity` — quantity damaged.
4. `destroyed_quantity` — quantity destroyed.
5. `repair_cost_estimate` — estimated repair cost.
6. `replacement_cost_estimate` — estimated replacement cost.
7. `direct_damage_estimate` — explicit direct physical damage value.
8. `economic_loss_estimate` — explicit indirect or flow loss value.
9. `admin_compensation_value` — reimbursement-linked or compensation-rule value.
10. `valuation_method_code` — valuation approach used.
11. `valuation_reference_id` — link to unit-cost or valuation reference.
12. `expected_revenue_baseline` — baseline revenue or production flow.
13. `actual_revenue_after_event` — observed post-event revenue or production flow.
14. `assistance_received_value` — financial or in-kind assistance already received.
15. `verification_status` — reviewer-confirmed status.
16. `reviewed_by` — reviewer identity or organization.
17. `reviewed_at` — review timestamp.
18. `observation_note` — free-text context note.

### 4.2.4 Value-type rule

If monetary values are present, the model shall preserve separate fields for at least three distinct meanings.

1. `admin_compensation_value`;
2. `direct_damage_estimate`;
3. `economic_loss_estimate`.

These values must not be merged into a single generic amount field because they are produced by different methods and serve different analytical and administrative purposes, consistent with the Stage 2 judgment stance in [`Stage2_Judgment_Notes.md`](Stage2_Judgment_Notes.md:30).

## 4.3 Baseline reference structure

The minimum viable design should allow a separate baseline structure or reference link rather than embedding all pre-disaster values inside rapid event reporting.

Recommended fields:

1. `baseline_reference_id`;
2. `baseline_dataset_name`;
3. `baseline_indicator_name`;
4. `baseline_value`;
5. `unit_of_measure`;
6. `reference_period`;
7. `spatial_unit_code`;
8. `source_organization`;
9. `source_document`;
10. `quality_note`.

## 4.4 Valuation reference structure

The minimum viable design should allow a separate valuation reference structure to support later estimation without converting Stage 3 into a full estimation engine.

Recommended fields:

1. `valuation_reference_id`;
2. `sector_code`;
3. `impact_item_label`;
4. `valuation_method_code`;
5. `unit_cost`;
6. `repair_cost_unit`;
7. `replacement_cost_unit`;
8. `currency_code`;
9. `price_year`;
10. `source_organization`;
11. `source_document`;
12. `valid_from_date`;
13. `valid_to_date`.

## 5. Linkage rules

### 5.1 Primary linkage

1. One [`DISASTER_RECORD`](Stage3_LossDamage_DataModel_Technical_Specification_Draft.md:48) may link to zero, one, or many [`LOSS_DAMAGE_RECORD`](Stage3_LossDamage_DataModel_Technical_Specification_Draft.md:104) entries.
2. Each `LOSS_DAMAGE_RECORD` must link to exactly one `DISASTER_RECORD`.

### 5.2 Optional support linkage

1. One `LOSS_DAMAGE_RECORD` may link to zero or one baseline reference snapshot.
2. One `LOSS_DAMAGE_RECORD` may link to zero or one valuation reference at minimum, while future versions may support multiple references.
3. Event-level and observation-level records may both link to provenance and workflow audit entries.

## 6. Required-versus-later-completion logic

The data model shall use phased completeness rather than one-time completeness.

### 6.1 Required-now rule

A field belongs in the required-now core only if all three conditions hold.

1. The field is plausibly collectible within current or near-current DDPM-style rapid reporting practice.
2. The field is necessary to identify the event or describe immediate impacts for operational use.
3. The field does not depend on later valuation, baseline reconstruction, or specialist sector verification.

### 6.2 Later-completion rule

A field belongs in later-completion status if one or more of the following applies.

1. It requires sector specialist input.
2. It depends on a baseline dataset.
3. It requires valuation references or calculation logic.
4. It is typically unavailable at the time of urgent reporting.
5. It becomes reliable only after verification or consolidation.

### 6.3 Current completeness categories

For application to real events under [`TOR 5.3.7`](../../inbox_source/CRDB%20-%20TOR.md:192), each field should be scored as:

1. `available_now`;
2. `derivable_later`;
3. `not_currently_available`.

## 7. Validation rules

### 7.1 Identifier and referential integrity

1. `disaster_record_id` and `loss_damage_record_id` must be unique.
2. Every `LOSS_DAMAGE_RECORD` must have a valid parent `disaster_record_id`.
3. `revision_number` must increment by one for each accepted revision.

### 7.2 Controlled-value validation

The following fields should be validated against controlled code lists.

1. `hazard_type_code`;
2. `disaster_management_level`;
3. `collection_phase`;
4. `record_status`;
5. `sector_code`;
6. `ownership_type`;
7. `damage_state`;
8. `valuation_method_code` where used.

### 7.3 Date and sequence validation

1. `event_end_date` must not precede `event_start_date`.
2. `reporting_date` must not precede `event_start_date` unless explicitly flagged as retrospective backfill.
3. `updated_at` must not precede `created_at`.
4. `reviewed_at` must not precede `observation_date`.

### 7.4 Quantity and amount validation

1. Counts and quantities must be non-negative.
2. Monetary fields must store currency code and, where relevant, price year.
3. `damaged_quantity` and `destroyed_quantity` should not exceed `baseline_quantity` when baseline exists, unless explicitly justified by a note.

### 7.5 Completeness validation

1. No record may advance to `submitted` status if required-now fields are empty.
2. Later-completion fields may remain null at rapid stage without blocking submission.
3. Null later-stage fields should be distinguishable from zero values and from not-applicable states.

## 8. Provenance rules

Every event-level and observation-level record shall preserve provenance sufficient to answer four questions: who reported it, through what source, at what phase, and with what verification state.

Minimum provenance requirements:

1. `source_system`;
2. `source_document_type`;
3. `reporting_organization`;
4. `collection_phase`;
5. `record_status`;
6. `created_at`;
7. `updated_at`;
8. `revision_number`.

Recommended additional provenance fields:

1. `reported_by`;
2. `reviewed_by`;
3. `source_document_reference`;
4. `evidence_confidence`;
5. `verification_note`.

## 9. Revision and workflow rules

### 9.1 Status transition rule

The model should support staged status transitions rather than overwrite-only updates. A minimum workflow is:

1. `draft` → `submitted` → `consolidated` → `verified` → `closed`.

The status `revised` may be used when a previously submitted or verified record is updated on the basis of new evidence.

### 9.2 Revision rule

1. Every accepted update must increment `revision_number`.
2. The prior value state should remain recoverable in the audit trail.
3. Verification notes should explain material changes to quantities or monetary values.

### 9.3 Multi-phase rule

The same event may begin as a rapid record and later accumulate verified sector observations, valuation references, and recovery-oriented detail without changing the event identifier.

## 10. Timeliness rules

The specification adopts a timeliness principle aligned to phased reporting rather than one universal deadline.

### 10.1 Rapid phase

Rapid phase records should prioritize event identity, immediate human impact, basic housing impact, utility disruption, urgent needs, and provenance.

### 10.2 Follow-up phase

Follow-up records should add sector observations, baseline links, and early quantified damage where available.

### 10.3 Verified or recovery-oriented phase

Verified or recovery-oriented records may add repair cost, replacement cost, direct damage, economic loss, compensation values, and review outcomes.

### 10.4 Backfill distinction

Historical backfill records must be distinguishable from operational intake by source-system and phase metadata, consistent with the historical-data distinction captured in [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:33).

## 11. Sector structure rule

The logical model should use a broader sector registry rather than hard-coding one presentation taxonomy. However, it should support at minimum the five Thai-facing sector groups signaled by NESDC and summarized in [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:34):

1. agriculture;
2. production;
3. housing;
4. public utilities;
5. cultural heritage.

This approach preserves interoperability while allowing NESDC-aligned reporting views.

## 12. Explicit non-requirement statement

This Stage 3 specification does not require the CRDB Loss and Damage data model to implement a full loss-estimation engine. In practical terms, the draft model may preserve fields and reference hooks for valuation inputs, but it does not require:

1. complete unit-cost libraries across all sectors;
2. automatic estimation formulas for all damage and loss categories;
3. macroeconomic impact computation;
4. complete national reconstruction of historical losses.

Any such expansion should be treated as a separate analytical or implementation work package beyond the minimum viable dataset and reporting-form design required by [`TOR 5.3.6`](../../inbox_source/CRDB%20-%20TOR.md:190).

## 13. Draft implementation reading for Stage 4 writing

For report-writing purposes, this specification supports the following narrative line.

1. The minimum viable core should remain operationally realistic for DDPM-style reporting.
2. The model should separate event headers from repeated loss/damage observations.
3. Richer valuation and baseline-dependent content should be staged as later completion rather than mandatory intake.
4. Provenance, phase, revision, and timeliness controls are the key mechanism that makes this conservative model extensible.

## 14. Draft conclusion

The Stage 2 evidence supports a conservative but extensible technical specification for the LossDamage data model. The minimum operational core should be carried by [`DISASTER_RECORD`](Stage3_LossDamage_DataModel_Technical_Specification_Draft.md:48), while sectoral and valuation detail should be carried by [`LOSS_DAMAGE_RECORD`](Stage3_LossDamage_DataModel_Technical_Specification_Draft.md:104) and related support structures. This keeps the model aligned with current DDPM reporting reality, while still establishing the control fields and logical extension paths needed for later PDNA-oriented and standards-aligned use.
