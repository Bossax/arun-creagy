"""Prepare (Silver) province boundaries enriched with canonical `prov_code`.

This is the province-only equivalent of [`prep_dopa_boundaries.py`](ψ/incubate/DCCE/CRI/data_system/script/ELT/prep_dopa_boundaries.py:1)
without any tambon processing.

Input
-----
- Gold spine: data/2_gold/dopa/dim_location_master.csv
- DOPA province shapefile: data/0_bronze/dopa/thailanda-administrative-boundary/THA_Province.shp

Output
------
- data/1_silver/dopa/province_boundaries_enriched.shp

Contract
--------
- Output includes `prov_code` as a 2-digit string (00-padded)
- 1 row per province geometry as provided by DOPA source
- Audit any join failures to tmp/

Run (Windows)
------------
  cd ψ\incubate\DCCE\CRI\data_system
  .\.venv\Scripts\python.exe .\script\ELT\prep_dopa_province_boundaries.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd


def normalize_admin_name(value: object) -> str:
    if value is None:
        return ""
    s = str(value).strip()
    s = s.replace("\u200b", "").replace("\xa0", " ").replace("\r", "").replace("\n", "")
    s = re.sub(r"\s+", " ", s)
    prefixes = ["จังหวัด", "จ."]
    for p in prefixes:
        if s.startswith(p):
            s = s[len(p) :].strip()
    return s.replace("ฯ", "").strip()


def main() -> None:
    # Ensure Thai/ψ paths can be printed in Windows terminals
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # py3.7+
    except Exception:
        pass

    base = Path(__file__).resolve().parent.parent.parent

    spine_path = base / "data/2_gold/dopa/dim_location_master.csv"
    prov_shp_path = base / "data/0_bronze/dopa/thailanda-administrative-boundary/THA_Province.shp"

    out_province = base / "data/1_silver/dopa/province_boundaries_enriched.shp"
    out_province.parent.mkdir(parents=True, exist_ok=True)

    project_tmp = base / "tmp"
    project_tmp.mkdir(parents=True, exist_ok=True)

    if not spine_path.exists():
        raise FileNotFoundError(f"Missing Gold spine: {spine_path}")
    if not prov_shp_path.exists():
        raise FileNotFoundError(f"Missing DOPA province shapefile: {prov_shp_path}")

    print(f"Reading location master from {spine_path}...")
    spine = pd.read_csv(spine_path, dtype={"province_code": str})

    # Province-level spine (authoritative code list)
    if "province_name_th" not in spine.columns or "province_code" not in spine.columns:
        raise KeyError(
            "Gold spine missing required columns: province_name_th, province_code. "
            f"Columns: {list(spine.columns)}"
        )

    spine_p = spine[["province_name_th", "province_code"]].drop_duplicates()
    spine_p["province_code"] = (
        spine_p["province_code"].astype(str).str.extract(r"(\d+)")[0].fillna("").str[-2:].str.zfill(2)
    )
    spine_p["province_name_th_norm"] = spine_p["province_name_th"].apply(normalize_admin_name)

    print(f"Reading DOPA province boundaries from {prov_shp_path}...")
    gdf_p = gpd.read_file(prov_shp_path)
    if gdf_p.crs is None or gdf_p.crs.to_epsg() != 4326:
        gdf_p = gdf_p.to_crs(epsg=4326)

    if "P_NAME_T" not in gdf_p.columns:
        raise KeyError(f"Expected DOPA province column 'P_NAME_T' not found. Columns: {list(gdf_p.columns)}")

    gdf_p["p_norm"] = gdf_p["P_NAME_T"].apply(normalize_admin_name)

    print("Joining province geometries to Gold spine (name-normalized)...")
    enriched_p = gdf_p.merge(
        spine_p,
        left_on="p_norm",
        right_on="province_name_th_norm",
        how="left",
    )
    enriched_p = enriched_p.rename(columns={"province_code": "prov_code"})

    # Audit join failures
    missing_code = enriched_p[enriched_p["prov_code"].isna() | enriched_p["prov_code"].eq("")].copy()
    if not missing_code.empty:
        audit_file = project_tmp / "province_boundary_join_failures.csv"
        missing_code[["P_NAME_T", "p_norm"]].drop_duplicates().to_csv(audit_file, index=False, encoding="utf-8-sig")
        print(f"WARNING: {len(missing_code)} province rows missing prov_code. Logged to {audit_file}")
    else:
        print("SUCCESS: 100% province join coverage achieved.")

    # Final cleanup: ensure prov_code is 2-digit string
    enriched_p["prov_code"] = (
        enriched_p["prov_code"].astype(str).str.extract(r"(\d+)")[0].fillna("").str[-2:].str.zfill(2)
    )

    # Write out (exclude helper norm columns + redundant spine name)
    drop_cols = [c for c in enriched_p.columns if c.endswith("_norm")]
    drop_cols += [c for c in ["province_name_th"] if c in enriched_p.columns]
    cols_out = [c for c in enriched_p.columns if c not in set(drop_cols)]

    try:
        enriched_p[cols_out].to_file(out_province, driver="ESRI Shapefile", encoding="utf-8")
        print(f"Saved: {out_province}")
    except PermissionError:
        alt = out_province.with_name(out_province.stem + "_new" + out_province.suffix)
        enriched_p[cols_out].to_file(alt, driver="ESRI Shapefile", encoding="utf-8")
        print(f"WARNING: Could not overwrite locked file: {out_province}")
        print(f"Saved (fallback): {alt}")

    print("DONE: Province silver boundaries prepared.")


# NOTE (Windows / Python):
# Avoid backslashes in docstrings like "\incubate" because they create invalid escape sequences
# (e.g. "\i") and raise SyntaxWarning. Prefer double-backslashes or forward slashes.


if __name__ == "__main__":
    main()

