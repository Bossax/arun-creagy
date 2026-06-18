"""Tambon drilldown page fragment."""
from __future__ import annotations

import pydeck as pdk
import streamlit as st

from components.period_controls import plot_period_control
from components.table_helpers import render_rank_table
from runtime import load_metric, tambon_geojson_for_province, tambon_period_key, tambon_province_options, tambon_rank_rows


TAMBON_METRICS = {
    "tambon_affected_households": "Tambon affected households",
    "tambon_deaths": "Tambon deaths",
}


def _selected_province(dataset: dict[str, object]) -> tuple[str, str]:
    options = tambon_province_options(dataset)
    labels = [item["province_name_th"] for item in options]
    selected_label = st.selectbox("Province", labels, key="tambon_selected_province")
    selected = next(item for item in options if item["province_name_th"] == selected_label)
    return selected["province_code"], selected["province_name_th"]


def _render_selected_province_map(dataset: dict[str, object], province_code: str, province_name: str) -> None:
    geojson = tambon_geojson_for_province(dataset, province_code)
    features = geojson.get("features", [])
    if not features:
        st.info("No tambon geometry available for the selected province.")
        return

    layer = pdk.Layer(
        "GeoJsonLayer",
        geojson,
        stroked=True,
        filled=True,
        pickable=True,
        get_line_color="properties.line_color",
        line_width_min_pixels=1,
        get_fill_color="properties.fill_color",
    )

    view_state = pdk.data_utils.compute_view(features)
    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={
            "html": "<b>{subdistrict_name_th}</b><br/>อำเภอ: {district_name_th}<br/>ค่า: {display_value}",
            "style": {"backgroundColor": "#0f172a", "color": "white"},
        },
        map_style=None,
    )
    st.caption(f"Selected-province drilldown renders the full tambon boundary set for {province_name} and overlays Stage 1 values onto those polygons.")
    st.pydeck_chart(deck, use_container_width=True)


def render() -> None:
    st.subheader("Tambon drilldown")
    st.caption("Nationwide and selected-province states are intentionally different. Boundary rendering is reserved for the selected-province drilldown.")

    metric_key = st.selectbox("Tambon metric", list(TAMBON_METRICS), format_func=TAMBON_METRICS.get, key="tambon_metric_key")
    period_choice = plot_period_control("tambon_view")
    period_key = tambon_period_key(period_choice)
    dataset = load_metric(metric_key, period_key)

    scope = st.radio(
        "Tambon scope",
        ["Nationwide", "Selected province"],
        horizontal=True,
        key="tambon_scope",
    )

    if scope == "Nationwide":
        st.markdown("#### Nationwide tambon ranking")
        st.caption("National mode stays lean: no province tambon polygons are drawn here, avoiding a false impression of cross-province drilldown continuity.")
        left, right = st.columns(2, gap="large")
        with left:
            st.caption("Top 10 tambons nationwide")
            render_rank_table(tambon_rank_rows(dataset, descending=True, limit=10))
        with right:
            st.caption("Bottom 10 tambons nationwide")
            render_rank_table(tambon_rank_rows(dataset, descending=False, limit=10))
        return

    province_code, province_name = _selected_province(dataset)
    st.markdown(f"#### {province_name} tambon drilldown")
    _render_selected_province_map(dataset, province_code, province_name)

    left, right = st.columns(2, gap="large")
    with left:
        st.caption(f"Highest tambon values in {province_name}")
        render_rank_table(tambon_rank_rows(dataset, province_code=province_code, descending=True, limit=10))
    with right:
        st.caption(f"Lowest tambon values in {province_name}")
        render_rank_table(tambon_rank_rows(dataset, province_code=province_code, descending=False, limit=10))
