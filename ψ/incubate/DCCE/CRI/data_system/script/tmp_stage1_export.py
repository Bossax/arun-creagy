from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd


BASE = Path(r"c:/Users/sitth/OracleWorkspace/Arun_Creagy/ψ/incubate/DCCE/CRI/data_system")
SRC = BASE / "data"
OUT = BASE / "build_exports" / "stage1"


def minmax(series: pd.Series) -> pd.Series:
    denom = series.max() - series.min()
    if pd.isna(denom) or denom == 0:
        return pd.Series([0.0] * len(series), index=series.index)
    return (series - series.min()) / denom


def descending_rank(values: pd.Series) -> pd.Series:
    ranked = values.rank(ascending=False, method="min")
    return ranked.fillna(0).astype(int)


def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, encoding="utf-8")


def _stdout_utf8() -> None:
    try:
        import sys

        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def pick(col_candidates, cols):
    for c in col_candidates:
        if c in cols:
            return c
    return None


def province_lookup_from_shp(gdf: gpd.GeoDataFrame) -> pd.DataFrame:
    cols = set(gdf.columns)
    code_col = pick(["province_code", "prov_code", "prov_cd", "provcode", "PROV_CODE", "prov_cde"], cols)
    name_th_col = pick(["province_name_th", "prov_name_th", "prov_tname", "THAI_NAME", "province_th"], cols)
    name_en_col = pick(["province_name_en", "prov_name_en", "prov_ename", "ENG_NAME", "province_en"], cols)
    if code_col is None:
        raise RuntimeError(f"Could not find province code column in {list(gdf.columns)}")
    out = pd.DataFrame({
        "province_code": gdf[code_col].astype(str).str.zfill(2),
        "province_name_th": gdf[name_th_col].astype(str) if name_th_col else gdf[code_col].astype(str),
        "province_name_en": gdf[name_en_col].astype(str) if name_en_col else None,
        "geometry": gdf.geometry,
    })
    return out


def province_lookup_from_csv(df: pd.DataFrame) -> pd.DataFrame:
    cols = set(df.columns)
    code_col = pick(["province_code"], cols)
    name_th_col = pick(["province_name_th"], cols)
    name_en_col = pick(["province_name_en"], cols)
    if code_col is None or name_th_col is None:
        raise RuntimeError(f"Could not find province code/name columns in {list(df.columns)}")
    out = pd.DataFrame({
        "province_code": df[code_col].astype(str).str.zfill(2),
        "province_name_th": df[name_th_col].astype(str),
        "province_name_en": df[name_en_col].astype(str) if name_en_col else None,
    })
    return out.drop_duplicates(subset=["province_code"])


def tambon_lookup_from_shp(gdf: gpd.GeoDataFrame) -> pd.DataFrame:
    cols = set(gdf.columns)
    sub_col = pick(["subdistrict_code", "subdist_cd", "tambon_code", "tambon_cd", "SUBDISTRICT", "SUBDIST_CODE"], cols)
    sub_name_col = pick(["subdistrict_name_th", "subdist_name_th", "tambon_name_th", "tam_name_th", "TAMBON_T"], cols)
    dist_name_col = pick(["district_name_th", "amphoe_name_th", "amphoe_t", "AMPHOE_T"], cols)
    prov_code_col = pick(["province_code", "prov_code", "prov_cd", "province_cd", "PROV_CODE"], cols)
    prov_name_col = pick(["province_name_th", "prov_name_th", "prov_tname", "PROV_T"], cols)
    if sub_col is None:
        raise RuntimeError(f"Could not find tambon code column in {list(gdf.columns)}")
    out = pd.DataFrame({
        "subdistrict_code": gdf[sub_col].astype(str).str.zfill(6),
        "subdistrict_name_th": gdf[sub_name_col].astype(str) if sub_name_col else gdf[sub_col].astype(str),
        "district_name_th": gdf[dist_name_col].astype(str) if dist_name_col else None,
        "province_code": gdf[prov_code_col].astype(str).str.zfill(2) if prov_code_col else gdf[sub_col].astype(str).str[:2],
        "province_name_th": gdf[prov_name_col].astype(str) if prov_name_col else None,
        "geometry": gdf.geometry,
    })
    return out


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def rebuild_yearly_ddpm_fact(ddpm_dir: Path) -> tuple[Path, list[str], list[str]]:
    """Rebuild the aggregate yearly DDPM fact from the hazard-specific lineage.

    Returns the rebuilt path, the upstream files used, and the columns normalized
    into the repaired output.
    """

    source_files = sorted(
        p for p in ddpm_dir.glob("fact_ddpm_tambon_impact_climate_yearly_*_2560_2567.csv")
        if p.name != "fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv"
    )
    if not source_files:
        raise RuntimeError(f"No hazard-specific yearly DDPM files found in {ddpm_dir}")

    required_cols = [
        "canonical_hazard_id",
        "canonical_hazard_code",
        "canonical_hazard_name_th",
        "subdistrict_code",
        "year_be",
        "affected_households_sum",
        "affected_people_sum",
        "deaths_sum",
        "province_code",
        "yoy_delta_affected_households",
    ]

    frames = []
    missing_report = []
    for path in source_files:
        frame = load_csv(path)
        missing = [c for c in required_cols if c not in frame.columns]
        if missing:
            missing_report.append(f"{path.name}: missing {missing}")
            continue
        frames.append(frame[required_cols].copy())

    if not frames:
        raise RuntimeError("None of the hazard-specific yearly DDPM files had the required schema")

    rebuilt = pd.concat(frames, ignore_index=True)
    rebuilt["subdistrict_code"] = rebuilt["subdistrict_code"].astype(str).str.zfill(6)
    rebuilt["province_code"] = rebuilt["province_code"].astype(str).str.zfill(2)
    rebuilt["year_be"] = rebuilt["year_be"].astype(str)
    rebuilt = rebuilt.sort_values(
        ["canonical_hazard_code", "subdistrict_code", "year_be"],
        kind="mergesort",
    ).reset_index(drop=True)

    out_path = ddpm_dir / "fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv"
    rebuilt.to_csv(out_path, index=False, encoding="utf-8-sig")
    return out_path, [p.name for p in source_files], missing_report


def metric_top_bottom(df: pd.DataFrame, value_col: str, code_col: str, name_th_col: str, name_en_col: str | None = None, national: bool = False):
    ordered = df.sort_values([value_col, code_col], ascending=[False, True]).copy()
    ordered["rank_desc"] = descending_rank(ordered[value_col])
    top = ordered.head(10)
    bottom = ordered.sort_values([value_col, code_col], ascending=[True, True]).head(10)

    def recs(frame):
        rows = []
        for _, r in frame.iterrows():
            item = {
                code_col: r[code_col],
                name_th_col: r[name_th_col],
                value_col: float(r[value_col]),
                "display_value": r["display_value"],
                "rank_desc": int(r["rank_desc"]),
            }
            if name_en_col is not None:
                item[name_en_col] = r[name_en_col]
            rows.append(item)
        return rows

    return recs(top), recs(bottom), ordered


def province_metric_payload(metric_key, metric_label, period_key, period_label, unit_label, source_mode, df):
    df = df.copy()
    df["display_value"] = df["value"].map(lambda x: f"{x:.6f}".rstrip("0").rstrip(".") if isinstance(x, (int, float, np.floating)) else str(x))
    df["rank_desc"] = descending_rank(df["value"])
    if metric_key == "cri_score" or metric_key.startswith("heat_"):
        df["normalized_value"] = minmax(df["value"]) if metric_key == "cri_score" else None
    else:
        df["normalized_value"] = minmax(df["value"])
    if metric_key == "cri_score":
        df["normalized_value"] = minmax(df["value"])
    legend = {
        "min": float(df["value"].min()),
        "max": float(df["value"].max()),
        "display_min": f"{df['value'].min():.6f}".rstrip("0").rstrip("."),
        "display_max": f"{df['value'].max():.6f}".rstrip("0").rstrip("."),
        "color_scheme": "OrRd" if metric_key != "cri_score" else "GnBu",
    }
    records = []
    for _, r in df.iterrows():
        records.append({
            "province_code": str(r["province_code"]).zfill(2),
            "province_name_th": r["province_name_th"],
            "province_name_en": r.get("province_name_en", None),
            "value": float(r["value"]),
            "display_value": r["display_value"],
            "rank_desc": int(r["rank_desc"]),
            "normalized_value": None if pd.isna(r.get("normalized_value", None)) else float(r["normalized_value"]),
        })
    top, bottom, _ = metric_top_bottom(df, "value", "province_code", "province_name_th", "province_name_en")
    return {
        "metric_key": metric_key,
        "metric_label": metric_label,
        "period_key": period_key,
        "period_label": period_label,
        "unit_label": unit_label,
        "source_mode": source_mode,
        "legend": legend,
        "records": records,
        "rankings": {"top_10": top, "bottom_10": bottom},
    }


def tambon_metric_payload(metric_key, metric_label, period_key, period_label, unit_label, source_mode, df):
    df = df.copy()
    df["display_value"] = df["value"].map(lambda x: f"{x:.6f}".rstrip("0").rstrip(".") if isinstance(x, (int, float, np.floating)) else str(x))
    df = df.sort_values(["value", "subdistrict_code"], ascending=[False, True]).copy()
    df["rank_desc"] = descending_rank(df["value"])
    records = []
    for _, r in df.iterrows():
        records.append({
            "subdistrict_code": str(r["subdistrict_code"]).zfill(6),
            "subdistrict_name_th": r["subdistrict_name_th"],
            "district_name_th": r["district_name_th"],
            "province_code": str(r["province_code"]).zfill(2),
            "province_name_th": r["province_name_th"],
            "value": float(r["value"]),
            "display_value": r["display_value"],
        })
    top, bottom, _ = metric_top_bottom(df, "value", "subdistrict_code", "subdistrict_name_th", "province_name_th")
    return {
        "metric_key": metric_key,
        "metric_label": metric_label,
        "period_key": period_key,
        "period_label": period_label,
        "unit_label": unit_label,
        "source_mode": source_mode,
        "records": records,
        "rankings": {"national_top_10": top, "national_bottom_10": bottom},
    }


def main():
    _stdout_utf8()
    yearly_path, yearly_sources, yearly_missing = rebuild_yearly_ddpm_fact(SRC / "2_gold/ddpm")
    print(f"[REPAIR] Rebuilt yearly DDPM fact: {yearly_path}")
    print(f"[REPAIR] Upstream yearly sources: {', '.join(yearly_sources)}")
    if yearly_missing:
        print("[REPAIR] Skipped due to missing schema: " + "; ".join(yearly_missing))

    ddpm = load_csv(SRC / "2_gold/ddpm/fact_ddpm_tambon_impact_climate_2560_2567.csv")
    ddpm_yearly = load_csv(yearly_path)
    pop = load_csv(SRC / "1_silver/population/silver_population_annual.csv")
    hh = load_csv(SRC / "1_silver/population/silver_household_annual.csv")
    loss = load_csv(SRC / "1_silver/govt_adv_payment/silver_govt_adv_payment_annual_long.csv")
    gpp = load_csv(SRC / "1_silver/gpp/silver_gpp_annual_long.csv")
    heat = load_csv(SRC / "1_silver/heatwave/silver_heatwave_impact_long.csv")
    prov_code_lookup = load_csv(SRC / "1_silver/dopa/province_code_lookup.csv")
    prov_gdf = gpd.read_file(SRC / "1_silver/dopa/province_boundaries_enriched.shp")
    tambon_gdf = gpd.read_file(SRC / "1_silver/dopa/tambon_boundaries_enriched.shp")

    # Normalize join keys to stable string form
    for frame, cols in [
        (ddpm, ["province_code", "subdistrict_code", "year_be"]),
        (ddpm_yearly, ["province_code", "subdistrict_code", "year_be"]),
        (pop, ["province_code", "year_be"]),
        (hh, ["province_code", "year_be"]),
        (loss, ["province_code", "year_be"]),
        (gpp, ["province_code", "year_be"]),
        (heat, ["province_code", "year_be"]),
    ]:
        for col in cols:
            if col in frame.columns:
                frame[col] = frame[col].astype(str)

    if "year_be" in ddpm.columns:
        ddpm["year_be"] = ddpm["year_be"].astype(str)
    if "year_be" in ddpm_yearly.columns:
        ddpm_yearly["year_be"] = ddpm_yearly["year_be"].astype(str)
    if "year_be" in pop.columns:
        pop["year_be"] = pop["year_be"].astype(str)
    if "year_be" in hh.columns:
        hh["year_be"] = hh["year_be"].astype(str)
    if "year_be" in loss.columns:
        loss["year_be"] = loss["year_be"].astype(str)
    if "year_be" in gpp.columns:
        gpp["year_be"] = gpp["year_be"].astype(str)
    if "year_be" in heat.columns:
        heat["year_be"] = heat["year_be"].astype(str)

    # Yearly DDPM fact stores the canonical province code in suffixed merge columns.
    if "province_code" not in ddpm_yearly.columns:
        ddpm_yearly["province_code"] = np.nan
    if "province_code_y" in ddpm_yearly.columns:
        ddpm_yearly["province_code"] = ddpm_yearly["province_code"].where(
            ddpm_yearly["province_code"].notna() & (ddpm_yearly["province_code"].astype(str).str.strip() != ""),
            ddpm_yearly["province_code_y"],
        )
    if "province_code_x" in ddpm_yearly.columns:
        ddpm_yearly["province_code"] = ddpm_yearly["province_code"].where(
            ddpm_yearly["province_code"].notna() & (ddpm_yearly["province_code"].astype(str).str.strip() != "") & (ddpm_yearly["province_code"].astype(str) != "nan"),
            ddpm_yearly["province_code_x"],
        )
    if "province_code" in ddpm_yearly.columns and "subdistrict_code" in ddpm_yearly.columns:
        ddpm_yearly["province_code"] = ddpm_yearly["province_code"].fillna(ddpm_yearly["subdistrict_code"].astype(str).str[:2])
    if "province_code" in ddpm.columns:
        ddpm["province_code"] = ddpm["province_code"].astype(str)
    if "province_code" in ddpm_yearly.columns:
        ddpm_yearly["province_code"] = ddpm_yearly["province_code"].astype(str)
        ddpm_yearly.loc[ddpm_yearly["province_code"].str.lower().isin(["nan", "none", ""]), "province_code"] = ddpm_yearly.loc[
            ddpm_yearly["province_code"].str.lower().isin(["nan", "none", ""]), "subdistrict_code"
        ].astype(str).str[:2]

    tambon_lookup_ddpm = ddpm[["subdistrict_code", "subdistrict_name_th", "district_name_th", "province_code"]].drop_duplicates()

    ensure_dir(OUT)
    ensure_dir(OUT / "period_2560_2567")
    ensure_dir(OUT / "period_2567")
    ensure_dir(OUT / "spatial" / "tambon")

    prov_lookup = province_lookup_from_csv(prov_code_lookup).merge(
        province_lookup_from_shp(prov_gdf)[["province_code", "geometry"]],
        on="province_code",
        how="left",
    )
    tambon_lookup = tambon_lookup_from_shp(tambon_gdf)

    # Province metrics for 2560-2567 average
    human = ddpm.groupby(["province_code"], dropna=False).agg(
        deaths_sum=("deaths_sum", "sum"),
        affected_households_sum=("affected_households_sum", "sum"),
    ).reset_index()
    human["deaths_abs"] = human["deaths_sum"] / 8.0
    human["affected_hh_abs"] = human["affected_households_sum"] / 8.0

    # Ensure we only average the specific 8-year period for population and households
    period_years = [str(y) for y in range(2560, 2568)]
    
    # Correct multi-step aggregation:
    # 1. Sum tambons to get Province Total per Year
    # 2. Average the Annual Province Totals
    pop_annual = pop[pop["year_be"].isin(period_years)].groupby(["province_code", "year_be"], dropna=False)["population_total"].sum().reset_index()
    pop_avg = pop_annual.groupby("province_code", dropna=False)["population_total"].mean().reset_index()
    
    hh_annual = hh[hh["year_be"].isin(period_years)].groupby(["province_code", "year_be"], dropna=False)["household_total"].sum().reset_index()
    hh_avg = hh_annual.groupby("province_code", dropna=False)["household_total"].mean().reset_index()
    gpp_avg = gpp[gpp["metric_code"] == "GPP_CURRENT_MARKET_PRICE"].groupby("province_code", dropna=False)["value"].mean().reset_index().rename(columns={"value": "gpp_avg"})
    loss_avg = loss.groupby("province_code", dropna=False)["value"].sum().reset_index()
    loss_avg["loss_abs"] = (loss_avg["value"] / 8.0)  # Keep in THB (Government Advance Payment)

    prov_avg = prov_lookup.merge(human[["province_code", "deaths_abs", "affected_hh_abs"]], on="province_code", how="left")
    prov_avg = prov_avg.merge(pop_avg, on="province_code", how="left")
    prov_avg = prov_avg.merge(hh_avg, on="province_code", how="left")
    prov_avg = prov_avg.merge(gpp_avg, on="province_code", how="left")
    prov_avg = prov_avg.merge(loss_avg[["province_code", "loss_abs"]], on="province_code", how="left")
    prov_avg["deaths_rate"] = prov_avg["deaths_abs"] / prov_avg["population_total"] * 100000
    prov_avg["affected_rate"] = prov_avg["affected_hh_abs"] / prov_avg["household_total"] * 100
    
    # GPP is in Million THB, Relief (loss_abs) is in THB.
    # Ratio (%) = (Relief_THB / (GPP_Million_THB * 1,000,000)) * 100
    gpp_thb = prov_avg["gpp_avg"] * 1_000_000
    prov_avg["loss_per_gpp"] = (prov_avg["loss_abs"] / gpp_thb) * 100.0 
    
    for c in ["deaths_abs", "deaths_rate", "affected_hh_abs", "affected_rate", "loss_abs", "loss_per_gpp"]:
        prov_avg[f"s_{c}"] = minmax(prov_avg[c])
    prov_avg["cri_score"] = (
        prov_avg["s_deaths_abs"] * 0.075
        + prov_avg["s_deaths_rate"] * 0.225
        + prov_avg["s_affected_hh_abs"] * 0.05
        + prov_avg["s_affected_rate"] * 0.15
        + prov_avg["s_loss_abs"] * 0.125
        + prov_avg["s_loss_per_gpp"] * 0.375
    )
    prov_avg["province_name_en"] = prov_avg["province_name_en"].where(pd.notna(prov_avg["province_name_en"]), None)

    avg_specs = [
        ("deaths_abs", "Total Deaths (Absolute)", "Annual deaths"),
        ("deaths_rate", "Death Rate", "Per 100,000 population"),
        ("affected_hh_abs", "Total Affected Households (Absolute)", "Annual households"),
        ("affected_rate", "Affected Rate", "Per 100 households"),
        ("loss_abs", "Government Advance Payment", "THB"),
        ("loss_per_gpp", "Relief per Unit GPP", "Percentage points (%)"),
        ("cri_score", "CRI Phase 1 Score", "Score [0-1]"),
    ]
    for metric_key, metric_label, unit_label in avg_specs:
        payload = province_metric_payload(metric_key, metric_label, "period_2560_2567", "2560–2567 average", unit_label, "average_window", prov_avg[["province_code", "province_name_th", "province_name_en", metric_key]].rename(columns={metric_key: "value"}))
        write_json(OUT / "period_2560_2567" / f"{metric_key}.json", payload)

    # Province metrics for 2567
    yearly_2567 = ddpm_yearly[ddpm_yearly["year_be"] == "2567"].copy()
    human_2567 = yearly_2567.groupby(["province_code"], dropna=False).agg(
        deaths_sum=("deaths_sum", "sum"),
        affected_households_sum=("affected_households_sum", "sum"),
    ).reset_index()
    human_2567["deaths_abs"] = human_2567["deaths_sum"]
    human_2567["affected_hh_abs"] = human_2567["affected_households_sum"]
    human_2567 = human_2567.merge(prov_lookup[["province_code", "province_name_th", "province_name_en"]], on="province_code", how="left")

    pop_2567 = pop[(pop["geography_level"] == "province") & (pop["year_be"] == "2567")].groupby("province_code", dropna=False)["population_total"].mean().reset_index()
    hh_2567 = hh[hh["year_be"] == "2567"].groupby("province_code", dropna=False)["household_total"].mean().reset_index()
    gpp_2567 = gpp[(gpp["metric_code"] == "GPP_CURRENT_MARKET_PRICE") & (gpp["year_be"] == "2567")].groupby("province_code", dropna=False)["value"].mean().reset_index().rename(columns={"value": "gpp_avg"})
    loss_2567 = loss[loss["year_be"] == "2567"].groupby("province_code", dropna=False)["value"].sum().reset_index().rename(columns={"value": "loss_abs"})
    # loss_2567["loss_abs"] is already in THB from sum

    prov_2567 = prov_lookup.merge(human_2567[["province_code", "deaths_abs", "affected_hh_abs"]], on="province_code", how="left")
    prov_2567 = prov_2567.merge(pop_2567, on="province_code", how="left")
    prov_2567 = prov_2567.merge(hh_2567, on="province_code", how="left")
    prov_2567 = prov_2567.merge(gpp_2567, on="province_code", how="left")
    prov_2567 = prov_2567.merge(loss_2567, on="province_code", how="left")
    prov_2567["deaths_rate"] = prov_2567["deaths_abs"] / prov_2567["population_total"] * 100000
    prov_2567["affected_rate"] = prov_2567["affected_hh_abs"] / prov_2567["household_total"] * 100
    
    # Ratio calculation for 2567
    gpp_thb_2567 = prov_2567["gpp_avg"] * 1_000_000
    prov_2567["loss_per_gpp"] = (prov_2567["loss_abs"] / gpp_thb_2567) * 100.0 

    for c in ["deaths_abs", "deaths_rate", "affected_hh_abs", "affected_rate", "loss_abs", "loss_per_gpp"]:
        prov_2567[f"s_{c}"] = minmax(prov_2567[c])
    prov_2567["cri_score"] = (
        prov_2567["s_deaths_abs"] * 0.075
        + prov_2567["s_deaths_rate"] * 0.225
        + prov_2567["s_affected_hh_abs"] * 0.05
        + prov_2567["s_affected_rate"] * 0.15
        + prov_2567["s_loss_abs"] * 0.125
        + prov_2567["s_loss_per_gpp"] * 0.375
    )
    prov_2567["province_name_en"] = prov_2567["province_name_en"].where(pd.notna(prov_2567["province_name_en"]), None)
    
    # Define specs after both blocks to ensure consistency
    avg_specs = [
        ("deaths_abs", "Total Deaths (Absolute)", "Annual deaths"),
        ("deaths_rate", "Death Rate", "Per 100,000 population"),
        ("affected_hh_abs", "Total Affected Households (Absolute)", "Annual households"),
        ("affected_rate", "Affected Rate", "Per 100 households"),
        ("loss_abs", "Government Advance Payment", "THB"),
        ("loss_per_gpp", "Relief per Unit GPP", "Percentage points (%)"),
        ("cri_score", "CRI Phase 1 Score", "Score [0-1]"),
    ]
    for metric_key, metric_label, unit_label in avg_specs:
        payload = province_metric_payload(metric_key, metric_label, "period_2567", "2567 only", unit_label, "single_year", prov_2567[["province_code", "province_name_th", "province_name_en", metric_key]].rename(columns={metric_key: "value"}))
        write_json(OUT / "period_2567" / f"{metric_key}.json", payload)

    # Tambon metrics follow the same lineage as province metrics: 2560–2567 uses the full
    # range fact averaged to an annual value, while 2567 only stays as the single-year slice.
    tambon_avg = ddpm.groupby(["subdistrict_code", "province_code"], dropna=False).agg(
        deaths_sum=("deaths_sum", "sum"),
        affected_households_sum=("affected_households_sum", "sum"),
    ).reset_index()
    tambon_avg["deaths_abs"] = tambon_avg["deaths_sum"] / 8.0
    tambon_avg["affected_hh_abs"] = tambon_avg["affected_households_sum"] / 8.0
    tambon_avg = tambon_avg.merge(tambon_lookup_ddpm, on=["subdistrict_code", "province_code"], how="left")
    tambon_avg = tambon_avg.merge(prov_lookup[["province_code", "province_name_th"]], on="province_code", how="left")
    if "province_name_th_y" in tambon_avg.columns:
        tambon_avg["province_name_th"] = tambon_avg["province_name_th"].where(
            tambon_avg["province_name_th"].notna()
            & (tambon_avg["province_name_th"].astype(str).str.strip() != "")
            & (tambon_avg["province_name_th"].astype(str) != tambon_avg["province_code"].astype(str)),
            tambon_avg["province_name_th_y"],
        )
        tambon_avg = tambon_avg.drop(columns=["province_name_th_y"])
    tambon_avg_deaths = tambon_avg[["subdistrict_code", "subdistrict_name_th", "district_name_th", "province_code", "province_name_th", "deaths_abs"]].rename(columns={"deaths_abs": "value"})
    tambon_avg_aff = tambon_avg[["subdistrict_code", "subdistrict_name_th", "district_name_th", "province_code", "province_name_th", "affected_hh_abs"]].rename(columns={"affected_hh_abs": "value"})

    tambon_2567 = ddpm_yearly[ddpm_yearly["year_be"] == "2567"].groupby(["subdistrict_code", "province_code"], dropna=False).agg(
        deaths_sum=("deaths_sum", "sum"),
        affected_households_sum=("affected_households_sum", "sum"),
    ).reset_index()
    tambon_2567 = tambon_2567.merge(tambon_lookup_ddpm, on=["subdistrict_code", "province_code"], how="left")
    tambon_2567 = tambon_2567.merge(prov_lookup[["province_code", "province_name_th"]], on="province_code", how="left")
    if "province_name_th_y" in tambon_2567.columns:
        tambon_2567["province_name_th"] = tambon_2567["province_name_th"].where(
            tambon_2567["province_name_th"].notna()
            & (tambon_2567["province_name_th"].astype(str).str.strip() != "")
            & (tambon_2567["province_name_th"].astype(str) != tambon_2567["province_code"].astype(str)),
            tambon_2567["province_name_th_y"],
        )
        tambon_2567 = tambon_2567.drop(columns=["province_name_th_y"])
    tambon_2567_deaths = tambon_2567[["subdistrict_code", "subdistrict_name_th", "district_name_th", "province_code", "province_name_th", "deaths_sum"]].rename(columns={"deaths_sum": "value"})
    tambon_2567_aff = tambon_2567[["subdistrict_code", "subdistrict_name_th", "district_name_th", "province_code", "province_name_th", "affected_households_sum"]].rename(columns={"affected_households_sum": "value"})
    write_json(OUT / "period_2560_2567" / "tambon_deaths.json", tambon_metric_payload("tambon_deaths", "Tambon Deaths", "period_2560_2567", "2560–2567 average", "Annual deaths", "average_window", tambon_avg_deaths))
    write_json(OUT / "period_2560_2567" / "tambon_affected_households.json", tambon_metric_payload("tambon_affected_households", "Tambon Affected Households", "period_2560_2567", "2560–2567 average", "Annual households", "average_window", tambon_avg_aff))
    write_json(OUT / "period_2567" / "tambon_deaths.json", tambon_metric_payload("tambon_deaths", "Tambon Deaths", "period_2567", "2567 only", "Annual deaths", "single_year", tambon_2567_deaths))
    write_json(OUT / "period_2567" / "tambon_affected_households.json", tambon_metric_payload("tambon_affected_households", "Tambon Affected Households", "period_2567", "2567 only", "Annual households", "single_year", tambon_2567_aff))

    # Heat metrics - period 2560-2567 average and 2567 only
    # Note: Heat data is only available from 2561-2567 (7 years)
    heat_def = heat.copy()
    heat_def["metric_code"] = heat_def["metric_code"].astype(str)
    
    heat_avg_sum = heat_def[heat_def["time_scope"] == "range_2561_2567"].groupby(["province_code", "province_name_th", "metric_code"], dropna=False)["value"].sum().reset_index()
    heat_avg = heat_avg_sum.copy()
    heat_avg["value"] = heat_avg["value"] / 7.0
    
    heat_257 = heat_def[heat_def["time_scope"] == "year_2567"].groupby(["province_code", "province_name_th", "metric_code"], dropna=False)["value"].sum().reset_index()

    def heat_metric(metric_code: str, frame: pd.DataFrame, period_key: str, period_label: str):
        sub = frame[frame["metric_code"] == metric_code][["province_code", "province_name_th", "value"]].copy()
        if sub.empty:
            raise RuntimeError(f"Heat metric {metric_code} missing for {period_key}")
        sub = sub.rename(columns={"province_name_th": "province_name_th_src"})
        sub = prov_lookup.merge(sub, on="province_code", how="left")
        if "province_name_th_src" in sub.columns:
            sub["province_name_th"] = sub["province_name_th_src"].where(
                sub["province_name_th_src"].notna() & (sub["province_name_th_src"].astype(str).str.strip() != ""),
                sub["province_name_th"],
            )
            sub = sub.drop(columns=["province_name_th_src"])
        sub["province_name_en"] = None
        return province_metric_payload(
            f"heat_{metric_code.lower()}",
            "Heat-Related Deaths" if metric_code == "DEATHS" else "Heat-Related Injured",
            period_key,
            period_label,
            "Annual deaths" if metric_code == "DEATHS" else "Annual injuries",
            "average_window" if period_key == "period_2560_2567" else "single_year",
            sub,
        )

    write_json(OUT / "period_2560_2567" / "heat_deaths.json", heat_metric("DEATHS", heat_avg, "period_2560_2567", "2560–2567 average"))
    write_json(OUT / "period_2560_2567" / "heat_injured.json", heat_metric("INJURED", heat_avg, "period_2560_2567", "2560–2567 average"))
    write_json(OUT / "period_2567" / "heat_deaths.json", heat_metric("DEATHS", heat_257, "period_2567", "2567 only"))
    write_json(OUT / "period_2567" / "heat_injured.json", heat_metric("INJURED", heat_257, "period_2567", "2567 only"))

    # Spatial assets
    prov_out = prov_gdf.copy()
    prov_out.to_file(OUT / "spatial" / "province_boundaries.geojson", driver="GeoJSON")
    tambon_by_prov = []
    for pcode, group in tambon_lookup.groupby("province_code"):
        file = OUT / "spatial" / "tambon" / f"{pcode}.geojson"
        group_gdf = gpd.GeoDataFrame(group.drop(columns=["geometry"]), geometry=group["geometry"], crs=tambon_gdf.crs)
        group_gdf.to_file(file, driver="GeoJSON")
        tambon_by_prov.append({
            "province_code": pcode,
            "province_name_th": str(group["province_name_th"].dropna().iloc[0]) if group["province_name_th"].notna().any() else None,
            "file": f"spatial/tambon/{pcode}.geojson",
        })

    manifest = {
        "version": "2026-06-17-stage1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "periods": [
            {"period_key": "period_2560_2567", "period_label": "2560–2567 average"},
            {"period_key": "period_2567", "period_label": "2567 only"},
        ],
        "metric_groups": {
            "cri": ["deaths_abs", "deaths_rate", "affected_hh_abs", "affected_rate", "loss_abs", "loss_per_gpp", "cri_score"],
            "tambon": ["tambon_deaths", "tambon_affected_households"],
            "heat": ["heat_deaths", "heat_injured"],
        },
        "assets": {
            "province_geometry": "spatial/province_boundaries.geojson",
            "tambon_manifest": "spatial/manifest.json",
        },
    }
    spatial_manifest = {
        "province_geometry": "spatial/province_boundaries.geojson",
        "tambon_by_province": sorted(tambon_by_prov, key=lambda x: x["province_code"]),
    }
    write_json(OUT / "manifest.json", manifest)
    write_json(OUT / "spatial" / "manifest.json", spatial_manifest)

    validation = {
        "province_metric_files": sorted([p.name for p in (OUT / "period_2560_2567").glob("*.json") if p.name not in {"tambon_deaths.json", "tambon_affected_households.json"}] + [p.name for p in (OUT / "period_2567").glob("*.json") if p.name not in {"tambon_deaths.json", "tambon_affected_households.json"}]),
        "tambon_files": sorted([p.name for p in (OUT / "period_2560_2567").glob("tambon_*.json")]) + sorted([p.name for p in (OUT / "period_2567").glob("tambon_*.json")]),
        "heat_files": sorted([p.name for p in (OUT / "period_2560_2567").glob("heat_*.json")]) + sorted([p.name for p in (OUT / "period_2567").glob("heat_*.json")]),
        "spatial_province_exists": (OUT / "spatial" / "province_boundaries.geojson").exists(),
        "spatial_manifest_exists": (OUT / "spatial" / "manifest.json").exists(),
        "province_metric_count": len(list((OUT / "period_2560_2567").glob("*.json"))) + len(list((OUT / "period_2567").glob("*.json"))),
    }
    write_json(OUT / "validation_summary.json", validation)


if __name__ == "__main__":
    main()
