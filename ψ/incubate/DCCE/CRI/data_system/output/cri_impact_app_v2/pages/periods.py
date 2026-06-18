"""Period control demonstration page fragment."""
from __future__ import annotations

import streamlit as st

from components.period_controls import plot_period_control, tab_period_fallback
from runtime import load_manifest


def render() -> None:
    st.subheader("Time period controls")
    st.caption("Per-plot toggles are the default control pattern. Tab fallback remains available.")
    manifest = load_manifest()
    plot_choice = plot_period_control("primary_plot")
    tab_choice = tab_period_fallback("fallback_tab")
    st.write({"plot_period": plot_choice, "tab_period": tab_choice, "available_periods": [p.get("period_label") for p in manifest.get("periods", [])]})

