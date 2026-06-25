# Standards-review extraction for CRDB loss-and-damage rewrite

**Source scope:** Extracted only from [`Disaster_Loss_Standards_Analysis.md`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) for the standards-review block requested for the CRDB loss-and-damage rewrite. No other source was analyzed for this note.

## 1. [`DesInventar`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) / DELTA

### Purpose and analytical unit
- The source frames classic [`DesInventar`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) as a system for **highly localized disaster event capture** using a [`DataCard`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:18) relational structure, with DELTA as the modern API-ready successor aligned to global disaster statistics frameworks.
- Its primary relational focus is the **disaster event spatial-temporal record** rather than sector models or macroeconomic accounts, and its storage unit of analysis is the **event card itself** rather than a household, asset portfolio, or national balance sheet.
- The methodological orientation is **historical risk profiling and trend analysis**, with a retrospective horizon over long time periods rather than forward recovery modeling.

### Core data structure or field logic
- The schema is event-card based, with each record anchored by a unique [`id`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:22) and status-controlled through [`record_status`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:26).
- The core logic is strongly structured around:
  - nested administrative geography: [`geography_level_0`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:27), [`geography_level_1`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:28), [`geography_level_2`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:29), plus optional [`site_specific`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:30)
  - explicit event timing: [`disaster_year`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:31), [`disaster_month`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:32), [`disaster_day`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:33), [`duration_days`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:34)
  - standardized hazard coding: [`event_type`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:35), [`cause_type`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:36), [`magnitude_value`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:37), [`magnitude_scale`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:38)
  - human impacts as counts: [`num_dead`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:39), [`num_missing`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:40), [`num_injured_sick`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:41), [`num_homeless`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:42), [`num_evacuated`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:43), [`num_relocated`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:44), [`num_affected`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:45)
  - coarse asset effects: [`dwellings_destroyed`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:46), [`dwellings_damaged`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:47), [`losses_local_currency`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:48), [`losses_usd`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:49)
  - infrastructure presence flags: [`infra_transport`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:50) through [`infra_water_sewer`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:56)
- DELTA adds machine-readable mappings such as [`target_indicator`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:57) and optional disaggregation extensions like [`demographic_sex`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:58), [`demographic_age`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:59), and [`demographic_disability`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:60).

### Damage/loss treatment
- The source characterizes [`DesInventar`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) as using **flat direct valuation** and reported losses rather than an explicit asset-flow economic model.
- Damage and loss are stored as **event-level reported counts and total valuations**, not decomposed into sector baselines, counterfactual trajectories, or multi-year recovery losses.
- In practice the system records that impacts occurred and can include a monetary total, but it does not itself encode the deeper valuation logic required for reconstruction economics.

### Workflow expectations
- The system is built for **data entry, quality control, and export**, with controlled menus, validation constraints, and workflow statuses.
- Governance is described as **national focal points with sovereign metadata systems**, and DELTA/DesInventar is positioned as a low-threshold national registry.
- The source explicitly connects it to standardized exports, API-ready architecture, and Sendai target mapping, which implies routine ingestion rather than rare, expert-only assessment missions.

### What it contributes to the MVD design
- It contributes the clearest template for a **minimum viable intake registry**:
  - unique event record
  - nested geography
  - explicit start-date logic
  - standardized hazard taxonomy
  - direct human impact fields
  - simple damaged/destroyed housing counts
  - optional total monetary estimate
  - validation and approval workflow
- It also contributes the principle that the MVD should separate **entry-layer structure** from **analytical-layer methods**, because [`DesInventar`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) is strong on standardized event ingestion but intentionally lighter on economic modeling.
- DELTA’s mapping fields and disaggregation extensions suggest that an MVD can stay minimal while remaining extensible for policy reporting.

### What is unsuitable for rapid DDPM intake
- The source itself identifies a structural limitation: classic event-card models were designed mainly for **sudden-onset disasters** with a distinct start, end, and impact area.
- This makes them less suitable as-is for **slow-onset loss-and-damage processes** that unfold continuously and do not fit a single event boundary.
- The infrastructure fields are also **binary presence markers**, which are useful for screening but too shallow for sectoral loss estimation.
- Reported flat-loss totals are insufficient where DDPM intake would later need causal decomposition, sector reconstruction costing, or flow-loss modeling.

## 2. [`DaLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) / PDNA

### Purpose and analytical unit
- The source presents [`DaLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) as a **post-disaster economic assessment methodology** for estimating damage, losses, and recovery implications.
- Its unit of analysis is the **physical asset structure by sector**, not the event card. Each record is anchored to an [`asset_id`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:70) within sector and subsector templates.
- Methodologically it is forward-looking and geared toward **recovery and reconstruction financing**, typically over a two- to three-year horizon.

### Core data structure or field logic
- The schema is organized around sector templates comparing pre-disaster baselines to post-disaster effects.
- Core field logic includes:
  - asset identity and ownership: [`asset_id`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:70), [`sector_type`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:71), [`subsector_type`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:72), [`owner_type`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:73)
  - baseline quantities and costing assumptions: [`qty_baseline_units`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:74), [`unit_measure`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:75), [`unit_replacement_cost`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:76), [`unit_repair_cost`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:77)
  - physical damage counts: [`qty_destroyed_units`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:78), [`qty_damaged_units`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:79)
  - calculated capital damage: [`monetary_damage`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:80)
  - projected and actual economic flows: [`revenue_projected`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:81), [`revenue_actual`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:82), [`increased_op_costs`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:83), [`unexpected_expenses`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:84), [`monetary_losses`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:85)
  - PDHA links for vulnerable households and service access: [`pdha_vulnerable_groups`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:86), [`pdha_demographics`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:87), [`pdha_services_loss`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:88)

### Damage/loss treatment
- [`DaLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) uses a strict **asset-flow model**:
  - **Damage** is the direct physical destruction of assets, valued at replacement or repair cost at the time of disaster.
  - **Losses** are subsequent changes in economic flows over the recovery period, including foregone revenues, increased operating costs, and emergency expenditures.
- The source is explicit that [`monetary_damage`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:80) is formula-derived from destroyed and damaged unit counts times replacement/repair costs.
- It is equally explicit that [`monetary_losses`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:85) is not just observed shortfall but a computed gap between expected and actual flows plus increased operating costs.
- The methodology further expects counterfactual baseline modeling and, for historical comparison, normalization techniques such as the Pielke-style adjustments described in the source.

### Workflow expectations
- The source portrays [`DaLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) as **expert-led, sector-template based, and validation-heavy**.
- Validation is not embedded mainly in a native transactional system; the comparison table instead characterizes it as relying on **manual spreadsheets and validator review**.
- Governance is joint and mission-oriented: **UN, EC, and World Bank validation teams**.
- The workflow assumes post-disaster deployment of specialists able to build baselines, avoid double counting, and assess intersectoral dependencies.

### What it contributes to the MVD design
- It contributes the crucial conceptual split the MVD will need later: **direct asset damage vs. downstream economic loss**.
- It also contributes field design ideas for any later-stage extension table:
  - baseline quantity
  - damaged/destroyed quantity
  - replacement/repair unit costs
  - expected vs. actual flows
  - increased operating costs
- Most importantly, it demonstrates that if the CRDB MVD stores only one monetary number, it must not pretend that a single figure is analytically equivalent to full [`DaLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md)-style loss estimation.

### What is unsuitable for rapid DDPM intake
- The source repeatedly stresses that frameworks like [`DaLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) require **economists, scientists, counterfactual baselines, intersectoral analysis, and detailed sector templates**.
- That makes it unsuitable as the front-end logic for rapid DDPM intake, because local officials usually cannot compute expected-vs-actual flow models during immediate reporting.
- Its spreadsheet-heavy, expert-validation workflow is also too slow and cognitively heavy for first-notification municipal capture.
- In short: it is fit for **secondary analysis and financing cases**, not for the first-pass intake form.

## 3. [`ADLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) / eDLA

### Purpose and analytical unit
- The source defines [`ADLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) as a **specialized agricultural damage and loss methodology**, digitized through the web-based [`eDLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:94) platform.
- Its analytical unit is not a generic disaster event or macroeconomic zone, but the **subsector production volume and asset damage** of agriculture.
- The scope is explicitly micro-structured across five subsectors: crops, livestock, forestry, aquaculture, and fisheries.

### Core data structure or field logic
- The schema is highly subsector-specific.
- For annual crops it tracks fields such as [`crop_type_code`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:98), [`area_planted_ha`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:99), [`area_destroyed_ha`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:100), [`area_damaged_ha`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:101), [`yield_baseline_mt_ha`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:102), [`yield_actual_mt_ha`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:103), [`stored_output_lost_mt`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:104), and [`stored_input_lost`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:105).
- For perennial crops it adds recovery-sensitive fields such as [`trees_fully_destroyed`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:107) and [`recovery_years`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:108).
- For livestock it uses fields like [`animal_breed_type`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:109), [`animals_dead_count`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:110), [`salvage_revenue_usd`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:111), and [`feed_destroyed_mt`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:112).
- Forestry, aquaculture, and fisheries each introduce their own production-unit and asset fields such as [`burned_surface_ha`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:114), [`seedlings_lost_count`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:115), [`pond_surface_ha`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:116), [`broodstock_lost_count`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:117), [`vessel_status`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:119), and [`gear_destroyed_count`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:120).
- The field logic is therefore **biophysical and commodity-specific**, not generic.

### Damage/loss treatment
- [`ADLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) is the most explicit source on mathematical decomposition inside a sector.
- It distinguishes:
  - destruction of stored outputs and inputs
  - destruction or damage of standing production area
  - short-run yield reduction on surviving area
  - extra expenditure needed to keep surviving production viable
  - future recovery lag for perennial systems and herd rebuilding
  - salvage value offsets for dead livestock
- For annual crops, production loss depends on damaged area, destroyed area, expected yield, actual yield effect, and extra short-run expenditure.
- For livestock, production damage subtracts salvage revenue from the value of dead animals, while production loss also includes discounted future production foregone from dead animals and stressed survivors.
- For forestry, the methodology distinguishes stored timber/standing tree damage from discounted future harvest loss.
- The source therefore treats “damage” and “loss” as **subsector-specific production economics**, not as one universal formula.

### Workflow expectations
- The workflow is digital and specialized: the source describes [`eDLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:122) as a customizable web solution that integrates farm-gate data with remote sensing and GIS overlays.
- Validation is partly software- and geography-assisted through spatial checks and satellite-derived overlays.
- Governance is tied to agricultural administration, specifically ministries of agriculture and related institutional machinery.
- The operational model expects specialized subsector enumerators or authorities, not generic all-hazard intake staff.

### What it contributes to the MVD design
- It contributes the strongest evidence that **agriculture cannot be collapsed into a single undifferentiated “damage/loss” field** if the system later needs analytical credibility.
- For the MVD, the implication is not to import the whole [`ADLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) structure, but to preserve enough intake hooks so agriculture can later expand into:
  - crop area affected
  - crop area destroyed vs. damaged
  - livestock deaths
  - destroyed stored inputs/outputs
  - subsector tag
- It also contributes a model for handling **slow-onset and seasonal stress** better than event-card systems, because the source explicitly says [`ADLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) shifts the baseline from a fixed event point to a dynamic agronomic calendar.

### What is unsuitable for rapid DDPM intake
- The schema is too **subsector-dense and formula-dependent** for a general rapid municipal intake form.
- Many fields depend on technical baselines, farm-gate prices, discounting, recovery periods, salvage assumptions, or seasonal calendars that are not available at first report.
- The GIS and remote-sensing integration is analytically powerful but operationally beyond the threshold of ordinary DDPM first-entry workflows.
- Therefore [`ADLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) should inform downstream agricultural modules, not define the universal intake payload.

## 4. [`ECLAC`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md)

### Purpose and analytical unit
- The source describes [`ECLAC`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) as an integrated **social-environmental macroeconomic assessment framework**.
- Its relational focus is **macro-socio-economic structural aggregates**, and its storage unit is the **geographic and socio-demographic administrative zone** rather than the individual event-card or asset record.
- It is designed to support balanced national recovery and reconstruction planning.

### Core data structure or field logic
- The schema centers on administrative-zone aggregates and demographic vulnerability:
  - [`admin_boundary_code`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:130)
  - [`total_population`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:131)
  - [`primary_affected`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:132)
  - [`secondary_affected`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:133)
  - [`vulnerable_indigenous`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:134)
- It extends beyond physical/economic fields to psychosocial metrics such as [`dts_sample_size`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:135), [`dts_score_average`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:136), and [`dts_above_threshold`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:137).
- It also encodes ownership breakdown and environmental asset treatment through [`public_asset_damage`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:138), [`private_asset_damage`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:139), [`environmental_asset`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:140), [`lost_surface_ha`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:141), and [`debris_volume_m3`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:142).

### Damage/loss treatment
- The source places [`ECLAC`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) in the same conceptual family as [`DaLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md): an **asset-flow model** with direct damage and subsequent losses.
- But it broadens the frame beyond sector capital and output to include:
  - public/private ownership breakdown
  - demographic vulnerability
  - psychosocial effects
  - environmental assets and debris
  - non-market environmental valuation challenges
- The source specifically notes that traditional [`ECLAC`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) and [`DaLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) practice tends to value environmental impacts mainly through **restoration costs**, which misses lost ecosystem services during recovery.

### Workflow expectations
- Validation is consensus-based and institutionally heavy: national statistical registries, statistical software/database systems, and ECLAC specialist involvement.
- Governance is led by **national statistical offices and ECLAC specialists**.
- The workflow therefore presumes access to national datasets, specialist synthesis, and cross-sector consolidation rather than local rapid intake.

### What it contributes to the MVD design
- It contributes the strongest justification for ensuring the MVD can distinguish:
  - primary vs. secondary affected populations
  - public vs. private asset implications
  - environmental asset categories
  - non-economic or hard-to-monetize impacts as explicit placeholders
- It also pushes the MVD to avoid a purely engineering view of damage by keeping room for **social vulnerability and environmental dimensions**, even if those are initially lightweight.
- In particular, the distinction between [`primary_affected`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:132) and [`secondary_affected`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md:133) is directly useful for a minimum intake logic.

### What is unsuitable for rapid DDPM intake
- The macro-socio-economic, psychosocial, and environmental valuation layers are too complex for first-pass reporting.
- Measures like trauma scale averages, consensus public/private valuation, and environmental restoration economics require specialized surveys and institutional compilation.
- Like [`DaLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md), the framework is suitable for structured national assessment, not frontline municipal event notification.

## Comparative synthesis for sharpening [`5.3.6`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:190)

### Core comparative conclusion
- The source supports a hard distinction between **minimum viable intake design** and **full analytical methodologies**.
- Among the four standards, only [`DesInventar`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) is structurally close to a practical rapid-intake model, because it is event-based, geographically nested, validation-oriented, and count-driven.
- [`DaLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md), [`ADLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md), and [`ECLAC`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md) should not be treated as intake templates; they are **secondary analytical frameworks** layered on top of validated base records.

### Strongest standard-specific claims extractable from the source
- [`DesInventar`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md): best model for the MVD’s core event record, but weak for slow-onset processes and deep economic valuation.
- [`DaLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md): establishes the decisive distinction between **asset damage** and **flow losses**, but is too expert-heavy and counterfactual-dependent for rapid intake.
- [`ADLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md): shows that agriculture requires subsector-specific logic and dynamic seasonal baselines, but its formulas and domain detail are too complex for a universal intake form.
- [`ECLAC`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md): broadens the frame to primary/secondary affected populations, psychosocial effects, ownership splits, and environmental assets, but belongs to national synthesis rather than first-notification capture.

### Direct implication for how [`5.3.6`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:190) should be sharpened
- [`5.3.6`](ψ/incubate/DCCE/CRDB/inbox_source/CRDB%20-%20TOR.md:190) should describe the CRDB loss-and-damage MVD as a **DesInventar-like intake layer with selective downstream compatibility hooks**, not as a compressed clone of [`DaLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md), [`ADLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md), or [`ECLAC`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md).
- The MVD should capture only the fields that can be reported quickly and consistently: event identity, geography, hazard, date, affected people, basic damaged/destroyed counts, broad sector tagging, and optional rough monetary estimate.
- It should then preserve extensibility for later analytical modules:
  - [`DaLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md)-style baseline and flow-loss tables
  - [`ADLA`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md)-style agricultural subsector tables
  - [`ECLAC`](ψ/incubate/DCCE/CRDB/inbox_source/Disaster_Loss_Standards_Analysis.md)-style social/environmental aggregate tables
- The design danger to avoid is category collapse: a single “loss and damage” field cannot faithfully represent all four standards because they operate on **different analytical units, valuation logics, and workflows**.
