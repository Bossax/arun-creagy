"""Build national Gold fact tables: DDPM tambon (subdistrict) impacts, climate hazards only (B.E. 2560–2567).

Plan reference:
- [`plans/2026-05-18_national-ddpm-tambon-impact-notebook-plan.md`](plans/2026-05-18_national-ddpm-tambon-impact-notebook-plan.md:1)

Hard guardrails:
- Join key is 6-digit DOPA `subdistrict_code` only (no name-based fallback).
- Outputs are CSV-only for this implementation cycle.
- Mandatory QA gate: Stats → geometry coverage must pass (fail run if missing).
"""

from __future__ import annotations

import sys
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
import geopandas as gpd


@dataclass(frozen=True)
class Config:
    year_be_start: int = 2560
    year_be_end: int = 2567
    output_format: str = "csv"  # locked this cycle

    # Root resolves to data_system/
    base_path: Path = Path(__file__).resolve().parent.parent.parent

    ddpm_master_csv: Path = base_path / "data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv"
    hazard_dim_csv: Path = base_path / "data/2_gold/dim_hazard_canonical.csv"
    location_spine_csv: Path = base_path / "data/2_gold/dopa/dim_location_master.csv"
    tambon_enriched_shp: Path = base_path / "data/1_silver/dopa/tambon_boundaries_enriched.shp"

    out_gold_dir: Path = base_path / "data/2_gold/ddpm"
    out_qa_dir: Path = base_path / "data/2_gold/ddpm/qa"


def _stdout_utf8() -> None:
    """Avoid UnicodeEncodeError when printing Thai/ψ paths on Windows consoles."""

    try:
        sys.stdout.reconfigure(encoding="utf-8")  # py3.7+
    except Exception:
        pass


def _read_csv_flex(path: Path) -> pd.DataFrame:
    """Read CSV using UTF-8, fallback to cp874 for older Thai-encoded exports."""

    try:
        return pd.read_csv(path, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="cp874")


def _extract_digits(value: object) -> str:
    if value is None:
        return ""
    s = str(value).strip()
    m = re.search(r"(\d+)", s)
    return m.group(1) if m else ""


def _clean_subdistrict_code(series: pd.Series) -> pd.Series:
    """Return 6-digit string codes; invalids become empty string."""

    s = series.astype(str)
    s = s.str.replace(r"\.0$", "", regex=True).str.strip()
    s = s.map(_extract_digits)
    s = s.str[-6:].fillna("")
    # strict 6-digit numeric
    s = s.where(s.str.fullmatch(r"\d{6}", na=False), "")
    # drop dummy/blank
    s = s.where(~s.isin(["", "000000", "nan", "None"]), "")
    return s


def _find_code_column(gdf: gpd.GeoDataFrame, candidates: Iterable[str]) -> str:
    for c in candidates:
        if c in gdf.columns:
            return c
    raise KeyError(f"No code column found in geometry file. Tried: {list(candidates)}. Columns: {list(gdf.columns)}")


def _pct_rank_0_100(values: pd.Series) -> pd.Series:
    """Deterministic percentile rank where higher value => higher percentile.

    - Percentile in [0, 100]
    - Tie strategy: average rank (pandas default), deterministic for stable inputs.
    """

    v = pd.to_numeric(values, errors="coerce").fillna(0)
    # rank in [1..n]
    r = v.rank(method="average", ascending=True)
    n = len(v)
    if n <= 1:
        return pd.Series([100.0] * n, index=v.index)
    return ((r - 1) / (n - 1) * 100).astype(float)


def _build_hazard_map(hazard_dim: pd.DataFrame) -> pd.DataFrame:
    # Expect canonical_hazard_name_th + hazard_group
    needed = {"canonical_hazard_id", "canonical_hazard_code", "canonical_hazard_name_th", "hazard_group"}
    missing = needed.difference(hazard_dim.columns)
    if missing:
        raise KeyError(f"Hazard dim missing columns: {sorted(missing)}")

    hz = hazard_dim.copy()
    hz["canonical_hazard_name_th"] = hz["canonical_hazard_name_th"].astype(str).str.strip()
    return hz


def build() -> int:
    _stdout_utf8()
    cfg = Config()

    print(f"[INFO] Base path: {cfg.base_path}")
    print(f"[INFO] Output format locked: {cfg.output_format}")

    cfg.out_gold_dir.mkdir(parents=True, exist_ok=True)
    cfg.out_qa_dir.mkdir(parents=True, exist_ok=True)

    # --- Load inputs ---
    if not cfg.ddpm_master_csv.exists():
        raise FileNotFoundError(cfg.ddpm_master_csv)
    if not cfg.hazard_dim_csv.exists():
        raise FileNotFoundError(cfg.hazard_dim_csv)
    if not cfg.location_spine_csv.exists():
        raise FileNotFoundError(cfg.location_spine_csv)
    if not cfg.tambon_enriched_shp.exists():
        raise FileNotFoundError(cfg.tambon_enriched_shp)

    print(f"[LOAD] DDPM master: {cfg.ddpm_master_csv}")
    ddpm = _read_csv_flex(cfg.ddpm_master_csv)

    print(f"[LOAD] Hazard dim: {cfg.hazard_dim_csv}")
    hazard_dim = _read_csv_flex(cfg.hazard_dim_csv)
    hazard_dim = _build_hazard_map(hazard_dim)

    print(f"[LOAD] Location spine: {cfg.location_spine_csv}")
    spine = _read_csv_flex(cfg.location_spine_csv)

    # Names should come from spine, not shapefile.
    if "admin_level" in spine.columns:
        spine_sd = spine.loc[
            spine["admin_level"].astype(str).eq("subdistrict"),
            [
                "subdistrict_code",
                "province_code",
                "province_name_th",
                "district_name_th",
                "subdistrict_name_th",
            ],
        ].drop_duplicates(subset=["subdistrict_code"])
    else:
        spine_sd = spine[[
            "subdistrict_code",
            "province_code",
            "province_name_th",
            "district_name_th",
            "subdistrict_name_th",
        ]].drop_duplicates(subset=["subdistrict_code"])

    spine_sd["subdistrict_code"] = _clean_subdistrict_code(spine_sd["subdistrict_code"])
    spine_sd["province_code"] = spine_sd["province_code"].astype(str).map(_extract_digits).str[-2:].str.zfill(2)
    spine_sd = spine_sd.loc[spine_sd["subdistrict_code"].ne("")].copy()

    # --- DDPM normalize & filter ---
    required_cols = {
        "ปี",
        "Disaster Type",
        "Subdistrict Code",
        "Affected Households",
        "Affected People",
        "Deaths",
    }
    missing = required_cols.difference(ddpm.columns)
    if missing:
        raise KeyError(f"DDPM master missing columns: {sorted(missing)}")

    ddpm_w = ddpm.copy()
    ddpm_w["year_be"] = pd.to_numeric(ddpm_w["ปี"], errors="coerce")
    ddpm_w = ddpm_w.loc[ddpm_w["year_be"].between(cfg.year_be_start, cfg.year_be_end)].copy()

    # Map observed DDPM hazard variants to canonical Thai names
    ddpm_w["disaster_type_th"] = ddpm_w["Disaster Type"].astype(str).str.strip()
    ddpm_w["disaster_type_th"] = ddpm_w["disaster_type_th"].replace(
        {
            "ดินโคลนถล่ม": "ดินถล่ม",
            "ดินโคลนถล่ม/ดินถล่ม": "ดินถล่ม",
        }
    )

    ddpm_w = ddpm_w.merge(
        hazard_dim[["canonical_hazard_id", "canonical_hazard_code", "canonical_hazard_name_th", "hazard_group"]],
        left_on="disaster_type_th",
        right_on="canonical_hazard_name_th",
        how="left",
    )

    ddpm_w = ddpm_w.loc[ddpm_w["hazard_group"].astype(str).eq("climate")].copy()

    ddpm_w["subdistrict_code"] = _clean_subdistrict_code(ddpm_w["Subdistrict Code"])
    ddpm_w["province_code"] = ddpm_w["subdistrict_code"].str[:2]

    # numeric metrics
    for src, dst in [
        ("Affected Households", "affected_households"),
        ("Affected People", "affected_people"),
        ("Deaths", "deaths"),
    ]:
        ddpm_w[dst] = pd.to_numeric(
            ddpm_w[src].astype(str).str.replace(",", "", regex=False),
            errors="coerce",
        ).fillna(0)

    # invalid-code accounting
    invalid_mask = ddpm_w["subdistrict_code"].eq("")
    invalid = ddpm_w.loc[invalid_mask, ["year_be", "disaster_type_th", "Subdistrict Code"]].copy()
    valid = ddpm_w.loc[~invalid_mask].copy()

    # Drops per province: for invalid codes we can't compute province from subdistrict_code.
    # We will still report counts, and for valid rows we also report a sanity breakdown.
    qa_invalid_total = pd.DataFrame(
        {
            "year_be_start": [cfg.year_be_start],
            "year_be_end": [cfg.year_be_end],
            "invalid_code_rows": [int(len(invalid))],
            "valid_code_rows": [int(len(valid))],
        }
    )
    qa_invalid_total.to_csv(
        cfg.out_qa_dir / f"qa_invalid_code_totals_{cfg.year_be_start}_{cfg.year_be_end}.csv",
        index=False,
        encoding="utf-8-sig",
    )

    qa_valid_rows_by_prov = (
        valid.groupby("province_code", dropna=False)
        .size()
        .reset_index(name="valid_rows")
        .sort_values("province_code")
    )
    qa_valid_rows_by_prov.to_csv(
        cfg.out_qa_dir / f"qa_valid_rows_by_province_{cfg.year_be_start}_{cfg.year_be_end}.csv",
        index=False,
        encoding="utf-8-sig",
    )

    # --- Fact (yearly) ---
    yearly = (
        valid.groupby(["subdistrict_code", "province_code", "year_be"], as_index=False)
        .agg(
            affected_households_sum=("affected_households", "sum"),
            affected_people_sum=("affected_people", "sum"),
            deaths_sum=("deaths", "sum"),
        )
    )

    # Fill missing years with 0 for yoy computation
    years = list(range(cfg.year_be_start, cfg.year_be_end + 1))
    idx = pd.MultiIndex.from_product(
        [yearly["subdistrict_code"].drop_duplicates().sort_values(), years],
        names=["subdistrict_code", "year_be"],
    )
    yearly_filled = (
        yearly.set_index(["subdistrict_code", "year_be"])
        .reindex(idx)
        .reset_index()
    )
    yearly_filled = yearly_filled.merge(
        yearly[["subdistrict_code", "province_code"]].drop_duplicates(),
        on="subdistrict_code",
        how="left",
    )
    for c in ["affected_households_sum", "affected_people_sum", "deaths_sum"]:
        yearly_filled[c] = pd.to_numeric(yearly_filled[c], errors="coerce").fillna(0)

    # avg_yoy_change based on affected_households_sum yearly
    yearly_filled = yearly_filled.sort_values(["subdistrict_code", "year_be"]).copy()
    yearly_filled["yoy_delta_affected_households"] = (
        yearly_filled.groupby("subdistrict_code")["affected_households_sum"].diff().fillna(0)
    )
    # mean over y=2561..2567 (diff includes first year delta=0 which we exclude)
    yoy_for_mean = yearly_filled.loc[yearly_filled["year_be"].between(cfg.year_be_start + 1, cfg.year_be_end)].copy()
    avg_yoy = (
        yoy_for_mean.groupby("subdistrict_code", as_index=False)["yoy_delta_affected_households"].mean()
        .rename(columns={"yoy_delta_affected_households": "avg_yoy_change"})
    )

    # --- Fact (period aggregate) ---
    fact = (
        valid.groupby(["subdistrict_code", "province_code"], as_index=False)
        .agg(
            affected_households_sum=("affected_households", "sum"),
            affected_people_sum=("affected_people", "sum"),
            deaths_sum=("deaths", "sum"),
        )
    )
    fact = fact.merge(avg_yoy, on="subdistrict_code", how="left")
    fact["avg_yoy_change"] = pd.to_numeric(fact["avg_yoy_change"], errors="coerce").fillna(0)

    # Attach Thai names from spine (authoritative)
    fact = fact.merge(
        spine_sd[[
            "subdistrict_code",
            "province_name_th",
            "district_name_th",
            "subdistrict_name_th",
        ]],
        on="subdistrict_code",
        how="left",
    )

    # National percentiles
    for m in [
        "affected_households_sum",
        "affected_people_sum",
        "deaths_sum",
        "avg_yoy_change",
    ]:
        fact[f"pct_national_{m}"] = _pct_rank_0_100(fact[m])

    # Deterministic ordering
    fact = fact.sort_values(["subdistrict_code"]).reset_index(drop=True)
    yearly_filled = yearly_filled.sort_values(["subdistrict_code", "year_be"]).reset_index(drop=True)

    # --- QA gate: Stats → geometry coverage ---
    print(f"[LOAD] Geometry (silver enriched): {cfg.tambon_enriched_shp}")
    gdf = gpd.read_file(cfg.tambon_enriched_shp)
    code_col = _find_code_column(gdf, candidates=["subdist_cd", "subdistrict_code", "SUBDISTRIC", "T_CODE"])
    geom_codes = _clean_subdistrict_code(gdf[code_col])
    geom_code_set = set(geom_codes.loc[geom_codes.ne("")].unique().tolist())
    stat_code_set = set(fact["subdistrict_code"].unique().tolist())
    missing_geom = sorted(stat_code_set.difference(geom_code_set))

    qa_missing_geom_path = cfg.out_qa_dir / f"qa_missing_geometry_{cfg.year_be_start}_{cfg.year_be_end}.csv"
    pd.DataFrame({"subdistrict_code": missing_geom}).to_csv(qa_missing_geom_path, index=False, encoding="utf-8-sig")
    print(f"[QA] Missing-geometry codes written: {qa_missing_geom_path}")
    if missing_geom:
        raise RuntimeError(
            f"[FAIL] Stats→geometry coverage gate failed: {len(missing_geom)} subdistrict_code(s) missing geometry. "
            f"See {qa_missing_geom_path}"
        )

    # --- Write outputs (CSV-only) ---
    out_fact = cfg.out_gold_dir / f"fact_ddpm_tambon_impact_climate_{cfg.year_be_start}_{cfg.year_be_end}.csv"
    out_yearly = cfg.out_gold_dir / f"fact_ddpm_tambon_impact_climate_yearly_{cfg.year_be_start}_{cfg.year_be_end}.csv"
    fact.to_csv(out_fact, index=False, encoding="utf-8-sig")
    yearly_filled.to_csv(out_yearly, index=False, encoding="utf-8-sig")
    print(f"[WRITE] {out_fact}")
    print(f"[WRITE] {out_yearly}")

    print("[OK] Gold DDPM tambon impact build complete.")
    return 0


def main() -> int:
    try:
        return build()
    except Exception as e:
        _stdout_utf8()
        print(f"[ERROR] {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

