"""Build national province-level score maps (min–max normalized).

Scoring formula
---------------
score = (x - min(x)) / (max(x) - min(x))

where min/max are computed nationally across *provinces* for each metric.

This script mirrors the province aggregation + min–max normalization pattern in
[`ddpm_province_and_chiangrai_minmax_scores.ipynb`](ψ/incubate/DCCE/CRI/data_system/script/analysis_notebooks/ddpm_province_and_chiangrai_minmax_scores.ipynb:77)
but produces reproducible PNG outputs.

Inputs
------
- Gold fact (tambon impacts): data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv
- Silver province geometry:  data/1_silver/dopa/province_boundaries_enriched.shp

Outputs
-------
- output/national/province_score_maps/*.png

Run (Windows)
------------
  cd ψ\incubate\DCCE\CRI\data_system
  .\.venv\Scripts\python.exe .\script\analysis\build_national_province_score_maps.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


METRICS: list[str] = [
    "affected_households_sum",
    "affected_people_sum",
    "deaths_sum",
]


def _read_csv_flex(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="cp874")


def _clean_code_2(s: pd.Series) -> pd.Series:
    out = s.astype(str).str.extract(r"(\d+)")[0].fillna("")
    out = out.str[-2:].str.zfill(2)
    return out


def _clean_code_6(s: pd.Series) -> pd.Series:
    out = s.astype(str).str.extract(r"(\d+)")[0].fillna("")
    out = out.str[-6:].str.zfill(6)
    return out


def minmax_score(series: pd.Series) -> pd.Series:
    s = pd.to_numeric(series, errors="coerce").fillna(0.0).astype(float)
    mn = float(s.min()) if len(s) else 0.0
    mx = float(s.max()) if len(s) else 0.0
    denom = mx - mn
    if denom <= 0:
        return pd.Series(np.zeros(len(s)), index=s.index, dtype=float)
    return (s - mn) / denom


def plot_province_score(
    gdf: gpd.GeoDataFrame,
    score_col: str,
    title: str,
    out_png: Path,
    *,
    cmap: str = "Reds",
) -> None:
    fig, ax = plt.subplots(1, 1, figsize=(12, 12))
    ax.set_title(title, fontsize=16)
    ax.set_axis_off()

    gdf.plot(
        column=score_col,
        ax=ax,
        cmap=cmap,
        legend=True,
        legend_kwds={"shrink": 0.6, "fraction": 0.04, "pad": 0.02},
        linewidth=0.4,
        edgecolor="#222222",
        vmin=0,
        vmax=1,
        missing_kwds={"color": "#f0f0f0", "edgecolor": "none", "label": "No data"},
    )
    fig.tight_layout()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=200)
    plt.close(fig)


def main() -> None:
    # Ensure Thai/ψ paths can be printed in Windows terminals
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    base = Path(__file__).resolve().parent.parent.parent

    fact_path = base / "data/2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv"
    prov_shp = base / "data/1_silver/dopa/province_boundaries_enriched.shp"
    out_dir = base / "output/national/province_score_maps"

    if not fact_path.exists():
        raise FileNotFoundError(f"Missing fact CSV: {fact_path}")
    if not prov_shp.exists():
        raise FileNotFoundError(f"Missing province shapefile: {prov_shp}")

    print(f"Reading fact: {fact_path}")
    fact = _read_csv_flex(fact_path)
    if "subdistrict_code" not in fact.columns:
        raise KeyError("Missing subdistrict_code in fact")

    fact = fact.copy()
    fact["subdistrict_code"] = _clean_code_6(fact["subdistrict_code"])
    fact = fact.loc[fact["subdistrict_code"].ne("")].copy()
    fact["province_code"] = fact["subdistrict_code"].str[:2]

    for m in METRICS:
        if m not in fact.columns:
            raise KeyError(f"Missing metric in fact: {m}")
        fact[m] = pd.to_numeric(fact[m], errors="coerce").fillna(0.0)

    # Province aggregation from tambon facts
    prov_stats = fact.groupby("province_code", as_index=False)[METRICS].sum(numeric_only=True)
    prov_stats["province_code"] = _clean_code_2(prov_stats["province_code"])

    # Province-level score columns using national min/max across provinces
    for m in METRICS:
        prov_stats[f"score_{m}"] = minmax_score(prov_stats[m])

    print(f"Reading province geometry: {prov_shp}")
    gdf_prov = gpd.read_file(prov_shp)
    if gdf_prov.crs is None or gdf_prov.crs.to_epsg() != 4326:
        gdf_prov = gdf_prov.to_crs(epsg=4326)

    if "prov_code" not in gdf_prov.columns:
        raise KeyError(f"Province geometry missing prov_code. Columns: {list(gdf_prov.columns)}")
    gdf_prov = gdf_prov.copy()
    gdf_prov["province_code"] = _clean_code_2(gdf_prov["prov_code"])

    prov_map = gdf_prov.merge(prov_stats, on="province_code", how="left")
    for m in METRICS:
        prov_map[f"score_{m}"] = pd.to_numeric(prov_map[f"score_{m}"], errors="coerce").fillna(0.0)

    # Basic join coverage check
    missing = prov_map[prov_map[[f"score_{m}" for m in METRICS]].isna().any(axis=1)]
    print(f"Province geometries: {len(prov_map):,}")
    print(f"Join coverage: {len(prov_map) - len(missing):,} with scores, {len(missing):,} missing")

    titles = {
        "affected_households_sum": "Province score (min–max): affected households | 2560–2567",
        "affected_people_sum": "Province score (min–max): affected people | 2560–2567",
        "deaths_sum": "Province score (min–max): deaths | 2560–2567",
    }

    for m in METRICS:
        out_png = out_dir / f"province_score_minmax_{m}_2560_2567.png"
        plot_province_score(
            prov_map,
            score_col=f"score_{m}",
            title=titles.get(m, f"Province score (min–max): {m} | 2560–2567"),
            out_png=out_png,
            cmap="Reds",
        )
        print(f"Saved: {out_png}")


if __name__ == "__main__":
    main()

