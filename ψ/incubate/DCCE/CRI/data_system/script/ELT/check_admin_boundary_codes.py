"""Check (and optionally build) admin boundary code consistency.

Purpose
-------
We need a province boundary layer whose province code matches the tambon layer's
province code convention:

- tambon `subdist_cd` is 6 digits (DOPA subdistrict code)
- tambon `prov_code` is 2 digits
- invariant: `subdist_cd[:2] == prov_code`

This script:
1) Validates the tambon invariant above.
2) Validates that province layer has `prov_code` and its codes match tambon codes.
3) (Optional) Builds a province layer by dissolving tambon geometries by `prov_code`
   so codes are guaranteed to align.

Run with the project venv:
  .\.venv\Scripts\python.exe .\script\ELT\check_admin_boundary_codes.py
  .\.venv\Scripts\python.exe .\script\ELT\check_admin_boundary_codes.py --build-province-from-tambon
"""

from __future__ import annotations

import argparse
from pathlib import Path

import geopandas as gpd
import pandas as pd


def _clean_digits(s: pd.Series, width: int) -> pd.Series:
    # keep digits only, then right-truncate to width and zfill
    out = s.astype(str).str.extract(r"(\d+)")[0].fillna("")
    out = out.str[-width:].str.zfill(width)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--build-province-from-tambon",
        action="store_true",
        help="Create a province layer by dissolving tambon geometries on prov_code.",
    )
    ap.add_argument(
        "--tambon",
        default=None,
        help="Override tambon shapefile path (default: data/1_silver/dopa/tambon_boundaries_enriched.shp)",
    )
    ap.add_argument(
        "--province",
        default=None,
        help="Override province shapefile path (default: data/1_silver/dopa/province_boundaries_enriched.shp)",
    )
    args = ap.parse_args()

    base = Path(__file__).resolve().parent.parent.parent
    tambon_path = Path(args.tambon) if args.tambon else base / "data/1_silver/dopa/tambon_boundaries_enriched.shp"
    province_path = Path(args.province) if args.province else base / "data/1_silver/dopa/province_boundaries_enriched.shp"

    if not tambon_path.exists():
        raise FileNotFoundError(f"Missing tambon shapefile: {tambon_path}")

    print(f"Reading tambon: {tambon_path}")
    gt = gpd.read_file(tambon_path)

    required_t_cols = {"prov_code", "subdist_cd"}
    missing_t = sorted(required_t_cols - set(gt.columns))
    if missing_t:
        raise KeyError(f"Tambon missing required columns: {missing_t}. Columns: {list(gt.columns)}")

    gt["prov_code"] = _clean_digits(gt["prov_code"], 2)
    gt["subdist_cd"] = _clean_digits(gt["subdist_cd"], 6)

    bad_prefix = gt.loc[gt["subdist_cd"].str[:2] != gt["prov_code"]].copy()
    print(f"Tambon rows: {len(gt):,}")
    print(f"Tambon distinct prov_code: {gt['prov_code'].nunique():,}")
    print(f"Tambon subdist_cd prefix mismatches: {len(bad_prefix):,}")

    if len(bad_prefix) > 0:
        audit_dir = base / "tmp"
        audit_dir.mkdir(parents=True, exist_ok=True)
        audit_file = audit_dir / "tambon_prov_code_prefix_mismatches.csv"
        bad_prefix[["prov_code", "subdist_cd"]].drop_duplicates().to_csv(audit_file, index=False, encoding="utf-8-sig")
        print(f"Wrote mismatch audit: {audit_file}")

    tambon_codes = set(gt["prov_code"].dropna().unique())

    if province_path.exists():
        print(f"Reading province: {province_path}")
        gp = gpd.read_file(province_path)
        if "prov_code" not in gp.columns:
            raise KeyError(f"Province layer missing 'prov_code'. Columns: {list(gp.columns)}")

        gp["prov_code"] = _clean_digits(gp["prov_code"], 2)
        province_codes = set(gp["prov_code"].dropna().unique())

        only_in_t = sorted(tambon_codes - province_codes)
        only_in_p = sorted(province_codes - tambon_codes)
        print(f"Province rows: {len(gp):,}")
        print(f"Province distinct prov_code: {len(province_codes):,}")
        print(f"Codes only in tambon: {len(only_in_t):,}")
        print(f"Codes only in province: {len(only_in_p):,}")
        if only_in_t:
            print(f"  sample only-in-tambon: {only_in_t[:15]}")
        if only_in_p:
            print(f"  sample only-in-province: {only_in_p[:15]}")
    else:
        print(f"Province shapefile not found (ok): {province_path}")

    if args.build_province_from_tambon:
        print("Building province layer by dissolving tambon geometries on prov_code...")

        # Keep one Thai name per prov_code if present in tambon layer.
        name_cols = [c for c in ["province_name_th", "P_NAME_T", "p_name_t"] if c in gt.columns]
        keep_name = name_cols[0] if name_cols else None

        cols_for_dissolve = ["prov_code"] + ([keep_name] if keep_name else [])
        gtd = gt[cols_for_dissolve + ["geometry"]].copy()

        # Prefer prov_code-only dissolve; then reattach name as first non-null per prov_code
        dissolved = gtd[["prov_code", "geometry"]].dissolve(by="prov_code", as_index=False)
        dissolved = dissolved.set_geometry("geometry")
        if dissolved.crs is None:
            dissolved = dissolved.set_crs(epsg=4326)

        if keep_name:
            name_map = (
                gtd[["prov_code", keep_name]]
                .dropna(subset=[keep_name])
                .drop_duplicates(subset=["prov_code"])
            )
            dissolved = dissolved.merge(name_map, on="prov_code", how="left")

        out_path = base / "data/1_silver/dopa/province_boundaries_from_tambon.shp"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        dissolved.to_file(out_path, driver="ESRI Shapefile", encoding="utf-8")
        print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()

