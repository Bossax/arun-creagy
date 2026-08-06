# Comparative Analysis: DaLA, DesInventar, and PDNA

## Purpose of this artifact

This comparative note translates the current evidence base into design judgments for the CRDB layered Minimum Viable Dataset (MVD). It compares DaLA, DesInventar, and PDNA across purpose, timing, unit of analysis, data structure, strengths, limitations, and design implications. The comparison is evidence-led but intentionally bounded: the DaLA and DesInventar logic are comparatively well supported by the present extracted material, while the PDNA side is strong enough to draft but is still agriculture-weighted in its detailed field evidence.

Primary supporting sources for this comparison are [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:5), [`2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md`](archive/extracts/2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md:13), [`notebooklm_runs/2026-06-26_0901_raw_dala.json`](../../../../../../notebooklm_runs/2026-06-26_0901_raw_dala.json), and [`notebooklm_runs/2026-06-26_0903_raw_ddpm.txt`](../../../../../../notebooklm_runs/2026-06-26_0903_raw_ddpm.txt:1).

## 1. Comparative table

| Dimension               | DaLA                                                                                                                                                                                                                                                                                                              | DesInventar                                                                                                                                                                                                                     | PDNA                                                                                                                                                                                                                                                                                                                                  |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Primary purpose**     | Post-disaster economic assessment for estimating damage, losses, and recovery/reconstruction needs; see [`DaLA_methodology_report.md`](DaLA_methodology_report.md:1) and [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:54) | Localized disaster event capture and historical risk profiling through event cards; see [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:7) | Post-emergency needs assessment and recovery strategy formulation within a staged DDPM/sector workflow; see [`DDPM_PDNA_methodology_report.md`](DDPM_PDNA_methodology_report.md:1) and [`2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md`](archive/extracts/2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md:41) |
| **Typical timing**      | After the disaster once a formal assessment is triggered and specialists are mobilized                                                                                                                                                                                                                            | Ongoing registry-style event recording, suitable for routine intake and historical compilation                                                                                                                                  | After early emergency phases, especially Phase 3–4 in the DDPM framing                                                                                                                                                                                                                                                                |
| **Unit of analysis**    | Sectoral assets and economic flows                                                                                                                                                                                                                                                                                | Event card / disaster record in a defined place and time                                                                                                                                                                        | Staged assessment linked to a disaster event, with detailed field evidence strongest in agricultural sector tables                                                                                                                                                                                                                    |
| **Core data structure** | Baseline-versus-post-disaster sector templates, separate damage and loss logic, valuation assumptions, and downstream needs estimation                                                                                                                                                                            | Event-card structure with hazard, date, geography, human impacts, basic asset counts, and optional total monetary values                                                                                                        | Multi-phase form architecture: early event and rapid assessment forms plus later baseline, damage, loss, validation, and recovery blocks                                                                                                                                                                                              |
| **Analytical strength** | Strongest for distinguishing physical asset damage from economic flow loss and linking these to recovery/reconstruction planning                                                                                                                                                                                  | Strongest for standardized minimum viable disaster event intake and long-run event cataloguing                                                                                                                                  | Strongest for bridging emergency assessment to recovery planning in an operational government workflow                                                                                                                                                                                                                                |
| **Main limitation**     | Too expert-heavy and baseline-dependent for rapid frontline intake                                                                                                                                                                                                                                                | Too shallow for full sectoral economic valuation and recovery economics                                                                                                                                                         | Current evidence is not equally broad across all sectors; detailed field evidence is agriculture-weighted                                                                                                                                                                                                                             |

## 2. Purpose and problem each methodology solves

### 2.1 DesInventar solves the event-registry problem

The standards review frames DesInventar as a system for highly localized event capture using a datacard structure; see [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:7). Its purpose is to create standardized, historically analyzable disaster records with clear hazard, timing, geography, and effect fields.

For CRDB, this is the closest analogue to the minimal intake layer.

### 2.2 DaLA solves the economic assessment problem

DaLA addresses a different problem: how to value direct asset destruction, estimate indirect or downstream economic losses, and derive recovery and reconstruction needs. Its logic is not primarily about event registration but about economic interpretation after the event; see [`DaLA_methodology_report.md`](DaLA_methodology_report.md:7).

For CRDB, this is the clearest justification for downstream analytical modules.

### 2.3 PDNA solves the recovery-planning workflow problem

The DDPM evidence places PDNA in a staged institutional process that connects preparedness, rapid assessment, validation, and later recovery strategy; see [`DDPM_PDNA_methodology_report.md`](DDPM_PDNA_methodology_report.md:7). In practical terms, PDNA is where the system moves from “what happened” toward “what is needed next.”

For CRDB, this means the architecture must support workflow progression, not only data storage.

## 3. Timing and operational rhythm

### 3.1 DesInventar is closest to routine intake

Because it is structured around event cards, validation constraints, and controlled data entry, DesInventar fits regular registry operations better than mission-style specialist deployments; see [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:28).

### 3.2 DaLA is episodic and specialist-led

DaLA is triggered, staffed, and executed as a post-disaster analytical exercise requiring sector experts and baseline work; see [`notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json`](../../../../../../notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json).

### 3.3 PDNA sits between emergency reporting and full recovery programming

The DDPM evidence shows PDNA as a later-phase process that begins after the immediate emergency window and moves through data collection, validation, and strategy formulation; see [`DDPM_PDNA_methodology_report.md`](DDPM_PDNA_methodology_report.md:16).

This temporal comparison matters because it argues strongly for a layered MVD rather than one overloaded all-at-once form.

## 4. Unit of analysis and relational consequences

### 4.1 DesInventar: one event card per localized event/geographic unit

The data card logic emphasizes event identity, geography, date, hazard, and a limited set of effect fields; see [`raw-extraction-from-notebooklm_Disaster-Risk Reduction-Thailand's-Department-of-Disaster Prevention-and-Mitigation.md`](../../../inbox_source/raw-extraction-from-notebooklm_Disaster-Risk%20Reduction-Thailand's-Department-of-Disaster%20Prevention-and-Mitigation.md:95). This favors a strong primary disaster record.

### 4.2 DaLA: sector asset and flow records

DaLA’s analytical unit is not the event card itself but sectoral assets and economic flows relative to a baseline; see [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:54).

### 4.3 PDNA: staged forms linked back to the disaster event

The DDPM evidence shows Phase 1 and 2 forms with an assessment reference number, but later agriculture forms appear to rely more on contextual linking than on a universal key; see [`DDPM_PDNA_methodology_report.md`](DDPM_PDNA_methodology_report.md:24).

Relational implication: CRDB must enforce cleaner key architecture than the source materials necessarily demonstrate.

## 5. Data structure comparison

### 5.1 DesInventar structure

DesInventar is strong on:

- hazard taxonomy
- nested geography
- event date and duration
- human impact counts
- basic damage/dwelling counts
- optional top-line monetary loss
- validation status

See [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:12).

### 5.2 DaLA structure

DaLA is strong on:

- baseline quantities
- destroyed/damaged quantities
- replacement and repair costs
- projected versus actual flows
- increased costs and unexpected expenses
- derived damage and loss calculations
- recovery/reconstruction needs

See [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:59).

### 5.3 PDNA structure

PDNA, as evidenced here, is strong on staged block logic:

- baseline block
- event impact block
- damage block
- loss block
- validation block
- recovery strategy block

The most concrete field detail currently comes from agriculture; see [`2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md`](archive/extracts/2026-06-25_PDNA_evidence_extraction_for_TOR_5.3.6_5.3.7.md:88).

## 6. Strengths and limitations

### 6.1 DesInventar strengths and limitations

**Strengths**

- practical for minimum viable intake
- standardized event record structure
- useful for historical series and Sendai-style reporting

**Limitations**

- shallow for full economic valuation
- weak for sector baselines and flow-loss modeling
- less suitable as-is for slow-onset and prolonged loss processes

See [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:46).

### 6.2 DaLA strengths and limitations

**Strengths**

- rigorous damage/loss distinction
- explicit baseline and counterfactual logic
- direct relevance to recovery and reconstruction planning

**Limitations**

- expert-heavy
- time-consuming
- unsuitable as a frontline municipal intake form

See [`DaLA_methodology_report.md`](DaLA_methodology_report.md:81).

### 6.3 PDNA strengths and limitations

**Strengths**

- connects assessment to actual institutional workflow
- adds validation and recovery-strategy stages
- provides a bridge from early assessment to later sector planning

**Limitations**

- current evidence indicates incomplete practical coverage, especially beyond early DDPM-produced forms
- strongest detailed field evidence is agriculture-weighted
- later-stage form linkage to a universal event key appears weak in the present material

See [`DDPM_PDNA_methodology_report.md`](DDPM_PDNA_methodology_report.md:52).

## 7. Implications for the CRDB layered MVD design

The current evidence supports a three-layer design logic more strongly than a one-form logic.

### 7.1 Layer A: DesInventar-like event anchor

CRDB needs a minimum viable intake registry with:

- unique disaster/event ID
- hazard type
- geography hierarchy
- start/end timing
- direct human impacts
- basic damaged/destroyed counts
- workflow status and provenance

This layer is most closely justified by DesInventar and by DDPM Phase 1–2 forms.

### 7.2 Layer B: PDNA/DaLA-compatible post-disaster analytical modules

CRDB then needs linked downstream modules for:

- sector baseline data
- physical damage valuation
- economic loss estimation
- validation and revision workflow
- recovery and reconstruction needs

This layer is primarily justified by DaLA logic and by the later-stage PDNA agricultural evidence.

### 7.3 Layer C: synthesis and aggregation layer

The final layer should support:

- roll-up to sector summaries
- macro comparisons where needed
- policy-ready recovery planning outputs
- later narrative synthesis for Topic 2 to Topic 6

This layer should not be confused with first-entry reporting.

## 8. Most important design danger to avoid

The main analytical danger is category collapse: treating one field, one table, or one reporting moment as if it can represent all three methodologies at once. The evidence does not support that simplification.

- DesInventar is optimized for event registration.
- DaLA is optimized for economic assessment.
- PDNA is optimized for staged post-disaster needs and recovery planning.

These functions overlap, but they are not identical.

## 9. Bounded conclusion for the next redesign step

The current evidence supports a clear synthesis judgment for CRDB: the target architecture should be a **DesInventar-like intake layer with explicit compatibility hooks for PDNA and DaLA-style downstream analysis**, not a compressed clone of any one methodology.

The safest bounded statement on PDNA is that the workflow logic is sufficiently evidenced to shape database design, but the field-level detail remains strongest in agriculture and should not be overgeneralized beyond that without additional sector evidence. That caveat is preserved here so the next orchestration step can use this comparison confidently without overstating methodological coverage.
