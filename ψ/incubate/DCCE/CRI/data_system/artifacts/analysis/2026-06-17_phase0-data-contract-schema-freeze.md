# Phase 0 — Data Contract Schema Freeze

## Purpose

This artifact closes the highest-risk gap in the CRI web app execution plan by freezing the exact JSON structures that Stage 1 must produce and Stages 4–6 must consume.

This file is authoritative for export schema and frontend input shape.

It must be read together with:

- [`2026-06-17_phase0-data-contract-outline.md`](./2026-06-17_phase0-data-contract-outline.md)
- [`2026-06-17_phase0-workstream1-metric-freeze.md`](./2026-06-17_phase0-workstream1-metric-freeze.md)
- [`2026-06-17_cri-webapp-orchestrator-execution-plan.md`](./2026-06-17_cri-webapp-orchestrator-execution-plan.md)

---

## 1. Global contract rules

1. All exported assets are JSON unless explicitly marked as spatial geometry.
2. All exported metric files are read-only frontend inputs.
3. Stages 4–6 must not recompute analytics; they only read these exported files plus spatial assets.
4. All metric files must include embedded ranking payloads.
5. All period-specific files must use one of these keys only:
   - `period_2560_2567`
   - `period_2567`
6. All province-level metric files use province grain only.
7. All tambon-level metric files use tambon grain only.
8. Ranking ties must follow the same descending-rank method as the notebook freeze unless explicitly superseded.

---

## 2. Export destination structure

Required export layout:

- `manifest.json`
- `period_2560_2567/deaths_abs.json`
- `period_2560_2567/deaths_rate.json`
- `period_2560_2567/affected_hh_abs.json`
- `period_2560_2567/affected_rate.json`
- `period_2560_2567/loss_abs.json`
- `period_2560_2567/loss_per_gpp.json`
- `period_2560_2567/cri_score.json`
- `period_2560_2567/tambon_deaths.json`
- `period_2560_2567/tambon_affected_households.json`
- `period_2560_2567/heat_deaths.json`
- `period_2560_2567/heat_injured.json`
- `period_2567/deaths_abs.json`
- `period_2567/deaths_rate.json`
- `period_2567/affected_hh_abs.json`
- `period_2567/affected_rate.json`
- `period_2567/loss_abs.json`
- `period_2567/loss_per_gpp.json`
- `period_2567/cri_score.json`
- `period_2567/tambon_deaths.json`
- `period_2567/tambon_affected_households.json`
- `period_2567/heat_deaths.json`
- `period_2567/heat_injured.json`
- `spatial/province_boundaries.geojson`
- `spatial/tambon/<province_code>.geojson`
- `spatial/manifest.json`

---

## 3. Shared field conventions

### 3.1 Required scalar conventions

- `metric_key`: machine-stable identifier
- `metric_label`: human-readable label
- `period_key`: `period_2560_2567` or `period_2567`
- `period_label`: display label for UI
- `unit_label`: explicit unit text for UI
- `source_mode`: `average_window` or `single_year`

### 3.2 Required ranking conventions

- `top_10` must be sorted descending by metric value
- `bottom_10` must be sorted ascending by metric value
- ranking payloads are embedded in each metric file
- all ranking records must carry both code and display name fields

### 3.3 Required legend conventions

Each map-supporting metric file must include a `legend` object with:

- `min`
- `max`
- `display_min`
- `display_max`
- `color_scheme`

---

## 4. `manifest.json` schema

### 4.1 Required top-level structure

```json
{
  "version": "string",
  "generated_at": "ISO8601 string",
  "periods": [
    {
      "period_key": "period_2560_2567",
      "period_label": "2560–2567 average"
    },
    {
      "period_key": "period_2567",
      "period_label": "2567 only"
    }
  ],
  "metric_groups": {
    "cri": ["deaths_abs", "deaths_rate", "affected_hh_abs", "affected_rate", "loss_abs", "loss_per_gpp", "cri_score"],
    "tambon": ["tambon_deaths", "tambon_affected_households"],
    "heat": ["heat_deaths", "heat_injured"]
  },
  "assets": {
    "province_geometry": "spatial/province_boundaries.geojson",
    "tambon_manifest": "spatial/manifest.json"
  }
}
```

### 4.2 Required behavior

- frontend uses `manifest.json` as the single discovery file
- frontend must not hardcode metric availability outside the manifest

---

## 5. Province metric file schema

Applies to:

- `deaths_abs.json`
- `deaths_rate.json`
- `affected_hh_abs.json`
- `affected_rate.json`
- `loss_abs.json`
- `loss_per_gpp.json`
- `cri_score.json`
- `heat_deaths.json`
- `heat_injured.json`

### 5.1 Required top-level structure

```json
{
  "metric_key": "deaths_abs",
  "metric_label": "Total Deaths (Absolute)",
  "period_key": "period_2560_2567",
  "period_label": "2560–2567 average",
  "unit_label": "Annual deaths",
  "source_mode": "average_window",
  "legend": {
    "min": 0,
    "max": 100,
    "display_min": "0",
    "display_max": "100",
    "color_scheme": "OrRd"
  },
  "records": [],
  "rankings": {
    "top_10": [],
    "bottom_10": []
  }
}
```

### 5.2 Required `records[]` shape

```json
{
  "province_code": "58",
  "province_name_th": "แม่ฮ่องสอน",
  "province_name_en": null,
  "value": 0.625,
  "display_value": "0.625",
  "rank_desc": 1,
  "normalized_value": 0.2083
}
```

### 5.3 Required `rankings.top_10[]` and `rankings.bottom_10[]` shape

```json
{
  "province_code": "58",
  "province_name_th": "แม่ฮ่องสอน",
  "province_name_en": null,
  "value": 0.625,
  "display_value": "0.625",
  "rank_desc": 1
}
```

### 5.4 Required notes

- `normalized_value` is required for CRI component metrics and `cri_score`
- `normalized_value` may be `null` for heat metrics if raw values alone are visualized

---

## 6. Tambon metric file schema

Applies to:

- `tambon_deaths.json`
- `tambon_affected_households.json`

### 6.1 Required top-level structure

```json
{
  "metric_key": "tambon_deaths",
  "metric_label": "Tambon Deaths",
  "period_key": "period_2567",
  "period_label": "2567 only",
  "unit_label": "Annual deaths",
  "source_mode": "single_year",
  "records": [],
  "rankings": {
    "national_top_10": [],
    "national_bottom_10": []
  }
}
```

### 6.2 Required `records[]` shape

```json
{
  "subdistrict_code": "500101",
  "subdistrict_name_th": "ศรีภูมิ",
  "district_name_th": "เมืองเชียงใหม่",
  "province_code": "50",
  "province_name_th": "เชียงใหม่",
  "value": 2,
  "display_value": "2"
}
```

### 6.3 Required behavior

- the file must contain enough province linkage fields for province-level filtering in the frontend
- province-specific top/bottom rankings may be derived client-side from `records[]`
- national top/bottom rankings must be embedded

---

## 7. Heat metric file schema

Heat files use the province metric schema in [5](./2026-06-17_phase0-data-contract-schema-freeze.md:91), with these additional rules:

- `metric_key` must be exactly `heat_deaths` or `heat_injured`
- `metric_label` must reflect the frozen heat wording
- `source_mode` must reflect the selected period mode
- heat files must not be merged into a combined health-burden file

---

## 8. `spatial/manifest.json` schema

### 8.1 Required top-level structure

```json
{
  "province_geometry": "spatial/province_boundaries.geojson",
  "tambon_by_province": [
    {
      "province_code": "50",
      "province_name_th": "เชียงใหม่",
      "file": "spatial/tambon/50.geojson"
    }
  ]
}
```

### 8.2 Required behavior

- frontend loads province geometry globally
- frontend loads tambon geometry by selected province only

---

## 9. Tie-handling rule

The export layer must preserve the notebook-compatible descending ranking convention.

If equal metric values occur:

- ties must share the same displayed descending rank if the export reproduces notebook semantics
- this rule must be applied consistently across all province-level metrics

The exact implementation must not vary by metric.

---

## 10. Validation checklist for Stage 1 handoff

Stage 1 is not complete until all of the following are true:

1. every required file in [2](./2026-06-17_phase0-data-contract-schema-freeze.md:20) exists
2. every metric file matches its frozen schema
3. rankings are embedded in every required metric file
4. `manifest.json` references the available periods and metric groups correctly
5. `spatial/manifest.json` references province/tambon geometry correctly
6. province metric files carry `province_code`, `province_name_th`, and `value`
7. tambon metric files carry `subdistrict_code`, `province_code`, and `value`
8. heat files remain separate as deaths and injured
9. no frontend stage needs to infer missing schema fields

---

## 11. Instruction to Orchestrator mode

When assigning the Stage 1 subtask, require the agent to:

1. follow the concrete source files listed in [`2026-06-17_phase0-data-contract-outline.md`](./2026-06-17_phase0-data-contract-outline.md:20)
2. preserve the formulas and period logic frozen in [`2026-06-17_phase0-workstream1-metric-freeze.md`](./2026-06-17_phase0-workstream1-metric-freeze.md:1)
3. emit files exactly following this schema freeze
4. hand off only after the Stage 1 validation checklist passes
