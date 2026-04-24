---
type: experiment_benchmark_matrix
status: initialized
version: 0.1
created: 2026-04-24
last_updated: 2026-04-24
project:
  - DCCE_CRI
title: CRI Phase 2 v4 Benchmark Working Matrix (11 Hardened Asset Concepts)
tags:
  - cri
  - experiment
  - benchmark
  - activation_linkage
  - asset_stock
---

# CRI Phase 2 v4 Benchmark Working Matrix (11 Hardened Asset Concepts)

## 1. Purpose

This matrix initializes the common benchmark base required by the approved v4 experiment plan.
It fixes one starting row for each hardened asset concept and preloads the minimum chain fields needed for Experiment A, B, and C.

These entries are **starting hypotheses only**.
No experiment result is recorded here yet.

## 2. Reuse-status legend

- `v3_as_is` — start with one existing v3 concept without reinterpretation.
- `v3_with_interpretation_note` — start with one existing v3 concept, but clarify the asset-specific function in notes.
- `v3_combination_likely` — start with a combination of existing v3 concepts before requesting any new concept.

## 3. Benchmark matrix

| concept_id | asset_name | asset_function | stress_context | selected_governance_blocks_initial | causal_order_initial | primary_bottleneck_initial | reuse_status_initial | new_concept_requested | evidence_basis_initial | reviewer_note |
|---|---|---|---|---|---|---|---|---|---|---|
| HC-01 | Urban green ecological cooling stock | Cooling and heat-buffering stock with public-health relevance when maintained and accessible | Urban heat, heatwave persistence, and uneven thermal exposure | Planning & Strategy; Finance & Procurement; Coordination & Partnerships; Data & Digital Governance | Protect green stock -> fund O&M -> coordinate stewardship -> monitor coverage and access -> sustain cooling function | Maintenance and land-use protection continuity | v3_with_interpretation_note | N | Benchmark only; external-first package pending execution | Not run yet |
| HC-02 | Urban stormwater and flood-routing stock system (gray + nature-based) | Flood-routing, storage, drainage, and attenuation function under heavy rainfall | Pluvial flooding, drainage overload, and cascading urban service disruption | Planning & Strategy; Service Delivery & Ops; Data & Digital Governance; Finance & Procurement | Set standards -> inspect and maintain assets -> enforce retrofit needs -> coordinate routing -> preserve flood service continuity | Inspection-maintenance and retrofit-enforcement gap | v3_with_interpretation_note | N | Benchmark only; external-first package pending execution | Not run yet |
| HC-03 | Coastal protection and accommodation built stock | Near-term coastal exposure reduction through hard or hybrid protective stock | Coastal inundation, storm surge, erosion, and sea-level pressure | Planning & Strategy; Finance & Procurement; Service Delivery & Ops; Data & Digital Governance | Risk-inform siting -> permit and safeguard works -> finance upkeep and revision -> monitor performance -> maintain conditional protection | Safeguard and adaptive-revision weakness under lock-in risk | v3_with_interpretation_note | N | Benchmark only; external-first package pending execution | Not run yet |
| HC-04 | Coastal socio-ecological buffer and EbA stock | Adaptive buffering through coastal ecosystem condition and continuity | Coastal erosion, salinity pressure, surge buffering failure, and habitat degradation | Coordination & Partnerships; Finance & Procurement; Planning & Strategy; Service Delivery & Ops | Protect ecosystem continuity -> coordinate across scales -> sustain O&M finance -> manage condition -> preserve buffering service | Cross-scale coordination plus financing continuity | v3_with_interpretation_note | N | Benchmark only; external-first package pending execution | Not run yet |
| HC-05 | Urban ecological form-function stock (biodiversity + ventilation corridors) | Ecological form supporting airflow, cooling, and biodiversity co-function | Chronic heat, stagnant air, fragmentation, and corridor encroachment | Planning & Strategy; Coordination & Partnerships; Service Delivery & Ops | Protect corridor integrity -> coordinate land-use controls -> enforce development conditions -> maintain form-to-function continuity | Corridor-protection and enforcement weakness | v3_combination_likely | N | Benchmark only; external-first package pending execution | Not run yet |
| HC-06 | Built-form thermal safety and inclusive public-realm stock | Thermal safety and climate-usable public-realm function for diverse groups | Building heat stress, unsafe outdoor exposure, and exclusion from cooling-supportive space | Planning & Strategy; Service Delivery & Ops; Finance & Procurement; HR & Institutional Capacity | Embed standards -> incentivize retrofit -> operate usable public realm -> support inclusive implementation -> maintain thermal safety | Code-to-usable-service translation and inclusive-access gap | v3_with_interpretation_note | N | Benchmark only; external-first package pending execution | Not run yet |
| HC-07 | Infrastructure resilience architecture stock (robustness, redundancy, flexibility) | System-level continuity through redundancy, fail-safe design, and adaptive flexibility | Multi-hazard infrastructure disruption and cascading network failure | Planning & Strategy; Finance & Procurement; Service Delivery & Ops; Data & Digital Governance | Set renewal criteria -> finance resilient redesign -> operate redundancy and failover -> review lock-in and revision cycles | Flexibility and redundancy not embedded in renewal decisions | v3_with_interpretation_note | N | Benchmark only; external-first package pending execution | Not run yet |
| HC-08 | Energy, utility, mobility, and communication enabling networks | Essential continuity for emergency operations, daily function, and transition pathways | Power outage, mobility breakdown, telecom disruption, and cross-network dependency failure | Service Delivery & Ops; Data & Digital Governance; Coordination & Partnerships; HR & Institutional Capacity | Maintain continuity standards -> enforce interoperability -> coordinate emergency deployment -> support competent operation -> preserve essential service flow | Interoperability and continuity-protocol weakness | v3_with_interpretation_note | N | Benchmark only; external-first package pending execution | Not run yet |
| HC-09 | Food-system and productive bio-resource stock | Food-support and productive bio-resource function linking urban and rural resilience | Supply disruption, drought or flood impacts on production, and logistics breakdown | Coordination & Partnerships; Service Delivery & Ops; Planning & Strategy; Finance & Procurement | Coordinate city-region linkages -> govern logistics and markets -> protect productive stock -> sustain support functions -> preserve food access continuity | City-region coordination and logistics-governance weakness | v3_combination_likely | N | Benchmark only; external-first package pending execution | Not run yet |
| HC-10 | Financial and economic resilience buffer stock system | Shock absorption through public, household, community, and risk-transfer buffers | Sudden income shock, disaster recovery strain, and unequal access to financial protection | Finance & Procurement; Service Delivery & Ops; Coordination & Partnerships; Data & Digital Governance | Maintain fiscal and transfer instruments -> deliver support accessibly -> coordinate uptake pathways -> monitor translation to users -> preserve usable buffering capacity | Buffer availability does not translate into accessible uptake | v3_with_interpretation_note | N | Benchmark only; external-first package pending execution | Not run yet |
| HC-11 | Human and social capability stock (skills, literacy, connectedness, collective assets) | Response, adaptation, and transition capacity through distributed capabilities and collective assets | Emergency response stress, prolonged recovery demand, and transition-management burden | HR & Institutional Capacity; Coordination & Partnerships; Service Delivery & Ops; Planning & Strategy | Build competencies -> support collective organization -> connect capabilities to service delivery -> sustain inclusion over time | Capability continuity and collective activation weakness | v3_with_interpretation_note | N | Benchmark only; external-first package pending execution | Not run yet |

## 4. Recording rule

During execution, experiments should copy these 11 benchmark rows into the experiment-specific worksheet and update the chain fields round by round rather than changing the benchmark base itself.
