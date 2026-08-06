
# CRDB MVP “Service Prototype Cards” (v2) — Workshop Anchor Artifacts

This file synthesizes:

- the **storytelling material** from [`mvp_slide_ready_narratives_v3_Grounded.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/mvp/mvp_slide_ready_narratives_v3_Grounded.md:2), and
- the **Box 1–2–3 + Service Level** structure from [`mvp_grounded_dummies_v1.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/mvp/mvp_grounded_dummies_v1.md:2)

into **workshop-ready “prototype cards”** for **Morning Activity 2 — Guided Service and Product Expansion** in [`2026-04-30_crdb-workshop-master-design-v2.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/2026-04-30_crdb-workshop-master-design-v2.md:129).

Design intent: each MVP card should work as **(a)** a communication slide and **(b)** a table anchor for the **Decision Utility Matrix** discussion.

---

## How to use in the workshop (recommended)

- Print **1 page per MVP** (or 1 slide per MVP) and place it on each table.
- Facilitator framing: “We show two service levels for each MVP. Your task is to pick what gives you the most decision confidence, and tell us what is missing and what blocks adoption.”
- Table capture should align with the Activity 2 matrix in [`…master-design-v2.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/2026-04-30_crdb-workshop-master-design-v2.md:178).

---

## MVP-1: Policy Briefing Service 
*Grounded in UKCP & Climate-ADAPT patterns.*

### Product Objective
Turn “gridded climate data” into a **policy briefing** that a province can act on.

### Box 1 — The Pain Point
Local planners receive climate projections (e.g., “+2°C on a 12km grid”) but cannot translate it into administrative action. A **translation gap** separates science from policy choices.

### Box 2 — The Concept
An automated **Briefing Generator** that translates technical gridded data into a short **Strategic Briefing** linked to practical impacts and priorities.

### Box 3 — The User Journey 
- **Level 1 (Pragmatic): Tactical Narrative / Scoping**
  - **Mechanism**: proxy trends + pre-written vulnerability modules.
  - **Output**: a 2-page **Provincial Risk Narrative** (prioritization focus).
  - **Decision support value**: “Which districts / issues should we prioritize this decade?”
  - **Action**: policy scoping, regional prioritization.
- **Level 2 (Ideal): Technical Design / Climate Allowance**
  - **Mechanism**: higher-resolution analysis matched to infrastructure/asset context.
  - **Output**: engineering-ready **Climate Allowance** guidance (e.g., “+0.5m freeboard”, “+20% drainage capacity”).
  - **Decision support value**: “What safety margins must we apply in design/specs?”
  - **Action**: engineering specification, site design.

### Table prompts (to drive Activity 2 outputs)
1) **Which level is most useful for your job?** (L1 vs L2)
2) **Which decision does that level enable?** (name a real decision: budgeting, zoning, design standard, procurement)
3) **What’s missing in the logic for your sector?** (impact indicators, thresholds, local exposure data, sector modules)
4) **What blocks adoption?** (data availability, mandates, skills, trust/endorsement, time-to-produce)

---

## MVP-2: Climate Disaster Statistics
*Grounded in strategic data reuse of DDPM/CRI data; WWA/EM-DAT/UNDRR patterns.*

### Product Objective
Convert disaster statistics into **long-term climate impact evidence** that justifies adaptation.

### Box 1 — The Pain Point
Disaster data is scattered and optimized for **relief operations** (budgets, affected households). Climate planners struggle to reuse it to show **long-term frequency/intensity shifts** and economic exposure.

### Box 2 — The Concept
A **re-indexing pipeline** that joins disaster/relief statistics with hazard information and maps impacts onto **30+ year climate timescales**.

### Box 3 — The User Journey 
- **Level 1 (Pragmatic): Initial Data Integration**
  - **Mechanism**: filter climate-relevant events; manually join relief budget tables with hazard frequency.
  - **Output**: dashboard of accumulated cost and hotspot ranking.
  - **Decision support value**: “Where are the highest-cost climate hotspots to target budgets/programs?”
  - **Action**: budget advocacy, prioritization, program targeting.
- **Level 2 (Ideal): Impact Schema / Loss & Impact Attribution**
  - **Mechanism**: standardized impact schema + automated correlation to climate drivers/return periods.
  - **Output**: model of **climate-driven loss** and sectoral loss profiles.
  - **Decision support value**: “How much loss is climate-driven, and what is the ROI of shifting from relief to prevention?”
  - **Action**: national investment case, policy justification.

### Table prompts (to drive Activity 2 outputs)
1) **Which level is most decision-useful for your agency right now?**
2) **What impact variables must be included for credibility?** (people, crops, health, infrastructure, GDP, etc.)
3) **What minimum data-sharing agreements are needed?** (DDPM, sector ministries, finance)
4) **What would make the output trusted enough to use publicly?** (method note, endorsement, QA, uncertainty)

---

## MVP-3:  Data Inventory for Risk and Impact Assessment
*Grounded in NOA/Copernicus curation patterns.*

### Product Objective
Solve “search fatigue” by turning many datasets into a **curated, endorsed set** that people can trust.

### Box 1 — The Pain Point
Users find many versions of “rainfall/temperature/etc.” and face **decision paralysis**. They need to know what is **official/endorsed** for their sector and reporting.

### Box 2 — The Concept
A curated inventory (a “gallery”) that organizes datasets by **sectoral use case** and includes a visible **DCCE Validation** / endorsement from DCCE.

### Box 3 — The User Journey 
- **Level 1 (Pragmatic): Endorsed Gallery (Curation)**
  - **Mechanism**: “Top 10 per sector” pre-vetted list + recommended use notes.
  - **Output**: endorsed dataset page (what it is, what it’s for, limitations).
  - **Decision support value**: “Which dataset should we use for official reporting / planning this month?”
  - **Action**: fast selection by non-experts; consistent reporting.
- **Level 2 (Ideal): Federated Discovery (Integration)**
  - **Mechanism**: federated search/API bridge + full lineage metadata (DCAT/STAC-like).
  - **Output**: professional discovery tool with traceability.
  - **Decision support value**: “Which dataset is fit-for-purpose given method/coverage/lineage?”
  - **Action**: deep technical modeling; cross-sector consistency.

### Table prompts (to drive Activity 2 outputs)
1) **What does “endorsed” mean operationally?** (who signs off, how often reviewed)
2) **What minimum metadata is required for trust?** (coverage, method, update frequency, limitations)
3) **What’s the top sector page you need first?** (agri/health/water/transport)
4) **What would block adoption of an endorsed catalog?** (politics, conflicting standards, capacity)

---

## MVP-4: Data Uncertainty Interpretation Guideline 
*Grounded in IPCC lexicon & readiness tier patterns.*

### Product Objective
Prevent misuse by translating uncertainty into **decision-readiness labels**, not equations.

### Box 1 — The Pain Point
Risk of misuse: users apply coarse or uncertain projections to site-specific decisions. Uncertainty is hidden in appendices → “precision without accuracy.”

### Box 2 — The Concept
A “Decision Guardrails” interface that translates uncertainty into **administrative decision labels** (what this output can/cannot support).

### Box 3 — The User Journey (Service Level trade-off)
- **Level 1 (Pragmatic): Readiness Labels (Traffic Lights)**
  - **Mechanism**: qualitative Green/Amber/Red labels tied to decision types.
  - **Output**: “Suitable for scoping / not for design” guidance at point-of-use.
  - **Decision support value**: “Can I legally/administratively use this output for budgeting/scoping/design?”
  - **Action**: safer planning; reduced liability.
- **Level 2 (Ideal): Uncertainty Limits (Technical Probability)**
  - **Mechanism**: fan charts, probability distributions, confidence intervals.
  - **Output**: quantifiable uncertainty ranges for advanced users.
  - **Decision support value**: “What safety buffer is needed given probability/threshold?”
  - **Action**: risk-buffer calculation; technical design support.

### Table prompts (to drive Activity 2 outputs)
1) **What decision labels do you need?** (scoping, budgeting, zoning, design, procurement)
2) **What would you do when a label is Red?** (escalation path, consultation requirement)
3) **Who needs to agree on the labeling standard?** (DCCE, engineering councils, ministries)
4) **What is the biggest risk if the shield is missing?** (misinvestment, liability, loss of trust)

---

## Optional presenter confidence notes (do not show on the card)

- MVP-1: UKCP / Climate-ADAPT “summary briefing” patterns.
- MVP-2: WWA/EM-DAT/UNDRR demonstrate power of attribution + impact accounting; MVP adds “climate lens + national policy utility.”
- MVP-3: NOAA/Copernicus succeed via curation + application guides, not raw search.
- MVP-4: IPCC lexicon shows why standardized uncertainty language is necessary.

