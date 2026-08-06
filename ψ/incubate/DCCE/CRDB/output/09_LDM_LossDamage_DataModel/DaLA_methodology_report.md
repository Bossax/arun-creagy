# DaLA Methodology Report

## Purpose of this artifact

This report distills the evidence currently available on the Damage, Loss and Needs Assessment (DaLA) methodology so it can directly support later redesign of the CRDB loss-and-damage Minimum Viable Dataset (MVD) and later narrative synthesis for Topic 2 to Topic 6 of Section [`5.3.6`](../../../inbox_source/CRDB%20-%20TOR.md:190). It is not a full literature review. It is a bounded analytical note based on the current extracted evidence set, especially [`notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json`](../../../../../../notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json), [`notebooklm_runs/2026-06-26_0901_raw_dala.json`](../../../../../../notebooklm_runs/2026-06-26_0901_raw_dala.json), and the standards interpretation already captured in [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:52).

## 1. What DaLA is for

The current evidence consistently frames DaLA as a post-disaster economic assessment methodology used to estimate:

- direct destruction of assets as **damage**
- changes in economic flows as **losses**
- short-, medium-, and longer-term **recovery and reconstruction needs**

The NotebookLM extraction states that the methodology estimates “the value of the destruction of assets (damages) and of the changes (or losses) in the flows of the economy as a result of the disaster” and uses those estimates to define post-disaster recovery and reconstruction requirements in a structured way; see [`notebooklm_runs/2026-06-26_0901_raw_dala.json`](../../../../../../notebooklm_runs/2026-06-26_0901_raw_dala.json). The earlier extracted standards review likewise characterizes DaLA as a post-disaster economic assessment framework oriented to recovery and reconstruction financing rather than rapid intake; see [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:54).

For CRDB design, this means DaLA should not be treated as the front-end event capture template. It is better understood as the analytical layer that sits downstream from validated event records.

## 2. Methodological sequence

The available evidence supports the following methodological sequence.

### 2.1 Trigger and mobilization

The assessment is triggered by a formal request from the affected government authority to the relevant World Bank country leadership; see [`notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json`](../../../../../../notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json). This already signals that DaLA is not designed as a routine always-on registry. It is a mission-style assessment mobilized after a serious event.

### 2.2 Team formation and preparation

The extraction notes that DaLA teams require multidisciplinary expertise including architects, engineers, sociologists, and economists; see [`notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json`](../../../../../../notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json). The same source indicates that execution includes training on the methodology, baseline data collection, field visits, surveys, and sector-based estimation work.

Implication: DaLA depends on specialist judgment and coordinated sector work, not simple one-form reporting.

### 2.3 Define the pre-disaster baseline

The current evidence is explicit that baseline information is required and that a typical assessment begins by defining the pre-disaster baseline; see [`notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json`](../../../../../../notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json) and [`notebooklm_runs/2026-06-26_0901_raw_dala.json`](../../../../../../notebooklm_runs/2026-06-26_0901_raw_dala.json). This baseline includes demographic, social, and economic characteristics plus sector-specific operating conditions.

This is one of the most important design signals for CRDB. A database that wants later DaLA compatibility cannot only store what was visibly damaged. It must also preserve or link to baseline denominators, prices, quantities, capacities, service levels, and sector-specific normal operating conditions.

### 2.4 Develop the post-disaster situation

The next step is to establish the post-disaster condition against which the baseline will be compared; see [`notebooklm_runs/2026-06-26_0901_raw_dala.json`](../../../../../../notebooklm_runs/2026-06-26_0901_raw_dala.json). This is where field observation, sector investigation, and validation-heavy compilation become necessary.

### 2.5 Estimate damage and loss sector by sector

The evidence states that damage and losses are estimated on a sector-by-sector basis; see [`notebooklm_runs/2026-06-26_0901_raw_dala.json`](../../../../../../notebooklm_runs/2026-06-26_0901_raw_dala.json). The standards extraction makes the same point in data-model terms by describing sector templates keyed by asset identity, subsector, ownership, baseline quantities, unit costs, and projected versus actual flows; see [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:59).

### 2.6 Estimate recovery and reconstruction needs

The methodology then uses the damage and loss calculations to estimate recovery needs and reconstruction needs. The World Bank extraction states that recovery needs include short-term interventions to restart economic functions and medium- to long-term requirements to restore performance to pre-disaster levels, while reconstruction needs are derived from damage values plus improvements, mitigation measures, and inflation considerations; see [`notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json`](../../../../../../notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json).

## 3. Baseline logic and counterfactual reasoning

DaLA is not just a damage tally. Its logic depends on comparison between:

- a defined pre-disaster baseline
- an observed or estimated post-disaster condition
- a counterfactual expectation of what would have happened without the disaster

The standards review states this explicitly by describing projected versus actual economic flows and by noting that losses are computed from expected-versus-actual gaps plus increased operating costs; see [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:66). This is the core reason DaLA cannot be collapsed into a single “loss and damage amount” field.

For relational data modeling, baseline logic implies at least four distinct data classes:

1. event anchor and hazard timing
2. baseline stock or service state
3. observed damage state
4. projected and actual post-disaster flow values

Without this separation, later loss calculations become untraceable or analytically misleading.

## 4. Damage versus loss

The evidence is unusually clear on the conceptual distinction.

### 4.1 Damage

The extraction defines damage as total or partial destruction of physical assets in the affected area; see [`notebooklm_runs/2026-06-26_0901_raw_dala.json`](../../../../../../notebooklm_runs/2026-06-26_0901_raw_dala.json). The standards review translates that into field logic: destroyed and damaged unit counts multiplied by replacement or repair costs; see [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:69).

In database terms, damage requires:

- asset or asset-class identifier
- sector and subsector
- ownership or responsible entity where relevant
- severity state such as destroyed versus damaged
- physical quantity and unit of measure
- replacement cost and repair cost assumptions

### 4.2 Loss

The extraction defines losses as changes in economic flows arising from the disaster and notes that they continue until full recovery and reconstruction are achieved; see [`notebooklm_runs/2026-06-26_0901_raw_dala.json`](../../../../../../notebooklm_runs/2026-06-26_0901_raw_dala.json). The standards review explains that these are calculated from expected and actual revenues or production plus increased operational costs and unexpected expenses; see [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:69).

In database terms, loss requires:

- analysis horizon or recovery period
- baseline projected flow
- actual post-disaster flow
- price or valuation basis
- increased operating costs and unexpected expenditures
- explicit linkage to the related event, sector, and possibly damaged asset set

### 4.3 Why the distinction matters for CRDB

The current technical specification already separates [`DISASTER_RECORD`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:25), [`LD_ASSET_DAMAGE`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:39), and [`LD_ECONOMIC_LOSS`](Pillar_06_LDM_LossDamage_DataModel_Technical_Specification.md:55). The DaLA evidence supports this direction, but it also shows that the present schema remains incomplete if it does not explicitly preserve baseline provenance, valuation assumptions, time horizon, and validation status.

## 5. Recovery needs and reconstruction needs logic

The World Bank evidence separates needs estimation from damage/loss measurement.

- **Recovery needs** are linked more closely to restoring functioning and socio-economic performance.
- **Reconstruction needs** are linked more closely to rebuilding damaged assets, but not at bare replacement value alone; they may include quality improvement, risk reduction, and inflation adjustments.

This matters because recovery needs and reconstruction needs are not simply raw observed facts from the emergency phase. They are derived analytical outputs produced after damage and loss estimation.

For CRDB design, this argues against storing recovery needs as if they were ordinary first-notification fields inside the same event-intake payload. A stronger design is to model recovery and reconstruction needs as downstream analytical tables or outputs linked to validated sector assessments.

## 6. Workflow and governance implications

The available evidence portrays DaLA as:

- expert-led
- sector-template based
- validation-heavy
- dependent on baseline and specialist costing assumptions
- oriented to medium-term planning rather than immediate incident notification

The standards review explicitly notes reliance on manual spreadsheets and validator review in practice; see [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:77). This is a useful caution. If CRDB later wants DaLA-compatible outputs, it should not pretend that municipal or response-phase actors can fully populate DaLA fields in real time.

## 7. Implications for relational data modeling

The strongest MVD implications supported by the current evidence are as follows.

### 7.1 Keep the event anchor separate from post-disaster analytical tables

DaLA needs a validated event reference, but it is not itself an event-card methodology. The emergency event anchor should therefore remain logically distinct from asset damage, economic loss, and recovery-needs structures.

### 7.2 Model damage and loss as separate but linked entities

The distinction is not cosmetic. Damage and loss rely on different units, formulas, timelines, and validation routines. Separate tables are therefore methodologically justified.

### 7.3 Preserve baseline entities or baseline reference fields

If the database has no place for baseline production, asset stock, service capacity, price assumptions, or normal operating levels, it cannot credibly support DaLA-style loss estimation.

### 7.4 Add valuation metadata and provenance

DaLA-compatible records need fields for valuation basis, unit-cost source, estimation date, assessor, and validation status. Without such metadata, later synthesis will not be auditable.

### 7.5 Treat recovery and reconstruction as derived layers

Needs should sit downstream from validated damage and loss estimation, not inside the minimal intake layer.

### 7.6 Expect sector extensibility rather than one universal schema depth

DaLA works through sector templates. The CRDB core model should therefore remain layered: a stable common core plus sector-specific extensions.

## 8. Bounded conclusion for the next redesign step

The current evidence is sufficient to support a design judgment: DaLA provides the strongest conceptual justification for separating event capture, physical damage, economic loss, and derived recovery/reconstruction needs in the CRDB architecture. It does **not** support turning the emergency intake record into a full DaLA form.

The practical redesign consequence is that the later MVD should be framed as a layered architecture:

- a minimal validated event anchor for response-phase capture
- one or more post-disaster sectoral damage tables
- one or more post-disaster loss tables grounded in baseline-versus-actual comparison
- derived recovery and reconstruction layers created only after validation

That interpretation is consistent with both the World Bank NotebookLM outputs in [`notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json`](../../../../../../notebooklm_runs/2026-06-26_0721_raw_world-bank-dala.json) and [`notebooklm_runs/2026-06-26_0901_raw_dala.json`](../../../../../../notebooklm_runs/2026-06-26_0901_raw_dala.json), and the previously structured standards reading in [`2026-06-25_standards-review_extraction_for_TOR_5.3.6.md`](archive/extracts/2026-06-25_standards-review_extraction_for_TOR_5.3.6.md:52).
