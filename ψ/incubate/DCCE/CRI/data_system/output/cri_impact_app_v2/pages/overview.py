"""Overview tab content."""
from __future__ import annotations

import streamlit as st

from components.shell import render_metric
from runtime import available_metric_groups, available_periods, load_manifest


def render() -> None:
    st.subheader("Overview")
    manifest = load_manifest()
    cols = st.columns(4)
    with cols[0]:
        render_metric("Coverage", "National")
    with cols[1]:
        render_metric("Primary unit", "Province")
    with cols[2]:
        render_metric("Periods", str(len(available_periods())))
    with cols[3]:
        render_metric("Metric groups", str(len(available_metric_groups())))
    st.caption(f"Stage 1 export version: {manifest.get('version', 'unknown')}")

