---
type: knowledge_artifact
status: current
version: 1
created: 2026-02-19
project:
  - DCCE_CRI
title: CRI Phase 2 Capacity Tagging Dictionary
sticker: emoji//1f351
---

# CRI Phase 2 Capacity Tagging Dictionary

## Purpose

Provide a transparent, literature-backed tagging dictionary for classifying municipal indicators into Coping, Adaptive, and Transformative capacity tiers. This dictionary prioritizes **process indicators** tied to administrative events and reduces subjectivity through explicit rules and definitions.

## Scope

- Municipal urban resilience and governance indicators
- Administrative data and process metrics where possible
- Supports CRI Phase 2 capacity profiling

## Sources used

- [`Case studies of urban resilience indicators.md`](../sources/Case%20studies%20of%20urban%20resilience%20indicators.md)
- [`Process-based indicators for urban resilience - consensus.ai.md`](../sources/Process-based%20indicators%20for%20urban%20resilience%20-%20consensus.ai.md)

## Tagging rules (v1)

1. Prefer **process indicators** tied to administrative events (plan revisions, procurement cycles, coordination meetings).
2. Use **mandate-aligned naming** where possible (indicator names reflect legal duties or official KPIs).
3. Allow **readiness modifiers** (e.g., feasibility or governance-readiness factors) as cross-cutting tags rather than core capacity indicators.
4. Distinguish **process vs stock** explicitly to reduce subjectivity; treat stock indicators as supporting context only.
5. If a single indicator spans multiple functions, assign the **primary governance function** and document secondary linkages in notes.

## Capacity tier definitions (operational)

- **Coping:** Immediate response and stabilization capacity; short-term emergency management and relief.
- **Adaptive:** Medium-term adjustment and learning; planning, resource allocation, and iterative improvement.
- **Transformative:** Structural reform and system change; cross-sector integration, governance redesign, and long-term strategic shifts.

## Nominal indicator long-list (v1)

| Indicator (nominal)                      | Definition / signal                                                        | Capacity tier  | Governance function           | Process vs stock | Evidence anchor                                                                                 |
| ---------------------------------------- | -------------------------------------------------------------------------- | -------------- | ----------------------------- | ---------------- | ----------------------------------------------------------------------------------------------- |
| Plan revision cycle                      | Months since last update of climate or DRM plan                            | Adaptive       | Planning                      | Process          | City Resilience Framework – Resilient Cities Network                                            |
| After-action review completion rate      | % of major events with completed after-action reports within set timeframe | Adaptive       | Learning / accountability     | Process          | Feldmeyer et al. 2019. Indicators for Monitoring Urban Climate Change Resilience and Adaptation |
| Cross-department coordination meetings   | Number of formal inter-agency coordination meetings per year               | Adaptive       | Coordination                  | Process          | Institutionalizing Urban Resilience – Urban.org                                                 |
| Emergency budget disbursement timeliness | Average days to disburse emergency funds after event                       | Coping         | Finance / response            | Process          | Goonesekera & Olazabal 2022. Climate adaptation indicators and metrics                          |
| Emergency procurement cycle time         | Average days from request to contract award for response projects          | Coping         | Procurement / response        | Process          | Kenney & Gerst 2021. Synthesis of indicators, datasets, and frameworks                          |
| Climate budget tagging coverage          | % of municipal budget items tagged as climate-related                      | Adaptive       | Finance / accountability      | Process          | Climate Change Expenditure Tagging – NICCDIES                                                   |
| Service delivery timeliness              | Median processing time for core municipal services                         | Adaptive       | Service delivery              | Process          | Serdar et al. 2021. Urban Transportation Networks Resilience                                    |
| Case throughput rate                     | Resolved cases per staff per period in key departments                     | Adaptive       | Operations                    | Process          | Serdar et al. 2021. Urban Transportation Networks Resilience                                    |
| Governance readiness modifier            | Feasibility-adjusted score for institutional capacity to deliver options   | Transformative | Institutional feasibility     | Modifier         | Integrative Decision-Making Framework for Sustainable Urban Development (MDPI 2026)             |
| Formal coordination mechanism            | Existence + activation frequency of CRO or inter-agency taskforce          | Transformative | Governance reform             | Process          | Institutionalizing Urban Resilience – Urban.org                                                 |
| Performance dashboard coverage           | Public KPI dashboard with context + equity sections                        | Transformative | Transparency / accountability | Process          | 8 Local Government Public Dashboard Examples – Envisio                                          |
| Data interoperability score              | % of datasets compliant with shared metadata standards                     | Transformative | Data governance               | Process          | Prioritizing Core Data Sets for Smart City Governance: Evidence (MDPI)                          |
| Policy integration score                 | Share of sector plans explicitly integrating climate resilience            | Adaptive       | Policy integration            | Process          | Kauffman & Hill 2021. Climate Change, Adaptation Planning and Institutional Integration         |
| Community engagement frequency           | Number of documented participatory engagements per year                    | Transformative | Inclusion / legitimacy        | Process          | Inclusive engagement for equitable resilience: community case study insights                    |

## Notes on use

- Use this dictionary as the **baseline** for tagging LPA and other administrative indicators.
- Where only binary indicators exist, prefer **composite aggregation** but document the process vs stock limitation.
- If a candidate indicator is purely asset-based, retain it as **context only** unless no process proxy exists.
