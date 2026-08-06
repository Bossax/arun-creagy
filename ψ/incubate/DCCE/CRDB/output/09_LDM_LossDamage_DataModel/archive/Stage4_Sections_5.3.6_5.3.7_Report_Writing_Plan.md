# Stage 4 Draft — Report-Writing Plan for Sections 5.3.6 and 5.3.7

## 1. Purpose

This planning note translates the Stage 3 technical specification in [`Stage3_LossDamage_DataModel_Technical_Specification_Draft.md`](Stage3_LossDamage_DataModel_Technical_Specification_Draft.md:1) into a writing plan for the final prose required under [`TOR 5.3.6`](../../inbox_source/CRDB%20-%20TOR.md:190) and [`TOR 5.3.7`](../../inbox_source/CRDB%20-%20TOR.md:192). It follows the scope discipline set in [`plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md`](../../../../../../plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md:92).

## 2. Writing control line

The two sections should be written as adjacent but distinct outputs.

1. Section [`5.3.6`](../../inbox_source/CRDB%20-%20TOR.md:190) should explain why the draft Minimum Viable Dataset and reporting form are needed, how DDPM’s current collection practice compares with standards-oriented expectations, and why a PDNA-centered staged reporting form is the most workable design direction.
2. Section [`5.3.7`](../../inbox_source/CRDB%20-%20TOR.md:192) should explain only the method for applying the draft MVD to real events, with emphasis on event selection, field mapping, availability scoring, and gap interpretation.
3. Section [`5.3.7`](../../inbox_source/CRDB%20-%20TOR.md:192) must not drift into full event reconstruction, source excavation, or historical database population.
4. Do not reference internal artifacts, notes, etc. You need to reference the actual author of the sources. 

## 3. Section 5.3.6 writing plan

## 3.1 Section objective

The section should demonstrate that the proposed MVD and reporting form are grounded in three converging lines of evidence:

1. current DDPM data collection reality;
2. international and comparative standards expectations;
3. PDNA-oriented design logic for staged and progressively richer reporting.

## 3.2 Recommended section argument sequence

### 3.2.1 Subsection A — Current DDPM data collection status

Function:

Establish the operational baseline before introducing any proposed design.

Core points to cover:

1. DDPM currently uses a hierarchical urgent reporting flow from local to district to province to central consolidation; see [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:19).
2. Current practice is not PDNA-based and reported values serve reimbursement administration rather than full loss accounting; see [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:20) and [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:21).
3. Current practice does not extend to aggregate macroeconomic assessment, which reinforces the need to keep the minimum viable core operational and bounded; see [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:22).

Expected prose job:

Show that the section begins from actual collectability rather than from an abstract ideal standard.

### 3.2.2 Subsection B — Standards comparison and design implications

Function:

Compare current operational practice with the broader expectations found in standards-oriented and NESDC-aligned material.

Core points to cover:

1. International standards expect structured event metadata, spatial hierarchy, temporal tracking, human impacts, asset impacts, and workflow status; see [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:30).
2. Standards-oriented asset and loss structures require repeated sector or asset-level observations rather than a single flat event form; see [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:31).
3. NESDC adds a Thailand-facing signal that the country still lacks a standardized loss-and-damage database and requires a more consistent structure across sectors; see [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:32) to [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:35).

Expected prose job:

Move from comparison to synthesis by showing that the minimum viable design should not copy international schemas wholesale, but also should not remain limited to reimbursement-only fields.

### 3.2.3 Subsection C — PDNA-centered reporting-form design
%% is PDNA aligned with loss and damage record? or they serve different purpose. Need to analyze overlaps and non-overlaps as basis synthesis for proposing MVD that builds on existing standartd %%

Function:

Present the design resolution: one logical reporting structure with phase-partitioned completeness.

Core points to cover:

1. PDNA evidence separates preparedness baseline, rapid assessment, and detailed sector or recovery-oriented assessment; see [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:25) to [`Stage2_Evidence_Ledger.md`](Stage2_Evidence_Ledger.md:29).
2. The proposed design therefore uses one logical data model with staged field completion rather than one undifferentiated form or multiple disconnected forms; see [`Stage2_Judgment_Notes.md`](Stage2_Judgment_Notes.md:16) to [`Stage2_Judgment_Notes.md`](Stage2_Judgment_Notes.md:21).
3. The event header should remain close to rapid collectable fields, while richer sectoral and valuation fields should be later-completion modules; see [`Stage2_Judgment_Notes.md`](Stage2_Judgment_Notes.md:9) to [`Stage2_Judgment_Notes.md`](Stage2_Judgment_Notes.md:14) and [`Stage3_LossDamage_DataModel_Technical_Specification_Draft.md`](Stage3_LossDamage_DataModel_Technical_Specification_Draft.md:303).

Expected prose job:

End the section with a concise explanation of the chosen logical form: an operationally realistic event-reporting core with modular extension for verified sectoral and valuation detail.

## 3.3 Recommended section structure for 5.3.6

1. Opening paragraph: mandate and problem framing.
2. Current DDPM data collection status.
3. Comparison with standards and NESDC-aligned expectations.
4. Design rationale for the draft MVD and reporting form.
5. Explanation of required-now versus later-completion fields.
6. Closing paragraph linking to the methodology section in [`5.3.7`](../../inbox_source/CRDB%20-%20TOR.md:192).

## 3.4 Points to emphasize

1. Operational realism;
2. staged completeness;
3. distinction between observed counts and later valuation;
4. provenance and revision controls as enabling mechanisms.

## 3.5 Points to avoid

1. promising a complete national loss accounting system immediately;
2. implying that DDPM already operates a PDNA-based collection system;
3. describing the model as a full estimation engine.

## 4. Section 5.3.7 writing plan

## 4.1 Section objective

The section should explain the methodology for applying the draft MVD to selected real events in order to test field practicality, staged completeness, and evidence gaps.

## 4.2 Recommended section argument sequence

### 4.2.1 Subsection A — Objective and boundary of testing
%% we should mention DDPM datasets. You can refer to [[ψ/incubate/DCCE/CRI/data_system/metadata/data-lineage|data-lineage]] in CRI project for candidate sources %%
Function:

State clearly that testing means structured application of the MVD to representative events, not complete event reconstruction.

Core points to cover:

1. The controlling plan limits this section to methodology for applying the MVD to real events; see [`plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md`](../../../../../../plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md:39).
2. The purpose is to test field availability, mapping logic, and minimum-core realism.
3. The section should frame the exercise as a bounded validation method rather than a data excavation task.

### 4.2.2 Subsection B — Event selection logic

Function:

Explain how representative events should be chosen.

Core points to cover:

1. select a small number of events sufficient to test different hazard or reporting conditions;
2. prefer events with enough source material to support mapping without requiring full reconstruction;
3. ensure the selected set is adequate to reveal whether required-now fields are consistently collectable.

Expected prose job:

Keep the selection logic methodological and generic unless the final drafting stage is instructed to name specific events.

### 4.2.3 Subsection C — Field mapping procedure

Function:

Describe the operational steps for applying the MVD to each event.

Core points to cover:

1. compile the available event documents;
2. map each document to the fields in [`Stage3_LossDamage_DataModel_Technical_Specification_Draft.md`](Stage3_LossDamage_DataModel_Technical_Specification_Draft.md:1);
3. record whether each field is directly available, derivable later, or not currently available;
4. capture provenance and notes for every mapped field;
5. distinguish event-header fields from repeated sector or loss/damage observations.

Evidence anchor:

The sequence is directly aligned to the Stage 2 testing skeleton in [`Stage2_Technical_Synthesis_Skeleton.md`](Stage2_Technical_Synthesis_Skeleton.md:196).

### 4.2.4 Subsection D — Interpretation of testing results

Function:

Explain how the mapping results should be read.

Core points to cover:

1. fields consistently available across events support the minimum mandatory core;
2. fields frequently derivable only later should remain in later-completion modules;
3. fields consistently absent may indicate either an unrealistic requirement or a future system-improvement need;
4. the output should inform refinement of field priority, provenance rules, and phase logic.

Expected prose job:

Show that testing is used to calibrate the model, not to produce a definitive historical database.

## 4.3 Recommended section structure for 5.3.7

1. Opening paragraph: testing objective and boundary.
2. Event selection logic.
3. Field mapping and scoring procedure.
4. Gap interpretation and refinement logic.
5. Closing paragraph: how testing feedback improves the draft MVD.

## 4.4 Points to emphasize

1. bounded methodology;
2. field-availability scoring;
3. provenance capture during mapping;
4. feedback loop into model refinement.

## 4.5 Points to avoid

1. narrative drift into detailed case studies;
2. promises of complete backfill for all historical disasters;
3. turning the section into a standalone database-population plan.

## 5. Cross-section consistency rules

The final prose for both sections should maintain the following consistency rules.

1. Use the same distinction between `DISASTER_RECORD` and `LOSS_DAMAGE_RECORD` throughout the narrative; see [`Stage3_LossDamage_DataModel_Technical_Specification_Draft.md`](Stage3_LossDamage_DataModel_Technical_Specification_Draft.md:48) and [`Stage3_LossDamage_DataModel_Technical_Specification_Draft.md`](Stage3_LossDamage_DataModel_Technical_Specification_Draft.md:104).
2. Use the same staged completeness vocabulary: required-now, later-completion, and not-currently-available.
3. Preserve the same scope boundary against full loss-estimation engine claims; see [`Stage3_LossDamage_DataModel_Technical_Specification_Draft.md`](Stage3_LossDamage_DataModel_Technical_Specification_Draft.md:389).
4. Keep provenance, revision, and timeliness controls visible as central design logic rather than as technical afterthoughts.

## 6. Drafting handoff note for Stage 5

When moving into final prose drafting, the writing should proceed in this order.

1. draft [`5.3.6`](../../inbox_source/CRDB%20-%20TOR.md:190) first, because it establishes the operational problem, comparative standards frame, and MVD design rationale;
2. draft [`5.3.7`](../../inbox_source/CRDB%20-%20TOR.md:192) second, because it should read as the application method derived from the model described in [`5.3.6`](../../inbox_source/CRDB%20-%20TOR.md:190);
3. perform a consistency pass to ensure the model boundary, field-staging logic, and non-requirement for a full estimation engine are stated consistently across both sections.
