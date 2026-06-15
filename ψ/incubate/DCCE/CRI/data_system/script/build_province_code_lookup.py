#!/usr/bin/env python3
r"""
Build a reusable province-level lookup table for Silver joins.

This table is derived from the legacy province boundary crosswalk and is intended
to support workbook-derived province-only datasets such as Government Advance Payment.

Run from project root with the CRI data_system venv Python, for example:
    .\ψ\incubate\DCCE\CRI\data_system\.venv\Scripts\python.exe .\ψ\incubate\DCCE\CRI\data_system\script\build_province_code_lookup.py
"""

from __future__ import annotations

import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parents[6]

SOURCE_PATH = (
    PROJECT_ROOT
    / "ψ"
    / "incubate"
    / "DCCE"
    / "CRI"
    / "data_system"
    / "archive_stage3_legacy"
    / "data"
    / "1_silver"
    / "stage3_dopa_province_boundary_code_crosswalk.csv"
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
    / "dopa"
)

OUTPUT_CSV = OUTPUT_DIR / "province_code_lookup.csv"
OUTPUT_REPORT = OUTPUT_DIR / "province_code_lookup_report.json"

OUTPUT_HEADERS = [
    "province_name_norm",
    "province_code",
    "province_name_th",
    "province_name_en",
    "match_status",
    "lookup_source",
]


def normalize_text(value: object) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value).strip())


def write_csv(path: Path, headers: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if not SOURCE_PATH.exists():
        raise SystemExit(f"Source file not found: {SOURCE_PATH}")

    rows: list[dict[str, object]] = []
    duplicate_norms: dict[str, int] = {}

    with SOURCE_PATH.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            province_name_norm = normalize_text(row.get("province_name_norm"))
            province_code = normalize_text(row.get("province_code")).zfill(2)
            province_name_th = normalize_text(row.get("province_name_th"))
            province_name_en = normalize_text(row.get("P_NAME_E"))
            match_status = normalize_text(row.get("match_status"))

            if not province_name_norm or not province_code or not province_name_th:
                continue

            duplicate_norms[province_name_norm] = duplicate_norms.get(province_name_norm, 0) + 1

            rows.append(
                {
                    "province_name_norm": province_name_norm,
                    "province_code": province_code,
                    "province_name_th": province_name_th,
                    "province_name_en": province_name_en,
                    "match_status": match_status,
                    "lookup_source": SOURCE_PATH.name,
                }
            )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(OUTPUT_CSV, OUTPUT_HEADERS, rows)

    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_path": str(SCRIPT_PATH),
        "source_path": str(SOURCE_PATH),
        "output_csv": str(OUTPUT_CSV),
        "row_count": len(rows),
        "duplicate_province_name_norm_count": sum(1 for count in duplicate_norms.values() if count > 1),
        "duplicate_province_name_norm_values": [
            key for key, count in duplicate_norms.items() if count > 1
        ],
        "status": "ok",
    }

    OUTPUT_REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
