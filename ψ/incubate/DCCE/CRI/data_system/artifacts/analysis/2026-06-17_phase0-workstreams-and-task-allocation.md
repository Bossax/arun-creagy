# Phase 0 — Workstreams and Task Allocation Ground Truth

## Purpose

This file defines the complete workstreams that Orchestrator mode must allocate into subtasks for Phase 0.

It is paired with [`2026-06-17_phase0-decisions-freeze_ground-truth.md`](./2026-06-17_phase0-decisions-freeze_ground-truth.md).

---

## Workstream 1 — Analytical Definition Freeze

### Goal

Freeze the exact meaning of every metric used by the app.

### Required outputs

- metric dictionary
- period-definition matrix
- denominator and scaling table
- geography/grain table

### Subtask scope

The subtask must define, for each metric:

- display name
- internal metric key
- numerator
- denominator
- multiplier/scaling
- period logic for `2560–2567 average`
- period logic for `2567 only`
- geography level
- source family
- ranking grain

### Mandatory metrics

- `deaths_abs`
- `deaths_rate`
- `affected_hh_abs`
- `affected_rate`
- `loss_abs`
- `loss_per_gpp`
- `cri_score`
- tambon deaths
- tambon affected households
- heat deaths
- heat injured

---

## Workstream 2 — Data Lineage and Client-Facing Methodology Freeze

### Goal

Separate engineering lineage from client-safe methodology content.

### Required outputs

- internal source-lineage summary
- public methodology-content structure
- limitations register

### Subtask scope

The subtask must produce a structure for explaining:

- what datasets are used
- who owns them
- original forms of the data
- temporal coverage
- why household denominator is used for affected rate
- what limitations must be disclosed

### Hard constraint

No internal filenames or paths in the public narrative.

---

## Workstream 3 — Frontend Data Contract Freeze

### Goal

Freeze the file structure and schema the frontend will consume.

### Required outputs

- manifest schema
- metric-file schema
- heat-file schema
- ranking-table schema
- geometry file strategy

### Subtask scope

The subtask must decide:

- whether rankings are embedded or derived
- shared fields across all metric JSON files
- folder structure by period and metric
- naming for province and tambon geometry assets

### Minimum recommended package layout

- `manifest.json`
- `period_2560_2567/*.json`
- `period_2567/*.json`
- `spatial/province_boundaries.*`
- `spatial/tambon/<province_code>.*`

---

## Workstream 4 — UI Information Architecture Freeze

### Goal

Freeze app structure, navigation, and screen-level responsibilities.

### Required outputs

- screen map
- component map
- tab responsibilities
- control-state model

### Subtask scope

The subtask must define:

- landing page structure
- global time selector behavior
- CRI tab layout
- tambon tab layout
- heat tab layout
- province zoom behavior
- table behavior under each map

### Design requirement

The interface must align with [`coral-stay-DESIGN.md`](../../../../../../memory/resonance/coral-stay-DESIGN.md:40).

---

## Workstream 5 — Technical Architecture Freeze

### Goal

Freeze the implementation architecture before coding starts.

### Required outputs

- stack decision note
- map library choice rationale
- deployment model rationale
- geometry loading strategy
- performance-risk assumptions

### Subtask scope

The subtask must explicitly test and decide:

- Next.js suitability
- Vercel suitability
- MapLibre vs Leaflet
- lazy-loading plan for tambon assets
- build-time vs runtime data loading

---

## Workstream 6 — Implementation Sequence Freeze

### Goal

Define the post-Phase-0 execution order so implementation does not start in the wrong sequence.

### Required outputs

- phased roadmap
- dependency chain across work packages
- blockers and prerequisites table

### Subtask scope

The subtask must sequence:

1. data export build
2. frontend shell
3. methodology page
4. CRI tab
5. tambon tab
6. heat tab
7. deployment hardening

---

## Suggested Orchestrator allocation

### Subtask A — Analyst

Owns:

- Workstream 1
- analytical consistency check for Workstream 2

### Subtask B — Architect

Owns:

- Workstream 3
- Workstream 5

### Subtask C — Architect / UX

Owns:

- Workstream 4

### Subtask D — Ask / Documentation

Owns:

- public methodology structure in Workstream 2

### Subtask E — Orchestrator synthesis

Owns:

- Workstream 6
- integration of all workstreams into one approved Phase 0 packet

---

## Review gates by workstream

### Gate for Workstream 1

Must reflect household denominator logic from [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb:237).

### Gate for Workstream 2

Must not leak internal filenames in the public methodology structure.

### Gate for Workstream 3

Must support both `2560–2567 average` and `2567 only` for every metric file.

### Gate for Workstream 4

Must include two separate heat maps: deaths and injured.

### Gate for Workstream 5

Must constrain tambon geometry loading.

### Gate for Workstream 6

Must not schedule app implementation before analytical definitions and data contract are frozen.

---

## Instruction to Orchestrator mode

Allocate subtasks so that every workstream above is covered exactly once and synthesized back into one Phase 0 review package.
