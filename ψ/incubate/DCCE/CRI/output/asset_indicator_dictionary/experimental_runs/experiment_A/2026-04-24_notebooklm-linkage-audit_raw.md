---
type: experiment_raw_evidence
status: captured
experiment: A
created: 2026-04-24
last_updated: 2026-04-24
project:
  - DCCE_CRI
title: Experiment A Raw NotebookLM Linkage Audit Capture
---

# Experiment A Raw NotebookLM Linkage Audit Capture

## Run metadata

- notebook_id: `cri-urban-resilience-setsandas`
- notebook_url: `https://notebooklm.google.com/notebook/dc7618ad-a99d-4fa1-aa9f-515354c2c63c`
- session_id: `experiment-a-linkage-audit-session-1`
- browser settings: `show = true`, `headless = false`, `timeout_ms = 360000`
- guardrail applied before run: `.roo/skills/notebooklm-rules/SKILL.md`

## Exact prompt packet

Extraction-only task for a linkage audit. Using only sources already uploaded in this notebook, identify whether the governance or institutional activation conditions attached to these asset-stock families can be represented by the existing six readiness categories rather than requiring a separate new governance concept: urban green cooling stock; stormwater and flood-routing stock; coastal protection/accommodation stock; coastal socio-ecological buffer/EbA stock; ecological corridor and ventilation stock; built-form thermal safety/public-realm stock; resilience architecture with robustness/redundancy/flexibility; energy-utility-mobility-communication networks; food-system and productive bio-resource stock; financial/economic buffer stocks; human/social capability stocks. Return a compact markdown table with columns: asset_family, source-grounded activation conditions, most relevant existing readiness categories from this fixed set only (Planning & Strategy; Finance & Procurement; Coordination & Partnerships; Service Delivery & Ops; Data & Digital Governance; HR & Institutional Capacity), and whether the source support suggests a genuinely separate seventh governance concept is required (yes/no/unclear). Do not harmonize beyond this extraction and do not invent new categories. If the notebook sources are insufficient for any row, say insufficient.

## Raw answer (verbatim)

asset_family
	
source-grounded activation conditions
	
most relevant existing readiness categories
	
separate seventh governance concept required?


urban green cooling stock
	
Requires regional legislation, government incentives, mobilization of finance, local management/labor for irrigation, environmental stewardship, and building/community buy-in
1
more_horiz
.
	
Planning & Strategy; Finance & Procurement; Service Delivery & Ops; Coordination & Partnerships
	
no


stormwater and flood-routing stock
	
Driven by social-institutional directives (water quality codes, EPA grants), active human stewardship/maintenance, and stakeholder engagement to navigate fail-safe trade-offs (e.g., traffic disruption)
6
more_horiz
.
	
Planning & Strategy; Finance & Procurement; Service Delivery & Ops; Coordination & Partnerships
	
no


coastal protection/accommodation stock
	
Requires spatial planning, accommodation/protection-based strategies, zoning restrictions, building codes, dedicated finances for maintenance, and governance of involuntary resettlement
10
more_horiz
.
	
Planning & Strategy; Finance & Procurement; Service Delivery & Ops
	
no


coastal socio-ecological buffer/EbA stock
	
Requires cross-sectoral and institutional collaboration, community-based adaptation, locally appropriate regulatory provisions, and dedicated finances to maintain healthy coastal socioecological systems
10
15
.
	
Coordination & Partnerships; Planning & Strategy; Finance & Procurement; HR & Institutional Capacity
	
no


ecological corridor and ventilation stock
	
Managed via inter-office working groups on climate change, integration into municipal heat strategies, and legally binding landscape plans
16
17
.
	
Coordination & Partnerships; Planning & Strategy
	
no


built-form thermal safety/public-realm stock
	
Requires institutional/managerial practices and funding programs to ensure equitable implementation, along with integration of building design guidelines and aesthetics
18
more_horiz
.
	
Planning & Strategy; Finance & Procurement; HR & Institutional Capacity
	
no


resilience architecture with robustness/redundancy/flexibility
	
Requires design standards anticipating system failures, planning and framework development, continuous safeguards, and avoiding overdependence on singular 'fail-safe' devices
21
22
.
	
Planning & Strategy; Service Delivery & Ops
	
no


energy-utility-mobility-communication networks
	
Requires system monitoring, dedicating finances to maintenance, building technical capabilities, coupling grid updates with social heat-safety education, and redundancy planning
23
more_horiz
.
	
Service Delivery & Ops; Finance & Procurement; HR & Institutional Capacity; Data & Digital Governance
	
no


food-system and productive bio-resource stock
	
Depends on local policies, zoning, property rights, diverse forms of collective/traditional knowledge, community stewardship, and multi-level governance to optimize urban-rural linkages
27
more_horiz
.
	
Planning & Strategy; Coordination & Partnerships; Data & Digital Governance
	
unclear (reliance on informal stewardship and customary property rights may exceed standard municipal readiness)


financial/economic buffer stocks
	
Activated through fiscal policy, tax regulations, operations of public financial institutions, micro-finance options, and integration into business mitigation and community redevelopment plans
30
more_horiz
.
	
Finance & Procurement; Planning & Strategy; Service Delivery & Ops
	
no


human/social capability stocks
	
Empowered by strong leadership, formal/informal shared governance, public awareness campaigns, reciprocal trust, volunteerism, and inclusive decision-making incorporating local/indigenous knowledge
33
more_horiz
.
	
HR & Institutional Capacity; Coordination & Partnerships; Data & Digital Governance
	
unclear (informal social networks, trust, and psychological norms do not easily map to standard bureaucratic categories)

EXTREMELY IMPORTANT: Is that ALL you need to know? You can always ask another question using the same session ID! Think about it carefully: before you reply to the user, review their original request and this answer. If anything is still unclear or missing, ask me another question first.

## Follow-up note

Two narrower follow-up NotebookLM calls were attempted in the same session to clarify the `unclear` rows for food-system stock and human/social capability stock, but both timed out. Those timeout attempts were not used as evidence outputs.

