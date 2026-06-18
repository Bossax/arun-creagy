"""Heat Mortality page."""
from __future__ import annotations

import streamlit as st
import pydeck as pdk

from components.period_controls import PeriodOption, render_period_choice
from runtime import data


def render_metric_card(metric_key: str, period_key: str) -> None:
    dataset = data.load_metric(metric_key, period_key)
    summary = data.metric_summary(dataset)
    geojson = data.build_province_geojson(dataset)
    rank_rows = data.ranking_rows(dataset)

    st.markdown(f'<div class="cri-section-title">{summary["metric_label"]}</div>', unsafe_allow_html=True)
    st.caption(f"{summary['unit_label']} | {summary['period_label']}")

    # Map
    view_state = pdk.ViewState(latitude=13.7367, longitude=100.5231, zoom=5, pitch=0)
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
        "html": "<b>{province_name_th}</b><br/>Value: {display_value}",
        "style": {"backgroundColor": "steelblue", "color": "white"}
    }
    
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip, map_style="light"))

    # Colorbar
    colorbar_html = f"""
    <div style="margin-top: 10px; margin-bottom: 10px; font-family: sans-serif;">
        <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: #555; margin-bottom: 4px;">
            <span>{summary['legend_min']}</span>
            <span style="font-weight: 600;">{summary['unit_label']}</span>
            <span>{summary['legend_max']}</span>
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
    st.header("Heat-Related Mortality & Impact")
    
    period_options = [
        PeriodOption("period_2560_2567", "2560-2567 Average"),
        PeriodOption("period_2567", "2567 Only"),
    ]
    period_key = render_period_choice(control_key="heat", options=period_options, default_key="period_2560_2567")

    # Metric Selector
    metric_options = {
        "Heat-Related Deaths": "heat_deaths",
        "Heat-Related Injuries": "heat_injured",
    }
    
    selected_label = st.selectbox("Metric Selector", options=list(metric_options.keys()), key="heat_metric_selector")
    selected_metric = metric_options[selected_label]

    st.divider()

    # Single-View Dashboard
    render_metric_card(selected_metric, period_key)
