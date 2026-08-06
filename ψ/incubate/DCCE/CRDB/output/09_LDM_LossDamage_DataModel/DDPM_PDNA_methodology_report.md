# DDPM PDNA Methodology Report

## Purpose of this artifact

This report consolidates the currently available evidence on how the DDPM-linked PDNA workflow is described in the extracted material and what that means for later CRDB MVD redesign. It is intentionally bounded. The present evidence base is sufficient to draft a defensible methodological note, but it is not broad enough to claim full cross-sector coverage of all Thai PDNA practice. The strongest evidence is agriculture-weighted, especially through the Phase 3–4 agricultural form evidence captured in [`ψ/incubate/DCCE/CRDB/inbox_source/raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation.md`](../../../inbox_source/raw-extraction-from-notebooklm_Disaster-Risk%20Reduction-Thailand's-Department-of-Disaster%20Prevention-and-Mitigation.md:12) and [`2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md`](archive/extracts/2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md:68).

## 1. Institutional placement of PDNA in DDPM practice

The existing extraction places PDNA inside a broader DDPM-led disaster assessment architecture spanning Phase 0 to Phase 4 rather than as a standalone one-off form; see [`2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md`](archive/extracts/2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md:29). DDPM is described as having a significant role in early phases and a joint role with responsible sector agencies in later PDNA phases. For the agriculture case, the Ministry of Agriculture and Cooperatives is explicitly named as lead, with DDPM participating especially where human recovery needs and cross-sector coordination matter; see [`2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md`](archive/extracts/2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md:31).

This institutional placement matters for CRDB because it argues against designing the loss-and-damage data model as if DDPM alone owns every later-stage sector assessment field. The evidence instead supports a layered, cross-agency model with DDPM as the event and coordination anchor and sector agencies as deeper content owners for many recovery-oriented records.

## 2. Workflow stages

### 2.1 Phase logic across the wider assessment system

The extraction supports a staged sequence:

1. **Phase 0 preparedness** with baseline and readiness data
2. **Phase 1 initial disaster assessment** in the first 0–72 hours
3. **Phase 2 MIRA / CLA rapid assessment** within roughly 14 days
4. **Phase 3–4 PDNA / recovery strategy** after the emergency phase

These steps are summarized in [`2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md`](archive/extracts/2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md:50).

The raw NotebookLM extraction also returns a broader sequential PDNA process from initiation and preparation through data collection, consolidation, recovery strategy formulation, and resource mobilization; see [`ψ/incubate/DCCE/CRDB/inbox_source/raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation.md`](../../../inbox_source/raw-extraction-from-notebooklm_Disaster-Risk%20Reduction-Thailand's-Department-of-Disaster%20Prevention-and-Mitigation.md:22). Because the current source base is mixed between a DDPM report and a notebook extraction route, the safest interpretation is that DDPM practice is being framed as part of a staged post-disaster needs assessment architecture rather than a single emergency reporting form.

### 2.2 Operational steps in the agricultural Phase 3–4 evidence

The agricultural PDNA example gives the clearest operational sequence currently evidenced:

1. create pre-disaster baseline data
2. assess damages and losses
3. verify damage and loss data
4. formulate recovery strategy

This sequence is explicitly summarized in [`2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md`](archive/extracts/2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md:57).

For later CRDB redesign, this means PDNA-related structures must support not only impact recording but also baseline comparison, validation workflow, and recovery-planning outputs.

## 3. Forms, keys, and linking logic

### 3.1 Phase 1 and Phase 2 forms

The raw extraction identifies concrete field groups for:

- the Phase 1 initial disaster assessment form
- the Phase 2 MIRA multi-cluster rapid assessment form

Phase 1 fields include affected population, evacuation, deaths, injuries, missing persons, damaged utilities, and housing damage states; see [`raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation.md`](../../../inbox_source/raw-extraction-from-notebooklm_Disaster-Risk%20Reduction-Thailand's-Department-of-Disaster%20Prevention-and-Mitigation.md:1). Phase 2 fields expand into multi-cluster needs and sector conditions such as damaged occupational assets, public infrastructure, NFIs, WASH, health-service availability, and food access; see [`raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation.md`](../../../inbox_source/raw-extraction-from-notebooklm_Disaster-Risk%20Reduction-Thailand's-Department-of-Disaster%20Prevention-and-Mitigation.md:7).

### 3.2 Phase 3–4 agricultural PDNA tables

The strongest detailed evidence is the agriculture form. It contains baseline sheets for agricultural households, production, monthly readiness-to-market, water sources, and agricultural inputs/assets, followed by damage, loss, aggregation, validation, and recovery-planning blocks; see [`2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md`](archive/extracts/2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md:98) and [`raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation.md`](../../../inbox_source/raw-extraction-from-notebooklm_Disaster-Risk%20Reduction-Thailand's-Department-of-Disaster%20Prevention-and-Mitigation.md:12).

### 3.3 Explicit keys and identifiers

The raw extraction states that both the Phase 1 and Phase 2 forms use [`หมายเลขอ้างอิงแบบประเมิน`](../../../inbox_source/raw-extraction-from-notebooklm_Disaster-Risk%20Reduction-Thailand's-Department-of-Disaster%20Prevention-and-Mitigation.md:16) as an assessment reference number. For the agricultural Phase 3–4 form, no single clean ID was extracted; instead, linkage appears to rely contextually on crop year and affected province in the table headers; see [`raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation.md`](../../../inbox_source/raw-extraction-from-notebooklm_Disaster-Risk%20Reduction-Thailand's-Department-of-Disaster%20Prevention-and-Mitigation.md:16).

This is an important design warning. The current evidence suggests that later-phase sector tables may not yet share a clean universal relational event identifier. A CRDB redesign should therefore enforce an explicit foreign-key strategy linking all later assessments back to a master disaster record.

## 4. Validation logic

The validation evidence is strong enough to support a concrete design interpretation.

- The NotebookLM run states that PDNA requires checking and validating sectoral damage and loss information; see [`notebooklm_runs/2026-06-26_0903_raw_ddpm.txt`](../../../../../../notebooklm_runs/2026-06-26_0903_raw_ddpm.txt:1).
- The structured PDNA evidence extract describes meetings with sectoral teams, discussion of results, identification of data problems, and proposed fixes as part of a verification block; see [`2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md`](archive/extracts/2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md:183).

This means validation is not an optional editorial step. It is part of the method itself. For CRDB, PDNA-compatible records therefore need:

- assessor identity or source provenance
- review status
- validation meeting or review event metadata
- revision or correction trace
- date/time markers for when estimates were confirmed

Without those fields, the database could store values but would not preserve the assessment logic by which those values become credible.

## 5. Conceptual treatment of damage and loss in the DDPM PDNA evidence

The raw extraction provides a clear methodological distinction:

- **Damage** is direct physical destruction of assets and is monetized by repair or replacement cost.
- **Loss** is the change in economic flows relative to a pre-disaster baseline and may include income shortfalls, reduced output, disrupted services, and increased operating costs.

See [`raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation.md`](../../../inbox_source/raw-extraction-from-notebooklm_Disaster-Risk%20Reduction-Thailand's-Department-of-Disaster%20Prevention-and-Mitigation.md:33).

This aligns closely with the DaLA distinction, but the DDPM evidence demonstrates it most concretely through agricultural tables, especially pre/post production quantities, prices, and production value loss; see [`2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md`](archive/extracts/2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md:165).

## 6. Current practice limitations evidenced in the DDPM material

The current evidence supports several limitations that should be preserved honestly.

### 6.1 Phase coverage is incomplete in DDPM’s own produced forms

The DDPM sufficiency query explicitly states that the significant output produced was only assessment forms for Phase 0 to Phase 2 and that these still did not cover the fuller UNOCHA-style five-stage humanitarian assessment framework; see [`notebooklm_runs/2026-06-26_0903_raw_ddpm.txt`](../../../../../../notebooklm_runs/2026-06-26_0903_raw_ddpm.txt:1).

Interpretation: current DDPM practice appears stronger in early-stage assessment and weaker in fully institutionalized later-stage PDNA coverage.

### 6.2 The best-evidenced later-stage form is agriculture-weighted

The deepest field-level evidence for Phase 3–4 comes from the agriculture case. That makes the current analytical foundation sufficient for design seeding, but not sufficient to claim that all sectors are equally specified in the same way.

### 6.3 Current linking logic appears inconsistent across phases

Phase 1 and Phase 2 use a recognizable assessment reference field, but the agricultural Phase 3–4 evidence does not yet show a single normalized event key. This gap matters directly for relational integrity.

### 6.4 PDNA exceeds response-phase collection capacity

The evidence repeatedly implies that PDNA requires baseline assembly, sector expertise, validation meetings, and recovery-strategy work after the emergency phase. Therefore PDNA should not be mistaken for a form that local response actors can fully complete during the first notification window.

## 7. Implications for CRDB layered MVD design

The strongest design implications from the present evidence are these.

### 7.1 Preserve phase separation

Phase 1–2 event and rapid-assessment forms should feed the emergency event anchor. Phase 3–4 PDNA structures should be modeled as linked downstream assessment modules.

### 7.2 Enforce a universal disaster/event key across all phases

Because later-phase agricultural evidence appears to rely on contextual headers rather than a strong universal identifier, CRDB should impose a standard foreign-key strategy even if source forms currently do not.

### 7.3 Support baseline tables, not just impact tables

The agricultural evidence shows that baseline household, production, input, and water-source data are integral to later damage/loss analysis. A future-ready MVD must therefore either store or reference baseline entities.

### 7.4 Separate damage, loss, validation, and recovery-planning blocks

These are distinct methodological stages with different logic and should not be flattened into one undifferentiated “impact” record.

### 7.5 Use bounded cross-sector claims

Because the current evidence is agriculture-weighted, the design should extract general principles from the workflow while avoiding overclaiming that every sector already has the same field maturity.

## 8. Bounded conclusion for the next redesign step

The available evidence is sufficient to conclude that DDPM-linked PDNA practice should be treated as a later-stage, cross-agency, validation-heavy recovery assessment layer rather than a simple emergency reporting form. The evidence also supports a concrete modeling rule: the CRDB architecture should separate early event capture from later baseline-driven sector assessments and should require explicit relational keys, validation metadata, and recovery-planning outputs.

The most important caveat preserved in this write-up is that the detailed field evidence is strongest for agriculture. That does not weaken the design lesson; it only bounds how broadly the current evidence can be generalized across all sectors.
