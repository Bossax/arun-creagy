import pandas as pd
import geopandas as gpd
import re
from pathlib import Path

def normalize_admin_name(value):
    if value is None: return ""
    s = str(value).replace("\u200b", "").replace("\xa0", " ").strip()
    s = re.sub(r"\s+", " ", s)
    prefixes = ["จังหวัด", "จ.", "อำเภอ", "อ.", "เขต", "ตำบล", "ต.", "แขวง"]
    for p in prefixes:
        if s.startswith(p):
            s = s[len(p):].strip()
    return s.replace("ฯ", "").strip()

def main():
    base_path = Path(__file__).resolve().parent.parent.parent
    gold_spine_path = base_path / "data/2_gold/dim_location_master.csv"
    tambon_shp_path = base_path / "data/0_bronze/dopa/thailanda-administrative-boundary/THA_Tambon.shp"
    prov_shp_path = base_path / "data/0_bronze/dopa/thailanda-administrative-boundary/THA_Province.shp"
    
    out_tambon = base_path / "data/1_silver/dopa/tambon_boundaries_enriched.shp"
    out_province = base_path / "data/1_silver/dopa/province_boundaries_enriched.shp"
    
    out_tambon.parent.mkdir(parents=True, exist_ok=True)

    print(f"Reading location master from {gold_spine_path}...")
    spine = pd.read_csv(gold_spine_path, dtype={'subdistrict_code': str, 'province_code': str})
    
    # --- Part 1: Tambon Enrichment ---
    print("Processing Tambon boundaries...")
    spine_t = spine[['province_name_th', 'district_name_th', 'subdistrict_name_th', 'subdistrict_code', 'province_code']].drop_duplicates()
    for col in ['province_name_th', 'district_name_th', 'subdistrict_name_th']:
        spine_t[col + '_norm'] = spine_t[col].apply(normalize_admin_name)

    gdf_t = gpd.read_file(tambon_shp_path)
    if gdf_t.crs is None or gdf_t.crs.to_epsg() != 4326:
        gdf_t = gdf_t.to_crs(epsg=4326)

    gdf_t['p_norm'] = gdf_t['P_NAME_T'].apply(normalize_admin_name)
    gdf_t['a_norm'] = gdf_t['A_NAME_T'].apply(normalize_admin_name)
    gdf_t['t_norm'] = gdf_t['T_NAME_T'].apply(normalize_admin_name)

    enriched_t = gdf_t.merge(
        spine_t,
        left_on=['p_norm', 'a_norm', 't_norm'],
        right_on=['province_name_th_norm', 'district_name_th_norm', 'subdistrict_name_th_norm'],
        how='left'
    )
    enriched_t = enriched_t.rename(columns={'subdistrict_code': 'subdist_cd', 'province_code': 'prov_code'})
    
    cols_t = [c for c in enriched_t.columns if not c.endswith('_norm') and c not in ['province_name_th', 'district_name_th', 'subdistrict_name_th']]
    enriched_t[cols_t].to_file(out_tambon, driver='ESRI Shapefile', encoding='utf-8')
    print(f"Saved: {out_tambon}")

    # --- Part 2: Province Enrichment ---
    print("Processing Province boundaries...")
    spine_p = spine[['province_name_th', 'province_code']].drop_duplicates()
    spine_p['province_name_th_norm'] = spine_p['province_name_th'].apply(normalize_admin_name)

    gdf_p = gpd.read_file(prov_shp_path)
    if gdf_p.crs is None or gdf_p.crs.to_epsg() != 4326:
        gdf_p = gdf_p.to_crs(epsg=4326)

    gdf_p['p_norm'] = gdf_p['P_NAME_T'].apply(normalize_admin_name)

    enriched_p = gdf_p.merge(
        spine_p,
        left_on='p_norm',
        right_on='province_name_th_norm',
        how='left'
    )
    enriched_p = enriched_p.rename(columns={'province_code': 'prov_code'})
    
    cols_p = [c for c in enriched_p.columns if not c.endswith('_norm') and c != 'province_name_th']
    enriched_p[cols_p].to_file(out_province, driver='ESRI Shapefile', encoding='utf-8')
    print(f"Saved: {out_province}")

    print("SUCCESS: Silver boundaries prepared (Tambon and Province).")

if __name__ == "__main__":
    main()
