"""Stage 1 export loading helpers for CRI Impact App v2."""
from __future__ import annotations

import copy
import json
from functools import lru_cache
from pathlib import Path
from typing import Any


def _workspace_root() -> Path:
    return Path(__file__).resolve().parents[3]


STAGE1_DIR = _workspace_root() / "build_exports" / "stage1"
MANIFEST_PATH = STAGE1_DIR / "manifest.json"
SPATIAL_MANIFEST_PATH = STAGE1_DIR / "spatial" / "manifest.json"


@lru_cache(maxsize=1)
def load_manifest() -> dict[str, Any]:
    with MANIFEST_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


@lru_cache(maxsize=1)
def load_spatial_manifest() -> dict[str, Any]:
    with SPATIAL_MANIFEST_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


@lru_cache(maxsize=None)
def load_metric(metric_key: str, period_key: str = "period_2560_2567") -> dict[str, Any]:
    path = STAGE1_DIR / period_key / f"{metric_key}.json"
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


@lru_cache(maxsize=None)
def load_stage1_json(relative_path: str) -> dict[str, Any]:
    path = STAGE1_DIR / relative_path
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def available_periods() -> list[dict[str, Any]]:
    return list(load_manifest().get("periods", []))


def available_metric_groups() -> dict[str, list[str]]:
    return dict(load_manifest().get("metric_groups", {}))


def ranking_rows(dataset: dict[str, Any], ranking_key: str = "top_10") -> list[dict[str, Any]]:
    rankings = dataset.get("rankings") or {}
    rows: list[dict[str, Any]] = []
    for item in rankings.get(ranking_key, []):
        rows.append(
            {
                "rank": item.get("rank_desc") or item.get("rank") or "-",
                "thai_name": item.get("province_name_th") or item.get("thai_name") or "-",
                "value": item.get("display_value")
                if item.get("display_value") is not None
                else item.get("value", "-"),
            }
        )
    return rows


def metric_rows(dataset: dict[str, Any]) -> list[dict[str, Any]]:
    return list(dataset.get("records", []))


def tambon_period_key(period_choice: str) -> str:
    mapping = {
        "cumulative": "period_2560_2567",
        "specific_year": "period_2567",
        "period_2560_2567": "period_2560_2567",
        "period_2567": "period_2567",
    }
    return mapping.get(period_choice, "period_2560_2567")


def tambon_records(dataset: dict[str, Any], province_code: str | None = None) -> list[dict[str, Any]]:
    rows = list(dataset.get("records", []))
    if province_code:
        rows = [row for row in rows if str(row.get("province_code") or "") == str(province_code)]
    return rows


def tambon_province_options(dataset: dict[str, Any]) -> list[dict[str, str]]:
    seen: dict[str, str] = {}
    for row in tambon_records(dataset):
        province_code = str(row.get("province_code") or "")
        province_name = str(row.get("province_name_th") or province_code)
        if province_code and province_code not in seen:
            seen[province_code] = province_name
    return [
        {"province_code": province_code, "province_name_th": seen[province_code]}
        for province_code in sorted(seen, key=lambda code: seen[code])
    ]


def tambon_rank_rows(
    dataset: dict[str, Any],
    province_code: str | None = None,
    *,
    descending: bool = True,
    limit: int = 10,
) -> list[dict[str, Any]]:
    rows = tambon_records(dataset, province_code=province_code)
    rows = sorted(rows, key=lambda item: float(item.get("value") or 0), reverse=descending)
    output: list[dict[str, Any]] = []
    for index, item in enumerate(rows[:limit], start=1):
        tambon_name = item.get("subdistrict_name_th") or "-"
        district_name = item.get("district_name_th") or "-"
        output.append(
            {
                "rank": index,
                "thai_name": f"{tambon_name} · {district_name}",
                "value": item.get("display_value") if item.get("display_value") is not None else item.get("value", "-"),
            }
        )
    return output


def tambon_geojson_for_province(dataset: dict[str, Any], province_code: str) -> dict[str, Any]:
    spatial_manifest = load_spatial_manifest()
    tambon_files = {
        str(item.get("province_code")): item.get("file")
        for item in spatial_manifest.get("tambon_by_province", [])
        if item.get("province_code") and item.get("file")
    }
    relative_path = tambon_files[str(province_code)]
    geojson = copy.deepcopy(load_stage1_json(relative_path))

    record_map = {
        str(item.get("subdistrict_code") or ""): item
        for item in tambon_records(dataset, province_code=province_code)
        if item.get("subdistrict_code")
    }

    for feature in geojson.get("features", []):
        properties = feature.setdefault("properties", {})
        code = str(properties.get("subdistrict_code") or "")
        record = record_map.get(code, {})
        properties["subdistrict_name_th"] = record.get("subdistrict_name_th") or properties.get("subdistrict_name_th") or code
        properties["district_name_th"] = record.get("district_name_th") or properties.get("district_name_th") or "-"
        properties["province_name_th"] = record.get("province_name_th") or properties.get("province_name_th") or "-"
        value = float(record.get("value") or 0)
        intensity = min(max(value / 1000, 0), 1)
        properties["value"] = value
        properties["display_value"] = record.get("display_value") if record.get("display_value") is not None else str(record.get("value") or 0)
        properties["has_data"] = code in record_map
        properties["fill_color"] = [255, int(210 - (intensity * 70)), int(220 - (intensity * 110)), 180]
        properties["line_color"] = [25, 35, 52, 220]

    return geojson


def metric_summary(dataset: dict[str, Any]) -> dict[str, Any]:
    legend = dataset.get("legend") or {}
    return {
        "metric_label": dataset.get("metric_label", "Metric"),
        "period_label": dataset.get("period_label", ""),
        "unit_label": dataset.get("unit_label", ""),
        "source_mode": dataset.get("source_mode", ""),
        "legend_min": legend.get("display_min", legend.get("min", "-")),
        "legend_max": legend.get("display_max", legend.get("max", "-")),
        "legend_scheme": legend.get("color_scheme", ""),
    }

