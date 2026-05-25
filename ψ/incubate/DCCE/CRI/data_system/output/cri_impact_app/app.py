import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import base64
import sys
from pathlib import Path

# --- DIRECTORY RESOLUTION ---
def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return Path(base_path) / relative_path

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="CRI Impact Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CORAL STAY DESIGN TOKENS ---
CORAL_PRIMARY = "#FF5A5F"
TEXT_PRIMARY = "#222222"
TEXT_SECONDARY = "#717171"
BORDER = "#DDDDDD"

# --- CUSTOM CSS (Hardened) ---
def inject_custom_styling():
    font_dir = get_resource_path("assets/fonts")
    font_name = "Tahoma"
    font_css = ""
    
    if font_dir.exists():
        font_files = list(font_dir.glob("*.ttf")) + list(font_dir.glob("*.otf"))
        if font_files:
            target_font = next((f for f in font_files if "KaniGa" in f.name or "Sarabun" in f.name), font_files[0])
            try:
                fm.fontManager.addfont(str(target_font))
                font_name = fm.FontProperties(fname=str(target_font)).get_name()
                with open(target_font, "rb") as f:
                    font_data = base64.b64encode(f.read()).decode()
                    font_format = "truetype" if target_font.suffix == ".ttf" else "opentype"
                    font_css = f"@font-face {{ font-family: '{font_name}'; src: url(data:font/ttf;base64,{font_data}); }}"
            except: pass

    st.markdown(
        f"""
        <style>
        {font_css}
        html, body, [class*="css"] {{ font-family: '{font_name}', sans-serif !important; color: {TEXT_PRIMARY}; }}
        .main-card {{
            background-color: white;
            padding: 12px;
            border-radius: 12px;
            border: 1px solid {BORDER};
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            margin-bottom: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    # Set global matplotlib font
    plt.rcParams['font.family'] = font_name
    return font_name

# --- HELPER FUNCTIONS ---
def _clean_code_6(series: pd.Series) -> pd.Series:
    s = series.astype(str).str.replace(r'\.0$', '', regex=True).str.strip()
    s = s.replace('nan', '')
    s = s.str.extract(r'(\d+)', expand=False).fillna('')
    s = s.str[-6:].str.zfill(6)
    s = s.where(s.str.fullmatch(r'\d{6}'), '')
    return s

# --- DATA LOADER (Optimized) ---
@st.cache_data
def load_data():
    data_dir = get_resource_path("data")
    fact_df = pd.read_csv(data_dir / "fact_ddpm_tambon_impact_climate_2560_2567.csv", encoding='utf-8')
    yearly_df = pd.read_csv(data_dir / "fact_ddpm_tambon_impact_climate_yearly_2560_2567.csv", encoding='utf-8')
    
    fact_df['subdistrict_code'] = _clean_code_6(fact_df['subdistrict_code'])
    yearly_df['subdistrict_code'] = _clean_code_6(yearly_df['subdistrict_code'])
    
    gdf_tambon = gpd.read_file(data_dir / "tambon_boundaries_enriched.shp")
    gdf_prov = gpd.read_file(data_dir / "province_boundaries_enriched.shp")
    
    gdf_tambon['geometry'] = gdf_tambon.geometry.simplify(0.005, preserve_topology=True)
    gdf_tambon['subdist_cd'] = _clean_code_6(gdf_tambon['subdist_cd'])
    
    if gdf_tambon.crs != "EPSG:4326": gdf_tambon = gdf_tambon.to_crs("EPSG:4326")
    if gdf_prov.crs != "EPSG:4326": gdf_prov = gdf_prov.to_crs("EPSG:4326")
        
    return fact_df, yearly_df, gdf_tambon, gdf_prov

# --- OFFICIAL SEMANTIC LAYER ---
METRICS_CONFIG = {
    "Affected Households": {
        "abs": "affected_households_sum",
        "pct": "pct_national_affected_households_sum",
        "label_th": "จำนวนครัวเรือนที่ได้รับผลกระทบสะสม (ครัวเรือน)",
        "short_th": "ครัวเรือนที่ได้รับผลกระทบ"
    },
    "Affected People": {
        "abs": "affected_people_sum",
        "pct": "pct_national_affected_people_sum",
        "label_th": "จำนวนประชาชนที่ได้รับผลกระทบสะสม (คน)",
        "short_th": "ประชาชนที่ได้รับผลกระทบ"
    },
    "Deaths": {
        "abs": "deaths_sum",
        "pct": "pct_national_deaths_sum",
        "label_th": "จำนวนผู้เสียชีวิตสะสม (คน)",
        "short_th": "ผู้เสียชีวิต"
    },
    "YoY Change": {
        "abs": "avg_yoy_change",
        "pct": "pct_national_avg_yoy_change",
        "label_th": "ค่าเฉลี่ยการเปลี่ยนแปลงรายปี (YoY)",
        "short_th": "การเปลี่ยนแปลง YoY"
    }
}

def main():
    font_name = inject_custom_styling()
    fact_df, yearly_df, gdf_tambon, gdf_prov = load_data()

    # --- SIDEBAR ---
    st.sidebar.title("CRI Dashboard")
    scope = st.sidebar.selectbox("Analysis Scope", ["Whole Country", "Province Focus"])
    
    dim_loc = fact_df[['subdistrict_code', 'subdistrict_name_th', 'district_name_th', 'province_name_th']].drop_duplicates()

    selected_prov = None
    if scope == "Province Focus":
        prov_list = sorted(dim_loc['province_name_th'].unique())
        selected_prov = st.sidebar.selectbox("Select Province", prov_list, index=prov_list.index("เชียงใหม่") if "เชียงใหม่" in prov_list else 0)
    
    temporal_mode = st.sidebar.radio("Time Period", ["Cumulative (2560-2567)", "Specific Year"])
    selected_year = None
    if temporal_mode == "Specific Year":
        years = sorted(yearly_df['year_be'].dropna().unique().astype(int))
        selected_year = st.sidebar.slider("Select Year (B.E.)", min(years), max(years), max(years))

    metric_key = st.sidebar.selectbox("Impact Metric", list(METRICS_CONFIG.keys()))
    val_type = st.sidebar.radio("Value Type", ["National Percentile", "Absolute Count"])

    # --- DATA PROCESSING ---
    if temporal_mode == "Specific Year":
        working_df = yearly_df[yearly_df['year_be'] == selected_year].copy()
        working_df = working_df.merge(dim_loc, on='subdistrict_code', how='left')
        config = METRICS_CONFIG[metric_key]
        if metric_key == "YoY Change":
            actual_abs_col = "yoy_delta_affected_households" if "yoy_delta_affected_households" in working_df.columns else config["abs"]
        else:
            actual_abs_col = config["abs"]
            
        if val_type == "National Percentile":
            target_col = config["pct"]
            working_df[target_col] = working_df[actual_abs_col].rank(pct=True) * 100
        else:
            target_col = actual_abs_col
    else:
        working_df = fact_df.copy()
        config = METRICS_CONFIG[metric_key]
        target_col = config["pct"] if val_type == "National Percentile" else config["abs"]

    if scope == "Province Focus":
        working_df = working_df[working_df['province_name_th'] == selected_prov]

    map_data = gdf_tambon.merge(working_df, left_on='subdist_cd', right_on='subdistrict_code', how='inner' if scope == "Province Focus" else 'left')
    map_data[target_col] = pd.to_numeric(map_data[target_col], errors='coerce').fillna(0)

    # --- VISUALIZATION ---
    display_label = METRICS_CONFIG[metric_key]["label_th"]
    if val_type == "National Percentile":
        display_label = f"เปอร์เซ็นไทล์: {METRICS_CONFIG[metric_key]['short_th']}"
        
    st.title(f"🌍 {display_label}")
    st.markdown(f"**ขอบเขต**: {scope} ({selected_prov if selected_prov else 'ประเทศไทย'}) | **ช่วงเวลา**: {temporal_mode if temporal_mode == 'Cumulative (2560-2567)' else f'พ.ศ. {selected_year}'}")

    col_m, col_t = st.columns([3, 1])

    with col_m:
        if scope == "Whole Country":
            # Matplotlib for performance with FIXED Thai encoding on colorbar
            fig, ax = plt.subplots(figsize=(10, 12))
            plot = map_data.plot(column=target_col, ax=ax, cmap='Reds', legend=False)
            gdf_prov.boundary.plot(ax=ax, color='black', linewidth=0.3, alpha=0.5)
            
            # Explicitly create colorbar to control font
            sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=map_data[target_col].min(), vmax=map_data[target_col].max()))
            sm._A = []
            cbar = fig.colorbar(sm, ax=ax, orientation='horizontal', pad=0.02, shrink=0.8)
            cbar.set_label(display_label, fontname=font_name, fontsize=12)
            for t in cbar.ax.get_xticklabels():
                t.set_fontname(font_name)
            
            ax.set_title(f"แผนที่แสดง{display_label}", fontname=font_name, fontsize=16)
            ax.set_axis_off()
            st.pyplot(fig)
        else:
            # Plotly for province interaction - Hardened Aspect Ratio and Colorbar
            fig = px.choropleth_mapbox(
                map_data, geojson=map_data.geometry, locations=map_data.index,
                color=target_col, color_continuous_scale="Reds",
                mapbox_style="carto-positron", opacity=0.7,
                center={"lat": map_data.geometry.centroid.y.mean(), "lon": map_data.geometry.centroid.x.mean()},
                zoom=7, hover_name="subdistrict_name_th",
                labels={target_col: display_label}
            )
            fig.update_layout(
                margin={"r":0,"t":40,"l":0,"b":0},
                # Aspect Ratio: Height 2x Width (approximate via pixels)
                height=1000,
                title=dict(text=f"แผนที่แสดง{display_label}", font=dict(family=font_name, size=24)),
                coloraxis_colorbar=dict(
                    title=dict(text=display_label, side="right", font=dict(family=font_name, size=14)),
                    thicknessmode="pixels", thickness=20,
                    lenmode="fraction", len=0.7,
                    yanchor="middle", y=0.5,
                    ticks="outside"
                )
            )
            st.plotly_chart(fig, use_container_width=True)

    with col_t:
        st.subheader("ลำดับสูงสุด 10 ตำบล")
        top10 = map_data.sort_values(target_col, ascending=False).head(10)
        for _, r in top10.iterrows():
            name = r.get('subdistrict_name_th', 'ไม่ระบุ')
            prov = r.get('province_name_th', '')
            val = r[target_col]
            st.markdown(f"""
                <div class="main-card">
                    <small style="color:{TEXT_SECONDARY};">{prov}</small><br/>
                    <b style="font-size:1.1em;">{name}</b><br/>
                    <span style="color:{CORAL_PRIMARY}; font-size:1.3em; font-weight:700;">{val:,.1f}</span>
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
