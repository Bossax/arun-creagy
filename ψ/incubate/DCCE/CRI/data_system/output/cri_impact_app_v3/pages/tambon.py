"""Tambon-Level Human Impact page."""
from __future__ import annotations

import streamlit as st
import pydeck as pdk

from components.period_controls import PeriodOption, render_period_choice
from runtime import data


def render_tambon_map(metric_key: str, period_key: str, province_code: str) -> None:
    dataset = data.load_metric(metric_key, period_key)
    summary = data.metric_summary(dataset)
    geojson = data.tambon_geojson_for_province(dataset, province_code)
    rank_rows = data.tambon_rank_rows(dataset, province_code)
    
    # Calculate Local Maximum for the selected province
    local_max = 0.0
    for row in rank_rows:
        try:
            val = float(row.get("value", 0))
            if val > local_max:
                local_max = val
        except (ValueError, TypeError):
            pass
            
    # Format local max to match display style (e.g. integer if it's absolute)
    display_max = f"{local_max:,.1f}" if local_max % 1 != 0 else f"{int(local_max):,}"
    if local_max == 0:
         display_max = "0"

    st.markdown(f'<div class="cri-section-title">{summary["metric_label"]}</div>', unsafe_allow_html=True)
    st.caption(f"{summary['unit_label']} | {summary['period_label']}")

    # Map - we want to auto-center on the geojson if possible, but view_state is static here.
    # A better way would be to compute bounds, but let's stay simple.
    view_state = pdk.ViewState(latitude=13.7367, longitude=100.5231, zoom=7, pitch=0)
    layer = pdk.Layer(
        "GeoJsonLayer",
        geojson,
        pickable=True,
        opacity=1.0,
        stroked=True,
        filled=True,
        get_fill_color="properties.fill_color",
        get_line_color="properties.line_color",
        line_width_min_pixels=1,
        material=False,
    )
    
    tooltip = {
        "html": "<b>{subdistrict_name_th}</b><br/>{district_name_th}, {province_name_th}<br/>Value: {display_value}",
        "style": {"backgroundColor": "steelblue", "color": "white"}
    }
    
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip, map_style="light"))

    # Colorbar (Using local_max instead of summary['legend_max'])
    colorbar_html = f"""
    <div style="margin-top: 10px; margin-bottom: 10px; font-family: sans-serif;">
        <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: #555; margin-bottom: 4px;">
            <span>0</span>
            <span style="font-weight: 600;">{summary['unit_label']}</span>
            <span>{display_max}</span>
        </div>
        <div style="height: 12px; width: 100%; background: linear-gradient(to right, rgba(255,255,255,1.0), rgba(200,0,0,1.0)); border-radius: 6px; border: 1px solid #ddd;"></div>
    </div>
    """
    st.markdown(colorbar_html, unsafe_allow_html=True)

    # Ranking Table
    st.divider()
    st.markdown("**Ranking Table**")
    st.table(rank_rows)


def render() -> None:
    st.header("Tambon-Level Human Impact")
    
    period_options = [
        PeriodOption("period_2560_2567", "2560-2567 Average"),
        PeriodOption("period_2567", "2567 Only"),
    ]
    period_key = render_period_choice(control_key="tambon", options=period_options, default_key="period_2560_2567")

    # Metric Selector
    metric_options = {
        "Tambon Deaths": "tambon_deaths",
        "Tambon Affected Households": "tambon_affected_households",
    }
    
    selected_metric_label = st.selectbox("Metric Selector", options=list(metric_options.keys()), key="tambon_metric_selector")
    selected_metric = metric_options[selected_metric_label]

    # Get province options from one of the datasets
    base_dataset = data.load_metric(selected_metric, period_key)
    province_options = data.tambon_province_options(base_dataset)
    
    selected_province = st.selectbox(
        "Select Province to Zoom",
        options=province_options,
        format_func=lambda x: x["province_name_th"],
        key="tambon_province_selector"
    )

    if not selected_province:
        st.info("Please select a province to view tambon-level data.")
        return

    province_code = selected_province["province_code"]

    st.divider()

    # Single-View Dashboard
    render_tambon_map(selected_metric, period_key, province_code)
