# CRI Phase 1 — Data Review Checklist

Operational checklist for tracking data review and processing for the Phase 1 Impact / Fiscal Relief Index.

Use one row per item. Suggested status values: `not_started`, `in_progress`, `reviewed`, `ready_for_analysis`.

---

## Legend

- **Process**: Which workflow process this item belongs to (P1–P8 in [`plans/2026-04-02_cri-phase1-data-pipeline-workflow.md`](plans/2026-04-02_cri-phase1-data-pipeline-workflow.md)).
- **Data Item**: Dataset or derived table/layer.
- **Location**: Path or system where it is stored.
- **Reviewed?**: Has the content been inspected for correctness and completeness?
- **Processed?**: Has the planned transformation been applied?
- **Ready for analysis?**: Can this be used directly in analysis / index computation?
- **Comments**: Notes, issues, or follow-ups.

---

## P1 — Inventory and Mapping of Pilot Datasets

| Process | Data Item                     | Location | Reviewed? | Processed? | Ready for analysis? | Comments |
| ------- | ----------------------------- | -------- | --------- | ---------- | ------------------- | -------- |
| P1      | DDPM impact series (pilot)    |          |           |            |                     |          |
| P1      | OAE relief series (pilot)     |          |           |            |                     |          |
| P1      | NESDC GPP (pilot)             |          |           |            |                     |          |
| P1      | DOPA population (pilot)       |          |           |            |                     |          |
| P1      | Pilot calculation sheet (Cal) |          |           |            |                     |          |


---

## P2 — Cleaning and Harmonization of Core Tables

| Process | Data Item | Location | Reviewed? | Processed? | Ready for analysis? | Comments |
|--------|-----------|----------|-----------|------------|---------------------|----------|
| P2 | Clean DDPM impact table (standard schema) |  |  |  |  |  |
| P2 | Clean OAE relief table (standard schema) |  |  |  |  |  |
| P2 | Clean NESDC GPP table (standard schema) |  |  |  |  |  |
| P2 | Clean DOPA population table (standard schema) |  |  |  |  |  |

---

## P3 — Province-Year Impact Variables

| Process | Data Item | Location | Reviewed? | Processed? | Ready for analysis? | Comments |
|--------|-----------|----------|-----------|------------|---------------------|----------|
| P3 | Human impact indicators (absolute) |  |  |  |  |  |
| P3 | Human impact indicators (per 100k population) |  |  |  |  |  |
| P3 | Fiscal Relief Index numerator (relief totals) |  |  |  |  |  |
| P3 | Fiscal Relief Index per GPP (province-level) |  |  |  |  |  |
| P3 | Per-capita versions of key indicators |  |  |  |  |  |
| P3 | Per-GPP versions of key indicators |  |  |  |  |  |

---

## P4 — Denominators and Aggregate Province-Year Table

| Process | Data Item | Location | Reviewed? | Processed? | Ready for analysis? | Comments |
|--------|-----------|----------|-----------|------------|---------------------|----------|
| P4 | Confirmed GPP denominator choice (doc/note) |  |  |  |  |  |
| P4 | Confirmed population denominator choice (doc/note) |  |  |  |  |  |
| P4 | province_year_impact table (assembled) |  |  |  |  |  |

---

## P5 — Exposure Proxies from New Spatial Layers

| Process | Data Item | Location | Reviewed? | Processed? | Ready for analysis? | Comments |
|--------|-----------|----------|-----------|------------|---------------------|----------|
| P5 | WorldPop / GHS-POP raw layer |  |  |  |  |  |
| P5 | ESA WorldCover raw layer |  |  |  |  |  |
| P5 | Agri-Map raw layer |  |  |  |  |  |
| P5 | GISTDA flood/drought masks |  |  |  |  |  |
| P5 | Human exposure proxy layer |  |  |  |  |  |
| P5 | Agricultural exposure proxy layer |  |  |  |  |  |
| P5 | Urban/industrial exposure proxy layer |  |  |  |  |  |

---

## P6 — Constrained Redistribution and Dasymetric Mapping

| Process | Data Item | Location | Reviewed? | Processed? | Ready for analysis? | Comments |
|--------|-----------|----------|-----------|------------|---------------------|----------|
| P6 | Redistribution weights definition (method note) |  |  |  |  |  |
| P6 | Redistribution weights dataset |  |  |  |  |  |
| P6 | Spatial impact metrics at finer units (e.g., districts/grid) |  |  |  |  |  |

---

## P7 — Gap Flags and Data Quality Rules

| Process | Data Item | Location | Reviewed? | Processed? | Ready for analysis? | Comments |
|--------|-----------|----------|-----------|------------|---------------------|----------|
| P7 | Gap-flag protocol note (0 vs missing, AdminGap) |  |  |  |  |  |
| P7 | AdminGap flags applied in province_year_impact |  |  |  |  |  |
| P7 | Data quality labels applied (source, completeness, etc.) |  |  |  |  |  |
| P7 | Flags/labels applied in spatial impact dataset |  |  |  |  |  |

---

## P8 — Evidence Registration and Final Package

| Process | Data Item | Location | Reviewed? | Processed? | Ready for analysis? | Comments |
|--------|-----------|----------|-----------|------------|---------------------|----------|
| P8 | Updated CRI Evidence Registry entries (E-CRI IDs for all key datasets) |  |  |  |  |  |
| P8 | Updated CRI Evidence Coverage Map entries for Phase 1 |  |  |  |  |  |
| P8 | Frozen province_year_impact table |  |  |  |  |  |
| P8 | Frozen spatial impact dataset |  |  |  |  |  |
| P8 | Minimal Phase 1 data dictionary and rules note |  |  |  |  |  |

