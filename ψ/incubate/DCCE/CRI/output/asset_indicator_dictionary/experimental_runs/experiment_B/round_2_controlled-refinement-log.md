---
type: experiment_round_log
status: completed
experiment: B
round: 2
created: 2026-04-24
last_updated: 2026-04-24
project:
  - DCCE_CRI
title: Experiment B Round 2 Controlled-Refinement Log
---

# Experiment B Round 2 Controlled-Refinement Log

## Scope

Allow limited expansion while preserving kernel integrity, after testing existing-concept combinations first.

## Status

Completed.

## Round summary

- Failure points reviewed: 7
- Existing-concept combinations tested: 7
- Provisional new concepts admitted: 2
- Main conclusion: five Round 1 gaps were solved by controlled combination of existing v3 concepts plus interpretation notes; two community-mediated gaps cleared the medium-high evidence bar for provisional admission under Experiment B controls
- Corroboration note: the targeted NotebookLM follow-up returned `yes` for provisional concept pressure in HC-09 and HC-11, while the successful [`perplexity_ask()`](mcp--perplexity--perplexity_ask:1) retry supported only partial non-fit for HC-09 and stronger fold-back pressure for HC-11, setting up Round 3 pruning and merge review

| gap_id | affected_asset_concepts | failure_point_from_round_1 | existing-concept combination tested | decision | evidence basis | note |
|---|---|---|---|---|---|---|
| B-R2-01 | HC-05 | Corridor integrity and ecological function were not readable through one reused concept | Risk-informed planning + Policy Integration + Formal coordination bodies + Risk Assessment depth | Resolved by kernel combination | AS-2b Feldmeyer 2019; AS-1 Sharifi 2023 | No new corridor-governance concept admitted |
| B-R2-02 | HC-06 | Thermal safety and inclusive public-realm usability required more than code language alone | Risk-informed planning + Service delivery timeliness + Resource allocation scale + Emergency staff capacity / Staff Training frequency | Resolved by kernel combination | AS-1 Sharifi 2023 | Inclusion handled as cross-pillar activation burden, not a new concept |
| B-R2-03 | HC-07 | Robustness alone under-read flexibility and redundancy in renewal logic | Risk-informed planning + Resource allocation scale + Infrastructure robustness + Risk Assessment depth | Resolved by kernel combination | AS-1 Kim 2022; AS-2b Zeng 2022 | No separate resilience-architecture governance concept admitted |
| B-R2-04 | HC-08 | Interoperability and continuity protocols spanned multiple operating functions | Infrastructure robustness + Data interoperability + Digital climate services + Multi-stakeholder collab. + Emergency staff capacity | Resolved by kernel combination | AS-1 Kim 2022; AS-2b Zeng 2022 | No stand-alone interoperability concept admitted |
| B-R2-05 | HC-09 | Food-system activation still under-read informal stewardship, customary rights, and traditional knowledge after kernel combination | Multi-stakeholder collab. + Formal coordination bodies + Service delivery timeliness + Resource allocation scale | Provisional concept admitted: Community Stewardship & Traditional Knowledge Governance | AS-1 McPhearson 2022; AS-1 Sharifi 2023; `2026-04-24_notebooklm-targeted-gap-check_raw.md`; `2026-04-24_perplexity-ask-raw.md` | Existing kernel carried formal coordination but did not fully capture informal community stewardship and land-access logic |
| B-R2-06 | HC-10 | Buffer stock availability did not automatically imply accessible uptake | Emergency budget flow + Resource allocation scale + Service delivery timeliness + Data interoperability + Multi-stakeholder collab. | Resolved by kernel combination | AS-3 Sharifi & Yamagata 2016; AS-3 IMF 2021 | Uptake/translation kept as linkage note, not a new concept |
| B-R2-07 | HC-11 | Skills and connectedness required durable collective mobilization logic beyond formal staffing language | Emergency staff capacity + Staff Training frequency + Multi-stakeholder collab. + Formal coordination bodies + Service delivery timeliness | Provisional concept admitted: Grassroots Self-Organization & Social Capital | AS-3 Sharifi & Yamagata 2016; AS-3 World Bank 2024; `2026-04-24_notebooklm-targeted-gap-check_raw.md`; `2026-04-24_perplexity-ask-raw.md` | NotebookLM supported provisional admission, but web corroboration suggested this concept might be weaker as a stand-alone addition and should face pruning review |
