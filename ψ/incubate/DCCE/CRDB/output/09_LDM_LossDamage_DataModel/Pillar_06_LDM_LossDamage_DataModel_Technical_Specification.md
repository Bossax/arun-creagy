# Pillar 06: LDM (Loss & Damage Model) Technical Specification

## 1. Executive Summary & Design Position

This technical specification revises the Loss and Damage Model (LDM) Minimum Viable Dataset (MVD) so that it reflects the evidence-led three-layer logic established in the current orchestration plan: [`plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md`](../../../../../../plans/2026-06-25_crdb-ldm-5.3.6-5.3.7-execution-plan.md:205).

The design position is no longer that the intake layer is already DaLA-like or fully PDNA-ready. The current evidence instead supports a layered architecture:

1. **Layer A — DDPM current event capture reality**: a response-phase event anchor built from what DDPM and local actors can realistically collect in Phase 1 and Phase 2 style assessment workflows.
2. **Layer B — PDNA and DaLA post-disaster assessment requirements**: downstream analytical structures for baseline comparison, physical damage valuation, economic loss estimation, validation, and recovery planning.
3. **Layer C — CRDB target architecture**: a Thailand-ready relational model that links the emergency event anchor to later sector assessments without pretending they are the same data product.

This revision is consistent with the bounded findings in [`DaLA_methodology_report.md`](DaLA_methodology_report.md:157), [`DDPM_PDNA_methodology_report.md`](DDPM_PDNA_methodology_report.md:138), and [`comparative_analysis_DaLA_DesInventar_PDNA.md`](comparative_analysis_DaLA_DesInventar_PDNA.md:218).

### 1.1 Core design judgments

- **Do not treat the event-intake layer as a disguised DaLA form.** DaLA is a post-disaster economic assessment methodology, not a frontline intake template; see [`DaLA_methodology_report.md`](DaLA_methodology_report.md:157).
- **Do not assume DDPM alone can populate later-stage PDNA content.** The evidence supports DDPM as event and coordination anchor, with deeper sector content often owned by sector agencies; see [`DDPM_PDNA_methodology_report.md`](DDPM_PDNA_methodology_report.md:11).
- **Do not flatten damage, loss, and needs into one record.** The evidence supports separate but linked structures for event anchor, damage, loss, validation, and needs; see [`comparative_analysis_DaLA_DesInventar_PDNA.md`](comparative_analysis_DaLA_DesInventar_PDNA.md:208).
- **Preserve a bounded caveat on PDNA evidence depth.** Detailed Phase 3–4 field evidence remains strongest in agriculture and must not be overclaimed as full cross-sector DDPM operationalization; see [`DDPM_PDNA_methodology_report.md`](DDPM_PDNA_methodology_report.md:140).

### 1.2 Scope boundary for this specification

This specification defines the revised MVD design package for CRDB relational architecture. It does **not** claim that all required baseline, valuation, validation, and recovery-planning fields are already available in current DDPM operational intake. It also does **not** convert the MVD into a single all-purpose disaster record.

### 1.3 Platform Layer Tagging & Product Classification

Per the CRDB Final Sprint Architecture Plan ([`01_Business_Objective_Platform_Rationale/2026-08-06-Business-Objective-Platform-Rationale.md`](../01_Business_Objective_Platform_Rationale/2026-08-06-Business-Objective-Platform-Rationale.md)), this specification explicitly delineates the **Data Platform Engine** from the **Web Presentation Layer**:

- **Data Platform Core Engine (Backend & Schema)**: The 6 relational MVD tables (`DISASTER_EVENT`, `EVENT_LOCATION`, `ASSESSMENT_CONTEXT`, `LD_PHYSICAL_DAMAGE`, `LD_ECONOMIC_LOSS`, `LD_RECOVERY_RECONSTRUCTION_NEEDS`), G1–G5 data quality validation gates, and NESDC 5-sector valuation math ($\text{Damage} + \text{Loss}$).
- **Web Presentation Layer (Frontend & Services)**: Service Package 4 visualization endpoints (e.g. disaster risk maps, dashboard summary cards).
- **Data Ingestion & Field Collection Product**: The standalone field survey template ([`LossDamage_Printable_Reporting_Form.md`](LossDamage_Printable_Reporting_Form.md)) is classified as an explicit **Data Ingestion & Field Collection Product** backed by this MVD database schema, standardizing ground-level survey collection across provincial and local officers prior to database ingestion.

---

## 2. Why the architecture must be layered and relational

The main design danger in the previous framing was category collapse: treating one event record as if it could serve simultaneously as emergency notification, physical damage ledger, economic loss model, and recovery-planning instrument. The current evidence rejects that simplification.

### 2.1 Methodological reasons

The three methodologies in the evidence base solve different problems:

- **DesInventar-like logic** is closest to minimum viable event registration.
- **DaLA logic** is strongest for separating physical damage from economic loss and linking both to recovery and reconstruction needs.
- **PDNA logic** is strongest for staged validation and recovery-oriented assessment workflow.

This comparative position is stated explicitly in [`comparative_analysis_DaLA_DesInventar_PDNA.md`](comparative_analysis_DaLA_DesInventar_PDNA.md:218).

### 2.2 Data-model reasons

A flattened disaster record cannot credibly preserve all of the following distinct data classes:

1. event timing, location, and immediate human impacts
2. asset-level physical destruction and repair/replacement assumptions
3. baseline-versus-actual economic flow comparison
4. sector validation and revision history
5. recovery, reconstruction, and needs-related outputs

This separation is methodologically required by DaLA baseline and counterfactual logic; see [`DaLA_methodology_report.md`](DaLA_methodology_report.md:61).

### 2.3 Operational reasons

The DDPM evidence indicates that early forms and later PDNA structures do not yet demonstrate a single mature universal key across all phases. The CRDB target architecture must therefore impose relational linking more clearly than the source forms themselves currently do; see [`DDPM_PDNA_methodology_report.md`](DDPM_PDNA_methodology_report.md:60).

---

## 3. Three-Layer MVD Design Logic

### 3.1 Layer A — DDPM current event capture reality

**Purpose:** capture the minimum validated event anchor from response-phase and rapid-assessment workflows.

**Evidence base:** DDPM Phase 1 and Phase 2 logic, plus the comparative conclusion that the intake layer should remain closer to DesInventar-style event registration than to full economic assessment; see [`DDPM_PDNA_methodology_report.md`](DDPM_PDNA_methodology_report.md:118) and [`comparative_analysis_DaLA_DesInventar_PDNA.md`](comparative_analysis_DaLA_DesInventar_PDNA.md:169).

**What this layer should contain:**

- unique disaster/event identifier
- hazard type and event classification
- event timing and duration
- administrative and geospatial location references
- direct human impacts and emergency status indicators
- basic affected/damaged counts that are realistically available in early assessment
- provenance and workflow status fields

**What this layer should not claim to contain by default:**

- complete baseline data
- sector-complete physical valuation
- full economic loss calculations
- validated recovery or reconstruction needs

### 3.2 Layer B — PDNA and DaLA post-disaster assessment requirements

**Purpose:** support later sector-based assessment after the emergency phase, including baseline definition, damage valuation, loss estimation, validation, and recovery planning.

**Evidence base:** [`DaLA_methodology_report.md`](DaLA_methodology_report.md:159) and [`DDPM_PDNA_methodology_report.md`](DDPM_PDNA_methodology_report.md:116).

**What this layer should contain:**

- sector baseline records or baseline references
- physical damage assessment tables
- economic loss assessment tables
- validation and review metadata
- recovery and reconstruction / needs-related outputs where methodologically justified

### 3.3 Layer C — CRDB target architecture

**Purpose:** provide a normalized national architecture that bridges current DDPM event capture reality with future PDNA- and DaLA-compatible sector analysis.

**Design rule:** Layer C must not erase the distinction between the first-notification event card and later analytical valuation structures. It must preserve a strong event anchor while allowing one event to link to many downstream assessment records.

---

## 4. Revised Core Entity-Relationship Architecture

The revised CRDB MVD is organized around one event anchor and multiple downstream analytical structures.

### 4.1 Core entities

1. **`DISASTER_EVENT`** — the emergency/event anchor record
2. **`EVENT_LOCATION`** — one-to-many geography detail linked to the event where multiple affected administrative units or spatial extents must be preserved
3. **`ASSESSMENT_CONTEXT`** — metadata about assessment phase, responsible agency, provenance, review status, and linkage between Layer A and Layer B records
4. **`LD_PHYSICAL_DAMAGE`** — sectoral physical damage valuation records
5. **`LD_ECONOMIC_LOSS`** — sectoral economic loss estimation records
6. **`LD_RECOVERY_RECONSTRUCTION_NEEDS`** — derived recovery / reconstruction / needs-related records linked to validated assessments

### 4.2 Cardinality logic

- one [`DISASTER_EVENT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:81) may link to many [`EVENT_LOCATION`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:82) records
- one [`DISASTER_EVENT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:81) may link to many [`ASSESSMENT_CONTEXT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:83) records across phases or agencies
- one [`ASSESSMENT_CONTEXT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:83) may link to many [`LD_PHYSICAL_DAMAGE`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:84) records
- one [`ASSESSMENT_CONTEXT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:83) may link to many [`LD_ECONOMIC_LOSS`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:85) records
- one or more validated damage/loss groups may link to many [`LD_RECOVERY_RECONSTRUCTION_NEEDS`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:86) records

### 4.3 Why `ASSESSMENT_CONTEXT` is required

The prior design linked damage and loss directly to the event alone. That is insufficient for the current evidence because PDNA and DaLA are validation-heavy and phase-sensitive. A dedicated assessment metadata layer is needed to record:

- assessment phase such as Phase 1, Phase 2, Phase 3–4, or DaLA-style analytical pass
- responsible agency or sector lead
- assessor identity or source provenance
- estimation date and review date
- validation status and revision trace

This follows the methodological implications in [`DDPM_PDNA_methodology_report.md`](DDPM_PDNA_methodology_report.md:69) and [`DaLA_methodology_report.md`](DaLA_methodology_report.md:143).

---

## 5. Revised MVD Table Package and Roles

## 5.1 `DISASTER_EVENT` (Table: event anchor)

This table is the Layer A anchor. It captures what can be credibly established about the event during the response and rapid-assessment window.

| Field Name | Data Type | Validation / Description |
| :--- | :--- | :--- |
| `disaster_event_id` | VARCHAR(50) | **Primary Key**. CRDB master disaster/event identifier enforced across all layers. |
| `source_assessment_ref` | VARCHAR(100) | Source-side assessment reference where available, such as DDPM Phase 1 / Phase 2 reference number. |
| `hazard_type` | ENUM | Controlled hazard taxonomy aligned to CRDB / NESDC classification. |
| `event_name` | VARCHAR(255) | Optional human-readable event label. |
| `event_start_date` | DATE | Date impact began or was first confirmed. |
| `event_end_date` | DATE | Date impact ended or stabilized where known. |
| `event_duration_days` | INT | Calculated where start and end dates are available. |
| `event_status` | ENUM | `Reported`, `Under_Assessment`, `Validated`, `Closed`. |
| `reporting_level` | ENUM | e.g. `Province`, `District`, `Subdistrict`, `Multi-Area`. |
| `num_affected_pop` | INT | Directly affected population where available from early assessment. |
| `num_evacuated` | INT | Evacuated population where available. |
| `num_dead` | INT | Confirmed deaths. |
| `num_missing` | INT | Confirmed missing persons. |
| `num_injured` | INT | Confirmed injured persons. |
| `response_phase_note` | TEXT | Short note on event capture conditions or important intake limitations. |
| `created_by_agency` | VARCHAR(255) | Agency submitting or curating the event anchor. |
| `record_created_at` | DATETIME | Record creation timestamp. |
| `record_updated_at` | DATETIME | Last update timestamp. |

**Role clarification:** [`DISASTER_EVENT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:113) is not a full PDNA or DaLA assessment table. It is the universal event anchor required so later structures can link cleanly back to one master record.

## 5.2 `EVENT_LOCATION` (Table: affected geography detail)

This table separates event identity from affected-place detail so one event can relate to multiple provinces, districts, or spatial polygons.

| Field Name | Data Type | Validation / Description |
| :--- | :--- | :--- |
| `event_location_id` | VARCHAR(50) | **Primary Key**. |
| `disaster_event_id` | VARCHAR(50) | **Foreign Key** to [`DISASTER_EVENT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:113). |
| `admin_level` | ENUM | `Province`, `District`, `Subdistrict`, `Village`, `Polygon`. |
| `location_code` | VARCHAR(20) | Standard administrative or geospatial code. |
| `location_name` | VARCHAR(255) | Human-readable place name. |
| `is_primary_impact_area` | BOOLEAN | Marks the primary impact zone when relevant. |
| `spatial_reference_note` | TEXT | Notes on boundary quality, source, or uncertainty. |

## 5.3 `ASSESSMENT_CONTEXT` (Table: phase, provenance, and validation context)

This table creates the bridge between Layer A event capture and Layer B analytical assessment.

| Field Name | Data Type | Validation / Description |
| :--- | :--- | :--- |
| `assessment_context_id` | VARCHAR(50) | **Primary Key**. |
| `disaster_event_id` | VARCHAR(50) | **Foreign Key** to [`DISASTER_EVENT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:113). |
| `assessment_phase` | ENUM | `Phase_1_Initial`, `Phase_2_Rapid`, `Phase_3_4_PDNA`, `DaLA_Analytical`, `Other`. |
| `method_family` | ENUM | `DDPM_Event`, `PDNA`, `DaLA`, `Hybrid`. |
| `lead_agency` | VARCHAR(255) | Agency or unit responsible for the assessment pass. |
| `supporting_agency` | VARCHAR(255) | Optional collaborating agency or sector lead. |
| `assessor_name_or_team` | VARCHAR(255) | Named assessor, unit, or sector team. |
| `assessment_date` | DATE | Date of assessment or compilation. |
| `review_status` | ENUM | `Draft`, `Under_Review`, `Validated`, `Revised`, `Final`. |
| `validation_event_ref` | VARCHAR(100) | Meeting, workshop, or review reference where applicable. |
| `revision_trace_note` | TEXT | Short correction or change log. |
| `source_document_ref` | TEXT | Reference to form, worksheet, report, or evidence packet used. |

**Role clarification:** this table prevents the CRDB model from collapsing emergency intake and downstream validated analysis into one undifferentiated record.

## 5.4 `LD_PHYSICAL_DAMAGE` (Table: physical damage valuation)

This table stores Layer B direct physical damage records. It is explicitly downstream from the event anchor and should normally be attached through an assessment context.

| Field Name | Data Type | Validation / Description |
| :--- | :--- | :--- |
| `damage_record_id` | VARCHAR(50) | **Primary Key**. |
| `assessment_context_id` | VARCHAR(50) | **Foreign Key** to [`ASSESSMENT_CONTEXT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:136). |
| `disaster_event_id` | VARCHAR(50) | Redundant foreign key for easier querying and integrity checks. |
| `sector_id` | ENUM | High-level sector taxonomy: 'Agriculture', 'Production_Manufacturing', 'Housing', 'Public_Utilities', 'Cultural_Heritage'. |
| `subsector_id` | VARCHAR(100) | Subsector category (e.g., 'Crops', 'Livestock', 'Aquaculture', 'Manufacturing', 'Hotels'). |
| `asset_type` | VARCHAR(255) | Asset class or asset description. |
| `owner_or_responsible_entity` | VARCHAR(255) | Ownership or responsible entity where relevant. |
| `severity_state` | ENUM | `Destroyed`, `Damaged`, `Mixed`, `Unknown`. |
| `qty_destroyed` | DECIMAL(18,2) | Units fully destroyed. |
| `qty_damaged` | DECIMAL(18,2) | Units partially damaged. |
| `unit_measure` | VARCHAR(50) | Unit of measure such as household, rai, km, building, facility. |
| `unit_replacement_cost_thb` | DECIMAL(18,2) | Replacement cost assumption. |
| `unit_repair_cost_thb` | DECIMAL(18,2) | Repair cost assumption. |
| `valuation_basis_note` | TEXT | Cost source, price basis, or costing assumption. |
| `monetary_damage_thb` | DECIMAL(18,2) | Calculated or validated monetary damage amount. |
| `validation_status` | ENUM | `Draft`, `Reviewed`, `Validated`, `Revised`. |

**Role clarification:** [`LD_PHYSICAL_DAMAGE`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:154) is not an intake damage count table alone. It is the structure for sectoral physical valuation after sufficient assessment work exists.

## 5.5 `LD_ECONOMIC_LOSS` (Table: economic flow disruption)

This table stores Layer B economic loss records. It should not be populated as if loss were simply another immediate incident count.

| Field Name | Data Type | Validation / Description |
| :--- | :--- | :--- |
| `loss_record_id` | VARCHAR(50) | **Primary Key**. |
| `assessment_context_id` | VARCHAR(50) | **Foreign Key** to [`ASSESSMENT_CONTEXT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:136). |
| `disaster_event_id` | VARCHAR(50) | Redundant foreign key for easier querying and integrity checks. |
| `sector_id` | ENUM | High-level sector taxonomy: 'Agriculture', 'Production_Manufacturing', 'Housing', 'Public_Utilities', 'Cultural_Heritage'. |
| `subsector_id` | VARCHAR(100) | Subsector category (e.g., 'Crops', 'Livestock', 'Aquaculture', 'Manufacturing', 'Hotels'). |
| `loss_category` | ENUM | `Yield_Reduction`, `Foregone_Revenue`, `Service_Disruption`, `Increased_Op_Cost`, `Emergency_Expense`, `Rent_Housing`, `Other`. |
| `analysis_horizon_start` | DATE | Start date of the loss-estimation period. |
| `analysis_horizon_end` | DATE | End date of the loss-estimation period. |
| `baseline_quantity_or_value` | DECIMAL(18,2) | Expected baseline quantity or value in the no-disaster case. |
| `actual_post_disaster_quantity_or_value` | DECIMAL(18,2) | Observed or estimated post-disaster quantity or value. |
| `price_or_valuation_basis` | TEXT | Price assumption, market basis, or valuation note. |
| `increased_costs_thb` | DECIMAL(18,2) | Additional operating or coping costs. |
| `monetary_loss_thb` | DECIMAL(18,2) | Calculated or validated economic loss amount. |
| `loss_formula_note` | TEXT | Notes on formula, assumptions, or baseline construction. |
| `validation_status` | ENUM | `Draft`, `Reviewed`, `Validated`, `Revised`. |

**Role clarification:** [`LD_ECONOMIC_LOSS`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:176) is a baseline-versus-actual analytical table. It should be treated as post-disaster valuation logic, not as a normal first-notification payload.

## 5.6 `LD_RECOVERY_RECONSTRUCTION_NEEDS` (Table: derived needs layer)

This table stores needs-related outputs only after damage and/or loss records have reached a suitable level of validation.

| Field Name | Data Type | Validation / Description |
| :--- | :--- | :--- |
| `needs_record_id` | VARCHAR(50) | **Primary Key**. |
| `assessment_context_id` | VARCHAR(50) | **Foreign Key** to [`ASSESSMENT_CONTEXT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:136). |
| `disaster_event_id` | VARCHAR(50) | **Foreign Key** to [`DISASTER_EVENT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:113). |
| `sector_id` | ENUM | High-level sector taxonomy: 'Agriculture', 'Production_Manufacturing', 'Housing', 'Public_Utilities', 'Cultural_Heritage'. |
| `needs_type` | ENUM | `Recovery`, `Reconstruction`, `Rehabilitation`, `Risk_Reduction_Upgrade`, `Other`. |
| `time_horizon` | ENUM | `Short_Term`, `Medium_Term`, `Long_Term`. |
| `derived_from_damage` | BOOLEAN | Indicates whether calculation references damage records. |
| `derived_from_loss` | BOOLEAN | Indicates whether calculation references loss records. |
| `estimated_needs_thb` | DECIMAL(18,2) | Monetary estimate for the need. |
| `needs_basis_note` | TEXT | Notes on assumptions, improvement factors, inflation, or mitigation additions. |
| `validation_status` | ENUM | `Draft`, `Reviewed`, `Validated`, `Revised`. |

**Role clarification:** recovery and reconstruction needs are not normal emergency intake fields. They are derived planning outputs, consistent with the interpretation in [`DaLA_methodology_report.md`](DaLA_methodology_report.md).

---

## 6. Distinct roles of the major data structures

### 6.1 Event record / disaster anchor

The event anchor answers: **what happened, where, when, and with what immediately observable human and operational consequences?**

Its role is identity, timing, location, and minimal validated intake.

### 6.2 Physical damage tables

Physical damage tables answer: **what tangible assets were destroyed or damaged, in what quantity, and at what repair or replacement value?**

Their role is stock/asset destruction valuation.

### 6.3 Economic loss tables

Economic loss tables answer: **what post-disaster economic flows changed relative to baseline, over what period, and with what resulting monetary effect?**

Their role is flow disruption valuation.

### 6.4 Recovery / reconstruction / needs-related structures

Needs-related structures answer: **what interventions and resources are required to restore function, rebuild assets, or improve resilience after validated assessment?**

Their role is planning and programming, not initial event notification.

---

## 7. Sectoral workflow interpretation for the revised MVD

### 7.1 Early-phase workflow

DDPM and local actors populate [`DISASTER_EVENT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:113) and related [`EVENT_LOCATION`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:120) records using Phase 1 and Phase 2 style inputs.

### 7.2 Later-phase workflow

Sector agencies and later assessment teams populate [`ASSESSMENT_CONTEXT`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:136), [`LD_PHYSICAL_DAMAGE`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:154), [`LD_ECONOMIC_LOSS`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:176), and where justified [`LD_RECOVERY_RECONSTRUCTION_NEEDS`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:197).

### 7.3 Cross-sector caution

The workflow logic can be generalized at the architectural level, but detailed Phase 3–4 field evidence remains strongest in agriculture. Therefore this specification adopts shared structural principles while avoiding claims that every sector already has equally mature Thai PDNA field templates; see [`DDPM_PDNA_methodology_report.md`](DDPM_PDNA_methodology_report.md:132).

---

## 8. Implementation directives for CRDB target architecture

### 8.1 Required design controls

- enforce one CRDB master event key across all layers
- require assessment-phase and method-family metadata for downstream records
- separate physical damage from economic loss at table level
- preserve validation and revision metadata for analytical records
- allow sector extensions without changing the common event anchor

### 8.2 Recommended future sector extensibility

The core MVD should remain stable, while sector-specific child tables can later extend it for agriculture, housing, infrastructure, livelihoods, and other sectors. This aligns with the evidence that both DaLA and PDNA operate through sector templates rather than one universal full-detail schema; see [`DaLA_methodology_report.md`](DaLA_methodology_report.md:151).

### 8.3 Explicit non-claim

This technical specification does **not** claim that current DDPM intake already supplies all fields needed for DaLA-compatible loss estimation or full PDNA recovery planning. The design instead defines the relational target architecture needed to bridge from current event capture reality toward those later analytical capabilities.

---

## 9. Bounded conclusion

The revised MVD design package now reflects the evidence-led three-layer logic required by the current orchestration plan.

- **Layer A** preserves a clear event anchor grounded in DDPM current event-capture reality.
- **Layer B** separates physical damage, economic loss, and needs-related post-disaster analytical structures.
- **Layer C** defines the CRDB target architecture as a relational bridge between early intake and later sector assessment.

The strongest structural change is that the specification no longer assumes the intake layer is already DaLA-like or fully PDNA-ready. Instead, it treats the emergency event record as the anchor and locates damage, loss, validation, and recovery/reconstruction logic in linked downstream tables.

The preserved caveat is explicit: the current PDNA field evidence remains agriculture-weighted and should guide architectural layering, but it should not be overclaimed as full cross-sector DDPM operationalization.
