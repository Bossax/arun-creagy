# DDPM CRI to CRDB MVD Gap Analysis

## 1. Scope and compared artifacts

This report analyzes the gap between DDPM-related data actually available inside the CRI project and the minimum viable design expected by the CRDB loss-and-damage MVD.

Primary compared artifacts:

- DDPM availability review: [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:1)
- Proposed target design: [`Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:1)

Supporting methodological context used only where needed to interpret the design boundary:

- [`DDPM_PDNA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_PDNA_methodology_report.md:1)
- [`DaLA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DaLA_methodology_report.md:1)
- [`comparative_analysis_DaLA_DesInventar_PDNA.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/comparative_analysis_DaLA_DesInventar_PDNA.md:1)

The analysis is limited to the specific gap-identification task. It does **not** modify or reinterpret the target specification itself.

---

## 2. Comparison method and mapping logic

The comparison applies a three-layer mapping logic.

### 2.1 Evidence hierarchy

The analysis privileges currently materialized CRI evidence in the following order:

1. The CRI DDPM availability audit in [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:39)
2. The target MVD structure definitions in [`Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:142)
3. Methodology reports only where design intent depends on phase separation, validation, or analytical treatment of damage/loss, especially [`DDPM_PDNA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_PDNA_methodology_report.md:62)

### 2.2 Source classification used in this report

To avoid mixing unlike evidence, each mapped variable is interpreted against one of three CRI evidence classes:

1. **Native DDPM response reporting**  
   Source-near village/event records and workbook-defined relief reporting preserved in CRI; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:167).

2. **CRI-transformed analytical variables**  
   Canonical hazard mapping, tambon rollups, yearly panels, period totals, percentile fields, and trend fields derived by CRI; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:183).

3. **Post-disaster analytical requirements**  
   Variables expected by PDNA/DaLA-style damage, loss, validation, and recovery-needs logic that are not ordinary first-response DDPM intake fields; see [`DDPM_PDNA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_PDNA_methodology_report.md:108).

### 2.3 Status logic

- **Aligned** = CRI contains data close enough to seed the structure with limited transformation.
- **Partially aligned** = CRI contains some required fields or usable proxies, but important required fields are missing, inconsistent, or only available after CRI derivation.
- **Not aligned** = CRI does not contain the required structure in a credible way, or only contains a weak proxy that would misrepresent the MVD if treated as equivalent.

### 2.4 Gap-cause classification

Each gap is explicitly assigned to one or more of the following causes:

- **True DDPM source absence** = the source reporting itself does not provide the required information.
- **CRI transformation or aggregation choice** = CRI changes the grain, scope, taxonomy, or derivation logic such that the result is no longer a native DDPM variable.
- **Response-phase vs post-disaster analytical mismatch** = the MVD expects PDNA/DaLA-style assessment logic that should occur after early emergency intake.

---

## 3. DDPM availability baseline in CRI

The CRI project exposes two materially different DDPM-related streams, not one unified loss-and-damage dataset:

1. **Village/event impact stream** with event timing, location, affected population, evacuation, deaths, injuries, and multiple damage-category fields; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:41).
2. **Government advance payment stream** with province-hazard-year monetary relief values, explicitly about fiscal response rather than direct damage accounting; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:54).

This distinction is decisive. The richest native DDPM evidence in CRI is non-monetary and source-near, while the monetary stream is a limited public-finance response proxy rather than full damage, loss, or recovery-needs evidence; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:292).

---

## 4. High-level alignment summary

| MVD structure | Status | Short finding |
| :--- | :--- | :--- |
| [`DISASTER_EVENT`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:144) | Partially aligned | Native DDPM event/village reporting supports hazard, dates, status-like context, and human impacts, but not a clean CRDB event anchor with universal key and lifecycle metadata. |
| [`EVENT_LOCATION`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:171) | Partially aligned | Strong native administrative location fields exist, but event-to-place linkage is embedded in source rows rather than normalized into a separate many-to-one geography table. |
| [`ASSESSMENT_CONTEXT`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:185) | Not aligned | CRI DDPM evidence does not expose a materialized provenance/validation layer with phase, assessor, review status, revision trace, and source-document tracking as structured records. |
| [`LD_PHYSICAL_DAMAGE`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:206) | Partially aligned | DDPM contains damage-category reporting and some physical impact signals, but not valuation-ready asset, quantity, cost-basis, or validated monetary-damage records. |
| [`LD_ECONOMIC_LOSS`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:231) | Not aligned | DDPM in CRI does not provide baseline-vs-actual flow loss records. Government advance payment is a response-finance proxy, not economic loss. |
| [`LD_RECOVERY_RECONSTRUCTION_NEEDS`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:255) | Not aligned | No CRI DDPM structure materializes validated recovery or reconstruction needs estimates derived from damage/loss logic. |

---

## 5. Structure-by-structure gap analysis

## 5.1 [`DISASTER_EVENT`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:144)

**Status:** Partially aligned

### What aligns now

The source-near DDPM village stream contains many fields that can seed an event anchor:

- incident identifiers and labels such as `Incident Name` and `Title`; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:43)
- hazard typing in `Disaster Type`; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:45)
- event timing fields including `Disaster Date` and `End Disaster Date`; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:46)
- contextual fields such as `Status`, `Situation`, and `Cause`; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:48)
- human impact counts including affected people, evacuations, deaths, missing, and injured; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:49)

These are close to the intent of early event capture in [`DISASTER_EVENT`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:146).

### What only partially aligns

- A source-side event reference exists in practice, but CRI does not yet expose a single enforced CRDB-grade master event key spanning all downstream layers.
- Reporting level can be inferred from source grain, but is not modeled as an explicit normalized event-level attribute.
- Event status exists in source form, but not yet harmonized to the MVD lifecycle values `Reported`, `Under_Assessment`, `Validated`, `Closed`; compare [`Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:157).

### Clear gaps

- `disaster_event_id` as a universal CRDB anchor key
- `created_by_agency`
- `record_created_at`
- `record_updated_at`
- a normalized `source_assessment_ref` strategy that survives phase changes
- a consistent response-phase note that captures intake limitations as structured metadata

### Gap causes

- **True DDPM source absence:** lifecycle metadata such as record timestamps and curated agency ownership are not present as a relational event master.
- **CRI transformation/aggregation choice:** Gold tables aggregate to tambon and yearly views, which support analysis but weaken direct event-anchor semantics; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:141).
- **Response-phase vs post-disaster mismatch:** later-phase assessments need a universal event key, but current evidence suggests linking across phases is inconsistent; see [`DDPM_PDNA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_PDNA_methodology_report.md:104).

### Native DDPM vs CRI-derived separation

- **Native DDPM:** incident labels, dates, hazard label, human impact counts.
- **CRI-derived or curated requirement:** canonical hazard harmonization, cross-phase event key, lifecycle status mapping, and downstream relational integrity.

### Practical implication

[`DISASTER_EVENT`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:144) can be seeded now, but only as a curated event-anchor layer built from source-near DDPM records rather than directly loaded from any single existing CRI table.

---

## 5.2 [`EVENT_LOCATION`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:171)

**Status:** Partially aligned

### What aligns now

The DDPM village stream is spatially rich. It includes:

- `Province Code`, `Province`
- `District Code`, `District`
- `Subdistrict Code`, `Subdistrict`
- `Moo`, `Village Code`

See [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:47).

This provides strong seed data for `admin_level`, `location_code`, and `location_name` in [`EVENT_LOCATION`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:177).

### What only partially aligns

- DDPM source records carry affected geography directly in each reporting row, but they do not normalize one event to many locations in a dedicated table.
- CRI Gold tables support tambon-level analysis, but those are aggregated analytical views rather than explicit event-location records.

### Clear gaps

- `event_location_id`
- an explicit foreign-key link from each location row to one master `disaster_event_id`
- `is_primary_impact_area`
- `spatial_reference_note`
- polygon-level capture or uncertainty notes

### Gap causes

- **True DDPM source absence:** primary impact designation and spatial uncertainty notes are not native DDPM reporting fields in the available CRI evidence.
- **CRI transformation/aggregation choice:** CRI converts village/event observations into tambon-level aggregates and geometry-constrained outputs, which is useful analytically but not the same as a normalized event geography table; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:237) and [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:264).

### Native DDPM vs CRI-derived separation

- **Native DDPM:** administrative codes and names to village level.
- **CRI-derived or curated requirement:** normalized event-location rows, geometry QA conformance, and any designation of primary impact geography.

### Practical implication

[`EVENT_LOCATION`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:171) is seedable now from source-near location fields, but it requires explicit normalization logic in CRDB rather than reuse of current Gold outputs as if they were source-native location records.

---

## 5.3 [`ASSESSMENT_CONTEXT`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:185)

**Status:** Not aligned

### What aligns now

Only a limited subset of the intended semantics is visible in current evidence:

- DDPM evidence supports the conceptual need for phase separation and validation metadata; see [`DDPM_PDNA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_PDNA_methodology_report.md:69).
- Some response-stage references may exist in source forms, but they are not materialized in the reviewed CRI DDPM outputs as a dedicated structured context table.

### Clear gaps

Current CRI DDPM evidence does **not** materially expose the following as structured relational records:

- `assessment_context_id`
- normalized `assessment_phase`
- normalized `method_family`
- `lead_agency`
- `supporting_agency`
- `assessor_name_or_team`
- `assessment_date`
- `review_status`
- `validation_event_ref`
- `revision_trace_note`
- `source_document_ref`

### Why this is a real design gap

The target MVD requires a bridge between event capture and validated downstream analysis; see [`Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:187). The methodology evidence explicitly warns that validation is part of the method itself rather than an optional editorial step; see [`DDPM_PDNA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_PDNA_methodology_report.md:69).

### Gap causes

- **True DDPM source absence:** the reviewed CRI DDPM data products are dominated by event/village impacts and relief values, not provenance-rich assessment management records.
- **Response-phase vs post-disaster mismatch:** the target structure is inherently cross-phase and validation-heavy, while current DDPM practice is strongest in Phase 0–2 reporting and less mature in later standardized PDNA coverage; see [`DDPM_PDNA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_PDNA_methodology_report.md:94).

### Native DDPM vs CRI-derived separation

- **Native DDPM:** limited source references and event reporting context.
- **Needed but absent:** formal provenance, validation, reviewer, revision, and source-document structures.

### Practical implication

[`ASSESSMENT_CONTEXT`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:185) cannot be credibly backfilled from current CRI DDPM outputs alone. It requires new collection and governance workflows, even if seeded later from DDPM or PDNA forms.

---

## 5.4 [`LD_PHYSICAL_DAMAGE`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:206)

**Status:** Partially aligned

### What aligns now

DDPM source-near reporting contains multiple damage-category variables such as:

- `Housing Damage`
- `Business Damage`
- `Agriculture Damage`
- `Livestock Damage`
- `Fishing Damage`
- `Transport Damage`
- `Health Damage`
- `Culture Damage`
- `Education/Sports`
- `Utilities Damage`
- `Govt Property Damage`

See [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:50).

These can seed sector and subsector interpretation and indicate that DDPM captures physical impact categories at intake stage.

### What only partially aligns

- Some category values may represent counts or magnitudes, but the CRI audit does not support treating them as validated monetary physical damage values.
- Human impacts and category damage signals are present, but not the valuation-ready logic expected in [`LD_PHYSICAL_DAMAGE`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:208).

### Clear gaps

- `assessment_context_id`
- explicit `sector_id` and `subsector_id` aligned to CRDB/NESDC taxonomy
- `asset_type`
- `owner_or_responsible_entity`
- `severity_state`
- `qty_destroyed`
- `qty_damaged`
- `unit_measure`
- `unit_replacement_cost_thb`
- `unit_repair_cost_thb`
- `valuation_basis_note`
- `monetary_damage_thb`
- `validation_status`

### Gap causes

- **True DDPM source absence:** repair/replacement costing assumptions, asset ownership, validated monetary damage, and damage severity states are not available in the reviewed CRI DDPM source-near data.
- **Response-phase vs post-disaster mismatch:** the MVD table is explicitly for downstream valuation after sufficient assessment work; see [`Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:228). Native DDPM response data mostly captures counts and categories, not formal valuation.

### Native DDPM vs CRI-derived separation

- **Native DDPM:** damage category fields and some event-location context.
- **Needed but mostly absent:** valuation basis, quantity semantics, asset classification, and validated damage monetization.

### Practical implication

Current DDPM in CRI can seed a **damage-intake staging layer**, but not the full valuation logic of [`LD_PHYSICAL_DAMAGE`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:206). CRDB should not falsely equate DDPM category counts with PDNA/DaLA-grade physical damage valuation.

---

## 5.5 [`LD_ECONOMIC_LOSS`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:231)

**Status:** Not aligned

### What aligns now

Almost none of the required analytical structure is natively available.

The closest monetary DDPM-related evidence in CRI is the government advance payment stream by province, hazard, and year/period; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:98). But the same audit explicitly states that this stream is about **วงเงินทดรองราชการ** and excludes major categories such as local budget spending, agriculture compensation outside the mechanism, and donations; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:56).

### Why the payment stream is not acceptable as loss

[`LD_ECONOMIC_LOSS`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:231) requires baseline-versus-actual flow disruption logic, including:

- analysis horizon
- baseline quantity or value
- actual post-disaster quantity or value
- valuation basis
- increased operating costs
- calculated monetary loss

The financial relief stream contains only one substantive measure: payment amount; see [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:109). That is a fiscal response measure, not a loss estimate.

The methodological distinction is explicit in [`DDPM_PDNA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_PDNA_methodology_report.md:81): loss is a change in economic flows relative to baseline.

### Clear gaps

All major fields of [`LD_ECONOMIC_LOSS`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:231) are absent or unsupported as structured DDPM/CRI evidence:

- `assessment_context_id`
- `sector_id`, `subsector_id`
- `loss_category`
- `analysis_horizon_start`, `analysis_horizon_end`
- `baseline_quantity_or_value`
- `actual_post_disaster_quantity_or_value`
- `price_or_valuation_basis`
- `increased_costs_thb`
- `monetary_loss_thb`
- `loss_formula_note`
- `validation_status`

### Gap causes

- **True DDPM source absence:** no baseline-vs-actual loss variables are present in the reviewed CRI DDPM data products.
- **Response-phase vs post-disaster mismatch:** economic loss is methodologically a later analytical layer, not a normal first-notification payload; see [`Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:253).
- **CRI transformation/aggregation choice:** the available monetary transformation in CRI normalizes relief spending, which may be useful as a response-finance indicator but does not solve the absence of true loss estimation variables.

### Native DDPM vs CRI-derived separation

- **Native DDPM:** province-level relief disbursement proxy.
- **Needed but absent:** actual economic loss estimation logic.

### Practical implication

[`LD_ECONOMIC_LOSS`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:231) should **not** be pre-populated from the advance-payment stream. That would structurally confuse emergency expenditure with economic loss.

---

## 5.6 [`LD_RECOVERY_RECONSTRUCTION_NEEDS`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:255)

**Status:** Not aligned

### What aligns now

There is no reviewed CRI DDPM table that directly materializes recovery, reconstruction, rehabilitation, or risk-reduction-upgrade needs as validated monetary records.

At most, the methodology evidence supports the **need for such a layer** conceptually; see [`Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:257) and [`DDPM_PDNA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_PDNA_methodology_report.md:128).

### Clear gaps

All major fields are absent from the reviewed CRI DDPM evidence:

- `needs_record_id`
- `assessment_context_id`
- `sector_id`
- `needs_type`
- `time_horizon`
- `derived_from_damage`
- `derived_from_loss`
- `estimated_needs_thb`
- `needs_basis_note`
- `validation_status`

### Gap causes

- **True DDPM source absence:** no direct needs-estimation dataset is present in the available CRI DDPM streams.
- **Response-phase vs post-disaster mismatch:** this table is a derived planning layer that depends on validated damage and/or loss records, which themselves are not materially available from DDPM intake data; see [`Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:273).

### Native DDPM vs CRI-derived separation

- **Native DDPM:** none for formal needs estimation in the reviewed CRI outputs.
- **Needed later analytical layer:** validated sectoral needs logic after damage/loss assessment.

### Practical implication

[`LD_RECOVERY_RECONSTRUCTION_NEEDS`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:255) must remain a later analytical layer and should not be expected from DDPM-derived CRI data without new assessment workflows.

---

## 6. Explicit separation: native DDPM reporting vs CRI-derived analytical variables

This separation is critical for implementation integrity.

### 6.1 Native DDPM reporting actually available in CRI

From the village/event stream:

- event names / incident labels
- hazard labels
- event and declaration dates
- province, district, subdistrict, village identifiers
- affected people and households
- evacuees
- deaths, missing, injured
- multiple damage-category fields

From the advance-payment stream:

- province-hazard-year payment amount
- province-hazard-period total payment amount

See [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:169).

### 6.2 CRI-derived analytical variables that must not be miscatalogued as native DDPM reporting

- canonical hazard mapping
- climate-hazard filtering
- tambon rollups
- yearly panels with zero-filling
- year-over-year deltas and average year-over-year change
- national percentile metrics
- period totals reconstructed from annual values

See [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:185) and [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:288).

### 6.3 Consequence for CRDB design

CRDB can use CRI-derived outputs as **analytical seed layers** or convenience marts, but not as evidence that DDPM natively reports the full MVD structures.

---

## 7. Gap causes consolidated by type

### 7.1 True DDPM source absence

The following MVD expectations are genuinely absent from the reviewed DDPM evidence:

- universal cross-phase event key
- formal assessment-provenance records
- assessor and validation metadata
- sector valuation basis for physical damage
- baseline-vs-actual economic loss inputs
- validated recovery/reconstruction needs estimates

### 7.2 CRI transformation or aggregation choices

CRI improves usability but changes the meaning and grain of data through:

- canonical hazard mapping
- village-to-tambon aggregation
- yearly and multi-year rollups
- zero-filled panels
- national comparative metrics
- derived period totals
- geometry coverage gating and invalid-code exclusion

See [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:255) and [`DDPM_data_review_from_CRI_project.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_data_review_from_CRI_project.md:272).

These transformations are useful, but they mean some CRI-friendly tables cannot be treated as direct DDPM source reporting.

### 7.3 Response-phase reporting vs post-disaster analytical requirements

The deepest structural gap is methodological rather than technical.

- DDPM in CRI is strongest at early impact reporting.
- The target MVD expects later analytical logic for validated damage, economic loss, and needs.
- PDNA-style practice requires assessor identity, review status, revision trace, and baseline construction; see [`DDPM_PDNA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_PDNA_methodology_report.md:69).

So several gaps should **not** be interpreted as ETL failures. They are evidence that the target MVD intentionally spans beyond what early DDPM intake can supply.

---

## 8. Practical implications for CRDB implementation priorities

### 8.1 What can be seeded from DDPM now

Priority seed candidates from current CRI evidence:

1. **Event anchor seed** for [`DISASTER_EVENT`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:144) using incident labels, dates, hazard, status-like context, and human impacts.
2. **Affected geography seed** for [`EVENT_LOCATION`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:171) using province/district/subdistrict/village fields.
3. **Damage-intake staging categories** using DDPM source damage-category fields, but clearly flagged as non-valued, early-stage reporting rather than validated physical damage valuation.
4. **Response-finance indicator layer** using government advance payment, but explicitly classified as relief disbursement / fiscal response rather than economic loss.

### 8.2 What needs new collection or governance workflows

High-priority workflow additions:

1. A universal `disaster_event_id` strategy linking all phases and sectors.
2. A formal [`ASSESSMENT_CONTEXT`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:185) capture process for phase, method family, lead agency, assessor, review status, validation event, and revision trace.
3. Sectoral valuation templates for physical damage with quantity semantics, unit costs, valuation basis, and validation status.
4. Provenance capture rules so source forms, reports, or worksheets are attached to each analytical assessment pass.

### 8.3 What must remain post-disaster analytical layers

The following should remain later-stage analytical structures and should not be backcast into emergency DDPM intake:

1. Full [`LD_ECONOMIC_LOSS`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:231)
2. Full [`LD_RECOVERY_RECONSTRUCTION_NEEDS`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:255)
3. Validated monetary [`LD_PHYSICAL_DAMAGE`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:206) beyond intake-level category counts

### 8.4 Implementation caution

The main structural risk is false equivalence:

- treating CRI Gold aggregates as native DDPM reporting,
- treating government advance payment as economic loss,
- or treating DDPM category counts as validated damage valuation.

Any of those shortcuts would make the MVD appear more complete than the evidence supports.

---

## 9. Concise recommendations

### Recommendation 1: Build Layer A first from source-near DDPM evidence

Prioritize operational implementation of curated event and location anchor tables using source-near village/event reporting as the strongest available DDPM evidence base.

### Recommendation 2: Introduce an explicit intermediate staging layer for DDPM damage indicators

Do not load DDPM category fields directly into [`LD_PHYSICAL_DAMAGE`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:206). Stage them first as non-valued damage indicators pending assessment-context and valuation enrichment.

### Recommendation 3: Keep advance payment separate from loss tables

Store the government advance payment stream, if used, as a response-finance or relief-expenditure module rather than as [`LD_ECONOMIC_LOSS`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:231).

### Recommendation 4: Treat [`ASSESSMENT_CONTEXT`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:185) as a mandatory enabling layer

Without assessment-context capture, CRDB can store values but cannot preserve whether those values are draft intake, validated PDNA estimates, or revised analytical outputs; this follows the methodological warning in [`DDPM_PDNA_methodology_report.md`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/DDPM_PDNA_methodology_report.md:77).

### Recommendation 5: Sequence implementation by evidence maturity

- **Now:** [`DISASTER_EVENT`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:144), [`EVENT_LOCATION`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:171), DDPM damage-intake staging, relief-finance indicator layer
- **Next with workflow reform:** [`ASSESSMENT_CONTEXT`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:185), valuation-ready [`LD_PHYSICAL_DAMAGE`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:206)
- **Later analytical layer:** [`LD_ECONOMIC_LOSS`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:231), [`LD_RECOVERY_RECONSTRUCTION_NEEDS`](ψ/incubate/DCCE/CRDB/output/06_LDM_LossDamage_DataModel/Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:255)

---

## 10. Bottom-line conclusion

The CRI project provides enough DDPM evidence to seed **event**, **location**, and **early impact/damage-indicator** layers, but it does **not** provide a full native DDPM basis for the CRDB loss-and-damage MVD as designed. The sharpest gaps are not only missing fields; they are also methodological boundaries. Current DDPM evidence in CRI is strongest for response-stage event and impact reporting, while the CRDB MVD intentionally extends into validation-heavy, baseline-dependent post-disaster analytical layers for physical damage valuation, economic loss estimation, and recovery/reconstruction needs.

Therefore the correct implementation stance is not to flatten DDPM into the full MVD. It is to use DDPM as a strong Layer A seed, preserve CRI-derived analytics as derived layers, and establish new assessment-context and post-disaster analytical workflows for the Layer B and needs-oriented structures.
