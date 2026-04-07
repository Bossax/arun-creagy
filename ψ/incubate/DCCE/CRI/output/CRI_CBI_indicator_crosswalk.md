# CBI Indicator Crosswalk (CA1–TP3)

Purpose: provide a clear mapping from CBI indicators (CA1–TP3) into the CRI Phase 2 capacity framework and the v1 conceptual dictionary in [`CRI_Capacity_Tagging_Dictionary.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md).

This file is an implementation bridge, not a new conceptual schema. It shows, for each CBI indicator:
- which **capacity category** and **capacity dimension** it belongs to in CRI terms, and
- which **v1 indicator concept(s)** it supports (if any),
- or whether it constitutes a **new CBI-only concept group**.

## Legend

- **CBI capacity category** – Coping / Adaptive / Transformative (CBI pillars, mapped to CRI capacity categories).
- **CBI capacity dimension** – Asset / Process (CBI dimensions, mapped to CRI capacity dimensions).
- **v1 concept(s)** – names of indicator concepts from v1 in [`CRI_Capacity_Tagging_Dictionary.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary.md).
- **v1 capacity category** – capacity category of the mapped v1 concept(s).
- **Governance function** – primary governance role in the CRI lens.
- **Integration type**:
  - **A** – CBI indicator serves as a Baseline proxy for an existing v1 concept.
  - **B** – CBI indicator belongs to a new concept group (no direct v1 concept); to be handled via new v2-only rows.
  - **C** – CBI indicator is contextual only (not part of the core capacity index).

## 1. CBI → v1 mapping table

| CBI code | CBI indicator (short)                               | CBI capacity category | CBI capacity dimension | v1 concept(s)                            | v1 capacity category | Governance function                            | Integration type | Notes                                                                                                           |
| -------- | --------------------------------------------------- | --------------------- | ---------------------- | ---------------------------------------- | -------------------- | ---------------------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------- |
| CA1      | Emergency shelters per tambon                       | Coping                | Asset                  | —                                        | —                    | Emergency management / DRM infrastructure      | B                | CBI-only coping asset concept; no explicit v1 indicator concept.                                                |
| CA2      | Emergency disaster fund per 10k pop                 | Coping                | Asset                  | Emergency budget disbursement timeliness | Coping               | Public finance / contingency budgeting         | A                | CA2 provides magnitude Baseline for v1 finance concept; v1 Target remains timeliness and coverage.              |
| CA3      | Rescue equipment sets per tambon                    | Coping                | Asset                  | —                                        | —                    | Operational readiness / equipment provisioning | B                | CBI-only coping asset; complements governance-side readiness concepts.                                          |
| CA4      | Emergency medical personnel per 10k pop             | Coping                | Asset                  | —                                        | —                    | Health system surge capacity                   | B                | CBI-only health surge capacity concept; no direct v1 concept row.                                               |
| CP1      | Disaster response / evacuation plan exists          | Coping                | Process                | Plan revision cycle                      | Adaptive             | Planning / preparedness                        | A                | CP1 confirms existence of plans; v1 Target covers revision cadence.                                             |
| CP2      | Drill frequency (times/year)                        | Coping                | Process                | After-action review completion rate      | Adaptive             | Training / learning / preparedness             | A                | CP2 provides Baseline evidence of drills; v1 Target remains AAR quality.                                        |
| CP3      | Warning response time (hours)                       | Coping                | Process                | Service delivery timeliness              | Adaptive             | Early warning operations                       | A                | Treated as a timeliness-style Baseline aligned with v1 “Service delivery timeliness” concept.                   |
| CP4      | Risk communication channels (count)                 | Coping                | Process                | Community engagement frequency           | Transformative       | Public communication / outreach                | A                | CP4 quantifies communication capacity; v1 Target remains frequency + feedback loops.                            |
| AA1      | Early warning systems per district                  | Adaptive              | Asset                  | —                                        | —                    | Early warning infrastructure                   | B                | CBI-only coverage indicator; no direct v1 analogue.                                                             |
| AA2      | Recovery budget per 10k pop                         | Adaptive              | Asset                  | Emergency budget disbursement timeliness | Coping               | Public finance / recovery planning             | A                | AA2 adds recovery-budget magnitude to v1 finance concept.                                                       |
| AA3      | Disaster insurance coverage (%)                     | Adaptive              | Asset                  | —                                        | —                    | Risk transfer / financial protection           | C                | Context-only indicator; excluded from core capacity index to avoid conflating resilience with wealth.           |
| AA4      | Protective infrastructure (km per risk area)        | Adaptive              | Asset                  | —                                        | —                    | Structural risk reduction / DRR                | B                | CBI-only structural protection measure; no v1 row.                                                              |
| AP1      | Climate adaptation plan exists                      | Adaptive              | Process                | Plan revision cycle                      | Adaptive             | Strategic planning                             | A                | AP1 gives adaptation-specific plan existence; v1 covers revision/implementation.                                |
| AP2      | Climate data integration (1–5 scale)                | Adaptive              | Process                | Policy integration score                 | Adaptive             | Knowledge integration / policy integration     | A                | AP2 operationalizes v1 policy-integration concept with a 1–5 score.                                             |
| AP3      | Community participation in planning (1–5 scale)     | Adaptive              | Process                | Community engagement frequency           | Transformative       | Participation / co-production                  | A                | AP3 refines v1 engagement concept with qualitative participation scoring.                                       |
| AP4      | Public climate literacy (%)                         | Adaptive              | Process                | —                                        | —                    | Awareness / capacity building                  | B                | New awareness-focused concept; no explicit v1 row name.                                                         |
| TA1      | Green buffer areas (% of land area)                 | Transformative        | Asset                  | —                                        | —                    | Land-use / ecosystem-based measures            | B                | Ecosystem buffer concept; no v1 indicator row.                                                                  |
| TA2      | Climate resilience investment per 10k pop           | Transformative        | Asset                  | —                                        | —                    | Capital investment / development strategy      | B                | New concept on orientation of public investment toward resilience.                                              |
| TA3      | Climate-resilient infrastructure (% of stock)       | Transformative        | Asset                  | —                                        | —                    | Infrastructure standards / retrofitting        | B                | New concept on resilience of infrastructure stock; no v1 analogue.                                              |
| TP1      | Climate-informed zoning (binary)                    | Transformative        | Process                | —                                        | —                    | Land-use governance / regulation               | B                | Transformative governance concept; v1 has related governance rows but no direct zoning concept; treated as new. |
| TP2      | Local economic transition plan (binary)             | Transformative        | Process                | —                                        | —                    | Economic restructuring / just transition       | B                | New concept; economic transition plan is not encoded as a separate v1 indicator.                                |
| TP3      | Climate innovation adoption (projects per province) | Transformative        | Process                | —                                        | —                    | Innovation / experimentation                   | B                | New concept; innovation system strength not explicitly present in v1 rows.                                      |

## 2. Integration type summary

- **Type A** (Baseline proxy for existing v1 concepts):
  - CP1, CP2, CP3, CP4
  - AP1, AP2, AP3
  - CA2, AA2

- **Type B** (new concept groups with no direct v1 parent):
  - CA1, CA3, CA4
  - AA1, AA4
  - AP4
  - TA1, TA2, TA3
  - TP1, TP2, TP3

- **Type C** (context-only):
  - AA3

This crosswalk ensures that CBI indicators are fitted into existing v1 concept categories wherever there is a clear conceptual match, and that indicators without a v1 parent are explicitly marked as new CBI-driven concept groups or as contextual only.

