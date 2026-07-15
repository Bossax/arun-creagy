# Decision Log — GGGI NAP AP M&E Framework Study

**Date:** 2026-07-14  
**Purpose:** Record progress summaries, user decisions, unresolved questions, and next iteration plans for the comparative study of the three national M&E frameworks.

---

## Vocabulary Used in This Note

To maintain process consistency:
*   **Iteration** = A research round consisting of **multiple atomic micro-queries** in NotebookLM, followed by local synthesis and user alignment.


---

## Research Progress Snapshot

*   **Current Status:** End of **Iteration 1** (Depth 1: Conceptual Approaches).
*   **Iteration 1:** Completed 9 atomic micro-queries (MQ 1.1.A to MQ 1.3.C) extracting core planning hierarchies and system concepts.
*   **Iteration 2:** Planned focus on physical implementation, data flows, and verification models.

---

## Iteration 1 Summary (Depth 1: Conceptual Approaches)

### What Iteration 1 Did
*   Executed 9 single-question micro-queries sequentially using `scripts/notebooklm-run.ps1` against the notebook `c79455d7-3470-492f-9eea-cc4832a06897`.
*   Saved the raw JSON API outputs verbatim under `notebooklm_runs/` (converted to UTF-8 on disk for audit integrity).

### What Iteration 1 Established
We compared the theoretical bases of the three frameworks and identified their core alignments and divergences:

1.  **M&E Manual (`คู่มือการติดตามและประเมินผล.pdf`)**: 
    *   **Core Theories**: Anchored in the **IPCC Vulnerability Framework** (where vulnerability is a function of Exposure, Sensitivity, and Adaptive Capacity) and the **UNFCCC M&E Development Infrastructure** guidelines (Context $\rightarrow$ Content $\rightarrow$ Operationalization $\rightarrow$ Products).
    *   **Conceptual Framework**: Models adaptation assessment across a **three-dimensional results pathway**: Planning (readiness/context), Implementation (inputs/process), and Outcomes (systemic resilience changes). It aims to aggregate these dimensions into a quantitative **Climate Resilience Index**.
2.  **TDRI Action Plan (`แผนปฎิบัติการ NAP ฉบับสมบูรณ์.pdf`)**:
    *   **Core Theories**: Grounded in **Climate Change Adaptation Mainstreaming** and **Administrative Policy Implementation Theory**. It posits that climate adaptation must be integrated directly into national development planning rather than treated as a standalone scientific exercise.
    *   **Conceptual Framework**: Cascade mapping of policies into government operational mandates: Policies $\rightarrow$ Strategies $\rightarrow$ Measures $\rightarrow$ Activities. It categorizes adaptation measures using the **Structural vs. Non-structural Typology** (from Disaster/Climate Risk Management literature), separating physical engineering interventions from ecosystem-based (EbA), financial, legal, and institutional capacity-building measures.
3.  **DCCE M&E Platform (`DCCE_ระบบติดตามประเมินผล`)**:
    *   **Core Theories**: Anchored in the **Global Goal on Adaptation (GGA)** (Article 7.1 of the Paris Agreement) and **Social-Ecological Systems Resilience Theory** (Folke et al. focusing on coping/absorbing, reorganizing, retaining functions/identity, and learning capacity).
    *   **Conceptual Framework**: Uses the **Input-Process-Output-Outcome-Impact** chain. It explicitly splits M&E into two functions: **Monitoring** (Output tracking of local agency projects) and **Evaluation** (systemic Outcome/Impact tracking linked to national and global GGA targets). It embeds **Vulnerability Disaggregation** (social categories and economic sectors) to track equity/fairness in adaptation, aligning with UNFCCC 2023 guidelines.


### What Iteration 1 Left Unresolved
*   **MQ 1.2.C Fail-Fast Trigger**: The TDRI query for mapping KPIs to planning levels returned a fail-fast message. It remains unclear how the TDRI plan structurally connects its activities to quantitative outcome indicators in the text of the PDF.
*   **The Analytical Bottleneck**: Because the DCCE database stores answers in loose JSON fields, it behaves as a survey-collection tool rather than a queryable relational database. We need to identify how this impacts calculating the M&E Manual's "Climate Resilience Index."

---

## Locked Decisions

*(No decisions locked yet. Awaiting user review at the end of Iteration 1)*

---

## Open Decisions & Clarifications Needed

### 1. Framework Synthesis Scope
*   **Open Question:** Do you want our comparative study to highlight this core structural conflict (Scientific Resilience Index vs. Administrative Action Plan vs. E-Form Questionnaire DB)?

### 2. Iteration 2 Planning
*   **Open Question:** Shall we pivot Iteration 2 to focus on **data entry flows and institutional reporting roles** across the three documents?

---

## Updated Iteration 2 Plan (Depth 2: Logical Chains & MEL Feed-Forward Planning Loops)

Iteration 2 will target the following atomic queries focusing strictly on the logical chains of the frameworks and how M&E outcomes feed back into the planning cycle:

*   **MQ 2.1 (Manual - Logical Chain & MEL Loop)**:
    1. Extract the conceptual/theoretical justification and formula logic for aggregating indicators into a "Climate Resilience Index" (including weighting and normalization).
    2. Extract the text describing the conceptual link between MEL outcomes and the next cycle of adaptation planning and implementation (adaptive management feed-forward loop).
    *   *Target Source*: `คู่มือการติดตามและประเมินผล.pdf` (ID: `a8e10df8-1c98-4710-93d3-462294ef5526`)
*   **MQ 2.2 (TDRI - Mainstreaming & MEL Loop)**:
    1. Extract the conceptual integration of adaptation strategies into sectoral plans, and the theoretical justification for the structural vs. non-structural measure typologies.
    2. Extract the text implying or outlining how M&E findings/evaluation results feed back into the next cycle of sectoral planning and implementation.
    *   *Target Source*: `(Up) แผนปฎิบัติการ NAP ฉบับสมบูรณ์.pdf` (ID: `97d499c8-8b06-4601-b064-afd00f9841d6`)
*   **MQ 2.3 (DCCE - Resilience Capacities & MEL Loop)**:
    1. Extract the theoretical relationships between the four resilience capacities (coping, reorganizing, retaining, learning) and the conceptual logic bridging project-level Outputs and national/GGA Outcomes.
    2. Extract the text describing how platform evaluation outcomes conceptually inform and trigger updates in the next cycle of adaptation planning and implementation.
    *   *Target Source*: `DCCE_ระบบติดตามประเมินผล_เล่มงวดที่ 2_ V.07_25032026.pdf` (ID: `a69e4f87-a802-4ff4-a214-06931c301d2b`)

---

## Iteration 2 Summary (Logical Chains & MEL Feed-Forward Loops)

### What Iteration 2 Did
*   Executed 3 atomic micro-queries (MQ 2.1 to MQ 2.3) sequentially against the source documents.
*   Extracted raw passages defining the logical aggregation chains and the adaptive planning loop linking M&E outcomes back to design/implementation.

### What Iteration 2 Established

#### 1. The Logical Chains of the Frameworks
*   **M&E Manual**: Aggregates dimensional indicators (Exposure + Sensitivity + Adaptive Capacity) into a **Vulnerability Index**. Over a multi-year timeline, the trend of this index is mapped to evaluate the national **Climate Resilience Index** across sectoral domains, categorizing status as Low, Moderate, or High.
*   **TDRI Action Plan**: Maps policies to sectoral plans and measures. It categorizes adaptation measures strictly using a **Structural Typology** (physical/engineering builds) and **Non-structural Typology** (ecosystem-based, financial, policy, legal, warning readiness) to determine operational mandates.
*   **DCCE Platform**: Replaces traditional "activity-based reporting" (which only counts completed events) with a strict **Input-Process-Output-Outcome-Impact** logical framework. It grounds indicator definitions in **Social-Ecological Resilience** (IPCC/Folke), capturing four capacity metrics: Coping/Absorbing, Reorganizing, Retaining functions/identity, and Learning.

#### 2. The MEL Feed-Forward planning loops (Adaptive Management)
*   **M&E Manual**: Integrates M&E as a core step in the **Iterative Policy Cycle**. Evaluation outcomes feed back directly to:
    *   Sectoral project adjustments.
    *   Refinements of the national NAP strategies, indicators, and institutional frameworks.
    *   Continuous organizational learning.
*   **TDRI Action Plan**: Outlines a **Climate Risk Management (CRM) loop**: Prioritize & Fund $\rightarrow$ Implement $\rightarrow$ M&E $\rightarrow$ Learning Feedback. Annual reports capture success factors and implementation barriers, submitting recommendations to the National Climate Change Policy Committee to adjust project funding and design in subsequent cycles.
*   **DCCE Platform**: Formally adopts **UNFCCC LEG Element D (Reporting, monitoring, and review)** guidelines to frame M&E as **MEL (Monitoring, Evaluation and Learning)**. It models MEL as a **Closed Loop (วงจรปิด)** of 5 stages: Context $\rightarrow$ Targets $\rightarrow$ Monitoring $\rightarrow$ Evaluating & Learning (testing baseline hypotheses) $\rightarrow$ Adjusting (refining budgets, measure intensity, and legal frames). It cites Chile (4-5 year iterative planning loops) and Fiji (M&E-driven village relocation decisions) as international models for iterative planning.

### 3. Theory vs. Implementation Gaps (The Fragmentation Conflict)

Based on cross-referencing the theoretical texts (NotebookLM queries) with the actual implementation diagrams (`NAP_MandEPlatform_NAP-Action-Plan.jpg`) and analyst background notes, we identified major structural conflicts:

*   **TDRI Action Plan Gap (The Output-to-Outcome Illusion)**:
    *   *Theory*: The framework is supposed to map local planning activities through a Climate Risk Management loop.
    *   *Implementation Reality*: TDRI's plan **literally copied the global GGA outcome indicators** as its targets. However, because it maps directly from local line agency activities (which only have business-as-usual output data), it calculates these global outcomes using raw project outputs (e.g. number of trainings). This creates an attribution illusion where outputs are passed off as outcomes. Furthermore, the MQ 1.2.C "fail-fast" occurred because the plan bypassed mapping local indicators conceptually and instead directly adopted the global GGA indicators.
*   **DCCE M&E Platform Gap (The Indicator Pass-Through)**:
    *   *Theory*: The M&E Manual and DCCE Platform advocate for a strict outcome-based, scientific system (UNFCCC Element D) that aggregates an IPCC Vulnerability/Climate Resilience Index, while criticizing TDRI's "activity-based output reporting".
    *   *Implementation Reality*: The platform actually locks a strict **1-to-1 measure-to-indicator relationship**. The diagram reveals that the Platform's "Outcome Indicators" (`NAP-OUTCOME-xxx`) share exact identical IDs with the Action Plan's raw project-level "Data Needed" (`ACT-OUTCOME-xxx`). This exposes that the platform is not mathematically aggregating a vulnerability index; it is merely renaming and acting as a pass-through reporting shell for TDRI's raw output data.
    *   *The Visual Illusion*: The platform's diagram inserted an artificial middle tier ("Data Support" and "Output" layers) to make the direct pass-through look like a sophisticated multi-dimensional database mapping.

![](ψ/incubate/GGGI/NAP_AP/inbox_note/NAP_MandEPlatform_NAP-Action-Plan.jpg)

another comment is that, there are no *targets*. 

### Verbatim Raw Evidence Excerpts from Terminal Printouts

#### 📘 MQ 2.1 (M&E Manual) - Verbatim Excerpts
*   **Climate Resilience Index Aggregation**:
    > "เพื่อประเมินสถานะการมีภูมิคุ้มกันในแต่ละรายสาขาในระยะยาว ตัวชี้วัดที่กำหนดไว้ในทั้งสามด้านนี้จะถูกวิเคราะห์และประเมินเพื่อทำความเข้าใจดัชนีความเปราะบางรายปี... ประเมินการมีภูมิคุ้มกันต่อสภาพภูมิอากาศ... ว่าอยู่ในระดับที่ขาดการมีภูมิคุ้มกันหรือต่ำ ปานกลาง หรือสูง"
    > *(Translation: To assess long-term resilience per sector, indicators across the three dimensions are analyzed to compute a Yearly Vulnerability Index, allowing policy-makers to map trends and categorize sectoral climate resilience as Low, Moderate, or High.)*
*   **The MEL Loop & Policy Cycles**:
    > "M&E เป็นหนึ่งในสี่ขั้นตอนของวงจรนโยบายการปรับตัวแบบวนซ้ำ..."
    > "1) การประเมินผลโครงการจะช่วยสะท้อนกลับไปในกระบวนการตัดสินใจในการบริหารโครงการและการปรับปรุงยุทธศาสตร์การดำเนินงาน รวมถึงการปรับปรุงแผนการปรับตัวต่อการเปลี่ยนแปลงสภาพภูมิอากาศแห่งชาติ (NAP) ทั้งในเชิงโครงสร้างการบริหารจัดการ ตัวชี้วัด และยุทธศาสตร์ในการแปลงแผนไปสู่การปฏิบัติ"
    > *(Translation: M&E is one of the four stages of the iterative policy cycle. Project evaluation feeds back into project management decisions, operational strategy adjustments, and updates to the national NAP structure, indicators, and mainstreaming strategies.)*

#### 📙 MQ 2.2 (TDRI Action Plan) - Verbatim Excerpts
*   **Mainstreaming & Typology**:
    > "การบูรณาการประเด็นด้านการปรับตัวต่อผลกระทบจากการเปลี่ยนแปลงสภาพภูมิอากาศในแผนและยุทธศาสตร์รายสาขาและในพื้นที่ได้อย่างถูกต้องและเหมาะสม..."
    > "การดำเนินงานปรับตัว... ควรพิจารณาความเหมาะสมระหว่างการใช้มาตรการด้านโครงสร้าง (structural measures)... กับการใช้มาตรการที่ไม่ใช่โครงสร้าง (non-structural measures)..."
    > *(Translation: Integrating climate adaptation into sectoral plans and spatial strategies... Adaptation operations must weigh structural measures (physical/engineering builds) against non-structural measures (ecosystem-based, financial, legal, warning systems).)*
*   **CRM & Committee Feedback Loops**:
    > "มาตรการการบริหารจัดการความเสี่ยงต่อการเปลี่ยนแปลงสภาพภูมิอากาศ (CRM measures) จะช่วยให้สามารถพิจารณาแนวทางการดำเนินงาน... นำผลการเรียนรู้ที่ได้รับมาแก้ไขปรับปรุงการบริหารจัดการให้มีประสิทธิภาพยิ่งขึ้น..."
    > "จัดทำรายงานการติดตามการเปลี่ยนแปลงของตัวชี้วัดพร้อมวิเคราะห์ปัญหา อุปสรรค และปัจจัยสู่ความสำเร็จ... นำเสนอรายงาน... ต่อคณะกรรมการนโยบายการเปลี่ยนแปลงสภาพภูมิอากาศแห่งชาติเพื่อรับทราบและให้ข้อคิดเห็นหรือคำแนะนำ..."
    > *(Translation: Climate Risk Management (CRM) measures ensure learning outcomes are fed back to improve management efficiency. Annual indicator reports identifying barriers and success factors are submitted to the National Climate Change Policy Committee for policy guidance and adjustments.)*

#### 📗 MQ 2.3 (DCCE Platform) - Verbatim Excerpts
*   **Output vs. Outcome Chains**:
    > "ตัวชี้วัดควรถูกจัดโครงสร้างให้ครอบคลุมลำดับขั้นของผลลัพธ์ ได้แก่ input, process, output, และ outcome... เพื่อหลีกเลี่ยงปัญหาที่ระบบ M&E ในหลายกรณีเน้นเพียงการรายงานกิจกรรม (activity-based reporting) โดยไม่สามารถสะท้อนผลการปรับตัวที่แท้จริงได้"
    > *(Translation: Indicators must span the input-process-output-outcome chain to avoid traditional M&E systems getting trapped in activity-based reporting that fails to reflect actual adaptation outcomes.)*
*   **Resilience Pillars (Folke/IPCC)**:
    > "Resilience... สะท้อนองค์ประกอบสำคัญ 4 ประการ ประกอบด้วย (1) ความสามารถในการรับมือและดูดซับผลกระทบ (Coping & Absorbing) (2) ความสามารถในการปรับโครงสร้าง (Reorganizing) (3) การรักษาหน้าที่และอัตลักษณ์ของระบบ (Retaining functions & identity) และ (4) ศักยภาพในการเรียนรู้ (Learning capacity)"
    > *(Translation: Resilience reflects four core elements: (1) Coping & Absorbing capacity, (2) Reorganizing capacity, (3) Retaining system functions and identity under stress, and (4) Learning capacity.)*
*   **UNFCCC Element D Closed Loop & MEL learning**:
    > "Element D: Reporting, monitoring and review... ถูกวางให้เป็น วงจรปิด ของกระบวนการ NAP... สอดคล้องกับหลักการของ LEG ที่มอง NAP เป็นกระบวนการ ต่อเนื่อง ก้าวหน้า และวนซ้ำ (continuous, progressive, iterative)..."
    > "ใช้คำว่า MEL (Monitoring, Evaluation and Learning) แทน M&E เดิม... สร้าง วงจรการเรียนรู้ ที่หล่อเลี้ยง การวางแผนและการดำเนินมาตรการในรอบต่อไป..."
    > "(5) การปรับปรุงนโยบาย (Adjusting) การนำบทเรียนที่สังเคราะห์ได้มาปรับปรุง แผนงาน ไม่ว่าจะเป็นการเปลี่ยนระดับความเข้มข้นของมาตรการ การปรับเปลี่ยนเทคนิค หรือแม้แต่การทบทวน กรอบกฎหมายและงบประมาณ"
    > *(Translation: UNFCCC LEG Element D is structured as a closed loop, framing NAP as continuous, progressive, and iterative. Transitioning to MEL builds a learning ring that nourishes subsequent cycles. Policy adjusting synthesizes lessons to update plans, measure intensity, technical designs, budgets, and laws.)*

---
*Logged via /decision-log*

## Iteration 3 Summary (Depth 3: Conceptual Definitions and Disaggregation Rules)

### What Iteration 3 Did
*   Executed 3 micro-queries (MQ 3.1 to MQ 3.3) to extract specific mathematical calculation formulas, indicator variables, and data disaggregation guidelines.
*   Successfully ran MQ 3.1 (Manual) and MQ 3.2 (TDRI). 
*   MQ 3.3 (DCCE) triggered a fail-fast condition, which was resolved by cross-referencing DCCE's indicator logic and disaggregation levels from the Iteration 1 detailed query (MQ 3.d).

### What Iteration 3 Established

#### 1. The Missing Math of the M&E Manual (CRI Calculations)
*   **The Findings (MQ 3.1)**: While the manual details the qualitative Exposure-Sensitivity-Adaptive Capacity hierarchy and path ($Yearly\ Vulnerability\ Index \rightarrow\ Trend \rightarrow\ Climate\ Resilience\ Index$), the text **does not contain any mathematical formulas, weighting schemas, or normalization equations**.
*   **The Implications**: ==The "Climate Resilience Index" is a conceptual model only==. Any math implemented in the DCCE platform was developed from scratch by the consultants, rather than being grounded in manual-mandated formulas.

#### 2. TDRI's Specific Variable Calculation Formulas
*   **The Findings (MQ 3.2)**: Unlike the manual, the TDRI Action Plan provides concrete mathematical formulas for its copied GGA indicators:
    *   **Proportional Crop Quantity Damage (%)**:
        $$\text{Proportional Quantity Damage (\%)} = \frac{\sum Q_{i,\text{damaged}}}{\sum Q_{i,\text{total}}} \times 100$$
        *(Where $Q_i$ represents major crops: rice, sugarcane, maize, cassava in tons).*
    *   **Proportional Crop Value Damage (%)**:
        $$\text{Proportional Value Damage (\%)} = \frac{\sum V_{i,\text{damaged}}}{\text{Agricultural Sector GDP}} \times 100$$
        *(Where damage value $V_i$ is calculated from crop quantity damaged $\times$ average market unit price).*
    *   **Food Self-Sufficiency Ratio (SSR) (%)**:
        $$\text{SSR (\%)} = \frac{\text{Domestic Production Quantity}}{\text{Annual Domestic Consumption Quantity}} \times 100$$
    *   **Tourism Value Damage (%)**:
        $$\text{Provincial Tourism Loss (\%)} = \frac{\text{Decrease in tourists due to climate events} \times \text{Average spend}}{\text{Provincial Tourism Revenue}} \times 100$$
    *   **Urban Water Indicators**: Specifically maps urban drainage capacity (mm/hour), green infrastructure area (hectares of monkey cheeks), population warning coverage (% of risk population), and flood/drought damage value (% of GDP).

#### 3. DCCE Platform's Data Disaggregation Levels
*   **The Findings (MQ 3.d / 3.3)**: Confirms the central platform structures indicators into two main disaggregation dimensions to align with UNFCCC and "Leave No One Behind" (LNOB) equity principles:
    *   **Social Categories (มิติสังคม)**: Disaggregated by Gender (เพศ), Age (อายุ), Displaced/Migrant status (สถานะผู้พลัดถิ่น), Disability (ผู้พิการ), Indigenous/Ethnic status (ชนเผ่าพื้นเมือง), and Local Communities (ชุมชนท้องถิ่น).
    *   **Economic Sectors (มิติเศรษฐกิจ)**: Disaggregated by Agriculture (ภาคเกษตรกรรม), Tourism (การท่องเที่ยว), and Industry (ภาคอุตสาหกรรม).

#### 4. Units of Analysis Across the Three Frameworks
To map how data flows through these systems, we must understand what each framework considers its primary "unit of analysis" (both for reporting raw data and for calculating/aggregating outcomes):
*   **M&E Manual**:
    *   *Reporting Unit*: **Project/Local level**.
    *   *Analytical/Evaluation Unit*: **Sectoral Level (ระดับรายสาขา)**.
    *   *Concept*: Indicators are collected at local levels but are aggregated via dimensional weights (Exposure, Sensitivity, Adaptive Capacity) to form a sectoral **Yearly Vulnerability Index**, and evaluated over time to form a sectoral **Climate Resilience Index (CRI)**.
*   **TDRI Action Plan**:
    *   *Reporting Unit*: **Project/Activity Level (ระดับกิจกรรม/โครงการ)**.
    *   *Analytical/Evaluation Unit*: **Project/Activity Level (ระดับกิจกรรม/โครงการ)**.
    *   *Concept*: Grounded in policy mainstreaming, it matches actual funded projects of line agencies directly to NAP guidelines/measures. It tracks outcomes at the individual project activity level by mapping them directly to copied GGA outcome indicators.
*   **DCCE Platform**:
    *   *Reporting Unit*: **Project/Activity Level (ระดับโครงการ/กิจกรรม)** (Monitoring).
    *   *Analytical/Evaluation Unit*: **Systemic/Sectoral Level (ระดับเชิงระบบ/รายสาขา)** (Evaluation).
    *   *Concept*: Tracks raw project outputs for monitoring, but attempts to evaluate outcomes at a systemic level. Crucially, the platform enforces a **1-to-1 mapping between a Measure (ระดับมาตรการ) and its Outcome Indicator**.

#### 5. Criticism: The Mismatch of Units of Analysis and Indicators
The lack of alignment between the reporting units and the indicators creates severe structural friction:
1.  **The Output-to-Outcome Scale Mismatch (TDRI)**:
    *   *The Mismatch*: TDRI maps individual project activities directly to high-level **GGA Outcome Indicators** (which are global in scale, e.g., systemic vulnerability reduction) with no intermediate output layer.
    *   *The Friction*: Since line agencies can only collect project-level outputs (e.g., number of seedlings planted), TDRI's framework tries to verify global/sectoral outcomes using project-level output variables. This creates a severe scale mismatch where local project outputs are treated as proof of global outcome achievements.
2.  **The Rigid Database Locking Constraint (DCCE)**:
    *   *The Mismatch*: DCCE's platform collects data at the **Project/Activity level**, but the database locks outcome indicators **1-to-1 to the Measure level**.
    *   *The Friction*: By locking outcomes 1-to-1 to policy measures, the platform cannot handle the cross-cutting realities of actual projects. An agency activity might contribute to multiple measures, or a single measure might require an outcome aggregated from multiple projects. By forcing a rigid 1-to-1 lock at the measure level, the platform fails to model the multi-dimensional relationships of project data, forcing a false 1-to-1 mapping.
3.  **The Pass-Through Redundancy**:
    *   *The Mismatch*: Since the DCCE platform's outcome indicators (`NAP-OUTCOME-xxx`) are identical to TDRI's project data variables (`ACT-OUTCOME-xxx`), the platform isn't performing any complex sectoral aggregation.
    *   *The Friction*: Instead of aggregating project data to evaluate sectoral resilience (as envisioned by the M&E Manual), the platform acts as a simple pass-through reporting shell. It merely renames project-level variables to `NAP-` outcomes, making its sophisticated database mapping (the "Data Support" and many-to-many layers) an empty visual wrapper.


### Verbatim Raw Evidence Excerpts from Terminal Printouts

#### 📘 MQ 3.2 (TDRI Action Plan) - Verbatim Excerpts
*   **Agricultural Crop Damage Formulas**:
    > "สัดส่วนของปริมาณความเสียหาย (%) = $\frac{\sum Q_i\text{เสียหาย}}{\sum Q_i\text{รวม}} \times 100$"
    > "สัดส่วนของมูลค่าความเสียหาย (%) = $\frac{\sum V_i\text{เสียหาย}}{\text{GDP ภาคเกษตร}} \times 100$"
    > "โดยที่ Qiเสียหาย = ปริมาณพืชชนิดที่ i ที่เสียหาย (ตัน) และ Viเสียหาย = มูลค่าความเสียหายของพืชชนิดที่ (บาท)"
    > *(Translation: Proportional quantity damage (%) = (sum of Q_i damaged / sum of Q_i total) * 100; Proportional value damage (%) = (sum of V_i damaged / agricultural GDP) * 100. Where Qi is quantity of damaged crop i in tons, and Vi is value of damaged crop i in Baht.)*
*   **Self-Sufficiency Ratio (SSR) Formula**:
    > "อัตราการพึ่งพาตนเองด้านอาหาร (SSR) = $\frac{\text{ปริมาณผลผลิตที่ผลิตได้ในประเทศ}}{\text{ปริมาณผลผลิตที่ต้องใช้บริโภคในประเทศทั้งปี}} \times 100$"
    > *(Translation: Self-Sufficiency Ratio (SSR) = (Domestic production quantity / Annual domestic consumption quantity) * 100.)*
*   **Tourism Loss calculation**:
    > "มูลค่าความเสียหายจากการลดลงของจำนวนนักท่องเที่ยว คำนวณจากจำนวนการลดลงของนักท่องเที่ยว... ที่มีสาเหตุสืบเนื่องจากเหตุการณ์หรือปัจจัยที่เกี่ยวข้องกับการเปลี่ยนแปลงสภาพภูมิอากาศ เทียบกับรายได้จากการท่องเที่ยวระดับจังหวัด..."
    > *(Translation: Monetary damage from tourist reduction is calculated from the decrease in tourists... due to climate-related factors, compared against provincial tourism revenue to assess proportion of spatial economic impact.)*

#### 📗 MQ 3.d (DCCE Platform) - Verbatim Excerpts
*   **Vulnerability Disaggregation Categories**:
    > "การจำแนกข้อมูล (Disaggregation Levels) ซึ่งถือเป็นหัวใจสำคัญของกรอบ GGA... กำหนดให้มีการจำแนกข้อมูลในมิติที่ซับซ้อน... ในมิติสังคม (Social categories)... เช่น เพศ อายุ สถานะผู้พลัดถิ่น ผู้พิการ ชนเผ่าพื้นเมือง และชุมชนท้องถิ่น... สำหรับมิติเศรษฐกิจ (Economic Sectors) เช่น ภาคเกษตรกรรม การท่องเที่ยว หรือภาคอุตสาหกรรม"
    > *(Translation: Data Disaggregation Levels is the heart of the GGA framework... defining complex disaggregation in social categories (such as gender, age, displaced status, disability, indigenous status, and local communities) and economic sectors (such as agriculture, tourism, or industry).)*

---
*Logged via /decision-log*
