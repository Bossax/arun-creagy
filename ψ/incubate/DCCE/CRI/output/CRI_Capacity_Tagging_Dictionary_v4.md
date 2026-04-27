# CRI Phase 2 Capacity Tagging Dictionary v4.1 (Adopted Linkage Logic)

**Version**: 4.1 (Hardened Integration)
**Date**: 2026-04-27
**Status**: Adopted working default for Phase 2 linkage program (based on Experiment B)

---

## 1. Overview of the v4.1 Logic

This dictionary is the canonical operational reference for the CRI Phase 2 v4 methodology. It advances the v3 structure by explicitly integrating the findings of the **Phase 2 Linkage Experiments (A, B, and C)**.

The core shift in v4.1 is the transition from static, asset-heavy definitions to **process-aware governance anchors**. This means every governance concept is defined not by the "stock" it represents, but by the **activation discipline** required to turn that stock into a resilient service function.

### Key Logic Gates:
1.  **Stock-Potential vs. Governance-Activation**: Assets are treated as structural potential; Governance is the signal of institutional readiness to activate that potential under stress.
2.  **Complementary Signals**: Scores from the two groups are read as complementary condition signals, not as formula inputs or direct proof of outcome.
3.  **Six-Pillar Kernel**: The institutional governance structure remains anchored to six pillars. No seventh pillar is added.
4.  **Cross-cutting Scored CSOS**: `Community Self-Organization & Stewardship` is integrated as a cross-cutting scored concept that influences metric selection across pillars rather than being a separate visible category.
5.  **Internal-Only Chains**: Detailed "Activation Chains" (mapping Asset → Governance → Function) are used for internal analyst discipline only and are not exposed as public calculation mechanics.

---

## 2. Capacity Categories (the 'How')

Consistent with the 3-layer resilience framework, each concept is tagged with a primary capacity category.

-   **Coping (Absorptive)**: The ability of the system to endure and absorb shocks while maintaining basic functions using existing resources.
-   **Adaptive**: The ability of the system to adjust, learn, and modify its internal processes in response to changing risks and stress.
-   **Transformative**: The ability of the system to fundamentally alter its structure, logic, or goals to navigate systemic shifts and long-term climate pressure.

---

## 3. Aspect Definitions (the 'What')

Aspects organize governance indicators into functional families.

1.  **Planning & Strategy**: Governance of the future; how risk information steers land-use and development control.
2.  **Finance & Procurement**: Governance of the wallet; how money is tagged, reserved, and flowed during and after shocks.
3.  **Coordination & Partnerships**: Governance of the network; how departments, tiers, and stakeholders align and delegate.
4.  **Service Delivery & Ops**: Governance of the floor; how essential functions (water, power, aid) are maintained and managed.
5.  **Data & Digital Governance**: Governance of the signal; how risk data and digital services support shared awareness.
6.  **HR & Institutional Capacity**: Governance of the people; how skills, staffing, and training are maintained.

---

## 4. The v4.1 Indicator Concept Matrix (Hardened)

| indicator_concept                             | capacity_category | proposed_thai_anchor                               | evidence                                          | candidate_indicator_code | cross_cutting_tags | scoring_use_decision |
| :-------------------------------------------- | :---------------- | :------------------------------------------------- | :------------------------------------------------ | :----------------------- | :----------------- | :------------------- |
| **Pillar 1: Planning & Strategy**             |                   |                                                    |                                                   |                          |                    |                      |
| **Plan revision cycle**                       | Adaptive          | ความถี่ในการปรับปรุงแผน                            | OECD 2018 (Learning); Experiment A benchmark      |                          |                    |                      |
| **Risk-informed planning**                    | Transformative    | การใช้ข้อมูลความเสี่ยงในผังเมือง                   | Feldmeyer et al. 2019; v2 cluster                 |                          |                    |                      |
| **Policy Integration**                        | Transformative    | การบูรณาการนโยบายข้ามหน่วยงาน                      | MDPI 2019 (Integration); v1.1 row                 |                          | CSOS if relevant   |                      |
| **Pillar 2: Finance & Procurement**           |                   |                                                    |                                                   |                          |                    |                      |
| **Emergency budget flow**                     | Coping            | ความเร็วในการเบิกจ่ายงบฉุกเฉิน                     | IMF 2021 (Public Finance); v1.1 row               |                          |                    |                      |
| **Climate budget tagging**                    | Adaptive          | รหัสงบประมาณด้านภูมิอากาศ                          | UNDP (Budget Tagging); v1.1 row                   |                          |                    |                      |
| **Resource allocation scale**                 | Adaptive          | สัดส่วนงบประมาณด้านความยืดหยุ่น                    | Strategy& (Resource usage); v1.1 row              |                          |                    |                      |
| **Pillar 3: Coordination & Partnerships**     |                   |                                                    |                                                   |                          |                    |                      |
| **Multi-stakeholder collab.**                 | Adaptive          | ความถี่การประชุมคณะกรรมการร่วม                     | Urban.org; v2 cluster                             |                          | CSOS if relevant   |                      |
| **Formal coordination bodies**                | Transformative    | คำสั่งจัดตั้งหน่วยงาน/คณะทำงาน                     | Urban.org; v1.1 row                               |                          | CSOS if relevant   |                      |
| **Pillar 4: Service Delivery & Ops**          |                   |                                                    |                                                   |                          |                    |                      |
| **Service delivery timeliness**               | Adaptive          | เวลาเฉลี่ยในการตอบสนองเหตุ                         | Serdar et al. 2021; Strategy&                     |                          |                    |                      |
| **Infrastructure integrity & management**     | Absorptive        | บันทึกความถี่การบำรุงรักษาและการตรวจสอบความปลอดภัย | **SETS Hardened (Brito et al. 2026)**; v2 cluster |                          |                    |                      |
| **Pillar 5: Data & Digital Governance**       |                   |                                                    |                                                   |                          |                    |                      |
| **Data interoperability**                     | Transformative    | มาตรฐานการแลกเปลี่ยนข้อมูล (API)                   | MDPI (Smart City); v1.1 row                       |                          |                    |                      |
| **Digital climate services**                  | Transformative    | ระบบเตือนภัยล่วงหน้า (EWS)                         | v2 cluster; Sharifi 2023                          |                          | CSOS if relevant   |                      |
| **Risk Assessment depth**                     | Adaptive          | ความลึกของการศึกษาวิเคราะห์ความเสี่ยง              | Feldmeyer et al. 2019; v2 cluster                 |                          | CSOS if relevant   |                      |
| **Pillar 6: HR & Institutional Capacity**     |                   |                                                    |                                                   |                          |                    |                      |
| **Emergency staff capacity**                  | Coping            | สัดส่วนเจ้าหน้าที่กู้ชีพ/กู้ภัย                    | v2 cluster; Moench                                |                          | CSOS if relevant   |                      |
| **Staff Training frequency**                  | Adaptive          | บันทึกการฝึกอบรมด้านความยืดหยุ่น                   | Strategy&; v1.1 row                               |                          | CSOS if relevant   |                      |
| **Cross-cutting**                             |                   |                                                    |                                                   |                          |                    |                      |
| **Community Self-Organization & Stewardship** | Adaptive          | Volunteer capability & collective mobilization     | **Experiment B Adopted Overlay**                  |                          | CSOS (Core)        | Score in pillars     |

---

## 5. Concept definitions (Adopted v4.1 Hardened Rules)

These definitions are no longer static descriptions; they are **Hardened Interpretation Rules** for scanning and scoring.

### 5.1 Planning & Strategy

-   **Plan revision cycle**: The governance process of updating core strategies in light of new risk data and past failures. **Hardening**: Look for evidence of *after-action reviews* and *monitoring-to-plan feedback loops*, not just the date of the document.
-   **Risk-informed planning**: The degree to which multi-hazard diagnostics *legally steer* land-use and investment. **Hardening**: Look for *zoning enforcement* and *siting restrictions* linked to hazard maps.
-   **Policy Integration**: Alignment across departments to break silos. **Hardening**: Look for *joint budget lines* or *shared mandates* between climate and non-climate departments.

### 5.2 Finance & Procurement

-   **Emergency budget flow**: The reliability and speed of capital deployment post-shock. **Hardening**: Look for *pre-approved trigger mechanisms* and *flexible procurement SOPs*.
-   **Climate budget tagging**: Tracking resilience spend over time. **Hardening**: Look for *expenditure tracking* (not just budget labeling) that influences future allocation.
-   **Resource allocation scale**: The magnitude of resilience-relevant spending. **Hardening**: Look for *dedicated reserves* and *diversified funding sources* (public + private).

### 5.3 Coordination & Partnerships

-   **Multi-stakeholder collab.**: Quality of interactions between government and non-state actors. **Hardening**: Look for *Shared Learning Dialogues (SLDs)* and *institutionalized forums* that surface community knowledge.
-   **Formal coordination bodies**: Mandate for cross-departmental steering. **Hardening**: Look for a *Chief Resilience Officer (CRO)* type entity with real authority to link fragmented departments.

### 5.4 Service Delivery & Ops

-   **Service delivery timeliness**: Rapidity of response and recovery. **Hardening**: Look for *time-to-restore KPIs* for utilities and essential services under stress conditions.
-   **Infrastructure integrity & management**: The governance and operational processes ensuring physical networks maintain function or fail safely under shocks. It focuses on the discipline of maintenance, the enforcement of standards, and the active management of safe-to-fail protocols, rather than the mere presence of physical stock. **Hardening**: Look for *maintenance frequency*, *inspection discipline*, and the management of *fail-safe/redundancy protocols*. (See Brito et al. 2026 for functional-vs-physical separation).
-   🫥 **Case throughput rate** *(partially evidenced)*: Resolution rate of citizen-reported incidents (e.g., Traffy Fondue cases). **Hardening**: Look for *resolution closure rates* relative to inflow.

### 5.5 Data & Digital Governance

-   **Data interoperability**: Cross-sector situational awareness through shared standards. **Hardening**: Look for *API adherence* and *multi-agency data exchange compliance*.
-   **Digital climate services**: Deployment of monitoring and prediction tools (EWS, Digital Twins). **Hardening**: Look for *citizen-facing reliability* and *reach* among vulnerable groups.
-   **Risk Assessment depth**: Sophistication of diagnostics (multi-hazard, cascading impact). **Hardening**: Look for *participatory risk mapping* and *systemic vulnerability* inclusion.

### 5.6 HR & Institutional Capacity

-   **Emergency staff capacity**: Availability and competency of crisis personnel. **Hardening**: Look for *specialized skill-sets* and *cross-functional deployment readiness*.
-   **Staff Training frequency**: Regularity of resilience-specific training. **Hardening**: Look for *mandatory training requirements* and *competency framework* alignment.

### 5.7 Cross-cutting scored concept (assigned back into pillar scores)

-   **Community Self-Organization & Stewardship** *(cross-cutting scored concept)*: The degree to which communities organize and co-produce risk-relevant services. **Hardening**: Use this concept to admit metrics that formal pillars miss—e.g., *customary stewardship rights* or *trust-based social capital*. **Rule**: Score these metrics inside the existing six pillars.

---

## 6. Adoption Boundary & Lineage

1.  **Working Default**: Experiment B logic.
2.  **Benchmark**: Experiment A (presumption against growth).
3.  **Boundary**: Experiment C (stress-test confirmation).
4.  **Validation**: Higher scores suggest indicative conditions, not proven outcomes. Validity remains context-dependent and requires monitoring against observed stress performance.
