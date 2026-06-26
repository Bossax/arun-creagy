# Draft Report Sections 5.3.6 and 5.3.7 — CRDB Loss and Damage Workflow

## 5.3.6 Draft Minimum Viable Dataset (MVD) and Loss and Damage Reporting Form

### 1. Review of Disaster Risk Management of Thailand
The disaster risk management (DRM) architecture in Thailand operates under a hierarchical, highly structured administrative framework established by the National Disaster Prevention and Mitigation Act. At its core, the national strategy prioritizes rapid emergency response, life-saving interventions, and the swift distribution of immediate relief to affected populations. The system is designed to trigger incident commands that scale sequentially depending on the severity of the hazard. A localized flood is managed by the Local Administrative Organization (LAO), whereas a severe regional inundation escalates to the provincial governor or ultimately to the national command center. 

Because the primary objective of this DRM framework is operational response rather than long-term economic accounting, the data generated during the immediate aftermath of a disaster is inherently skewed toward emergency management. Information must flow rapidly from the village headman to the district office, and up to the central authorities, focusing on immediate human needs: evacuations required, houses destroyed, and emergency rations needed. While this ensures a robust response capability, it creates a structural challenge when attempting to use this same rapid-response data for comprehensive macroeconomic loss and damage analysis.

### 2. DDPM Data Collection Practices and the PDNA Standard
Within this national structure, the Department of Disaster Prevention and Mitigation (DDPM) serves as the central coordinating node for disaster data collection. DDPM’s current reporting practice relies heavily on an urgent disaster reporting chain. When a hazard strikes, local officials submit initial situational reports that are subsequently routed through district channels, quality-checked at the provincial level, and consolidated into central disaster information systems. 

Crucially, this front-line workflow is fundamentally incentive-backed by Ministry of Finance regulations governing the disbursement of emergency relief funds. The data collected by local officials is primarily used to secure compensation for affected households, farmers, and local infrastructure repair. 

As the global community shifts toward more rigorous disaster accounting, the Post-Disaster Needs Assessment (PDNA) standard has been officially recognized in Thailand as the target framework for comprehensive loss and damage estimation. However, a deep understanding of DDPM's operational reality reveals that PDNA cannot serve as the baseline standard for front-line data collection. The PDNA methodology requires extensive multisectoral baseline data (knowing exactly what existed before the disaster), counterfactual economic modeling (estimating what a business would have earned had the disaster not occurred), and extended recovery-phase timelines. Such requirements vastly exceed the realistic capacities of local administrative officials who are mandated to provide rapid, compensation-driven reports within days of a hazard event.

### 3. Review of International Disaster Data Standards
Before proposing an adjusted national data model that reconciles rapid relief with rigorous accounting, it is necessary to thoroughly review the broader landscape of international standards that govern disaster loss reporting. These standards operate on fundamentally different technical logic and serve different policy objectives.

**DesInventar (and the DELTA framework):**
Originating in Latin America and subsequently adopted globally by UNDRR, DesInventar is a localized disaster event capture registry designed primarily for historical risk profiling and long-term trend analysis. It is utilized heavily by national focal points to track disaster frequencies, particularly recurrent, low-severity events. Technically, its foundational unit of analysis is the "event card." The system organizes data by nested geographical boundaries, hazard types, and simple physical counts (e.g., number of damaged houses, number of evacuated individuals). Because it relies on direct, observable counts rather than complex economic formulas, it serves as an excellent foundational template for rapid data intake and Sendai Framework reporting.

**DaLA (Damage and Loss Assessment) / PDNA:**
Developed initially by the UN Economic Commission for Latin America and later standardized globally by the World Bank and UN agencies, DaLA/PDNA is a post-disaster economic assessment methodology used primarily to mobilize and guide international reconstruction financing. Technically, it relies on an intricate "asset-flow model." It establishes a strict conceptual separation between *Damage* (the direct physical destruction of capital assets, valued at replacement cost) and *Loss* (the subsequent downstream changes in economic flows, such as foregone revenue or increased operating costs). This standard requires deployed economists to calculate complex counterfactual baselines, making it a highly rigorous, albeit time-intensive, secondary assessment tool rather than a primary intake mechanism.

**ADLA (Agricultural Damage and Loss Assessment) / eDLA:**
Spearheaded by the Food and Agriculture Organization (FAO), ADLA is a specialized methodology used by ministries of agriculture to assess impacts specifically within crop, livestock, forestry, and fisheries subsectors. Technically, ADLA departs from generic disaster metrics and employs highly biophysical and commodity-specific logic. It utilizes dynamic seasonal baselines—recognizing that a flood in planting season has a vastly different economic consequence than a flood during harvest. It accounts for biological recovery times, salvage values of livestock, and destroyed stored inputs. This level of granularity demonstrates that agricultural loss cannot be accurately captured in a single, generic "monetary loss" field.

**ECLAC Methodology:**
Developed by the UN Economic Commission for Latin America and the Caribbean, this framework represents an integrated social-environmental macroeconomic approach. It is primarily utilized by national statistical offices to ensure a holistic understanding of a disaster's impact on a nation's development trajectory. Technically, it evaluates aggregate impacts at the administrative-zone level rather than the individual asset level. It incorporates complex psychosocial metrics, evaluates the destruction of non-market environmental assets, and distinctly measures impacts against demographic vulnerabilities (e.g., distinguishing between primary and secondary affected populations).

### 4. Comparison: PDNA Expectations vs. Actual DDPM Data Reality
When contrasting the theoretical expectations of the PDNA standard against the actual reality of historical DDPM-generated disaster data, a significant structural gap becomes apparent. Analysis of historical DDPM data streams from the past decade—specifically village-level impact reports and associated financial relief disbursement logs—demonstrates that the current system is operationally robust but analytically constrained.

The current DDPM reporting apparatus excels at capturing physical counts: tracking the exact number of affected villages, the scale of evacuated populations, and the administrative routing of compensation. However, because it is designed to trigger Ministry of Finance relief, the monetary figures generated by this system represent *administrative compensation values*, not full economic losses. A relief payment of 3,000 Baht to a flooded household is an administrative expenditure; it does not represent the true replacement cost of the home's destroyed assets (Damage) or the wages lost by the household during the recovery period (Loss).

Furthermore, front-line reports often lack the exact geospatial coordinates, the rigorous sector taxonomies, and the counterfactual valuation baselines required by PDNA. Therefore, expecting front-line DDPM data to inherently fulfill PDNA standards is a systemic mismatch. PDNA must be viewed as a target for staged, secondary enrichment, not as an accurate description of DDPM's current—and highly necessary—front-line emergency reporting reality.

### 5. MVD Design Principles
To bridge the gap between DDPM's urgent relief mandate and the nation's need for comprehensive loss and damage accounting, the design of a new Minimum Viable Dataset (MVD) must be rooted in administrative realism. This design builds upon the strategic direction established by the ongoing loss and damage database project led by the National Economic and Social Development Council (NESDC). The NESDC framework explicitly advocates for categorizing impacts across specific sectors (e.g., agriculture, production, housing, public utilities) and emphasizes the need for structured economic valuation.

The guiding design principles for the MVD are therefore established as follows:
*   **Operational Realism at Intake:** The initial data entry layer must align flawlessly with the existing LAO-to-Province DDPM workflow. It must only mandate the capture of fields that are consistently and reliably available during the urgent reporting phase.
*   **Definitive Separation of Counts and Valuation:** The database architecture must explicitly separate raw physical incident tracking (e.g., 500 hectares flooded) from subsequent financial valuation or compensation tracking. Conflating a physical count with an administrative payout degrades the integrity of economic analysis.
*   **Staged Completeness:** The system must abandon the paradigm of a single, static "form" that must be completed perfectly at once. Instead, it must allow a disaster event to be registered rapidly to support emergency response, and then systematically enriched with detailed sectoral and valuation data over weeks and months as secondary assessments are completed.

### 6. The Proposed Full Technical MVD Structure
Derived from these principles, the proposed Minimum Viable Dataset operates on a "Staged Enrichment" framework. It abandons the traditional flat-file spreadsheet approach in favor of a relational, two-tiered architecture designed to mature alongside the disaster recovery lifecycle.

**Component 1: The DISASTER_RECORD (Required-Now Intake Layer)**
This component acts as the rapid intake layer, resembling the DesInventar event-card logic. It captures only the minimum mandatory fields required for immediate situational awareness, emergency routing, and the establishment of a permanent historical anchor for the event. The required fields include:
*   A uniquely generated Event ID to link all subsequent data.
*   Standardized hazard classifications.
*   Nested administrative geography (Province, District, Subdistrict, Village).
*   Precise temporal markers (Start Date, End Date).
*   Immediate, observable human impact counts (affected populations, casualties, missing persons).
This layer is designed to be populated effortlessly by local DDPM officials during the chaotic first days of an incident.

**Component 2: The LOSS_DAMAGE_RECORD (Later-Completion Enrichment Layer)**
This modular enrichment layer houses the true analytical power of the database. Multiple `LOSS_DAMAGE_RECORD` entries can be linked back to a single parent `DISASTER_RECORD`. As various ministries and sectors conduct their post-event assessments, they append data to this layer. 
It houses the NESDC's sector impact categorizations, allowing the Ministry of Agriculture to input crop damage while the Ministry of Transport inputs infrastructure repair costs. Crucially, this layer structurally separates physical damage metrics (e.g., kilometers of road destroyed) from administrative compensation (e.g., relief funds disbursed) and eventual economic loss estimates (e.g., PDNA-calculated trade disruptions).

**Provenance and Revision Control:**
To ensure the analytical integrity of this staged process, the MVD enforces strict provenance tracking across all records. Every data point must log its source system, the specific collection phase (e.g., Urgent Response vs. Post-Recovery Audit), the reporting organization, and its revision status. This ensures that policymakers looking at the data three years later can easily distinguish between a rough, 24-hour initial estimate and a fully verified, World Bank-audited PDNA assessment.

---

## 5.3.7 Methodology for Applying the Draft MVD to Real Events

### 1. Objective and Boundary of Testing
The architecture of the draft MVD must be rigorously validated to ensure it survives contact with real-world administrative friction. The objective of this methodology is not to retroactively rebuild Thailand's entire historical disaster database, nor is it to conduct a new field survey. Rather, the objective is a bounded application test: to map the proposed MVD schema against actual, historical administrative records to test field practicality, data availability, and the resilience of the staged reporting logic.

### 2. Defining the Historical Test Subjects
To avoid the pitfalls of theoretical modeling, the testing methodology mandates applying the MVD against specific, high-fidelity historical disaster datasets previously curated from DDPM source systems. The test will utilize two distinct, historical data streams to evaluate the two components of the MVD:
*   **The DDPM Village Impact Stream:** Utilizing multi-year extracts of raw disaster reporting logs spanning from 2014 to 2024, this dataset represents the front-line reality of Thai disaster reporting. It will be used exclusively to test the population viability of the `DISASTER_RECORD` (Required-Now) fields, verifying if local officials consistently report the necessary geographic, temporal, and human impact data required to anchor an event.
*   **The DDPM Financial Relief Stream:** Utilizing historical relief expenditure ledgers and government advance payment logs, this dataset represents the secondary administrative response. It will be used to test the population of the `LOSS_DAMAGE_RECORD` (Later-Completion) fields, verifying how well administrative compensation values map into the system's segmented valuation layers without conflating them with true economic loss.

### 3. Field Mapping Procedure
The operational steps for applying the MVD schema to these historical datasets follow a strict, multi-stage mapping workflow:
1.  **Extract and Isolate:** Analysts will isolate the raw reporting outputs for a specific, high-impact historical event—for instance, the widespread monsoon flooding of 2022.
2.  **Header Mapping and Intake Validation:** The raw urgent reporting fields (e.g., incident date, province and district codes, identified hazard type, and initial evacuated counts) will be mapped directly to the proposed `DISASTER_RECORD` schema to ensure the mandatory fields do not trigger validation failures against actual historical data.
3.  **Sectoral Enrichment Mapping:** Analysts will extract the corresponding financial relief ledgers for the exact same temporal and spatial footprint. The disbursed compensation values, categorized by sector, will be mapped to the linked `LOSS_DAMAGE_RECORD` schema.
4.  **Provenance Tagging:** During the mapping, analysts will explicitly record the source document type, the reporting agency, and the operational phase for every populated field. This exercises the database's revision control and provenance tracking capabilities, proving that the system can handle data evolving from a "preliminary estimate" to an "audited payout."

### 4. Availability Scoring and Architectural Refinement
During the mapping procedure, every field in the proposed MVD schema will be scored against the historical evidence to continuously calibrate the model's operational realism. The scoring mechanism utilizes three classifications:
*   **Available Now:** The field can be populated directly and consistently from the front-line village impact stream during the rapid intake phase (e.g., "Number of affected villages"). High compliance here validates the core design of the `DISASTER_RECORD`.
*   **Derivable Later:** The field cannot be entered during the initial incident report, but evidence shows it can be confidently completed weeks later using financial relief streams or follow-up departmental surveys (e.g., "Approved relief compensation for agricultural damage"). High compliance here validates the staged enrichment logic of the `LOSS_DAMAGE_RECORD`.
*   **Not Currently Available:** The field exists in the MVD schema (likely borrowed from international standards like DaLA or ADLA) but the mapping exercise reveals it has no credible, consistent source within the current Thai administrative workflow (e.g., "Counterfactual loss of expected agricultural revenue"). 

The interpretation of these scores is the final, critical step of the methodology. Fields that are consistently scored as "Not Currently Available" will not be forced into the baseline requirement. Instead, they will be flagged as future system-improvement requirements. This ensures that the final MVD architecture delivered to the Thai government remains an operationally viable, highly practical tool that reflects the realities of DDPM, rather than an idealized academic standard that fails upon implementation.
