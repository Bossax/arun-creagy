---
type: experiment_evidence_log
status: completed
experiment: B
created: 2026-04-24
last_updated: 2026-04-24
project:
  - DCCE_CRI
title: Experiment B Evidence-Decision Log
---

# Experiment B Evidence-Decision Log

| decision_id | source_used | claim_extracted | reason_for_reuse_or_addition | affected_asset_concepts | status_after_pruning |
|---|---|---|---|---|---|
| B-E01 | AS-1 McPhearson 2022; AS-1 Sharifi 2023 | Urban green, green roofs, public green-space access, and hybrid drainage features deliver cooling and stormwater benefits only when maintenance, stewardship, and local management are continuous | Reuse existing v3 kernel with interpretation notes because activation conditions still map to planning, finance, coordination, service, and data functions already in the six-pillar structure | HC-01; HC-02 | Keep as reuse |
| B-E02 | AS-2a IPCC 2022 | Coastal protection works, accommodation measures, and healthy coastal socioecological systems depend on regulatory provisions, dedicated finance, and integrated multi-level coastal governance | Reuse existing kernel because literature points to cross-pillar activation conditions, not a distinct new governance family | HC-03; HC-04 | Keep as reuse |
| B-E03 | AS-2b Feldmeyer 2019; AS-1 Sharifi 2023 | Ventilation status, unsealed ground, conservation areas, and adapted urban ecological form are governed through plans, heat strategies, inter-office climate coordination, and diagnostics | Resolve Round 1 gap through combination of existing planning, coordination, service, and data concepts rather than admit a new corridor-governance concept | HC-05 | Keep as merge-to-kernel |
| B-E04 | AS-1 Sharifi 2023 | Thermal safety depends on building design, inclusive public cooling access, resilience hubs, clear planning goals, targeted outreach, and implementation capacity | Resolve built-form/public-realm gap through kernel combination; no new concept admitted because inclusion and service translation can be carried by existing pillars | HC-06 | Keep as merge-to-kernel |
| B-E05 | AS-1 Kim 2022; AS-2b Zeng 2022 | Robustness, redundancy, flexibility, decentralization, and polycentric operations are infrastructure properties that require renewal criteria, finance, operations, monitoring, and coordination to become real service continuity | Resolve architecture and network gaps with existing concepts combined; reject stand-alone resilience-architecture or interoperability concepts | HC-07; HC-08 | Keep as merge-to-kernel |
| B-E06 | AS-1 McPhearson 2022; AS-1 Sharifi 2023; `2026-04-24_notebooklm-targeted-gap-check_raw.md`; `2026-04-24_perplexity-ask-raw.md` | Food-system stock depends on local policies, property rights, community stewardship, collective/traditional knowledge, and city-region governance; web corroboration still flagged only partial fit in the six formal categories | Admit a provisional concept in Round 2 because the kernel combination under-read informal stewardship and land-access governance pressures specific to HC-09 | HC-09 | Merged into surviving overlay |
| B-E07 | AS-3 Sharifi & Yamagata 2016; AS-3 IMF 2021 | Savings, contingency funds, insurance, grants, guarantees, and development-bank style supports only buffer risk if translated into accessible uptake pathways and targeted delivery | Resolve uptake/translation problem with finance + service delivery + coordination + data combination; no new concept admitted | HC-10 | Keep as merge-to-kernel |
| B-E08 | AS-3 Sharifi & Yamagata 2016; AS-3 World Bank 2024; `2026-04-24_notebooklm-targeted-gap-check_raw.md`; `2026-04-24_perplexity-ask-raw.md` | Skills, literacy, connectedness, collective assets, and social capital become effective only when groups can self-organize and sustain reciprocal collective action; web corroboration suggested much of this still fits existing categories | Admit a provisional Round 2 concept because NotebookLM showed a meaningful residual gap, but mark it explicitly for pruning review because stand-alone survival was uncertain | HC-11 | Merged into surviving overlay |
| B-E09 | `2026-04-24_notebooklm-pruning-review_raw.md` | NotebookLM pruning review found strongest support for merging stewardship/traditional knowledge and self-organization/social capital into one integrated community-capacity function rather than keeping two separate additions | Use pruning evidence to collapse two provisional concepts into one narrower overlay concept and avoid concept inflation | HC-09; HC-11 | Keep as surviving thin-overlay addition |
| B-E10 | `2026-04-24_perplexity-ask-raw.md` | Perplexity corroborated partial non-fit for food-system stock (`land tenure reform`) but judged human/social capability stock largely representable within existing categories | Use this mixed web-grounded signal to narrow the surviving concept aggressively: keep one thin overlay only, not a new seventh pillar and not two separate concepts | HC-09; HC-11 | Keep as narrowed addition |
