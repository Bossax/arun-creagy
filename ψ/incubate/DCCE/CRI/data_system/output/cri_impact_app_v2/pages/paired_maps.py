"""Province CRI and heat paired-map views."""
from __future__ import annotations

import streamlit as st

from components.layout import MapPanel, render_paired_map_row
from components.period_controls import plot_period_control
from components.table_helpers import render_rank_table
from runtime import load_metric, metric_summary, ranking_rows


def _metric_body(summary: dict[str, object]) -> str:
    return (
        f"Unit: {summary['unit_label']} | "
        f"Legend: {summary['legend_min']} to {summary['legend_max']} | "
        f"Source: {summary['source_mode']}"
    )


def _render_metric_pair(metric_key: str, title: str, default_right: str = "specific_year") -> None:
    st.markdown(f"### {title}")
    left_period = plot_period_control(f"{metric_key}_left")
    right_period = plot_period_control(f"{metric_key}_right", default_key=default_right)

    left_dataset = load_metric(metric_key, left_period)
    right_dataset = load_metric(metric_key, right_period)
    left_summary = metric_summary(left_dataset)
    right_summary = metric_summary(right_dataset)

    render_paired_map_row(
        [
            MapPanel(
                title=f"{left_summary['metric_label']} · {left_summary['period_label']}",
                body=_metric_body(left_summary),
            ),
            MapPanel(
                title=f"{right_summary['metric_label']} · {right_summary['period_label']}",
                body=_metric_body(right_summary),
            ),
        ]
    )

    left_table, right_table = st.columns(2, gap="large")
    with left_table:
        st.caption("Top 10 provinces")
        render_rank_table(ranking_rows(left_dataset, "top_10"))
    with right_table:
        st.caption("Bottom 10 provinces")
        render_rank_table(ranking_rows(right_dataset, "bottom_10"))


def render() -> None:
    st.subheader("Province CRI & heat views")
    st.caption("Each paired section is wired to the Stage 1 export and switches periods per plot.")
    _render_metric_pair("cri_score", "Province CRI score")
    _render_metric_pair("heat_deaths", "Province heat deaths")
    _render_metric_pair("heat_injured", "Province heat injuries")

