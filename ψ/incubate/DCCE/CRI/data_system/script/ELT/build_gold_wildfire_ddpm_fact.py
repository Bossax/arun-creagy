import pandas as pd
import numpy as np
from pathlib import Path

# Setup paths
base_path = Path(__file__).resolve().parents[2]
bronze_csv = base_path / "data/0_bronze/2026-07-16-cri-proj-data/Wildfire_ppl_data.csv"
spine_csv = base_path / "data/2_gold/dopa/dim_location_master.csv"
out_dir = base_path / "data/2_gold/ddpm"

print(f"[INFO] Ingesting raw wildfire data from: {bronze_csv}")

# Read inputs
df = pd.read_csv(bronze_csv)
spine = pd.read_csv(spine_csv)

# Clean subdistrict codes helper
def clean_code(series):
    s = series.astype(str).str.replace(r"\.0$", "", regex=True).str.strip()
    return s.str.zfill(6)

df["tambon_code"] = clean_code(df["tambon_code"])

# Filter location spine for subdistricts
if "admin_level" in spine.columns:
    spine_sd = spine.loc[
        spine["admin_level"].astype(str).eq("subdistrict"),
        ["subdistrict_code", "province_code", "province_name_th", "district_name_th", "subdistrict_name_th"]
    ].drop_duplicates(subset=["subdistrict_code"])
else:
    spine_sd = spine[
        ["subdistrict_code", "province_code", "province_name_th", "district_name_th", "subdistrict_name_th"]
    ].drop_duplicates(subset=["subdistrict_code"])

spine_sd["subdistrict_code"] = clean_code(spine_sd["subdistrict_code"])

# Melt the wide columns for years 2560 to 2567
years = list(range(2560, 2568))

rows = []
for _, row in df.iterrows():
    subdist_code = row["tambon_code"]
    
    # Safely convert float/int prov_code to string
    try:
        prov_code = str(int(float(row["prov_code"]))).zfill(2)
    except Exception:
        prov_code = str(row["prov_code"]).split(".")[0].zfill(2)
        
    for y in years:
        y_short = str(y)[-2:]
        
        # Deaths
        death_col = f"wildfire_death_{y_short}"
        deaths = float(row[death_col]) if death_col in row and not pd.isna(row[death_col]) else 0.0
        
        # Affected households
        affected_col = f"wildfire_affected_{y_short}"
        affected = float(row[affected_col]) if affected_col in row and not pd.isna(row[affected_col]) else 0.0
        
        rows.append({
            "canonical_hazard_id": 12,
            "canonical_hazard_code": "WILDFIRE",
            "canonical_hazard_name_th": "ไฟป่า",
            "subdistrict_code": subdist_code,
            "year_be": y,
            "affected_households_sum": affected,
            "affected_people_sum": 0.0,
            "deaths_sum": deaths,
            "province_code": prov_code
        })

yearly_df = pd.DataFrame(rows)

# Add YoY change for each subdistrict
yearly_df = yearly_df.sort_values(["subdistrict_code", "year_be"]).reset_index(drop=True)
yearly_df["yoy_delta_affected_households"] = (
    yearly_df.groupby("subdistrict_code")["affected_households_sum"].diff().fillna(0.0)
)

# Period aggregate dataframe
fact_df = (
    yearly_df.groupby("subdistrict_code", as_index=False)
    .agg(
        affected_households_sum=("affected_households_sum", "sum"),
        affected_people_sum=("affected_people_sum", "sum"),
        deaths_sum=("deaths_sum", "sum"),
    )
)

# YoY average for years 2561-2567
yoy_for_mean = yearly_df.loc[yearly_df["year_be"].between(2561, 2567)].copy()
avg_yoy = (
    yoy_for_mean.groupby("subdistrict_code", as_index=False)["yoy_delta_affected_households"].mean()
    .rename(columns={"yoy_delta_affected_households": "avg_yoy_change"})
)
fact_df = fact_df.merge(avg_yoy, on="subdistrict_code", how="left").fillna(0.0)

# Merge with location spine for names
fact_df = fact_df.merge(spine_sd, on="subdistrict_code", how="left")
fact_df["province_code"] = fact_df["province_code"].astype(str).str.split(".").str[0].str.zfill(2)

fact_df.insert(0, "canonical_hazard_name_th", "ไฟป่า")
fact_df.insert(0, "canonical_hazard_code", "WILDFIRE")
fact_df.insert(0, "canonical_hazard_id", 12)

# Calculate percentiles
def pct_rank(val):
    v = pd.to_numeric(val, errors="coerce").fillna(0)
    r = v.rank(method="average", ascending=True)
    n = len(v)
    return ((r - 1) / (n - 1) * 100) if n > 1 else pd.Series([100.0] * n, index=v.index)

for m in ["affected_households_sum", "affected_people_sum", "deaths_sum", "avg_yoy_change"]:
    fact_df[f"pct_national_{m}"] = pct_rank(fact_df[m])

# Sort and Save
fact_df = fact_df.sort_values("subdistrict_code").reset_index(drop=True)
yearly_df = yearly_df.sort_values(["subdistrict_code", "year_be"]).reset_index(drop=True)

# Write output CSV files
out_dir.mkdir(parents=True, exist_ok=True)
fact_df.to_csv(out_dir / "fact_ddpm_tambon_impact_climate_wildfire_2560_2567.csv", index=False, encoding="utf-8-sig")
yearly_df.to_csv(out_dir / "fact_ddpm_tambon_impact_climate_yearly_wildfire_2560_2567.csv", index=False, encoding="utf-8-sig")

print(f"[OK] Ingested wildfire facts to gold layer successfully!")
