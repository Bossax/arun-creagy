#!/usr/bin/env python3
r"""
Normalize the Population bronze extracts into Silver-ready monthly, annual,
and period-total fact tables.

Run from project root with the CRI data_system venv Python, for example:
    .\ψ\incubate\DCCE\CRI\data_system\.venv\Scripts\python.exe .\ψ\incubate\DCCE\CRI\data_system\script\normalize_population_to_silver.py

Outputs:
- `data/1_silver/population/silver_population_monthly.csv`
- `data/1_silver/population/silver_population_annual.csv`
- `data/1_silver/population/silver_population_period_total.csv`
- `data/1_silver/population/population_normalization_report.json`
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
    / "population_extracts"
)
POP67_PATH = BRONZE_DIR / "pop67.raw.csv"
POP60_67_PATH = BRONZE_DIR / "pop60-67.raw.csv"
MANIFEST_PATH = BRONZE_DIR / "population.manifest.json"

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

OUTPUT_DIR = (
    PROJECT_ROOT
    / "ψ"
    / "incubate"
    / "DCCE"
    / "CRI"
    / "data_system"
    / "data"
    / "1_silver"
    / "population"
)
MONTHLY_OUTPUT_PATH = OUTPUT_DIR / "silver_population_monthly.csv"
ANNUAL_OUTPUT_PATH = OUTPUT_DIR / "silver_population_annual.csv"
PERIOD_OUTPUT_PATH = OUTPUT_DIR / "silver_population_period_total.csv"
REPORT_OUTPUT_PATH = OUTPUT_DIR / "population_normalization_report.json"
HOUSEHOLD_ANNUAL_OUTPUT_PATH = OUTPUT_DIR / "silver_household_annual.csv"

SOURCE_SYSTEM = "CRI_WORKBOOK_BUNDLE"
SOURCE_DATASET = "population"
SOURCE_FILE_MONTHLY = "pop67.raw.csv"
SOURCE_FILE_ANNUAL = "pop60-67.raw.csv"
SOURCE_SHEET_MONTHLY = "pop67"
SOURCE_SHEET_ANNUAL = "pop60-67"
PERIOD_LABEL = "2560-2567"
PERIOD_COLUMN = "2560 - 2567"
ANNUAL_YEAR_COLUMNS = [str(year) for year in range(2567, 2559, -1)]

EXPECTED_POP67_HEADERS = [
    "ปีเดือน",
    "รหัสจังหวัด",
    "ชื่อจังหวัด",
    "รหัสสำนักทะเบียน",
    "ชื่อสำนักทะเบียน",
    "รหัสตำบล",
    "รหัสตำบล_2",
    "ชื่อตำบล",
    "จำนวนประชากรชาย",
    "จำนวนประชากรหญิง",
    "จำนวนประชากรทั้งหมด",
]

EXPECTED_POP60_67_HEADERS = [
    "รหัสจังหวัด",
    "ชื่อจังหวัด",
    "รหัสสำนักทะเบียน",
    "ชื่อสำนักทะเบียน",
    "รหัสตำบล",
    "รหัสตำบล_2",
    "ชื่อตำบล",
    *ANNUAL_YEAR_COLUMNS,
    PERIOD_COLUMN,
]

MONTHLY_HEADERS = [
    "record_id",
    "record_class",
    "geography_key",
    "geography_level",
    "province_code",
    "province_name_th",
    "registration_office_code",
    "registration_office_name_th",
    "subdistrict_code",
    "subdistrict_name_th",
    "location_id",
    "admin_level",
    "geography_join_ready",
    "year_month",
    "year_be",
    "year_ce",
    "month",
    "population_male",
    "population_female",
    "population_total",
    "raw_subdistrict_code_formula",
    "raw_subdistrict_code_duplicate",
    "subdistrict_code_derivation_method",
    "source_system",
    "source_dataset",
    "source_file",
    "source_sheet",
    "source_row_number",
]

ANNUAL_HEADERS = [
    "record_id",
    "record_class",
    "geography_key",
    "geography_level",
    "province_code",
    "province_name_th",
    "registration_office_code",
    "registration_office_name_th",
    "subdistrict_code",
    "subdistrict_name_th",
    "location_id",
    "admin_level",
    "geography_join_ready",
    "year_be",
    "year_ce",
    "population_total",
    "raw_subdistrict_code_formula",
    "raw_subdistrict_code_duplicate",
    "subdistrict_code_derivation_method",
    "source_system",
    "source_dataset",
    "source_file",
    "source_sheet",
    "source_row_number",
    "source_column",
]

PERIOD_HEADERS = [
    "record_id",
    "record_class",
    "geography_key",
    "geography_level",
    "province_code",
    "province_name_th",
    "registration_office_code",
    "registration_office_name_th",
    "subdistrict_code",
    "subdistrict_name_th",
    "location_id",
    "admin_level",
    "geography_join_ready",
    "time_scope",
    "time_scope_type",
    "time_scope_label",
    "period_start_be",
    "period_end_be",
    "population_total",
    "annual_sum_population_total",
    "annual_sum_matches_period_total",
    "raw_subdistrict_code_formula",
    "raw_subdistrict_code_duplicate",
    "subdistrict_code_derivation_method",
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


def normalize_digits(value: object) -> str:
    return re.sub(r"\D", "", normalize_text(value))


def parse_int(value: object) -> int | None:
    text = normalize_text(value).replace(",", "")
    if not text or text.startswith("="):
        return None
    if not re.fullmatch(r"[-+]?\d+(?:\.0+)?", text):
        return None
    return int(float(text))


def write_csv(path: Path, headers: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def load_manifest(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_csv_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        return list(reader.fieldnames or []), list(reader)


def normalize_province_name_key(value: object) -> str:
    return normalize_text(value).replace(" ", "").casefold()


def load_province_lookup(path: Path) -> dict[str, dict[str, str]]:
    lookup: dict[str, dict[str, str]] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            province_code = normalize_digits(row.get("province_code")).zfill(2)
            province_name_th = normalize_text(row.get("province_name_th"))
            if not province_code or not province_name_th:
                continue
            lookup[province_code] = {
                "province_code": province_code,
                "province_name_th": province_name_th,
                "location_id": province_code,
                "admin_level": "province",
            }
            lookup.setdefault(normalize_province_name_key(province_name_th), lookup[province_code])
    return lookup


def load_location_lookup(path: Path) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    province_lookup: dict[str, dict[str, str]] = {}
    subdistrict_lookup: dict[str, dict[str, str]] = {}

    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            admin_level = normalize_text(row.get("admin_level")).casefold()
            province_code = normalize_digits(row.get("province_code")).zfill(2)
            province_name_th = normalize_text(row.get("province_name_th"))
            location_id = normalize_text(row.get("location_id"))

            if admin_level == "province" and province_code and province_code not in province_lookup:
                province_lookup[province_code] = {
                    "province_code": province_code,
                    "province_name_th": province_name_th,
                    "location_id": location_id or province_code,
                    "admin_level": "province",
                }

            if admin_level != "subdistrict":
                continue

            subdistrict_code = normalize_digits(row.get("subdistrict_code"))
            subdistrict_name_th = normalize_text(row.get("subdistrict_name_th"))
            if not subdistrict_code or subdistrict_code in subdistrict_lookup:
                continue
            subdistrict_lookup[subdistrict_code] = {
                "province_code": province_code,
                "province_name_th": province_name_th,
                "subdistrict_code": subdistrict_code,
                "subdistrict_name_th": subdistrict_name_th,
                "location_id": location_id or subdistrict_code,
                "admin_level": "subdistrict",
            }

    return province_lookup, subdistrict_lookup


def validate_manifest_headers(manifest: dict[str, object], issues: list[str]) -> None:
    sheets = manifest.get("sheets")
    if not isinstance(sheets, list):
        issues.append("Manifest sheets structure is not a list")
        return

    by_name = {
        normalize_text(sheet.get("sheet_name")): sheet
        for sheet in sheets
        if isinstance(sheet, dict)
    }

    pop67 = by_name.get(SOURCE_SHEET_MONTHLY)
    pop60_67 = by_name.get(SOURCE_SHEET_ANNUAL)

    if not isinstance(pop67, dict):
        issues.append("Manifest missing pop67 metadata")
    elif pop67.get("headers") != EXPECTED_POP67_HEADERS:
        issues.append("Manifest headers for pop67 differ from expected contract")

    if not isinstance(pop60_67, dict):
        issues.append("Manifest missing pop60-67 metadata")
    elif pop60_67.get("headers") != EXPECTED_POP60_67_HEADERS:
        issues.append("Manifest headers for pop60-67 differ from expected contract")


def validate_csv_headers(actual: list[str], expected: list[str], label: str, issues: list[str]) -> None:
    if actual != expected:
        issues.append(f"{label} headers differ from expected contract")
    missing = [header for header in expected if header not in actual]
    if missing:
        issues.append(f"{label} missing expected headers: {missing}")


def parse_year_month(value: str) -> tuple[str, str, str] | None:
    text = normalize_digits(value)
    if len(text) != 4:
        return None
    yy = int(text[:2])
    month = int(text[2:])
    if month < 1 or month > 12:
        return None
    year_be = str(2500 + yy)
    year_ce = str(int(year_be) - 543)
    return text, year_be, year_ce


def derive_subdistrict_code(raw_formula: str, raw_duplicate: str) -> tuple[str, str, bool]:
    duplicate_digits = normalize_digits(raw_duplicate)
    formula_digits = normalize_digits(raw_formula)

    duplicate_code = duplicate_digits[:6] if len(duplicate_digits) >= 6 else ""
    formula_code = formula_digits[:6] if len(formula_digits) >= 6 else ""

    conflict = bool(duplicate_code and formula_code and duplicate_code != formula_code)

    if duplicate_code:
        return duplicate_code, "duplicate_field_first6", conflict
    if formula_code:
        return formula_code, "formula_digits_first6", conflict
    if raw_formula.startswith("=") and duplicate_digits == "0":
        return "", "formula_resolves_to_aggregate", conflict
    if duplicate_digits == "0":
        return "", "aggregate_zero_duplicate", conflict
    return "", "unresolved", conflict


def classify_geography(
    province_code: str,
    registration_office_code: str,
    subdistrict_code: str,
    subdistrict_name_th: str,
) -> tuple[str, str]:
    if province_code == "00":
        return "country", "THA"
    if subdistrict_code:
        return "subdistrict", f"THA-SD-{subdistrict_code}"
    if registration_office_code and registration_office_code != "0000" and subdistrict_name_th in {"", "-"}:
        return "registration_office", f"THA-RO-{registration_office_code}"
    return "province", f"THA-PV-{province_code}"


def build_signature_key(province_code: str, registration_office_code: str, subdistrict_code: str) -> str:
    return "|".join(
        [
            province_code or "",
            registration_office_code or "",
            subdistrict_code or "",
        ]
    )


def analyze_subdistrict_collisions(*row_groups: list[dict[str, str]]) -> dict[str, dict[str, object]]:
    by_subdistrict: dict[str, set[str]] = {}

    for rows in row_groups:
        for row in rows:
            province_code_raw = normalize_digits(row.get("รหัสจังหวัด"))
            province_code = province_code_raw.zfill(2) if province_code_raw else ""
            registration_office_code_raw = normalize_digits(row.get("รหัสสำนักทะเบียน"))
            registration_office_code = (
                registration_office_code_raw.zfill(4) if registration_office_code_raw else ""
            )
            subdistrict_code, _, _ = derive_subdistrict_code(
                normalize_text(row.get("รหัสตำบล")),
                normalize_text(row.get("รหัสตำบล_2")),
            )
            if not subdistrict_code:
                continue
            signature = build_signature_key(
                province_code=province_code,
                registration_office_code=registration_office_code,
                subdistrict_code=subdistrict_code,
            )
            by_subdistrict.setdefault(subdistrict_code, set()).add(signature)

    collisions: dict[str, dict[str, object]] = {}
    for subdistrict_code, signatures in by_subdistrict.items():
        if len(signatures) <= 1:
            continue
        collisions[subdistrict_code] = {
            "signature_count": len(signatures),
            "signatures": sorted(signatures),
        }
    return collisions


def enrich_geography(
    base: dict[str, str],
    province_lookup: dict[str, dict[str, str]],
    dim_province_lookup: dict[str, dict[str, str]],
    subdistrict_lookup: dict[str, dict[str, str]],
) -> tuple[dict[str, str], list[str]]:
    issues: list[str] = []
    province_code = base["province_code"]
    subdistrict_code = base["subdistrict_code"]
    geography_level = base["geography_level"]

    location_id = ""
    admin_level = geography_level
    geography_join_ready = "false"

    province_ref = dim_province_lookup.get(province_code) or province_lookup.get(province_code)
    if province_ref:
        if not base["province_name_th"]:
            base["province_name_th"] = province_ref.get("province_name_th", "")

    if geography_level == "country":
        location_id = "THA"
        admin_level = "country"
        geography_join_ready = "true"
    elif geography_level == "province":
        if province_ref:
            location_id = province_ref.get("location_id", province_code)
            admin_level = "province"
            geography_join_ready = "true"
        else:
            issues.append(f"Province code {province_code} missing from province lookup")
    elif geography_level == "subdistrict":
        subdistrict_ref = subdistrict_lookup.get(subdistrict_code)
        if subdistrict_ref:
            location_id = subdistrict_ref.get("location_id", subdistrict_code)
            admin_level = "subdistrict"
            geography_join_ready = "true"
            if subdistrict_ref.get("province_code") and subdistrict_ref.get("province_code") != province_code:
                issues.append(
                    f"Subdistrict code {subdistrict_code} joins to province {subdistrict_ref.get('province_code')} but bronze province is {province_code}"
                )
        else:
            issues.append(f"Subdistrict code {subdistrict_code} missing from location dimension")
    else:
        admin_level = "registration_office"

    base["location_id"] = location_id
    base["admin_level"] = admin_level
    base["geography_join_ready"] = geography_join_ready
    return base, issues


def build_base_geography_row(
    row: dict[str, str],
    province_lookup: dict[str, dict[str, str]],
    dim_province_lookup: dict[str, dict[str, str]],
    subdistrict_lookup: dict[str, dict[str, str]],
    colliding_subdistricts: dict[str, dict[str, object]],
) -> tuple[dict[str, str], list[str], bool]:
    issues: list[str] = []

    province_code_raw = normalize_digits(row.get("รหัสจังหวัด"))
    province_code = province_code_raw.zfill(2) if province_code_raw else ""
    province_name_th = normalize_text(row.get("ชื่อจังหวัด"))
    registration_office_code_raw = normalize_digits(row.get("รหัสสำนักทะเบียน"))
    registration_office_code = registration_office_code_raw.zfill(4) if registration_office_code_raw else ""
    registration_office_name_th = normalize_text(row.get("ชื่อสำนักทะเบียน"))
    raw_formula = normalize_text(row.get("รหัสตำบล"))
    raw_duplicate = normalize_text(row.get("รหัสตำบล_2"))
    subdistrict_name_th = normalize_text(row.get("ชื่อตำบล"))

    subdistrict_code, derivation_method, has_conflict = derive_subdistrict_code(raw_formula, raw_duplicate)
    if has_conflict:
        issues.append(
            f"Conflicting derived subdistrict codes between raw formula '{raw_formula}' and duplicate field '{raw_duplicate}'"
        )

    if not province_code:
        issues.append("Missing province code")
    if not province_name_th and province_code != "00":
        issues.append("Missing province name")

    geography_level, geography_key = classify_geography(
        province_code=province_code or "",
        registration_office_code=registration_office_code or "",
        subdistrict_code=subdistrict_code,
        subdistrict_name_th=subdistrict_name_th,
    )

    record_class = geography_level
    collision_info = colliding_subdistricts.get(subdistrict_code)
    if geography_level == "subdistrict" and collision_info is not None:
        record_class = "subdistrict_registration_office"
        geography_key = f"THA-SDRO-{province_code}-{registration_office_code}-{subdistrict_code}"
        issues.append(
            "Subdistrict code is reused across multiple province/registration-office signatures; silver grain separated by registration office"
        )

    base = {
        "record_class": record_class,
        "geography_key": geography_key,
        "geography_level": geography_level,
        "province_code": province_code,
        "province_name_th": province_name_th,
        "registration_office_code": registration_office_code,
        "registration_office_name_th": registration_office_name_th,
        "subdistrict_code": subdistrict_code,
        "subdistrict_name_th": "" if subdistrict_name_th == "-" else subdistrict_name_th,
        "raw_subdistrict_code_formula": raw_formula,
        "raw_subdistrict_code_duplicate": raw_duplicate,
        "subdistrict_code_derivation_method": derivation_method,
        "location_id": "",
        "admin_level": "",
        "geography_join_ready": "false",
    }

    base, enrich_issues = enrich_geography(
        base=base,
        province_lookup=province_lookup,
        dim_province_lookup=dim_province_lookup,
        subdistrict_lookup=subdistrict_lookup,
    )
    issues.extend(enrich_issues)

    is_malformed = bool(issues and province_code != "00")
    return base, issues, is_malformed


def parse_monthly_rows(
    rows: list[dict[str, str]],
    province_lookup: dict[str, dict[str, str]],
    dim_province_lookup: dict[str, dict[str, str]],
    subdistrict_lookup: dict[str, dict[str, str]],
    colliding_subdistricts: dict[str, dict[str, object]],
) -> tuple[list[dict[str, object]], dict[str, object]]:
    normalized_rows: list[dict[str, object]] = []
    malformed_rows: list[dict[str, object]] = []
    issue_counter: Counter[str] = Counter()
    geography_counter: Counter[str] = Counter()
    derivation_counter: Counter[str] = Counter()
    monthly_balance_failures = 0

    for row_number, row in enumerate(rows, start=2):
        base, issues, is_malformed = build_base_geography_row(
            row=row,
            province_lookup=province_lookup,
            dim_province_lookup=dim_province_lookup,
            subdistrict_lookup=subdistrict_lookup,
            colliding_subdistricts=colliding_subdistricts,
        )

        parsed_year_month = parse_year_month(normalize_text(row.get("ปีเดือน")))
        male = parse_int(row.get("จำนวนประชากรชาย"))
        female = parse_int(row.get("จำนวนประชากรหญิง"))
        total = parse_int(row.get("จำนวนประชากรทั้งหมด"))

        if parsed_year_month is None:
            issues.append("Invalid year_month value")
        if male is None:
            issues.append("Invalid male population value")
        if female is None:
            issues.append("Invalid female population value")
        if total is None:
            issues.append("Invalid total population value")
        if male is not None and female is not None and total is not None and male + female != total:
            issues.append("Male + female does not equal total population")
            monthly_balance_failures += 1

        for issue in issues:
            issue_counter[issue] += 1

        derivation_counter[base["subdistrict_code_derivation_method"]] += 1

        if issues:
            malformed_rows.append(
                {
                    "source_row_number": row_number,
                    "geography_key": base["geography_key"],
                    "issues": issues,
                }
            )

        if parsed_year_month is None or male is None or female is None or total is None:
            continue

        year_month, year_be, year_ce = parsed_year_month
        geography_counter[base["geography_level"]] += 1

        record = {
            **base,
            "record_id": f"{base['geography_key']}_{year_month}",
            "year_month": year_month,
            "year_be": year_be,
            "year_ce": year_ce,
            "month": year_month[2:],
            "population_male": male,
            "population_female": female,
            "population_total": total,
            "source_system": SOURCE_SYSTEM,
            "source_dataset": SOURCE_DATASET,
            "source_file": SOURCE_FILE_MONTHLY,
            "source_sheet": SOURCE_SHEET_MONTHLY,
            "source_row_number": row_number,
        }
        normalized_rows.append(record)

    summary = {
        "input_rows": len(rows),
        "output_rows": len(normalized_rows),
        "rows_by_geography_level": dict(geography_counter),
        "subdistrict_code_derivation_methods": dict(derivation_counter),
        "monthly_balance_failures": monthly_balance_failures,
        "malformed_row_count": len(malformed_rows),
        "malformed_row_samples": malformed_rows[:20],
        "issue_counts": dict(issue_counter),
    }
    return normalized_rows, summary


def parse_annual_rows(
    rows: list[dict[str, str]],
    province_lookup: dict[str, dict[str, str]],
    dim_province_lookup: dict[str, dict[str, str]],
    subdistrict_lookup: dict[str, dict[str, str]],
    colliding_subdistricts: dict[str, dict[str, object]],
) -> tuple[list[dict[str, object]], list[dict[str, object]], dict[str, object]]:
    annual_rows: list[dict[str, object]] = []
    period_rows: list[dict[str, object]] = []
    malformed_rows: list[dict[str, object]] = []
    issue_counter: Counter[str] = Counter()
    annual_geography_counter: Counter[str] = Counter()
    period_geography_counter: Counter[str] = Counter()
    derivation_counter: Counter[str] = Counter()
    annual_period_mismatch_count = 0

    for row_number, row in enumerate(rows, start=2):
        base, issues, _ = build_base_geography_row(
            row=row,
            province_lookup=province_lookup,
            dim_province_lookup=dim_province_lookup,
            subdistrict_lookup=subdistrict_lookup,
            colliding_subdistricts=colliding_subdistricts,
        )
        derivation_counter[base["subdistrict_code_derivation_method"]] += 1

        annual_values: list[int] = []
        annual_value_map: dict[str, int] = {}
        for year_be in ANNUAL_YEAR_COLUMNS:
            value = parse_int(row.get(year_be))
            if value is None:
                issues.append(f"Invalid annual population value for {year_be}")
                continue
            annual_values.append(value)
            annual_value_map[year_be] = value

        period_total = parse_int(row.get(PERIOD_COLUMN))
        if period_total is None:
            issues.append("Invalid period total value")

        if len(annual_values) == len(ANNUAL_YEAR_COLUMNS) and period_total is not None:
            annual_sum = sum(annual_values)
            if annual_sum != period_total:
                issues.append("Annual sum does not equal 2560 - 2567 total")
                annual_period_mismatch_count += 1
        else:
            annual_sum = None

        for issue in issues:
            issue_counter[issue] += 1

        if issues:
            malformed_rows.append(
                {
                    "source_row_number": row_number,
                    "geography_key": base["geography_key"],
                    "issues": issues,
                }
            )

        for year_be, value in annual_value_map.items():
            annual_geography_counter[base["geography_level"]] += 1
            annual_rows.append(
                {
                    **base,
                    "record_id": f"{base['geography_key']}_{year_be}",
                    "year_be": year_be,
                    "year_ce": str(int(year_be) - 543),
                    "population_total": value,
                    "source_system": SOURCE_SYSTEM,
                    "source_dataset": SOURCE_DATASET,
                    "source_file": SOURCE_FILE_ANNUAL,
                    "source_sheet": SOURCE_SHEET_ANNUAL,
                    "source_row_number": row_number,
                    "source_column": year_be,
                }
            )

        if period_total is not None:
            period_geography_counter[base["geography_level"]] += 1
            period_rows.append(
                {
                    **base,
                    "record_id": f"{base['geography_key']}_{PERIOD_LABEL}",
                    "time_scope": "range_2560_2567",
                    "time_scope_type": "multi_year_range",
                    "time_scope_label": PERIOD_LABEL,
                    "period_start_be": "2560",
                    "period_end_be": "2567",
                    "population_total": period_total,
                    "annual_sum_population_total": "" if annual_sum is None else annual_sum,
                    "annual_sum_matches_period_total": "" if annual_sum is None else str(annual_sum == period_total).lower(),
                    "source_system": SOURCE_SYSTEM,
                    "source_dataset": SOURCE_DATASET,
                    "source_file": SOURCE_FILE_ANNUAL,
                    "source_sheet": SOURCE_SHEET_ANNUAL,
                    "source_row_number": row_number,
                    "source_column": PERIOD_COLUMN,
                }
            )

    summary = {
        "input_rows": len(rows),
        "annual_output_rows": len(annual_rows),
        "period_output_rows": len(period_rows),
        "annual_rows_by_geography_level": dict(annual_geography_counter),
        "period_rows_by_geography_level": dict(period_geography_counter),
        "subdistrict_code_derivation_methods": dict(derivation_counter),
        "annual_period_mismatch_count": annual_period_mismatch_count,
        "malformed_row_count": len(malformed_rows),
        "malformed_row_samples": malformed_rows[:20],
        "issue_counts": dict(issue_counter),
    }
    return annual_rows, period_rows, summary


def count_duplicate_record_ids(rows: list[dict[str, object]]) -> int:
    counts = Counter(str(row.get("record_id")) for row in rows)
    return sum(1 for value in counts.values() if value > 1)


def summarize_collision_samples(colliding_subdistricts: dict[str, dict[str, object]], limit: int = 20) -> list[dict[str, object]]:
    samples: list[dict[str, object]] = []
    for subdistrict_code in sorted(colliding_subdistricts)[:limit]:
        collision_info = colliding_subdistricts[subdistrict_code]
        samples.append(
            {
                "subdistrict_code": subdistrict_code,
                "signature_count": collision_info["signature_count"],
                "signatures": collision_info["signatures"],
            }
        )
    return samples


def normalize_dopa_household_population() -> None:
    import pandas as pd
    
    bronze_dir = PROJECT_ROOT / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system" / "data" / "0_bronze" / "dopa"
    records = []

    for year_num in range(60, 68):
        year_str = str(year_num)
        path = bronze_dir / f"bronze_dopa_population_pop{year_str}.csv"
        if not path.exists():
            print(f"[WARNING] Missing DOPA population bronze file: {path}")
            continue
        
        df = pd.read_csv(path)
        
        # Standardize columns
        df["province_code"] = df["รหัสจังหวัด"].astype(str).str.replace(r"\.0$", "", regex=True).str.strip().str.zfill(2)
        df["province_name_th"] = df["ชื่อจังหวัด"].astype(str).str.strip()
        df["subdistrict_code_raw"] = df["รหัสตำบล"].astype(str).str.replace(r"\.0$", "", regex=True).str.strip()
        df["subdistrict_name_th"] = df["ชื่อตำบล"].astype(str).str.strip()
        df["subdistrict_code"] = df["subdistrict_code_raw"].str.zfill(8).str[:6]
        
        df["population_total"] = pd.to_numeric(df["จำนวนประชากรทั้งหมด"], errors="coerce").fillna(0.0)
        df["household_total"] = pd.to_numeric(df["จำนวนบ้าน (หลังคาเรือน)"], errors="coerce").fillna(0.0)
        
        # Filter subdistrict level
        df_sub = df[df["subdistrict_code"].str.fullmatch(r"\d{6}") & (df["subdistrict_code"] != "000000")].copy()
        
        df_sub["year_be"] = "25" + year_str
        
        # Group/sum to resolve split records
        df_clean = df_sub.groupby(
            ["year_be", "province_code", "province_name_th", "subdistrict_code", "subdistrict_name_th"],
            dropna=False
        ).agg(
            population_total=("population_total", "sum"),
            household_total=("household_total", "sum")
        ).reset_index()
        
        records.append(df_clean)

    if not records:
        print("[ERROR] No DOPA bronze population files found to build silver_household_annual.csv")
        return
        
    final_df = pd.concat(records, ignore_index=True)
    
    # Sort for deterministic output
    final_df = final_df.sort_values(["year_be", "province_code", "subdistrict_code"]).reset_index(drop=True)
    
    final_df.to_csv(HOUSEHOLD_ANNUAL_OUTPUT_PATH, index=False, encoding="utf-8-sig")
    print(f"Wrote {HOUSEHOLD_ANNUAL_OUTPUT_PATH}")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    report: dict[str, object] = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_path": str(SCRIPT_PATH),
        "inputs": {
            "pop67_csv_path": str(POP67_PATH),
            "pop60_67_csv_path": str(POP60_67_PATH),
            "manifest_path": str(MANIFEST_PATH),
            "location_dim_path": str(LOCATION_DIM_PATH),
            "province_lookup_path": str(PROVINCE_LOOKUP_PATH),
        },
        "outputs": {
            "monthly_output_path": str(MONTHLY_OUTPUT_PATH),
            "annual_output_path": str(ANNUAL_OUTPUT_PATH),
            "period_output_path": str(PERIOD_OUTPUT_PATH),
            "report_output_path": str(REPORT_OUTPUT_PATH),
        },
        "validation": {
            "issues": [],
        },
    }

    validation_issues: list[str] = report["validation"]["issues"]  # type: ignore[index]

    manifest = load_manifest(MANIFEST_PATH)
    validate_manifest_headers(manifest, validation_issues)

    monthly_headers, monthly_source_rows = load_csv_rows(POP67_PATH)
    annual_headers, annual_source_rows = load_csv_rows(POP60_67_PATH)

    validate_csv_headers(monthly_headers, EXPECTED_POP67_HEADERS, "pop67", validation_issues)
    validate_csv_headers(annual_headers, EXPECTED_POP60_67_HEADERS, "pop60-67", validation_issues)

    province_lookup = load_province_lookup(PROVINCE_LOOKUP_PATH)
    dim_province_lookup, subdistrict_lookup = load_location_lookup(LOCATION_DIM_PATH)
    colliding_subdistricts = analyze_subdistrict_collisions(monthly_source_rows, annual_source_rows)

    monthly_rows, monthly_summary = parse_monthly_rows(
        rows=monthly_source_rows,
        province_lookup=province_lookup,
        dim_province_lookup=dim_province_lookup,
        subdistrict_lookup=subdistrict_lookup,
        colliding_subdistricts=colliding_subdistricts,
    )
    annual_rows, period_rows, annual_summary = parse_annual_rows(
        rows=annual_source_rows,
        province_lookup=province_lookup,
        dim_province_lookup=dim_province_lookup,
        subdistrict_lookup=subdistrict_lookup,
        colliding_subdistricts=colliding_subdistricts,
    )

    write_csv(MONTHLY_OUTPUT_PATH, MONTHLY_HEADERS, monthly_rows)
    write_csv(ANNUAL_OUTPUT_PATH, ANNUAL_HEADERS, annual_rows)
    write_csv(PERIOD_OUTPUT_PATH, PERIOD_HEADERS, period_rows)
    
    # Consolidate and normalize DOPA household and population (silver_household_annual.csv)
    normalize_dopa_household_population()

    report["normalized_schema"] = {
        "monthly_grain": "one row per record_class-qualified geography + year_month",
        "annual_grain": "one row per record_class-qualified geography + year",
        "period_grain": "one row per record_class-qualified geography + period",
        "monthly_headers": MONTHLY_HEADERS,
        "annual_headers": ANNUAL_HEADERS,
        "period_headers": PERIOD_HEADERS,
    }
    report["duplicate_grain_resolution"] = {
        "colliding_subdistrict_code_count": len(colliding_subdistricts),
        "resolution_rule": "If a subdistrict code appears under multiple province/registration-office signatures in bronze, emit record_class=subdistrict_registration_office and key it by province + registration office + subdistrict code.",
        "collision_samples": summarize_collision_samples(colliding_subdistricts),
    }
    report["source_row_counts"] = {
        "pop67": len(monthly_source_rows),
        "pop60_67": len(annual_source_rows),
    }
    report["output_row_counts"] = {
        "monthly": len(monthly_rows),
        "annual": len(annual_rows),
        "period": len(period_rows),
    }
    report["validation"]["monthly_normalization"] = monthly_summary
    report["validation"]["annual_normalization"] = annual_summary
    report["validation"]["record_id_duplicate_counts"] = {
        "monthly": count_duplicate_record_ids(monthly_rows),
        "annual": count_duplicate_record_ids(annual_rows),
        "period": count_duplicate_record_ids(period_rows),
    }

    REPORT_OUTPUT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Wrote {MONTHLY_OUTPUT_PATH}")
    print(f"Wrote {ANNUAL_OUTPUT_PATH}")
    print(f"Wrote {PERIOD_OUTPUT_PATH}")
    print(f"Wrote {REPORT_OUTPUT_PATH}")


if __name__ == "__main__":
    main()
