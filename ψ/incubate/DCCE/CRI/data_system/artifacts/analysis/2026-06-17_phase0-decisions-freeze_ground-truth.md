# Phase 0 — Decisions Freeze Ground Truth

## Purpose

This file is the authoritative baseline for Orchestrator-mode task allocation for the CRI Impact Index web app.

It freezes the decisions that must be treated as ground truth before implementation begins.

---

## 1. Scope of Phase 0

Phase 0 exists to freeze:

1. hosting and deployment model
2. frontend framework and map stack
3. data packaging strategy
4. metric definitions and period logic
5. household denominator policy
6. heat tab semantics
7. UI information architecture
8. client-facing methodology constraints

Phase 0 does **not** implement the app.

---

## 2. Frozen product modes

The app must support exactly two time modes:

1. **2560–2567 average**
2. **2567 only**

No mixed-period calculations are allowed.

---

## 3. Frozen analytical definitions

### 3.1 CRI score structure

The CRI score uses a **50/50 split** between Human and Economic pillars and keeps the 6-indicator structure defined in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb:20).

Indicators:

1. `deaths_abs`
2. `deaths_rate`
3. `affected_hh_abs`
4. `affected_rate`
5. `loss_abs`
6. `loss_per_gpp`

### 3.2 Human denominator freeze

The affected-rate denominator is frozen to **households**, not population.

Ground truth from [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb:223):

- `deaths_rate = deaths_abs / population_total * 100000`
- `affected_rate = affected_hh_abs / household_total * 100`

This reflects the hardening recorded in [`12.05_cri-denominator-hardening.md`](../../../../../../memory/retrospectives/2026-06/17/12.05_cri-denominator-hardening.md:9).

### 3.3 Source-family freeze for the two time modes

For **2560–2567 average**:

- DDPM uses the aggregate human-impact logic now represented in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb:187)
- population uses annual rows averaged across the window
- household count uses annual rows averaged across the window
- GPP uses annual rows averaged across the window
- loss uses annual rows summed then converted to annual average

For **2567 only**:

- DDPM must use the yearly fact source, not the aggregate fact
- population must filter to `year_be = 2567`
- household count must filter to `year_be = 2567`
- GPP must filter to `year_be = 2567`
- loss must filter to `year_be = 2567`

### 3.4 Heat tab freeze

The heat section is frozen to **two maps**:

1. **Heat-related deaths**
2. **Heat-related injured**

This supersedes the earlier unresolved ambiguity about whether the tab should show one combined metric.

Heat maps are therefore treated as **separate metrics**, each with its own map and table.

---

## 4. Frozen hosting and application architecture

### 4.1 Hosting

Phase 1 hosting baseline:

- **Frontend**: static-first React app
- **Hosting**: Vercel free tier
- **Backend**: avoid dedicated backend in first build unless blocked by payload/performance constraints

### 4.2 Framework baseline

- **App framework**: Next.js
- **UI styling**: Tailwind CSS
- **Map library**: MapLibre GL JS unless a subtask proves Leaflet is materially better for the required polygon rendering

### 4.3 Design baseline

The visual system must follow [`coral-stay-DESIGN.md`](../../../../../../memory/resonance/coral-stay-DESIGN.md:1):

- coral as primary action color
- rounded cards and controls
- warm neutral text
- generous spacing
- sticky header behavior
- card-based presentation for map panels and tables

---

## 5. Frozen data packaging strategy

### 5.1 Packaging principle

The browser must **not** read raw analytical CSVs directly.

The app consumes precomputed artifacts only.

### 5.2 Export strategy

Ground truth packaging pattern:

- one JSON file per metric
- one copy per period mode
- one manifest/index file
- separate spatial files for province and tambon geometry

### 5.3 Spatial loading rule

- province geometry may load globally
- tambon geometry must be lazy-loaded or partitioned by province

This is a hard constraint for responsiveness.

---

## 6. Frozen UI information architecture

The landing page is the **Methodology** page, per [`2026-06-17-CRI-Impact-Index-dashboard.md`](../../../inbox_note/2026-06-17-CRI-Impact-Index-dashboard.md:17).

Main app sections:

1. Methodology
2. CRI
3. Tambon Human Impact
4. Heat

Global control:

- one shared time-period selector for `2560–2567 average` and `2567 only`

### 6.1 CRI tab

Must include:

- 6 individual CRI metric maps in grid layout
- 1 CRI score map
- table below each plot showing top 10 highest and lowest provinces

### 6.2 Tambon Human Impact tab

Must include:

- deaths map
- affected households map
- provincial boundary overlay
- province dropdown for zoom
- ranking tables that switch geography grain depending on current extent

### 6.3 Heat tab

Must include:

- heat deaths map
- heat injured map
- table below each map showing top 10 highest and lowest provinces

---

## 7. Frozen methodology-content rule

The public methodology content must **not** expose internal filenames, pipeline paths, or system implementation references.

This comes directly from [`2026-06-17-CRI-Impact-Index-dashboard.md`](../../../inbox_note/2026-06-17-CRI-Impact-Index-dashboard.md:20).

The client-facing methodology must instead describe:

- data owners
- original data forms
- temporal coverage
- indicator definitions
- known limitations
- what is included in the web app

---

## 8. Required Phase 0 outputs

Orchestrator must allocate subtasks that produce:

1. decision freeze note
2. metric dictionary and period-definition artifact
3. frontend data contract artifact
4. UI information architecture artifact
5. methodology-content architecture artifact
6. implementation sequencing artifact

---

## 9. Non-negotiable review gates

Phase 0 is incomplete until all of the following are true:

1. household denominator language is consistent everywhere
2. both time modes are defined for every screen and metric
3. heat is frozen as **two separate maps**
4. client methodology excludes internal file/path references
5. tambon spatial-loading strategy is constrained explicitly

---

## 10. Instruction to Orchestrator mode

Treat this file as the authoritative baseline for task decomposition.

Every subtask plan must align with this ground truth unless a later explicit approval supersedes it.
