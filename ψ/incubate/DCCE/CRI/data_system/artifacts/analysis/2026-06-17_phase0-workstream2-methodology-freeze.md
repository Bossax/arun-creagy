# Workstream 2 — Data Lineage and Client-Facing Methodology Freeze

## Status

Executed as an internal and client-safe methodology baseline for the CRI Impact Index web app.

This artifact is derived from the Phase 0 decisions in [`2026-06-17_phase0-decisions-freeze_ground-truth.md`](./2026-06-17_phase0-decisions-freeze_ground-truth.md) and the current analytical baseline in [`cri_phase_1_demo.ipynb`](../../script/analysis_notebooks/cri_phase_1_demo.ipynb:1).

---

## 1. Purpose

Workstream 2 separates:

1. the **internal engineering lineage** needed to trust the app
2. the **client-facing methodology narrative** shown on the landing page

The public methodology must explain what the app does without exposing internal file names, pipeline paths, or implementation shortcuts.

---

## 2. Internal lineage summary by dataset family

### 2.1 DDPM human impacts

**Role in the app**
- Provider of deaths and affected-household impacts for province and tambon views.

**Lineage summary**
- The aggregate analytical fact table supports 2560–2567 average logic.
- The yearly fact table supports clean year-specific slicing, including 2567.
- The yearly fact is required for the `2567 only` mode.

**Key caveat**
- The aggregate file is not a yearly slice; it is a period-level rollup.

### 2.2 Population denominators

**Role in the app**
- Denominator for death rate.

**Lineage summary**
- Population is available as annual long-form records.
- The yearly structure supports both average-period and 2567-only modes.

### 2.3 Household denominators

**Role in the app**
- Denominator for affected-household rate.

**Lineage summary**
- Household data is available as annual long-form records.
- The app can use both an 8-year average household denominator for `2560–2567 average` and a year-specific household denominator for `2567 only`.
- The denominator policy is now frozen to households rather than population.

**Reason for inclusion**
- The affected metric is an impact-on-households indicator, so the denominator must remain household-based for conceptual purity.

### 2.4 GPP denominators

**Role in the app**
- Denominator for loss per unit GPP.

**Lineage summary**
- GPP is available in annual long-form structure.
- The yearly slice supports both time modes.

### 2.5 Government advance payment / economic loss

**Role in the app**
- Numerical basis for economic-loss metrics.

**Lineage summary**
- Annual-long records support both 2560–2567 averaging and 2567-only extraction.
- The period-total companion is aggregate-only and is not used for single-year slicing.

### 2.6 Heatwave source

**Role in the app**
- Feeds the heat tab.

**Lineage summary**
- The source supports a multi-year aggregate heat view and a dedicated 2567 slice.
- The app must expose two separate heat maps:
  1. heat deaths
  2. heat injured

---

## 3. Client-facing methodology content structure

The landing page methodology section must be authored as a narrative, not as a file dump.

### 3.1 Required sections

1. **What the CRI Impact Index is**
2. **How the score is calculated**
3. **What the indicators measure**
4. **What data sources are used**
5. **Who owns the data**
6. **What the time-period selector means**
7. **What the app includes**
8. **Known limitations and interpretation cautions**

### 3.2 Public wording rules

The public methodology must:

- describe source types in plain language
- describe temporal coverage in human terms
- explain why household denominator is used for affected rate
- explain that the app supports both 2560–2567 average and 2567 only
- explain that heat is shown as two separate views: deaths and injured

The public methodology must not:

- mention internal file names
- mention folder paths
- mention export scripts
- mention implementation shortcuts or temporary assumptions

---

## 4. Public data-source narrative blueprint

This is the narrative blueprint the methodology page should use.

### 4.1 Disaster impact data

Describe as:

- official disaster-impact records used to measure deaths and household impact
- available across the study period
- used at province and tambon scales depending on the view

### 4.2 Population data

Describe as:

- official demographic denominator data
- used only to normalize death rates

### 4.3 Household data

Describe as:

- official household denominator data
- used only to normalize affected-household rates
- available both as a multi-year average view and as a `2567 only` annual slice

### 4.4 Economic-loss data

Describe as:

- official relief or payment-based economic-loss records
- used to estimate the economic burden of hazards

### 4.5 GPP data

Describe as:

- official provincial productivity data
- used to scale economic loss against economic output

### 4.6 Heat data

Describe as:

- heat-related health impact data
- shown as deaths and injured
- available as a multi-year aggregate and a 2567-only slice

---

## 5. Required limitations register

The methodology page must disclose the following limitations:

1. **Affected-household choice**
   - The app uses affected households rather than affected people in the main affected metric because the household measure is the stabilized reporting unit.

2. **Period interpretation**
   - `2560–2567 average` is a multi-year view.
   - `2567 only` is a single-year view.
   - The two should not be compared as if they were identical statistical objects.

3. **Heat coverage limitation**
   - Heat metrics are not uniformly available for the full historical span used by the DDPM view.

4. **Geographic granularity limitation**
   - Tambon detail is available only in the human-impact tab and may be constrained by map performance.

5. **Interpretation caution**
   - The CRI score is a normalized composite index, not a raw measurement.

---

## 6. Data-ownership summary for the public page

The public methodology should identify each source family by owner class, not by technical path.

Recommended owner labels:

- **Disaster management authority** for disaster-impact inputs
- **Population/statistical authority** for demographic denominators
- **Household/statistical authority** for household denominators
- **Economic planning/statistical authority** for GPP
- **Climate-health or heat-impact authority** for heat metrics
- **Government relief/payment authority** for economic-loss inputs

If the exact owner name is to be shown publicly, it should be written in the final client voice, not in system notation.

---

## 7. What the app includes

The client-facing methodology must state that the web app includes:

1. a methodology page
2. CRI province-level maps
3. tambon-level human impact maps
4. heat impact maps
5. a time-period selector
6. ranking tables below each map

It must also state what is excluded, if needed, such as:

- raw source file downloads
- internal ETL implementation details
- unsupported years or unsupported geography layers

---

## 8. Acceptance criteria for Workstream 2

Workstream 2 is complete only when the following are true:

1. internal lineage is separated from client-safe narrative
2. public wording does not expose internal filenames or paths
3. all core datasets are described in owner/coverage/limitation terms
4. household denominator policy is represented clearly
5. heat is described as two separate maps
6. both time modes are explained in plain language

---

## 9. Next implementation dependency

The frontend data contract subtask must use this methodology freeze as the wording baseline for:

- manifest labels
- dataset descriptions
- help tooltips
- methodology page content
- ranking table labels

This document is the ground truth for the methodology workstream.
