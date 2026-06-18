"""Table-only page fragment."""
from __future__ import annotations

import streamlit as st

from components.period_controls import plot_period_control
from components.table_helpers import render_rank_table
from runtime import load_metric, ranking_rows


def render() -> None:
    st.subheader("Ranked table")
    left, right = st.columns(2)
    with left:
        period = plot_period_control("table_cri")
        dataset = load_metric("cri_score", period)
        st.markdown("#### CRI score ranking")
        render_rank_table(ranking_rows(dataset, "top_10"))
    with right:
        period = plot_period_control("table_heat")
        dataset = load_metric("heat_deaths", period)
        st.markdown("#### Heat deaths ranking")
        render_rank_table(ranking_rows(dataset, "top_10"))

