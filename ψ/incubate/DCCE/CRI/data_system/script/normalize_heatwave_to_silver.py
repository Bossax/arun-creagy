#!/usr/bin/env python3
r"""
Normalize the Heatwave bronze extract into a Silver-ready long fact table.

Run from project root with the CRI data_system venv Python, for example:
    .\ψ\incubate\DCCE\CRI\data_system\.venv\Scripts\python.exe .\ψ\incubate\DCCE\CRI\data_system\script\normalize_heatwave_to_silver.py

Outputs:
- `data/1_silver/heatwave/silver_heatwave_impact_long.csv`
- `data/1_silver/heatwave/heatwave_normalization_report.json`
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parents[6]

BRONZE_CSV_PATH = (
    PROJECT_ROOT
    / "ψ"
    / "incubate"
    / "DCCE"
    / "CRI"
    / "data_system"
    / "data"
    / "0_bronze"
    / "2026-06-12_cri_proj_data"
    / "heatwave_extracts"
    / "heatwave.raw.csv"
)
LOCATION_DIM_PATH = (
    PROJECT_ROOT
    / "ψ"
    / "incubate"
    / "DCCE"
    / "CRI"
    / "data_system"
    / "data"
    / "2_gold"
    / "dopa"
    / "dim_location_master.csv"
)
HAZARD_CANONICAL_PATH = (
    PROJECT_ROOT
    / "ψ"
    / "incubate"
    / "DCCE"
    / "CRI"
    / "data_system"
    / "data"
    / "2_gold"
    / "dim_hazard_canonical.csv"
)
HAZARD_TYPE_PATH = (
    PROJECT_ROOT
    / "ψ"
    / "incubate"
    / "DCCE"
    / "CRI"
    / "data_system"
    / "data"
    / "2_gold"
    / "dim_hazard_type.csv"
)
SECTOR_DIM_PATH = (
    PROJECT_ROOT
    / "ψ"
    / "incubate"
    / "DCCE"
    / "CRI"
    / "data_system"
    / "data"
    / "2_gold"
    / "dim_sector.csv"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "ψ"
    / "incubate"
    / "DCCE"
    / "CRI"
    / "data_system"
    / "data"
    / "1_silver"
    / "heatwave"
)
OUTPUT_CSV_PATH = OUTPUT_DIR / "silver_heatwave_impact_long.csv"
OUTPUT_REPORT_PATH = OUTPUT_DIR / "heatwave_normalization_report.json"

SOURCE_SYSTEM = "CRI_WORKBOOK_BUNDLE"
SOURCE_DATASET = "heatwave"
SOURCE_FILE = "heatwave.raw.csv"
SOURCE_SHEET = "Heatwave"
HAZARD_CODE = "HEATWAVE"
HAZARD_NAME_EN = "Heatwave"
HAZARD_NAME_TH = "คลื่นความร้อน"
DEFAULT_SECTOR_CODE = "HEALTH"

EXPECTED_HEADERS = [
    "Province Code | รหัสจังหวัด",
    "Province | จังหวัด",
    "จำนวนผู้เสียชีวิตและได้รับผลกระทบ (คน) | 2567 | Deaths",
    "Injured",
    "2561 - 2567 | Deaths",
    "Injured_2",
]

METRIC_COLUMN_SPECS = [
    {
        "source_column": "จำนวนผู้เสียชีวิตและได้รับผลกระทบ (คน) | 2567 | Deaths",
        "metric_code": "DEATHS",
        "metric_name": "Deaths",
        "time_scope": "year_2567",
        "time_scope_type": "single_year",
        "period_start_be": "2567",
        "period_end_be": "2567",
        "time_scope_label": "2567",
    },
    {
        "source_column": "Injured",
        "metric_code": "INJURED",
        "metric_name": "Injured",
        "time_scope": "year_2567",
        "time_scope_type": "single_year",
        "period_start_be": "2567",
        "period_end_be": "2567",
        "time_scope_label": "2567",
    },
    {
        "source_column": "2561 - 2567 | Deaths",
        "metric_code": "DEATHS",
        "metric_name": "Deaths",
        "time_scope": "range_2561_2567",
        "time_scope_type": "multi_year_range",
        "period_start_be": "2561",
        "period_end_be": "2567",
        "time_scope_label": "2561-2567",
    },
    {
        "source_column": "Injured_2",
        "metric_code": "INJURED",
        "metric_name": "Injured",
        "time_scope": "range_2561_2567",
        "time_scope_type": "multi_year_range",
        "period_start_be": "2561",
        "period_end_be": "2567",
        "time_scope_label": "2561-2567",
    },
]

OUTPUT_HEADERS = [
    "record_id",
    "province_code",
    "province_name_th",
    "location_id",
    "admin_level",
    "hazard_code",
    "hazard_name_en",
    "hazard_name_th",
    "canonical_hazard_code",
    "canonical_hazard_name_en",
    "canonical_hazard_name_th",
    "metric_code",
    "metric_name",
    "time_scope",
    "time_scope_type",
    "time_scope_label",
    "period_start_be",
    "period_end_be",
    "value",
    "value_type",
    "unit",
    "sector_code",
    "source_system",
    "source_dataset",
    "source_file",
    "source_sheet",
    "source_row_number",
    "raw_header_value",
]


def normalize_text(value: object) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value).strip())


def normalize_code(value: object) -> str:
    text = normalize_text(value)
    digits = re.sub(r"\D", "", text)
    if not digits:
        return ""
    return digits.zfill(2)


def parse_int(value: object) -> int | None:
    text = normalize_text(value)
    if not text:
        return None
    text = text.replace(",", "")
    if text.startswith("="):
        return None
    if not re.fullmatch(r"[-+]?\d+(?:\.0+)?", text):
        return None
    return int(float(text))


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        return list(reader)


def load_province_lookup(path: Path) -> dict[str, dict[str, str]]:
    lookup: dict[str, dict[str, str]] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            province_code = normalize_code(row.get("province_code"))
            if not province_code or province_code in lookup:
                continue
            lookup[province_code] = {
                "location_id": province_code,
                "province_name_th": normalize_text(row.get("province_name_th")),
                "admin_level": "province",
            }
    return lookup


def load_canonical_hazard(path: Path, hazard_code: str) -> dict[str, str]:
    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            if normalize_text(row.get("canonical_hazard_code")) == hazard_code:
                return {
                    "canonical_hazard_code": normalize_text(row.get("canonical_hazard_code")),
                    "canonical_hazard_name_en": normalize_text(row.get("canonical_hazard_name_en")),
                    "canonical_hazard_name_th": normalize_text(row.get("canonical_hazard_name_th")),
                }
    return {
        "canonical_hazard_code": "",
        "canonical_hazard_name_en": "",
        "canonical_hazard_name_th": "",
    }


def has_hazard_type(path: Path, hazard_code: str) -> bool:
    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        return any(normalize_text(row.get("hazard_code")) == hazard_code for row in reader)


def has_sector(path: Path, sector_code: str) -> bool:
    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        return any(normalize_text(row.get("sector_code")) == sector_code for row in reader)


def build_record_id(province_code: str, metric_code: str, time_scope: str) -> str:
    return f"{province_code}_{metric_code}_{time_scope}_{HAZARD_CODE}"


def validate_headers(actual_headers: list[str]) -> list[str]:
    issues: list[str] = []
    if actual_headers != EXPECTED_HEADERS:
        issues.append("Bronze headers differ from expected Heatwave normalization contract")
    missing = [header for header in EXPECTED_HEADERS if header not in actual_headers]
    if missing:
        issues.append(f"Missing expected bronze headers: {missing}")
    return issues


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    timestamp = datetime.now(timezone.utc).isoformat()
    report: dict[str, object] = {
        "generated_at_utc": timestamp,
        "script_path": str(SCRIPT_PATH),
        "input_bronze_csv_path": str(BRONZE_CSV_PATH),
        "output_csv_path": str(OUTPUT_CSV_PATH),
        "output_report_path": str(OUTPUT_REPORT_PATH),
        "supporting_dimensions": {
            "location": str(LOCATION_DIM_PATH),
            "hazard_canonical": str(HAZARD_CANONICAL_PATH),
            "hazard_type": str(HAZARD_TYPE_PATH),
            "sector": str(SECTOR_DIM_PATH),
        },
        "issues": [],
    }

    required_paths = [
        BRONZE_CSV_PATH,
        LOCATION_DIM_PATH,
        HAZARD_CANONICAL_PATH,
        HAZARD_TYPE_PATH,
        SECTOR_DIM_PATH,
    ]
    missing_paths = [str(path) for path in required_paths if not path.exists()]
    if missing_paths:
        report["issues"] = [f"Missing required input: {path}" for path in missing_paths]
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        OUTPUT_REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        raise SystemExit(1)

    bronze_rows = load_csv_rows(BRONZE_CSV_PATH)
    actual_headers = list(bronze_rows[0].keys()) if bronze_rows else []
    issues = validate_headers(actual_headers)

    province_lookup = load_province_lookup(LOCATION_DIM_PATH)
    canonical_hazard = load_canonical_hazard(HAZARD_CANONICAL_PATH, HAZARD_CODE)
    hazard_type_exists = has_hazard_type(HAZARD_TYPE_PATH, HAZARD_CODE)
    sector_exists = has_sector(SECTOR_DIM_PATH, DEFAULT_SECTOR_CODE)

    normalized_rows: list[dict[str, object]] = []
    source_row_counter = 1
    skipped_total_rows = 0
    invalid_numeric_rows: list[dict[str, str]] = []
    province_mismatches: list[dict[str, str]] = []

    for bronze_row in bronze_rows:
        province_code = normalize_code(bronze_row.get("Province Code | รหัสจังหวัด"))
        province_name_th = normalize_text(bronze_row.get("Province | จังหวัด"))

        if province_code.casefold() == "" and province_name_th == "":
            skipped_total_rows += 1
            source_row_counter += 1
            continue

        if province_code.lower() == "total" or province_name_th.lower() == "total":
            skipped_total_rows += 1
            source_row_counter += 1
            continue

        province_dim = province_lookup.get(province_code)
        if province_dim is None:
            province_mismatches.append(
                {
                    "province_code": province_code,
                    "province_name_th": province_name_th,
                    "issue": "province_code_not_found_in_dim_location_master",
                }
            )
            source_row_counter += 1
            continue

        dim_name = province_dim["province_name_th"]
        if province_name_th and dim_name and province_name_th != dim_name:
            province_mismatches.append(
                {
                    "province_code": province_code,
                    "province_name_th": province_name_th,
                    "dim_province_name_th": dim_name,
                    "issue": "province_name_mismatch",
                }
            )

        for spec in METRIC_COLUMN_SPECS:
            raw_value = bronze_row.get(spec["source_column"], "")
            value = parse_int(raw_value)
            if value is None:
                invalid_numeric_rows.append(
                    {
                        "province_code": province_code,
                        "source_column": spec["source_column"],
                        "raw_value": normalize_text(raw_value),
                    }
                )
                continue

            normalized_rows.append(
                {
                    "record_id": build_record_id(province_code, spec["metric_code"], spec["time_scope"]),
                    "province_code": province_code,
                    "province_name_th": dim_name or province_name_th,
                    "location_id": province_dim["location_id"],
                    "admin_level": province_dim["admin_level"],
                    "hazard_code": HAZARD_CODE,
                    "hazard_name_en": HAZARD_NAME_EN,
                    "hazard_name_th": HAZARD_NAME_TH,
                    "canonical_hazard_code": canonical_hazard["canonical_hazard_code"],
                    "canonical_hazard_name_en": canonical_hazard["canonical_hazard_name_en"],
                    "canonical_hazard_name_th": canonical_hazard["canonical_hazard_name_th"],
                    "metric_code": spec["metric_code"],
                    "metric_name": spec["metric_name"],
                    "time_scope": spec["time_scope"],
                    "time_scope_type": spec["time_scope_type"],
                    "time_scope_label": spec["time_scope_label"],
                    "period_start_be": spec["period_start_be"],
                    "period_end_be": spec["period_end_be"],
                    "value": value,
                    "value_type": "count",
                    "unit": "person",
                    "sector_code": DEFAULT_SECTOR_CODE,
                    "source_system": SOURCE_SYSTEM,
                    "source_dataset": SOURCE_DATASET,
                    "source_file": SOURCE_FILE,
                    "source_sheet": SOURCE_SHEET,
                    "source_row_number": source_row_counter,
                    "raw_header_value": spec["source_column"],
                }
            )

        source_row_counter += 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV_PATH.open("w", encoding="utf-8-sig", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=OUTPUT_HEADERS)
        writer.writeheader()
        writer.writerows(normalized_rows)

    unique_keys = {
        (row["province_code"], row["metric_name"], row["time_scope"])
        for row in normalized_rows
    }
    duplicate_keys = [
        {"province_code": province_code, "metric_name": metric_name, "time_scope": time_scope, "count": count}
        for (province_code, metric_name, time_scope), count in Counter(
            (row["province_code"], row["metric_name"], row["time_scope"])
            for row in normalized_rows
        ).items()
        if count > 1
    ]
    time_scope_counts = Counter(row["time_scope"] for row in normalized_rows)
    metric_counts = Counter(row["metric_name"] for row in normalized_rows)

    if not canonical_hazard["canonical_hazard_code"]:
        issues.append("No canonical hazard mapping found for HEATWAVE in dim_hazard_canonical")
    if not hazard_type_exists:
        issues.append("No hazard type mapping found for HEATWAVE in dim_hazard_type")
    if not sector_exists:
        issues.append("No sector mapping found for HEALTH in dim_sector")
    if invalid_numeric_rows:
        issues.append(f"{len(invalid_numeric_rows)} metric cells could not be parsed as integers")
    if duplicate_keys:
        issues.append(f"{len(duplicate_keys)} duplicate grain keys detected")
    if province_mismatches:
        issues.append(f"{len(province_mismatches)} province mapping/name issues detected")

    report.update(
        {
            "status": "ok" if not issues else "warning",
            "input_row_count": len(bronze_rows),
            "output_row_count": len(normalized_rows),
            "skipped_total_rows": skipped_total_rows,
            "expected_grain": "one row per province_code + metric_name + time_scope",
            "output_schema": OUTPUT_HEADERS,
            "bronze_headers": actual_headers,
            "validation": {
                "header_contract_matches_expected": actual_headers == EXPECTED_HEADERS,
                "unique_key_count": len(unique_keys),
                "duplicate_keys": duplicate_keys,
                "time_scope_counts": dict(time_scope_counts),
                "metric_counts": dict(metric_counts),
                "province_codes_missing_from_dim": [
                    item for item in province_mismatches if item.get("issue") == "province_code_not_found_in_dim_location_master"
                ],
                "province_name_mismatches": [
                    item for item in province_mismatches if item.get("issue") == "province_name_mismatch"
                ],
                "invalid_numeric_rows": invalid_numeric_rows[:20],
                "canonical_hazard_found": bool(canonical_hazard["canonical_hazard_code"]),
                "hazard_type_found": hazard_type_exists,
                "sector_found": sector_exists,
            },
        }
    )

    OUTPUT_REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
