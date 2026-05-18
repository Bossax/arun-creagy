import pandas as pd
import geopandas as gpd
import re
from pathlib import Path
import sys

def normalize_admin_name(value):
    if value is None: return ""
    # Standardize whitespace and invisible characters
    s = str(value).strip()
    s = s.replace("\u200b", "").replace("\xa0", " ").replace("\r", "").replace("\n", "")
    s = re.sub(r"\s+", " ", s)
    # Strip common admin prefixes
    prefixes = ["จังหวัด", "จ.", "อำเภอ", "อ.", "เขต", "ตำบล", "ต.", "แขวง", "กิ่งอำเภอ"]
    for p in prefixes:
        if s.startswith(p):
            s = s[len(p):].strip()
    return s.replace("ฯ", "").strip()

def apply_surgical_patches(row):
    """
    Applies GIS-to-Gold-Spine mappings to handle administrative splits, 
    legacy naming in shapefiles, and 'King Amphoe' prefixes.
    """
    p, a, t = row['p_norm'], row['a_norm'], row['t_norm']
    
    # Define Patch Map: (Normalized Shapefile Name) -> (Target Gold Spine Canonical Name)
    PATCH_MAP = {
        # Chiang Mai: Mae Chaem -> Galyani Vadhana Split (2009)
        # Shapefile still labels these under Mae Chaem
        ('เชียงใหม่', 'แม่แจ่ม', 'บ้านจันทร์'): ('เชียงใหม่', 'กัลยาณิวัฒนา', 'บ้านจันทร์'),
        ('เชียงใหม่', 'แม่แจ่ม', 'แม่แดด'): ('เชียงใหม่', 'กัลยาณิวัฒนา', 'แม่แดด'),
        ('เชียงใหม่', 'แม่แจ่ม', 'แจ่มหลวง'): ('เชียงใหม่', 'กัลยาณิวัฒนา', 'แจ่มหลวง'),
        
        # Khon Kaen: Phu Wiang -> Wiang Kao Split (2006)
        ('ขอนแก่น', 'ภูเวียง', 'ในเมือง'): ('ขอนแก่น', 'เวียงเก่า', 'ในเมือง'),
        ('ขอนแก่น', 'ภูเวียง', 'เมืองเก่าพัฒนา'): ('ขอนแก่น', 'เวียงเก่า', 'เมืองเก่าพัฒนา'),
        ('ขอนแก่น', 'ภูเวียง', 'เขาน้อย'): ('ขอนแก่น', 'เวียงเก่า', 'เขาน้อย'),
        
        # Korat: King Amphoe -> Full District Rename
        ('นครราชสีมา', 'กิ่งอำเภอบัวลาย', t): ('นครราชสีมา', 'บัวลาย', t),
        ('นครราชสีมา', 'กิ่งอำเภอพระทองคำ', t): ('นครราชสีมา', 'พระทองคำ', t),
        ('นครราชสีมา', 'กิ่งอำเภอเมืองยาง', t): ('นครราชสีมา', 'เมืองยาง', t),
        ('นครราชสีมา', 'กิ่งอำเภอเทพารักษ์', t): ('นครราชสีมา', 'เทพารักษ์', t),
        ('นครราชสีมา', 'กิ่งอำเภอสีดา', t): ('นครราชสีมา', 'สีดา', t),
        ('นครราชสีมา', 'กิ่งอำเภอลำทะเมนชัย', t): ('นครราชสีมา', 'ลำทะเมนชัย', t),
        
        # Korat: Nong Bun Nak (Legacy) -> Nong Bun Mak (Current)
        ('นครราชสีมา', 'หนองบุนนาก', t): ('นครราชสีมา', 'หนองบุญมาก', t),

        # Roi Et: Po Phan Variant
        ('ร้อยเอ็ด', 'เมืองร้อยเอ็ด', 'ปอภาร'): ('ร้อยเอ็ด', 'เมืองร้อยเอ็ด', 'ปอภาร (ปอพาน)'),
        
        # Nan: Suak -> Bo Suak (Rename)
        ('น่าน', 'เมืองน่าน', 'สวก'): ('น่าน', 'เมืองน่าน', 'บ่อสวก'),
        
        # Bangkok: Subdivision (2017) Mapping to Primary Code
        ('กรุงเทพมหานคร', 'บางนา', 'บางนา'): ('กรุงเทพมหานคร', 'บางนา', 'บางนาเหนือ'),
        ('กรุงเทพมหานคร', 'บางบอน', 'บางบอน'): ('กรุงเทพมหานคร', 'บางบอน', 'บางบอนเหนือ'),
        
        # Narathiwat: Su-ngai Kolok Hyphenation
        ('นราธิวาส', 'สุไหงโกลก', t): ('นราธิวาส', 'สุไหงโก-ลก', t),

        # --- Forensic Patches (2026-05-18): Final 11 GIS Mismatches ---
        ('อุตรดิตถ์', 'ท่าปลา', 'ท่าแฝก'): ('อุตรดิตถ์', 'น้ำปาด', 'ท่าแฝก'),
        ('อุบลราชธานี', 'สิรินธร', 'นิคมลำโดมน้อย'): ('อุบลราชธานี', 'สิรินธร', 'นิคมสร้างตนเองลำโดมน้อย'),
        ('เชียงใหม่', 'แม่วาง', 'ทุ่งปี้'): ('เชียงใหม่', 'แม่วาง', 'ทุ่งปี๊'),
        ('ชัยภูมิ', 'เกษตรสมบูรณ์', 'ซับสีทอง'): ('ชัยภูมิ', 'เมืองชัยภูมิ', 'ซับสีทอง'),
        ('หนองคาย', 'เมืองหนองคาย', 'สองห้อง'): ('หนองคาย', 'เมืองหนองคาย', 'โพนสว่าง'),
        ('เชียงใหม่', 'อมก๋อย', 'สบโขง'): ('เชียงใหม่', 'อมก๋อย', 'แม่หลอง'),
        ('บึงกาฬ', 'เมืองบึงกาฬ', 'หนองเข็ง'): ('บึงกาฬ', 'เมืองบึงกาฬ', 'โนนสว่าง'),
        ('นครสวรรค์', 'เมืองนครสวรรค์', 'วัดไทร'): ('นครสวรรค์', 'เมืองนครสวรรค์', 'วัดไทรย์'),
        ('แพร่', 'เมืองแพร่', 'วังหงษ์'): ('แพร่', 'เมืองแพร่', 'วังหงส์'),
        ('มหาสารคาม', 'ยางสีสุราช', 'ขามเรียน'): ('มหาสารคาม', 'ยางสีสุราช', 'สร้างแซ่ง'),
        ('อุบลราชธานี', 'วารินชำราบ', 'ห้วยขะยูง'): ('อุบลราชธานี', 'วารินชำราบ', 'ห้วยขะยุง'),
    }
    
    # Check for exact (P, A, T) match first
    if (p, a, t) in PATCH_MAP:
        return pd.Series(PATCH_MAP[(p, a, t)])
    
    # Check for wildcards (P, A, ALL_TAMBONS)
    if (p, a, t) not in PATCH_MAP:
        # Check if there is a district-level wildcard
        district_patch = {k: v for k, v in PATCH_MAP.items() if len(k) == 3 and k[2] == t}
        # This is complex in a dict, let's simplify logic
        pass

    # Simplified wildcard logic for King Amphoe and District renames
    if p == 'นครราชสีมา':
        if a == 'กิ่งอำเภอบัวลาย': return pd.Series(['นครราชสีมา', 'บัวลาย', t])
        if a == 'กิ่งอำเภอพระทองคำ': return pd.Series(['นครราชสีมา', 'พระทองคำ', t])
        if a == 'กิ่งอำเภอเมืองยาง': return pd.Series(['นครราชสีมา', 'เมืองยาง', t])
        if a == 'กิ่งอำเภอเทพารักษ์': return pd.Series(['นครราชสีมา', 'เทพารักษ์', t])
        if a == 'กิ่งอำเภอสีดา': return pd.Series(['นครราชสีมา', 'สีดา', t])
        if a == 'กิ่งอำเภอลำทะเมนชัย': return pd.Series(['นครราชสีมา', 'ลำทะเมนชัย', t])
        if a == 'หนองบุนนาก': return pd.Series(['นครราชสีมา', 'หนองบุญมาก', t])
    
    if p == 'นราธิวาส' and a == 'สุไหงโกลก':
        return pd.Series(['นราธิวาส', 'สุไหงโก-ลก', t])

    return pd.Series([p, a, t])

def main():
    # Ensure Thai/ψ paths can be printed in Windows terminals
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # py3.7+
    except Exception:
        pass

    base_path = Path(__file__).resolve().parent.parent.parent
    # Referencing the newly created GOLD Spine
    spine_path = base_path / "data/2_gold/dopa/dim_location_master.csv"
    tambon_shp_path = base_path / "data/0_bronze/dopa/thailanda-administrative-boundary/THA_Tambon.shp"
    prov_shp_path = base_path / "data/0_bronze/dopa/thailanda-administrative-boundary/THA_Province.shp"

    # Bangkok admin boundary (Bronze; BMA OpenData)
    # Use this geometry for Bangkok subdistricts (khwaeng) instead of the legacy DOPA tambon shapefile
    bma_admin_bnd_path = base_path / "data/0_bronze/bma/admin_bnd/ADMIN_BND.shp"
    
    # Internal project tmp path for forensic audit
    project_tmp = base_path / "tmp"
    project_tmp.mkdir(parents=True, exist_ok=True)
    
    out_tambon = base_path / "data/1_silver/dopa/tambon_boundaries_enriched.shp"
    out_province = base_path / "data/1_silver/dopa/province_boundaries_enriched.shp"
    
    out_tambon.parent.mkdir(parents=True, exist_ok=True)

    print(f"Reading location master from {spine_path}...")
    spine = pd.read_csv(spine_path, dtype={'subdistrict_code': str, 'province_code': str})
    
    # --- Part 1: Tambon Enrichment ---
    print("Processing Tambon boundaries...")

    # Spine tambon rows only (avoid village-level duplicates)
    # Spine tambon rows only.
    # Use admin_level='subdistrict' so province/district/subdistrict names exist for Bangkok joins.
    if 'admin_level' in spine.columns:
        spine_t = spine.loc[
            spine['admin_level'].astype(str).eq('subdistrict'),
            ['province_name_th', 'district_name_th', 'subdistrict_name_th', 'subdistrict_code', 'province_code']
        ].drop_duplicates(subset=['subdistrict_code'])
    else:
        spine_t = spine[['province_name_th', 'district_name_th', 'subdistrict_name_th', 'subdistrict_code', 'province_code']].drop_duplicates(subset=['subdistrict_code'])

    spine_t['subdistrict_code'] = spine_t['subdistrict_code'].astype(str).str.zfill(6)
    spine_t['province_code'] = spine_t['province_code'].astype(str).str.zfill(2)

    # Defensive cleaning: strip any '.0' artifacts or embedded non-digits before zfill
    spine_t['subdistrict_code'] = (
        spine_t['subdistrict_code']
        .astype(str)
        .str.extract(r'(\d+)')[0]
        .fillna('')
        .str[-6:]
        .str.zfill(6)
    )
    spine_t['province_code'] = (
        spine_t['province_code']
        .astype(str)
        .str.extract(r'(\d+)')[0]
        .fillna('')
        .str[-2:]
        .str.zfill(2)
    )

    for col in ['province_name_th', 'district_name_th', 'subdistrict_name_th']:
        spine_t[col + '_norm'] = spine_t[col].apply(normalize_admin_name)

    gdf_t = gpd.read_file(tambon_shp_path)
    if gdf_t.crs is None or gdf_t.crs.to_epsg() != 4326:
        gdf_t = gdf_t.to_crs(epsg=4326)

    gdf_t['p_norm'] = gdf_t['P_NAME_T'].apply(normalize_admin_name)
    gdf_t['a_norm'] = gdf_t['A_NAME_T'].apply(normalize_admin_name)
    gdf_t['t_norm'] = gdf_t['T_NAME_T'].apply(normalize_admin_name)

    # Bangkok geometry policy (locked):
    # - Remove *all* Bangkok geometries from the legacy DOPA tambon shapefile
    # - Replace with Bangkok subdistrict geometries from BMA OpenData layer
    is_bkk_dopa = gdf_t['p_norm'].eq('กรุงเทพมหานคร')
    bkk_dopa_n = int(is_bkk_dopa.sum())
    if bkk_dopa_n > 0:
        gdf_t = gdf_t.loc[~is_bkk_dopa].copy()
        print(f"Removed {bkk_dopa_n} Bangkok geometries from THA_Tambon.shp (will replace with BMA admin boundaries).")

    # Note: apply_surgical_patches is now only used for mapping boundary-specific 
    # variants (like administrative splits) to the Gold Spine values.
    # Korat "Mueang" and Thepharat spelling are now handled UPSTREAM in the Gold Spine.
    print("Applying surgical patches for administrative splits...")
    gdf_t[['p_norm', 'a_norm', 't_norm']] = gdf_t.apply(apply_surgical_patches, axis=1)

    enriched_t = gdf_t.merge(
        spine_t,
        left_on=['p_norm', 'a_norm', 't_norm'],
        right_on=['province_name_th_norm', 'district_name_th_norm', 'subdistrict_name_th_norm'],
        how='left'
    )

    # --- Part 1B: Bangkok geometry replacement (BMA OpenData) ---
    # Goal: ensure DDPM stats→geometry coverage for Bangkok by using BMA's admin boundaries.
    # Strategy:
    # - DOPA Bangkok rows already removed from gdf_t above
    # - Append BMA subdistrict geometries (enriched by code using the sealed spine)
    if bma_admin_bnd_path.exists():
        print(f"Loading BMA admin boundary layer for Bangkok override: {bma_admin_bnd_path}")
        gdf_bma = gpd.read_file(bma_admin_bnd_path)
        if gdf_bma.crs is None or gdf_bma.crs.to_epsg() != 4326:
            gdf_bma = gdf_bma.to_crs(epsg=4326)

        # BMA code column discovered by audit script: SUBDISTRIC (6-digit khwaeng code)
        if 'SUBDISTRIC' not in gdf_bma.columns:
            raise KeyError(f"BMA layer is missing expected code column 'SUBDISTRIC'. Columns: {list(gdf_bma.columns)}")

        gdf_bma['subdistrict_code'] = (
            gdf_bma['SUBDISTRIC']
            .astype(str)
            .str.extract(r'(\d+)')[0]
            .fillna('')
            .str.strip()
            .str[-6:]
        )
        gdf_bma = gdf_bma.loc[gdf_bma['subdistrict_code'].str.fullmatch(r'10\d{4}', na=False)].copy()
        print(f"BMA Bangkok subdistrict rows (post code filter): {len(gdf_bma)}")

        # Ensure polygon geometry type matches tambon layer expectations
        gdf_bma = gdf_bma.loc[gdf_bma.geometry.notna()].copy()
        gdf_bma = gdf_bma.loc[~gdf_bma.geometry.is_empty].copy()

        # Join BMA to spine by code (authoritative names from spine; no name fallback)
        bma_enriched = gdf_bma.merge(
            spine_t[['subdistrict_code', 'province_code', 'province_name_th', 'district_name_th', 'subdistrict_name_th']],
            left_on='subdistrict_code',
            right_on='subdistrict_code',
            how='left'
        )
        print(f"BMA rows after spine code-join: {len(bma_enriched)}")

        # Report any BMA codes not found in spine (should not happen if spine is sealed)
        bma_not_in_spine = bma_enriched[bma_enriched['province_code'].isna()].copy()
        if not bma_not_in_spine.empty:
            audit_file = project_tmp / "bma_boundary_codes_missing_in_spine.csv"
            bma_not_in_spine[['subdistrict_code']].drop_duplicates().to_csv(audit_file, index=False, encoding='utf-8-sig')
            print(f"WARNING: {len(bma_not_in_spine)} BMA boundary rows missing in spine. Logged to {audit_file}")

        # NOTE: `spine_t` is derived from village-level rows, so `province_code` may be NaN.
        # Use `province_name_th` as the integrity check for Bangkok for this join step.
        if 'province_name_th' in bma_enriched.columns:
            bma_missing_name = bma_enriched[bma_enriched['province_name_th'].isna()].copy()
            if not bma_missing_name.empty:
                audit_file = project_tmp / "bma_boundary_codes_missing_in_spine_names.csv"
                bma_missing_name[['subdistrict_code']].drop_duplicates().to_csv(audit_file, index=False, encoding='utf-8-sig')
                print(f"WARNING: {len(bma_missing_name)} BMA boundary rows missing province/district/subdistrict names in spine. Logged to {audit_file}")

        # Align output schema with enriched_t (use the same final code columns)
        bma_enriched = bma_enriched.rename(columns={'subdistrict_code': 'subdist_cd', 'province_code': 'prov_code'})

        # Ensure join key fields are strings without '.0' artifacts downstream
        # NOTE: use r'(\d+)' (digit capture). Using r'(\\d+)' would literally match a backslash + 'd'
        # and would return NaNs for normal numeric codes, which then cascades into join/coverage failures.
        bma_enriched['subdist_cd'] = bma_enriched['subdist_cd'].astype(str).str.extract(r'(\d+)')[0].fillna('').str[-6:]
        bma_enriched['prov_code'] = bma_enriched['prov_code'].astype(str).str.extract(r'(\d+)')[0].fillna('').str[-2:].str.zfill(2)

        # Construct rows matching enriched_t schema
        for col in enriched_t.columns:
            if col not in bma_enriched.columns:
                bma_enriched[col] = pd.NA

        # Populate the key columns used later
        bma_enriched['subdistrict_code'] = bma_enriched['subdist_cd']
        bma_enriched['province_code'] = bma_enriched['prov_code']

        # Keep only the columns that will be written
        bma_enriched = bma_enriched[enriched_t.columns]

        # Append BMA rows (Bangkok-only)
        enriched_t = pd.concat([enriched_t, bma_enriched], ignore_index=True)
        print(f"Appended {len(bma_enriched)} Bangkok subdistrict geometries from BMA admin boundary layer.")
    else:
        print(f"WARNING: BMA admin boundary override not found at {bma_admin_bnd_path}. Skipping Bangkok geometry override.")
    
    # Forensic Audit: Capture join failures
    unmatched = enriched_t[enriched_t['subdistrict_code'].isna()]
    if not unmatched.empty:
        audit_file = project_tmp / "silver_boundary_join_failures.csv"
        unmatched[['P_NAME_T', 'A_NAME_T', 'T_NAME_T']].to_csv(audit_file, index=False, encoding='utf-8-sig')
        print(f"WARNING: {len(unmatched)} join failures remain. Logged to {audit_file}")
    else:
        print("SUCCESS: 100% boundary join coverage achieved.")

    enriched_t = enriched_t.rename(columns={'subdistrict_code': 'subdist_cd', 'province_code': 'prov_code'})

    # Ensure the key code columns are clean, digit-only strings (avoid 'xxxxxx.0' artifacts)
    for _c in ['subdist_cd', 'prov_code']:
        if _c in enriched_t.columns:
            enriched_t[_c] = (
                enriched_t[_c]
                .astype(str)
                # NOTE: use r'(\d+)' (digit capture). Using r'(\\d+)' would literally match a backslash + 'd'.
                .str.extract(r'(\d+)')[0]
                .fillna('')
                .str.strip()
            )
    if 'subdist_cd' in enriched_t.columns:
        enriched_t['subdist_cd'] = enriched_t['subdist_cd'].str[-6:]
    if 'prov_code' in enriched_t.columns:
        enriched_t['prov_code'] = enriched_t['prov_code'].str[-2:].str.zfill(2)
    
    cols_t = [c for c in enriched_t.columns if not c.endswith('_norm') and c not in ['province_name_th', 'district_name_th', 'subdistrict_name_th']]
    try:
        enriched_t[cols_t].to_file(out_tambon, driver='ESRI Shapefile', encoding='utf-8')
        print(f"Saved: {out_tambon}")
    except PermissionError as e:
        # Windows often locks shapefiles if they are open in QGIS/ArcGIS/Explorer preview.
        # Fall back to a safe alternate filename so the run can complete.
        alt_out_tambon = out_tambon.with_name(out_tambon.stem + "_new" + out_tambon.suffix)
        enriched_t[cols_t].to_file(alt_out_tambon, driver='ESRI Shapefile', encoding='utf-8')
        print(f"WARNING: Could not overwrite locked file: {out_tambon}")
        print(f"Saved (fallback): {alt_out_tambon}")

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
