"""CRI Impact App v2."""
from __future__ import annotations

import streamlit as st

from components.shell import NavItem, apply_shell_style, render_navigation, render_shell
from pages import overview, paired_maps, periods, tables, tambon


def main() -> None:
    st.set_page_config(page_title="CRI Impact Dashboard v2", page_icon="🌍", layout="wide")
    apply_shell_style()
    render_shell()

    selected = render_navigation(
        [
            NavItem("overview", "Overview"),
            NavItem("maps", "Province CRI & Heat"),
            NavItem("tambon", "Tambon Drilldown"),
            NavItem("tables", "Rankings"),
            NavItem("periods", "Period Controls"),
        ],
        active_key=st.session_state.get("cri_nav", "overview"),
    )
    st.session_state["cri_nav"] = selected

    tabs = st.tabs(["Overview", "Province CRI & Heat", "Tambon Drilldown", "Rankings", "Period Controls"])
    with tabs[0]:
        overview.render()
    with tabs[1]:
        paired_maps.render()
    with tabs[2]:
        tambon.render()
    with tabs[3]:
        tables.render()
    with tabs[4]:
        periods.render()


if __name__ == "__main__":
    main()

