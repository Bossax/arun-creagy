#!/usr/bin/env python3
r"""
Normalize the GPP bronze extracts into a Silver-ready annual long fact table.

Run from project root with the CRI data_system venv Python, for example:
    .\ψ\incubate\DCCE\CRI\data_system\.venv\Scripts\python.exe .\ψ\incubate\DCCE\CRI\data_system\script\normalize_gpp_to_silver.py

Outputs:
- `data/1_silver/gpp/silver_gpp_annual_long.csv`
- `data/1_silver/gpp/gpp_normalization_report.json`
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parents[6]

BRONZE_DIR = (
    PROJECT_ROOT
    / "ψ"
    / "incubate"
    / "DCCE"
    / "CRI"
    / "data_system"
    / "data"
    / "0_bronze"
    / "2026-06-12_cri_proj_data"
    / "gpp_extracts"
)
GPP_67_PATH = BRONZE_DIR / "gpp-67.raw.csv"
GPP_60_67_PATH = BRONZE_DIR / "gpp-60-67.raw.csv"
MANIFEST_PATH = BRONZE_DIR / "gpp.manifest.json"
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

OUTPUT_DIR = (
    PROJECT_ROOT
    / "ψ"
    / "incubate"
    / "DCCE"
    / "CRI"
    / "data_system"
    / "data"
    / "1_silver"
    / "gpp"
)
OUTPUT_CSV_PATH = OUTPUT_DIR / "silver_gpp_annual_long.csv"
OUTPUT_REPORT_PATH = OUTPUT_DIR / "gpp_normalization_report.json"

SOURCE_SYSTEM = "CRI_WORKBOOK_BUNDLE"
SOURCE_DATASET = "gpp"
SOURCE_FILE_67 = "gpp-67.raw.csv"
SOURCE_FILE_60_67 = "gpp-60-67.raw.csv"
SOURCE_SHEET_67 = "GPP 67"
SOURCE_SHEET_60_67 = "GPP 60-67"

EXPECTED_GPP67_HEADERS = [
    "Gross Provincial Product at Current Market Prices | จังหวัด",
    "รายละเอียด",
    "2567 | 2024p",
]
EXPECTED_GPP60_67_HEADERS = [
    "Gross Provincial Product at Current Market Prices",
    "column_2",
    "2560",
    "2561",
    "2562",
    "2563",
    "2564",
    "2565",
    "2566",
    "2567",
    "Total",
]
EXPECTED_YEARS_BE = [str(year) for year in range(2560, 2568)]
YEAR_2567 = "2567"

METRIC_SPECS = {
    "gross provincial product (gpp)": {
        "metric_code": "GPP_CURRENT_MARKET_PRICE",
        "metric_name": "Gross provincial product (GPP)",
        "unit": "million_baht",
        "value_type": "amount",
    },
    "gpp per capita (baht)": {
        "metric_code": "GPP_PER_CAPITA",
        "metric_name": "GPP Per capita (Baht)",
        "unit": "baht_per_person",
        "value_type": "amount",
    },
    "population (1,000 persons)": {
        "metric_code": "POPULATION_THOUSAND_PERSONS",
        "metric_name": "Population (1,000 persons)",
        "unit": "thousand_persons",
        "value_type": "count",
    },
}

OUTPUT_HEADERS = [
    "record_id",
    "area_code",
    "area_code_label",
    "area_label_en",
    "area_name_th",
    "province_code",
    "province_name_th",
    "location_id",
    "admin_level",
    "metric_code",
    "metric_name",
    "year_be",
    "year_ce",
    "value",
    "value_type",
    "unit",
    "source_system",
    "source_dataset",
    "source_file",
    "source_sheet",
    "source_row_number",
    "source_column",
    "source_priority",
    "raw_metric_label",
]


def normalize_text(value: object) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value).strip())


def metric_key(value: object) -> str:
    return normalize_text(value).strip('"').casefold()


def parse_decimal(value: object) -> Decimal | None:
    text = normalize_text(value).replace(",", "")
    if not text or text.startswith("="):
        return None
    try:
        return Decimal(text)
    except InvalidOperation:
        return None


def decimal_to_text(value: Decimal) -> str:
    normalized = format(value, "f")
    if "." in normalized:
        normalized = normalized.rstrip("0").rstrip(".")
    return normalized or "0"


def parse_area_code_label(value: str) -> tuple[str, str]:
    text = normalize_text(value)
    match = re.fullmatch(r"(\d{4})\s*-\s*(.+)", text)
    if not match:
        return "", ""
    return match.group(1), normalize_text(match.group(2))


def load_raw_rows(path: Path) -> list[list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        return [[normalize_text(cell) for cell in row] for row in csv.reader(fp)]


def load_manifest(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_location_lookup(path: Path) -> dict[str, dict[str, str]]:
    lookup: dict[str, dict[str, str]] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            province_name_th = normalize_text(row.get("province_name_th"))
            province_code = normalize_text(row.get("province_code"))
            if not province_name_th or not province_code or province_name_th in lookup:
                continue
            lookup[province_name_th] = {
                "province_code": province_code.zfill(2),
                "province_name_th": province_name_th,
                "location_id": province_code.zfill(2),
                "admin_level": "province",
            }
    return lookup


def build_record_id(area_code: str, metric_code: str, year_be: str) -> str:
    return f"{area_code}_{metric_code}_{year_be}"


def validate_manifest_headers(manifest: dict[str, object], issues: list[str]) -> None:
    sheets = manifest.get("sheets", [])
    if not isinstance(sheets, list):
        issues.append("Manifest sheets structure is not a list")
        return

    by_name = {normalize_text(sheet.get("sheet_name")): sheet for sheet in sheets if isinstance(sheet, dict)}

    gpp67 = by_name.get(SOURCE_SHEET_67)
    gpp60_67 = by_name.get(SOURCE_SHEET_60_67)
    if not isinstance(gpp67, dict):
        issues.append("Manifest missing GPP 67 sheet metadata")
    else:
        if gpp67.get("headers") != EXPECTED_GPP67_HEADERS:
            issues.append("Manifest headers for GPP 67 differ from expected contract")

    if not isinstance(gpp60_67, dict):
        issues.append("Manifest missing GPP 60-67 sheet metadata")
    else:
        if gpp60_67.get("headers") != EXPECTED_GPP60_67_HEADERS:
            issues.append("Manifest headers for GPP 60-67 differ from expected contract")


def parse_gpp67(
    rows: list[list[str]],
    location_lookup: dict[str, dict[str, str]],
) -> tuple[list[dict[str, object]], dict[str, object]]:
    extracted: list[dict[str, object]] = []
    issues: list[str] = []
    unexpected_rows: list[dict[str, object]] = []
    unknown_metric_labels: list[dict[str, object]] = []
    unmatched_locations: list[dict[str, object]] = []
    area_headers = 0
    metric_rows = 0
    current_area_name_th = ""
    current_area_code = ""
    current_area_code_label = ""
    current_area_label_en = ""

    for row_number, row in enumerate(rows[1:], start=2):
        padded = row + [""] * max(0, 3 - len(row))
        col1, col2, col3 = padded[:3]

        if not any((col1, col2, col3)):
            continue

        area_code, area_label_en = parse_area_code_label(col2)
        if area_code:
            area_headers += 1
            current_area_name_th = col1
            current_area_code = area_code
            current_area_code_label = col2
            current_area_label_en = area_label_en
            continue

        normalized_metric = metric_key(col2)
        spec = METRIC_SPECS.get(normalized_metric)
        if spec is None:
            unexpected_rows.append({
                "row_number": row_number,
                "row": padded[:3],
                "reason": "unexpected_non_metric_row",
            })
            continue

        metric_rows += 1
        if not current_area_code:
            unknown_metric_labels.append({
                "row_number": row_number,
                "metric_label": col2,
                "reason": "metric_row_without_active_area_block",
            })
            continue

        value = parse_decimal(col3)
        if value is None:
            issues.append(f"GPP 67 row {row_number} has non-numeric value for metric '{col2}'")
            continue

        location = location_lookup.get(current_area_name_th)
        if location is None:
            unmatched_locations.append({
                "row_number": row_number,
                "area_name_th": current_area_name_th,
                "area_code": current_area_code,
            })
            province_code = ""
            province_name_th = current_area_name_th
            location_id = ""
            admin_level = ""
        else:
            province_code = location["province_code"]
            province_name_th = location["province_name_th"]
            location_id = location["location_id"]
            admin_level = location["admin_level"]

        extracted.append(
            {
                "record_id": build_record_id(current_area_code, spec["metric_code"], YEAR_2567),
                "area_code": current_area_code,
                "area_code_label": current_area_code_label,
                "area_label_en": current_area_label_en,
                "area_name_th": current_area_name_th,
                "province_code": province_code,
                "province_name_th": province_name_th,
                "location_id": location_id,
                "admin_level": admin_level,
                "metric_code": spec["metric_code"],
                "metric_name": spec["metric_name"],
                "year_be": YEAR_2567,
                "year_ce": str(int(YEAR_2567) - 543),
                "value": decimal_to_text(value),
                "value_type": spec["value_type"],
                "unit": spec["unit"],
                "source_system": SOURCE_SYSTEM,
                "source_dataset": SOURCE_DATASET,
                "source_file": SOURCE_FILE_67,
                "source_sheet": SOURCE_SHEET_67,
                "source_row_number": row_number,
                "source_column": "2567 | 2024p",
                "source_priority": 1,
                "raw_metric_label": col2,
            }
        )

    summary = {
        "parsed_area_blocks": area_headers,
        "parsed_metric_rows": metric_rows,
        "extracted_row_count": len(extracted),
        "unexpected_rows": unexpected_rows[:20],
        "unexpected_row_count": len(unexpected_rows),
        "unmatched_locations": unmatched_locations[:20],
        "unmatched_location_count": len(unmatched_locations),
        "orphan_metric_rows": unknown_metric_labels[:20],
        "orphan_metric_row_count": len(unknown_metric_labels),
    }
    return extracted, {"issues": issues, "summary": summary}


def parse_gpp60_67(
    rows: list[list[str]],
    location_lookup: dict[str, dict[str, str]],
) -> tuple[list[dict[str, object]], dict[str, object]]:
    extracted: list[dict[str, object]] = []
    issues: list[str] = []
    unexpected_rows: list[dict[str, object]] = []
    unmatched_locations: list[dict[str, object]] = []
    yearly_sum_mismatches: list[dict[str, object]] = []
    area_headers = 0
    metric_rows = 0
    current_area_name_th = ""
    current_area_code = ""
    current_area_code_label = ""
    current_area_label_en = ""
    year_columns = rows[0][2:10]

    if year_columns != EXPECTED_YEARS_BE:
        issues.append(f"Unexpected GPP 60-67 year columns: {year_columns}")

    for row_number, row in enumerate(rows[1:], start=2):
        padded = row + [""] * max(0, 11 - len(row))
        col1 = padded[0]
        col2 = padded[1]
        values = padded[2:10]
        total_text = padded[10]

        if not any(padded):
            continue

        area_code, area_label_en = parse_area_code_label(col2)
        if area_code:
            area_headers += 1
            current_area_name_th = col1
            current_area_code = area_code
            current_area_code_label = col2
            current_area_label_en = area_label_en
            continue

        normalized_metric = metric_key(col2)
        spec = METRIC_SPECS.get(normalized_metric)
        if spec is None:
            unexpected_rows.append({
                "row_number": row_number,
                "row": padded,
                "reason": "unexpected_non_metric_row",
            })
            continue

        metric_rows += 1
        if not current_area_code:
            issues.append(f"GPP 60-67 row {row_number} is a metric row without an active area block")
            continue

        location = location_lookup.get(current_area_name_th)
        if location is None:
            unmatched_locations.append({
                "row_number": row_number,
                "area_name_th": current_area_name_th,
                "area_code": current_area_code,
            })
            province_code = ""
            province_name_th = current_area_name_th
            location_id = ""
            admin_level = ""
        else:
            province_code = location["province_code"]
            province_name_th = location["province_name_th"]
            location_id = location["location_id"]
            admin_level = location["admin_level"]

        annual_decimals: list[Decimal] = []
        for year_be, raw_value in zip(EXPECTED_YEARS_BE, values):
            value = parse_decimal(raw_value)
            if value is None:
                issues.append(f"GPP 60-67 row {row_number} has non-numeric value in year {year_be} for metric '{col2}'")
                continue
            annual_decimals.append(value)
            extracted.append(
                {
                    "record_id": build_record_id(current_area_code, spec["metric_code"], year_be),
                    "area_code": current_area_code,
                    "area_code_label": current_area_code_label,
                    "area_label_en": current_area_label_en,
                    "area_name_th": current_area_name_th,
                    "province_code": province_code,
                    "province_name_th": province_name_th,
                    "location_id": location_id,
                    "admin_level": admin_level,
                    "metric_code": spec["metric_code"],
                    "metric_name": spec["metric_name"],
                    "year_be": year_be,
                    "year_ce": str(int(year_be) - 543),
                    "value": decimal_to_text(value),
                    "value_type": spec["value_type"],
                    "unit": spec["unit"],
                    "source_system": SOURCE_SYSTEM,
                    "source_dataset": SOURCE_DATASET,
                    "source_file": SOURCE_FILE_60_67,
                    "source_sheet": SOURCE_SHEET_60_67,
                    "source_row_number": row_number,
                    "source_column": year_be,
                    "source_priority": 2,
                    "raw_metric_label": col2,
                }
            )

        total_value = parse_decimal(total_text)
        if total_value is not None and len(annual_decimals) == len(EXPECTED_YEARS_BE):
            annual_sum = sum(annual_decimals, start=Decimal("0"))
            if annual_sum != total_value:
                yearly_sum_mismatches.append(
                    {
                        "row_number": row_number,
                        "area_code": current_area_code,
                        "metric_name": spec["metric_name"],
                        "annual_sum": decimal_to_text(annual_sum),
                        "reported_total": decimal_to_text(total_value),
                    }
                )

    summary = {
        "parsed_area_blocks": area_headers,
        "parsed_metric_rows": metric_rows,
        "extracted_row_count": len(extracted),
        "unexpected_rows": unexpected_rows[:20],
        "unexpected_row_count": len(unexpected_rows),
        "unmatched_locations": unmatched_locations[:20],
        "unmatched_location_count": len(unmatched_locations),
        "yearly_sum_mismatches": yearly_sum_mismatches[:20],
        "yearly_sum_mismatch_count": len(yearly_sum_mismatches),
    }
    return extracted, {"issues": issues, "summary": summary}


def merge_with_2567_preference(
    long_60_67: list[dict[str, object]],
    annual_67: list[dict[str, object]],
) -> tuple[list[dict[str, object]], dict[str, object]]:
    merged = {
        (row["area_code"], row["metric_code"], row["year_be"]): dict(row)
        for row in long_60_67
    }
    cross_sheet_2567_mismatches: list[dict[str, object]] = []
    replaced_2567_rows = 0
    inserted_2567_rows = 0

    for row in annual_67:
        key = (row["area_code"], row["metric_code"], row["year_be"])
        existing = merged.get(key)
        if existing is None:
            merged[key] = dict(row)
            inserted_2567_rows += 1
            continue
        if normalize_text(existing["value"]) != normalize_text(row["value"]):
            cross_sheet_2567_mismatches.append(
                {
                    "area_code": row["area_code"],
                    "area_name_th": row["area_name_th"],
                    "metric_code": row["metric_code"],
                    "metric_name": row["metric_name"],
                    "year_be": row["year_be"],
                    "gpp_60_67_value": existing["value"],
                    "gpp_67_value": row["value"],
                }
            )
        merged[key] = dict(row)
        replaced_2567_rows += 1

    merged_rows = sorted(
        merged.values(),
        key=lambda row: (str(row["area_code"]), str(row["metric_code"]), int(str(row["year_be"]))),
    )
    summary = {
        "replaced_2567_rows": replaced_2567_rows,
        "inserted_2567_rows": inserted_2567_rows,
        "cross_sheet_2567_mismatches": cross_sheet_2567_mismatches[:20],
        "cross_sheet_2567_mismatch_count": len(cross_sheet_2567_mismatches),
    }
    return merged_rows, summary


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=OUTPUT_HEADERS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    timestamp = datetime.now(timezone.utc).isoformat()
    report: dict[str, object] = {
        "generated_at_utc": timestamp,
        "script_path": str(SCRIPT_PATH),
        "inputs": {
            "gpp_67": str(GPP_67_PATH),
            "gpp_60_67": str(GPP_60_67_PATH),
            "manifest": str(MANIFEST_PATH),
            "location_dim": str(LOCATION_DIM_PATH),
        },
        "outputs": {
            "silver_csv": str(OUTPUT_CSV_PATH),
            "report_json": str(OUTPUT_REPORT_PATH),
        },
        "issues": [],
    }

    required_paths = [GPP_67_PATH, GPP_60_67_PATH, MANIFEST_PATH, LOCATION_DIM_PATH]
    missing_paths = [str(path) for path in required_paths if not path.exists()]
    if missing_paths:
        report["issues"] = [f"Missing required input: {path}" for path in missing_paths]
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        OUTPUT_REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        raise SystemExit(1)

    manifest = load_manifest(MANIFEST_PATH)
    location_lookup = load_location_lookup(LOCATION_DIM_PATH)
    gpp67_rows = load_raw_rows(GPP_67_PATH)
    gpp60_67_rows = load_raw_rows(GPP_60_67_PATH)

    issues: list[str] = []
    validate_manifest_headers(manifest, issues)

    if not gpp67_rows or gpp67_rows[0] != EXPECTED_GPP67_HEADERS:
        issues.append("GPP 67 raw CSV headers differ from expected contract")
    if not gpp60_67_rows or gpp60_67_rows[0] != EXPECTED_GPP60_67_HEADERS:
        issues.append("GPP 60-67 raw CSV headers differ from expected contract")

    annual_67, annual_67_meta = parse_gpp67(gpp67_rows, location_lookup)
    long_60_67, long_60_67_meta = parse_gpp60_67(gpp60_67_rows, location_lookup)
    merged_rows, merge_summary = merge_with_2567_preference(long_60_67, annual_67)

    issues.extend(annual_67_meta["issues"])
    issues.extend(long_60_67_meta["issues"])

    unique_keys = {
        (row["area_code"], row["metric_name"], row["year_be"])
        for row in merged_rows
    }
    duplicate_keys = [
        {
            "area_code": area_code,
            "metric_name": metric_name,
            "year_be": year_be,
            "count": count,
        }
        for (area_code, metric_name, year_be), count in Counter(
            (row["area_code"], row["metric_name"], row["year_be"])
            for row in merged_rows
        ).items()
        if count > 1
    ]

    row_count_by_year = Counter(str(row["year_be"]) for row in merged_rows)
    row_count_by_metric = Counter(str(row["metric_name"]) for row in merged_rows)
    row_count_by_area = Counter(str(row["area_code"]) for row in merged_rows)
    malformed_rows = [
        row
        for row in merged_rows
        if metric_key(row["metric_name"]) not in METRIC_SPECS
        or not str(row["year_be"]).isdigit()
        or not normalize_text(row["area_code"])
    ]
    expected_area_blocks = 77
    expected_metric_rows_per_sheet = expected_area_blocks * len(METRIC_SPECS)
    expected_output_rows = expected_area_blocks * len(METRIC_SPECS) * len(EXPECTED_YEARS_BE)

    if annual_67_meta["summary"]["parsed_area_blocks"] != expected_area_blocks:
        issues.append("GPP 67 parsed area block count differs from expected 77 provinces")
    if long_60_67_meta["summary"]["parsed_area_blocks"] != expected_area_blocks:
        issues.append("GPP 60-67 parsed area block count differs from expected 77 provinces")
    if annual_67_meta["summary"]["parsed_metric_rows"] != expected_metric_rows_per_sheet:
        issues.append("GPP 67 metric row count differs from expected 231 rows")
    if long_60_67_meta["summary"]["parsed_metric_rows"] != expected_metric_rows_per_sheet:
        issues.append("GPP 60-67 metric row count differs from expected 231 rows")
    if merge_summary["cross_sheet_2567_mismatch_count"]:
        issues.append(f"{merge_summary['cross_sheet_2567_mismatch_count']} cross-sheet mismatches detected for 2567 values")
    if duplicate_keys:
        issues.append(f"{len(duplicate_keys)} duplicate grain keys detected in merged silver output")
    if malformed_rows:
        issues.append(f"{len(malformed_rows)} malformed rows detected in merged silver output")
    if len(merged_rows) != expected_output_rows:
        issues.append(
            f"Merged silver output row count {len(merged_rows)} differs from expected {expected_output_rows}"
        )
    if any(row_count_by_year.get(year, 0) != expected_area_blocks * len(METRIC_SPECS) for year in EXPECTED_YEARS_BE):
        issues.append("Year expansion counts are uneven across 2560-2567")
    if any(count != len(EXPECTED_YEARS_BE) * len(METRIC_SPECS) for count in row_count_by_area.values()):
        issues.append("Area-level row counts are uneven after block unfolding")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(OUTPUT_CSV_PATH, merged_rows)

    report.update(
        {
            "status": "ok" if not issues else "warning",
            "issues": issues,
            "normalized_grain": "one row per area_code_or_area_label + metric_name + year",
            "output_schema": OUTPUT_HEADERS,
            "input_row_counts": {
                "gpp_67_raw_rows_including_header": len(gpp67_rows),
                "gpp_60_67_raw_rows_including_header": len(gpp60_67_rows),
            },
            "output_row_count": len(merged_rows),
            "validation": {
                "expected_area_blocks": expected_area_blocks,
                "expected_metric_rows_per_sheet": expected_metric_rows_per_sheet,
                "expected_output_rows": expected_output_rows,
                "gpp_67": annual_67_meta["summary"],
                "gpp_60_67": long_60_67_meta["summary"],
                "merge": merge_summary,
                "unique_key_count": len(unique_keys),
                "duplicate_keys": duplicate_keys,
                "row_count_by_year": dict(sorted(row_count_by_year.items())),
                "row_count_by_metric": dict(sorted(row_count_by_metric.items())),
                "row_count_by_area_sample": dict(list(sorted(row_count_by_area.items()))[:10]),
                "malformed_rows": malformed_rows[:20],
                "manifest_header_checks": {
                    "gpp_67_expected": EXPECTED_GPP67_HEADERS,
                    "gpp_60_67_expected": EXPECTED_GPP60_67_HEADERS,
                },
                "location_lookup_count": len(location_lookup),
            },
        }
    )

    OUTPUT_REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
