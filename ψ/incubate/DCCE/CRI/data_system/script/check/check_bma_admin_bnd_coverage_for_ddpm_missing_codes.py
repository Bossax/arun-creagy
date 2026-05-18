"""Check BMA admin boundary shapefile coverage for DDPM tambon codes missing from national tambon geometry.

Context
-------
Gold DDPM build currently fails the *stats → geometry* hard gate because several Bangkok (province_code=10)
subdistrict codes exist in DDPM stats but are missing from the enriched national tambon boundary shapefile.

This script audits whether the new BMA OpenData boundary layer contains those missing subdistricts.

Inputs
------
- Missing-code list produced by the Gold DDPM ETL:
  - [`ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/qa/qa_missing_geometry_2560_2567.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/ddpm/qa/qa_missing_geometry_2560_2567.csv:1)
- Authoritative location spine (names/codes):
  - [`ψ/incubate/DCCE/CRI/data_system/data/2_gold/dopa/dim_location_master.csv`](ψ/incubate/DCCE/CRI/data_system/data/2_gold/dopa/dim_location_master.csv:1)
- New BMA boundary layer (Bronze):
  - [`ψ/incubate/DCCE/CRI/data_system/data/0_bronze/bma/admin_bnd/ADMIN_BND.shp`](ψ/incubate/DCCE/CRI/data_system/data/0_bronze/bma/admin_bnd/ADMIN_BND.shp:1)

Outputs
-------
Writes a diagnostic report (CSV) under:
- [`ψ/incubate/DCCE/CRI/data_system/artifacts/reports/bma_admin_bnd/`](ψ/incubate/DCCE/CRI/data_system/artifacts/reports/bma_admin_bnd:1)

Notes
-----
- Any name-based matching here is *diagnostic only* (never used as an ETL fallback join).
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


ROOT = Path(r"c:\Users\sitth\OracleWorkspace\Arun_Creagy")

MISSING_CODES_CSV = ROOT / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system" / "data" / "2_gold" / "ddpm" / "qa" / "qa_missing_geometry_2560_2567.csv"
SPINE_CSV = ROOT / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system" / "data" / "2_gold" / "dopa" / "dim_location_master.csv"
BMA_SHP = ROOT / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system" / "data" / "0_bronze" / "bma" / "admin_bnd" / "ADMIN_BND.shp"

OUT_DIR = ROOT / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system" / "artifacts" / "reports" / "bma_admin_bnd"


def _safe_stdout_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def _guess_code_columns(df: pd.DataFrame) -> list[str]:
    """Heuristic: columns that look like admin codes (contain 6-digit strings or are named like *CODE*)."""
    candidates: list[str] = []
    for c in df.columns:
        uc = c.upper()
        if "CODE" in uc or "DOPA" in uc or uc.endswith("CD") or "TAMB" in uc or "TAM" in uc:
            candidates.append(c)

    # also try any object/int columns that contain 6-digit patterns
    for c in df.columns:
        if c in candidates:
            continue
        s = df[c]
        if s.dtype == object or str(s.dtype).startswith("int") or str(s.dtype).startswith("float"):
            sample = s.dropna().astype(str).head(5000)
            if sample.str.contains(r"\b\d{6}\b", regex=True).any():
                candidates.append(c)
    return candidates


def _clean_code(series: pd.Series) -> pd.Series:
    s = series.astype(str).str.extract(r"(\d+)")[0]
    s = s.fillna("").str.strip().str[-6:]
    return s


def main() -> int:
    _safe_stdout_utf8()

    if not MISSING_CODES_CSV.exists():
        raise FileNotFoundError(str(MISSING_CODES_CSV))
    if not SPINE_CSV.exists():
        raise FileNotFoundError(str(SPINE_CSV))
    if not BMA_SHP.exists():
        raise FileNotFoundError(str(BMA_SHP))

    missing = pd.read_csv(MISSING_CODES_CSV, encoding="utf-8-sig")
    missing["subdistrict_code"] = missing["subdistrict_code"].astype(str).str.zfill(6)

    # Restrict to Bangkok (should already be true, but keep explicit)
    missing_bkk = missing.loc[missing.get("province_code", "").astype(str).str.zfill(2).eq("10")].copy()
    if missing_bkk.empty:
        print("[INFO] No Bangkok missing codes found in qa_missing_geometry_2560_2567.csv")
        return 0

    spine = pd.read_csv(SPINE_CSV, encoding="utf-8-sig", low_memory=False)
    spine_sub = spine.loc[spine["admin_level"].eq("subdistrict"), [
        "subdistrict_code",
        "subdistrict_name_th",
        "district_name_th",
        "province_code",
        "province_name_th",
    ]].drop_duplicates(subset=["subdistrict_code"]).copy()
    spine_sub["subdistrict_code"] = spine_sub["subdistrict_code"].astype(str).str.zfill(6)

    # Load BMA layer
    import geopandas as gpd

    bma = gpd.read_file(BMA_SHP)
    print("BMA layer loaded")
    print(f"- Rows: {len(bma)}")
    print(f"- Columns: {list(bma.columns)}")

    code_cols = _guess_code_columns(bma)
    print("\nCandidate code columns (heuristic):")
    for c in code_cols:
        print(f"- {c}")

    # Build a normalized code index from each candidate column and test whether it covers the missing codes
    missing_codes = set(missing_bkk["subdistrict_code"].astype(str))
    coverage_rows: list[dict] = []
    best_col: str | None = None
    best_hit = -1

    for c in code_cols:
        norm = _clean_code(bma[c])
        codes = set(norm.loc[norm.str.fullmatch(r"\d{6}", na=False)])
        hit = len(missing_codes & codes)
        coverage_rows.append({
            "candidate_col": c,
            "unique_6digit_codes": len(codes),
            "missing_code_hits": hit,
        })
        if hit > best_hit:
            best_hit = hit
            best_col = c

    coverage = pd.DataFrame(coverage_rows).sort_values(
        ["missing_code_hits", "unique_6digit_codes", "candidate_col"],
        ascending=[False, False, True],
        kind="mergesort",
    )

    # If no candidate hits, we still proceed with a name-only diagnostic
    print("\nCoverage summary (by candidate code column):")
    if not coverage.empty:
        print(coverage.to_string(index=False))
    else:
        print("(no candidate code columns found)")

    # Prepare report
    report = missing_bkk.merge(
        spine_sub,
        on="subdistrict_code",
        how="left",
        suffixes=("_missing", "_spine"),
    )

    report["found_by_code"] = False
    report["bma_code_col"] = ""
    report["bma_code_value"] = ""
    report["bma_name_col"] = ""
    report["bma_name_value"] = ""

    if best_col is not None and best_hit > 0:
        norm = _clean_code(bma[best_col])
        bma_idx = bma.copy()
        bma_idx["_norm_code"] = norm
        bma_idx = bma_idx.loc[bma_idx["_norm_code"].str.fullmatch(r"\d{6}", na=False)].copy()

        # Keep first occurrence per code for reporting
        bma_one = bma_idx.drop_duplicates(subset=["_norm_code"]).set_index("_norm_code")

        report["found_by_code"] = report["subdistrict_code"].map(lambda x: x in bma_one.index)
        report.loc[report["found_by_code"], "bma_code_col"] = best_col
        report.loc[report["found_by_code"], "bma_code_value"] = report.loc[report["found_by_code"], "subdistrict_code"]

    # Name diagnostic (do NOT use as join in production)
    name_cols = [c for c in bma.columns if any(k in c.upper() for k in ["NAME", "TNAME", "TH", "THAI"])]
    # pick likely Thai-name columns
    name_cols = [c for c in name_cols if bma[c].dtype == object]

    # best-effort: if we have a spine name, see if it exists as exact match in any name column
    spine_names = report.get("subdistrict_name_th", pd.Series([""] * len(report))).fillna("").astype(str).str.strip()
    for idx, nm in spine_names.items():
        if not nm:
            continue
        for c in name_cols:
            # exact match only (diagnostic)
            if (bma[c].astype(str).str.strip() == nm).any():
                report.at[idx, "bma_name_col"] = c
                report.at[idx, "bma_name_value"] = nm
                break
        # stop after first hit

    # Write outputs
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    out_report = OUT_DIR / f"bma_admin_bnd_missing_code_coverage_{stamp}.csv"
    out_cov = OUT_DIR / f"bma_admin_bnd_code_column_coverage_{stamp}.csv"

    report.to_csv(out_report, index=False, encoding="utf-8-sig")
    coverage.to_csv(out_cov, index=False, encoding="utf-8-sig")

    print("\n[OK] Wrote reports:")
    print(f"- {out_report}")
    print(f"- {out_cov}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

