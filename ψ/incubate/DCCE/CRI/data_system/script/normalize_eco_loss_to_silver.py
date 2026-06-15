#!/usr/bin/env python3
r"""
Normalize the Eco loss bronze hazard-sheet extracts into Silver-ready annual and period-total fact tables.

Run from project root with the CRI data_system venv Python, for example:
    .\ψ\incubate\DCCE\CRI\data_system\.venv\Scripts\python.exe .\ψ\incubate\DCCE\CRI\data_system\script\normalize_eco_loss_to_silver.py

Outputs:
- `data/1_silver/eco_loss/silver_eco_loss_annual_long.csv`
- `data/1_silver/eco_loss/silver_eco_loss_period_total.csv`
- `data/1_silver/eco_loss/eco_loss_normalization_report.json`
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
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
    / "eco_loss_extracts"
)
MANIFEST_PATH = BRONZE_DIR / "eco-loss.manifest.json"
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
PROVINCE_LOOKUP_PATH = (
    PROJECT_ROOT
    / "ψ"
    / "incubate"
    / "DCCE"
    / "CRI"
    / "data_system"
    / "data"
    / "1_silver"
    / "dopa"
    / "province_code_lookup.csv"
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

OUTPUT_DIR = (
    PROJECT_ROOT
    / "ψ"
    / "incubate"
    / "DCCE"
    / "CRI"
    / "data_system"
    / "data"
    / "1_silver"
    / "eco_loss"
)
ANNUAL_OUTPUT_PATH = OUTPUT_DIR / "silver_eco_loss_annual_long.csv"
PERIOD_OUTPUT_PATH = OUTPUT_DIR / "silver_eco_loss_period_total.csv"
REPORT_OUTPUT_PATH = OUTPUT_DIR / "eco_loss_normalization_report.json"

SOURCE_SYSTEM = "CRI_WORKBOOK_BUNDLE"
SOURCE_DATASET = "eco_loss"
VALUE_TYPE = "amount"
UNIT = "baht"
PERIOD_COLUMN = "2560 - 2567"
YEAR_COLUMNS = [str(year) for year in range(2567, 2559, -1)]
EXPECTED_HEADERS = ["จังหวัด", *YEAR_COLUMNS, PERIOD_COLUMN]
EXPECTED_SHEET_COUNT = 3
EXPECTED_ROWS_PER_HAZARD = 81

HAZARD_SPECS = {
    "Eco loss อุทกภัย": {
        "source_file": "eco-loss-อุทกภัย.raw.csv",
        "hazard_code": "FLOOD",
        "hazard_name_en": "Flood",
        "hazard_name_th": "อุทกภัย",
        "hazard_type_source": "DDPM",
        "hazard_type_name_th": "อุทกภัย",
    },
    "Eco loss ภัยแล้ง": {
        "source_file": "eco-loss-ภัยแล้ง.raw.csv",
        "hazard_code": "DROUGHT",
        "hazard_name_en": "Drought",
        "hazard_name_th": "ภัยแล้ง",
        "hazard_type_source": "DDPM",
        "hazard_type_name_th": "ภัยแล้ง",
    },
    "Eco loss วาตภัย": {
        "source_file": "eco-loss-วาตภัย.raw.csv",
        "hazard_code": "WINDSTORM",
        "hazard_name_en": "Windstorm",
        "hazard_name_th": "วาตภัย",
        "hazard_type_source": "DDPM",
        "hazard_type_name_th": "วาตภัย",
    },
}

ANNUAL_OUTPUT_HEADERS = [
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
    "raw_value",
]

PERIOD_OUTPUT_HEADERS = [
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
    "time_scope",
    "time_scope_type",
    "time_scope_label",
    "period_start_be",
    "period_end_be",
    "value",
    "value_type",
    "unit",
    "raw_period_value",
    "raw_period_is_formula",
    "derived_from_annual_values",
    "source_system",
    "source_dataset",
    "source_file",
    "source_sheet",
    "source_row_number",
    "source_column",
]


def normalize_text(value: object) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value).strip())


def normalize_name_key(value: object) -> str:
    text = normalize_text(value)
    text = text.replace("จังหวัด", "")
    text = text.replace("จ.", "")
    text = text.replace(" ", "")
    return text.casefold()


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


def load_manifest(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        return list(csv.DictReader(fp))


def write_csv(path: Path, headers: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def load_province_lookup(path: Path) -> dict[str, dict[str, str]]:
    lookup: dict[str, dict[str, str]] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            province_name_th = normalize_text(row.get("province_name_th"))
            province_code = normalize_text(row.get("province_code"))

            # Support either the canonical location dimension or the dedicated
            # province lookup table built from the province boundary crosswalk.
            admin_level = normalize_text(row.get("admin_level")) or "province"
            location_id = normalize_text(row.get("location_id"))
            if not location_id and province_code:
                location_id = f"{province_code.zfill(2)}"

            if normalize_text(row.get("admin_level")) and admin_level != "province":
                continue
            if not province_name_th or not province_code or not location_id:
                continue
            key = normalize_name_key(province_name_th)
            if key in lookup:
                continue
            lookup[key] = {
                "province_code": province_code.zfill(2),
                "province_name_th": province_name_th,
                "location_id": location_id,
                "admin_level": admin_level,
            }
    return lookup


def should_skip_non_province_row(province_name_th: str) -> bool:
    normalized = normalize_text(province_name_th)
    if not normalized:
        return True

    skip_values = {
        "วงเงินอำนาจอธิบดี",
        "หน่วยงานในสังกัด",
        "total",
    }
    if normalized.casefold() in skip_values:
        return True

    return False


def load_canonical_hazards(path: Path) -> dict[str, dict[str, str]]:
    lookup: dict[str, dict[str, str]] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            hazard_code = normalize_text(row.get("canonical_hazard_code"))
            if not hazard_code:
                continue
            lookup[hazard_code] = {
                "canonical_hazard_code": hazard_code,
                "canonical_hazard_name_en": normalize_text(row.get("canonical_hazard_name_en")),
                "canonical_hazard_name_th": normalize_text(row.get("canonical_hazard_name_th")),
            }
    return lookup


def hazard_type_exists(path: Path, source: str, hazard_name_th: str) -> bool:
    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            if normalize_text(row.get("source")) != source:
                continue
            if normalize_text(row.get("hazard_name_from_source")) == hazard_name_th:
                return True
    return False


def validate_manifest(manifest: dict[str, object]) -> tuple[list[str], dict[str, dict[str, object]]]:
    issues: list[str] = []
    sheet_lookup: dict[str, dict[str, object]] = {}
    sheets = manifest.get("sheets")
    if not isinstance(sheets, list):
        return ["Manifest sheets structure is not a list"], sheet_lookup

    if len(sheets) != EXPECTED_SHEET_COUNT:
        issues.append(f"Manifest sheet count {len(sheets)} differs from expected {EXPECTED_SHEET_COUNT}")

    for sheet in sheets:
        if not isinstance(sheet, dict):
            issues.append("Manifest contains a non-object sheet entry")
            continue
        sheet_name = normalize_text(sheet.get("sheet_name"))
        sheet_lookup[sheet_name] = sheet
        if sheet_name not in HAZARD_SPECS:
            issues.append(f"Unexpected sheet in manifest: {sheet_name}")
            continue
        headers = sheet.get("headers")
        if headers != EXPECTED_HEADERS:
            issues.append(f"Manifest headers for {sheet_name} differ from expected contract")
        row_count = sheet.get("row_count")
        if row_count != EXPECTED_ROWS_PER_HAZARD:
            issues.append(
                f"Manifest row_count for {sheet_name} is {row_count}, expected {EXPECTED_ROWS_PER_HAZARD}"
            )
    return issues, sheet_lookup


def year_be_to_ce(year_be: str) -> str:
    return str(int(year_be) - 543)


def build_annual_record_id(province_code: str, hazard_code: str, year_be: str) -> str:
    return f"{province_code}_{hazard_code}_{year_be}"


def build_period_record_id(province_code: str, hazard_code: str, period_start_be: str, period_end_be: str) -> str:
    return f"{province_code}_{hazard_code}_{period_start_be}_{period_end_be}"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    timestamp = datetime.now(timezone.utc).isoformat()
    report: dict[str, object] = {
        "generated_at_utc": timestamp,
        "script_path": str(SCRIPT_PATH),
        "inputs": {
            "manifest": str(MANIFEST_PATH),
            "bronze_dir": str(BRONZE_DIR),
            "location_dim": str(LOCATION_DIM_PATH),
            "province_lookup": str(PROVINCE_LOOKUP_PATH),
            "hazard_canonical_dim": str(HAZARD_CANONICAL_PATH),
            "hazard_type_dim": str(HAZARD_TYPE_PATH),
        },
        "outputs": {
            "annual_csv": str(ANNUAL_OUTPUT_PATH),
            "period_csv": str(PERIOD_OUTPUT_PATH),
            "report_json": str(REPORT_OUTPUT_PATH),
        },
        "issues": [],
    }

    required_paths = [MANIFEST_PATH, LOCATION_DIM_PATH, PROVINCE_LOOKUP_PATH, HAZARD_CANONICAL_PATH, HAZARD_TYPE_PATH]
    required_paths.extend(BRONZE_DIR / spec["source_file"] for spec in HAZARD_SPECS.values())
    missing_paths = [str(path) for path in required_paths if not path.exists()]
    if missing_paths:
        report["issues"] = [f"Missing required input: {path}" for path in missing_paths]
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        REPORT_OUTPUT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        raise SystemExit(1)

    manifest = load_manifest(MANIFEST_PATH)
    manifest_issues, manifest_sheet_lookup = validate_manifest(manifest)
    province_lookup = load_province_lookup(PROVINCE_LOOKUP_PATH)
    canonical_hazards = load_canonical_hazards(HAZARD_CANONICAL_PATH)

    issues: list[str] = list(manifest_issues)
    annual_rows: list[dict[str, object]] = []
    period_rows: list[dict[str, object]] = []
    unmatched_provinces: list[dict[str, str]] = []
    province_name_mismatches: list[dict[str, str]] = []
    malformed_annual_cells: list[dict[str, str]] = []
    malformed_period_rows: list[dict[str, str]] = []
    period_formula_rows: list[dict[str, str]] = []
    period_numeric_mismatches: list[dict[str, str]] = []
    input_row_counts: dict[str, int] = {}
    annual_counts_by_hazard = Counter()
    annual_counts_by_year = Counter()
    period_counts_by_hazard = Counter()
    skipped_rows_by_hazard = Counter()
    accepted_rows_by_hazard = Counter()
    hazard_header_checks: dict[str, bool] = {}
    hazard_type_checks: dict[str, bool] = {}

    for sheet_name, spec in HAZARD_SPECS.items():
        source_file = spec["source_file"]
        bronze_path = BRONZE_DIR / source_file
        bronze_rows = load_csv_rows(bronze_path)
        input_row_counts[sheet_name] = len(bronze_rows)

        actual_headers = list(bronze_rows[0].keys()) if bronze_rows else []
        hazard_header_checks[sheet_name] = actual_headers == EXPECTED_HEADERS
        if actual_headers != EXPECTED_HEADERS:
            issues.append(f"Raw CSV headers for {sheet_name} differ from expected contract")

        if len(bronze_rows) != EXPECTED_ROWS_PER_HAZARD:
            issues.append(
                f"Raw CSV row count for {sheet_name} is {len(bronze_rows)}, expected {EXPECTED_ROWS_PER_HAZARD}"
            )

        canonical = canonical_hazards.get(spec["hazard_code"], {})
        if not canonical.get("canonical_hazard_code"):
            issues.append(f"No canonical hazard mapping found for {spec['hazard_code']}")

        hazard_type_found = hazard_type_exists(
            HAZARD_TYPE_PATH,
            spec["hazard_type_source"],
            spec["hazard_type_name_th"],
        )
        hazard_type_checks[sheet_name] = hazard_type_found
        if not hazard_type_found:
            issues.append(
                f"No hazard type mapping found for {sheet_name} using source {spec['hazard_type_source']} and name {spec['hazard_type_name_th']}"
            )

        manifest_row_number_base = int(manifest_sheet_lookup.get(sheet_name, {}).get("first_data_row_number", 2))

        for row_index, bronze_row in enumerate(bronze_rows, start=0):
            source_row_number = manifest_row_number_base + row_index
            province_name_th = normalize_text(bronze_row.get("จังหวัด"))
            if should_skip_non_province_row(province_name_th):
                skipped_rows_by_hazard[sheet_name] += 1
                malformed_period_rows.append(
                    {
                        "sheet_name": sheet_name,
                        "source_row_number": str(source_row_number),
                        "issue": "non_province_or_missing_row",
                        "province_name_th": province_name_th,
                    }
                )
                continue

            province_dim = province_lookup.get(normalize_name_key(province_name_th))
            if province_dim is None:
                skipped_rows_by_hazard[sheet_name] += 1
                unmatched_provinces.append(
                    {
                        "sheet_name": sheet_name,
                        "province_name_th": province_name_th,
                        "source_row_number": str(source_row_number),
                    }
                )
                continue

            dim_name = province_dim["province_name_th"]
            if province_name_th != dim_name:
                province_name_mismatches.append(
                    {
                        "sheet_name": sheet_name,
                        "province_name_th": province_name_th,
                        "dim_province_name_th": dim_name,
                        "source_row_number": str(source_row_number),
                    }
                )

            annual_values: list[Decimal] = []
            annual_row_valid = True
            for year_be in YEAR_COLUMNS:
                raw_value = bronze_row.get(year_be, "")
                parsed = parse_decimal(raw_value)
                if parsed is None:
                    malformed_annual_cells.append(
                        {
                            "sheet_name": sheet_name,
                            "province_name_th": province_name_th,
                            "year_be": year_be,
                            "source_row_number": str(source_row_number),
                            "raw_value": normalize_text(raw_value),
                        }
                    )
                    annual_row_valid = False
                    break
                annual_values.append(parsed)

            if not annual_row_valid:
                skipped_rows_by_hazard[sheet_name] += 1
                continue

            accepted_rows_by_hazard[sheet_name] += 1
            for year_be, parsed in zip(YEAR_COLUMNS, annual_values):
                annual_rows.append(
                    {
                        "record_id": build_annual_record_id(province_dim["province_code"], spec["hazard_code"], year_be),
                        "province_code": province_dim["province_code"],
                        "province_name_th": dim_name,
                        "location_id": province_dim["location_id"],
                        "admin_level": province_dim["admin_level"],
                        "hazard_code": spec["hazard_code"],
                        "hazard_name_en": spec["hazard_name_en"],
                        "hazard_name_th": spec["hazard_name_th"],
                        "canonical_hazard_code": canonical.get("canonical_hazard_code", ""),
                        "canonical_hazard_name_en": canonical.get("canonical_hazard_name_en", ""),
                        "canonical_hazard_name_th": canonical.get("canonical_hazard_name_th", ""),
                        "year_be": year_be,
                        "year_ce": year_be_to_ce(year_be),
                        "value": decimal_to_text(parsed),
                        "value_type": VALUE_TYPE,
                        "unit": UNIT,
                        "source_system": SOURCE_SYSTEM,
                        "source_dataset": SOURCE_DATASET,
                        "source_file": source_file,
                        "source_sheet": sheet_name,
                        "source_row_number": source_row_number,
                        "source_column": year_be,
                        "raw_value": normalize_text(bronze_row.get(year_be, "")),
                    }
                )
                annual_counts_by_hazard[spec["hazard_code"]] += 1
                annual_counts_by_year[year_be] += 1

            derived_period_total = sum(annual_values, Decimal("0"))
            raw_period_value = normalize_text(bronze_row.get(PERIOD_COLUMN, ""))
            raw_period_is_formula = raw_period_value.startswith("=")
            parsed_period_value = parse_decimal(raw_period_value)

            if raw_period_is_formula:
                period_formula_rows.append(
                    {
                        "sheet_name": sheet_name,
                        "province_name_th": province_name_th,
                        "source_row_number": str(source_row_number),
                        "raw_period_value": raw_period_value,
                    }
                )
            elif parsed_period_value is not None and parsed_period_value != derived_period_total:
                period_numeric_mismatches.append(
                    {
                        "sheet_name": sheet_name,
                        "province_name_th": province_name_th,
                        "source_row_number": str(source_row_number),
                        "raw_period_value": decimal_to_text(parsed_period_value),
                        "derived_period_value": decimal_to_text(derived_period_total),
                    }
                )
            elif not raw_period_is_formula and parsed_period_value is None:
                malformed_period_rows.append(
                    {
                        "sheet_name": sheet_name,
                        "province_name_th": province_name_th,
                        "source_row_number": str(source_row_number),
                        "issue": "period_total_not_numeric_or_formula",
                        "raw_period_value": raw_period_value,
                    }
                )

            period_rows.append(
                {
                    "record_id": build_period_record_id(province_dim["province_code"], spec["hazard_code"], "2560", "2567"),
                    "province_code": province_dim["province_code"],
                    "province_name_th": dim_name,
                    "location_id": province_dim["location_id"],
                    "admin_level": province_dim["admin_level"],
                    "hazard_code": spec["hazard_code"],
                    "hazard_name_en": spec["hazard_name_en"],
                    "hazard_name_th": spec["hazard_name_th"],
                    "canonical_hazard_code": canonical.get("canonical_hazard_code", ""),
                    "canonical_hazard_name_en": canonical.get("canonical_hazard_name_en", ""),
                    "canonical_hazard_name_th": canonical.get("canonical_hazard_name_th", ""),
                    "time_scope": "range_2560_2567",
                    "time_scope_type": "multi_year_range",
                    "time_scope_label": "2560-2567",
                    "period_start_be": "2560",
                    "period_end_be": "2567",
                    "value": decimal_to_text(derived_period_total),
                    "value_type": VALUE_TYPE,
                    "unit": UNIT,
                    "raw_period_value": raw_period_value,
                    "raw_period_is_formula": str(raw_period_is_formula).lower(),
                    "derived_from_annual_values": "true",
                    "source_system": SOURCE_SYSTEM,
                    "source_dataset": SOURCE_DATASET,
                    "source_file": source_file,
                    "source_sheet": sheet_name,
                    "source_row_number": source_row_number,
                    "source_column": PERIOD_COLUMN,
                }
            )
            period_counts_by_hazard[spec["hazard_code"]] += 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(ANNUAL_OUTPUT_PATH, ANNUAL_OUTPUT_HEADERS, annual_rows)
    write_csv(PERIOD_OUTPUT_PATH, PERIOD_OUTPUT_HEADERS, period_rows)

    annual_unique_keys = {
        (row["province_code"], row["hazard_code"], row["year_be"])
        for row in annual_rows
    }
    annual_duplicate_keys = [
        {
            "province_code": province_code,
            "hazard_code": hazard_code,
            "year_be": year_be,
            "count": count,
        }
        for (province_code, hazard_code, year_be), count in Counter(
            (row["province_code"], row["hazard_code"], row["year_be"])
            for row in annual_rows
        ).items()
        if count > 1
    ]
    period_unique_keys = {
        (row["province_code"], row["hazard_code"], row["period_start_be"], row["period_end_be"])
        for row in period_rows
    }
    period_duplicate_keys = [
        {
            "province_code": province_code,
            "hazard_code": hazard_code,
            "period_start_be": period_start_be,
            "period_end_be": period_end_be,
            "count": count,
        }
        for (province_code, hazard_code, period_start_be, period_end_be), count in Counter(
            (row["province_code"], row["hazard_code"], row["period_start_be"], row["period_end_be"])
            for row in period_rows
        ).items()
        if count > 1
    ]

    expected_accepted_rows = EXPECTED_ROWS_PER_HAZARD * EXPECTED_SHEET_COUNT
    expected_annual_rows = expected_accepted_rows * len(YEAR_COLUMNS)
    expected_period_rows = expected_accepted_rows

    if unmatched_provinces:
        issues.append(f"{len(unmatched_provinces)} province rows could not join to dim_location_master")
    if province_name_mismatches:
        issues.append(f"{len(province_name_mismatches)} province names normalized to dim values")
    if malformed_annual_cells:
        issues.append(f"{len(malformed_annual_cells)} annual value cells could not be parsed as decimals")
    if malformed_period_rows:
        issues.append(f"{len(malformed_period_rows)} period total rows were malformed")
    if period_numeric_mismatches:
        issues.append(f"{len(period_numeric_mismatches)} numeric period totals differed from derived annual sums")
    if annual_duplicate_keys:
        issues.append(f"{len(annual_duplicate_keys)} duplicate annual grain keys detected")
    if period_duplicate_keys:
        issues.append(f"{len(period_duplicate_keys)} duplicate period grain keys detected")
    if len(annual_rows) != expected_annual_rows:
        issues.append(f"Annual output row count {len(annual_rows)} differs from expected {expected_annual_rows}")
    if len(period_rows) != expected_period_rows:
        issues.append(f"Period output row count {len(period_rows)} differs from expected {expected_period_rows}")
    if any(annual_counts_by_year.get(year_be, 0) != expected_accepted_rows for year_be in YEAR_COLUMNS):
        issues.append("Annual row expansion counts are uneven across years 2560-2567")

    annual_counts_by_hazard_year: dict[str, dict[str, int]] = defaultdict(dict)
    for hazard_code in sorted({spec["hazard_code"] for spec in HAZARD_SPECS.values()}):
        for year_be in YEAR_COLUMNS:
            annual_counts_by_hazard_year[hazard_code][year_be] = sum(
                1
                for row in annual_rows
                if row["hazard_code"] == hazard_code and row["year_be"] == year_be
            )

    report.update(
        {
            "status": "ok" if not issues else "warning",
            "issues": issues,
            "normalized_schema": {
                "annual": ANNUAL_OUTPUT_HEADERS,
                "period_total": PERIOD_OUTPUT_HEADERS,
            },
            "normalized_grain": {
                "annual": "one row per province + hazard + year",
                "period_total": "one row per province + hazard + period",
            },
            "input_row_counts": input_row_counts,
            "output_row_counts": {
                "annual": len(annual_rows),
                "period_total": len(period_rows),
            },
            "validation": {
                "manifest_headers_expected": EXPECTED_HEADERS,
                "hazard_header_contract_matches": hazard_header_checks,
                "hazard_type_join_ready": hazard_type_checks,
                "province_lookup_count": len(province_lookup),
                "accepted_rows_by_hazard": dict(accepted_rows_by_hazard),
                "skipped_rows_by_hazard": dict(skipped_rows_by_hazard),
                "annual_counts_by_hazard": dict(annual_counts_by_hazard),
                "annual_counts_by_year": dict(sorted(annual_counts_by_year.items())),
                "annual_counts_by_hazard_year": annual_counts_by_hazard_year,
                "period_counts_by_hazard": dict(period_counts_by_hazard),
                "expected_rows": {
                    "per_hazard_input": EXPECTED_ROWS_PER_HAZARD,
                    "accepted_total_rows": expected_accepted_rows,
                    "annual_output": expected_annual_rows,
                    "period_total_output": expected_period_rows,
                },
                "formula_handling": {
                    "period_formula_row_count": len(period_formula_rows),
                    "period_formula_rows_sample": period_formula_rows[:20],
                    "numeric_period_mismatch_count": len(period_numeric_mismatches),
                    "numeric_period_mismatches_sample": period_numeric_mismatches[:20],
                    "policy": "Bronze preserves raw formulas; Silver derives period totals from annual values and compares against any numeric period totals",
                },
                "province_join_readiness": {
                    "unmatched_province_count": len(unmatched_provinces),
                    "unmatched_provinces_sample": unmatched_provinces[:20],
                    "province_name_mismatch_count": len(province_name_mismatches),
                    "province_name_mismatches_sample": province_name_mismatches[:20],
                },
                "malformed_rows": {
                    "annual_cell_count": len(malformed_annual_cells),
                    "annual_cells_sample": malformed_annual_cells[:20],
                    "period_row_count": len(malformed_period_rows),
                    "period_rows_sample": malformed_period_rows[:20],
                },
                "duplicate_keys": {
                    "annual_count": len(annual_duplicate_keys),
                    "annual_sample": annual_duplicate_keys[:20],
                    "period_count": len(period_duplicate_keys),
                    "period_sample": period_duplicate_keys[:20],
                },
                "unique_key_counts": {
                    "annual": len(annual_unique_keys),
                    "period_total": len(period_unique_keys),
                },
            },
        }
    )

    REPORT_OUTPUT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
