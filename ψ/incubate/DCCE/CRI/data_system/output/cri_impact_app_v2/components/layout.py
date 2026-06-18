"""Layout primitives for paired maps and section shells."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import streamlit as st


@dataclass(frozen=True)
class MapPanel:
    title: str
    body: str


def section(title: str, subtitle: str | None = None) -> None:
    st.markdown(f"<div class='cri-section'><strong>{title}</strong></div>", unsafe_allow_html=True)
    if subtitle:
        st.caption(subtitle)


def paired_map_columns():
    return st.columns(2, gap="large")


def render_paired_map_row(panels: Sequence[MapPanel]) -> None:
    """Render one or more map panels in a two-column row layout."""
    if not panels:
        return

    if len(panels) == 1:
        left, right = st.columns([1, 1], gap="large")
        with left:
            render_map_panel(panels[0])
        with right:
            st.empty()
        return

    left, right = paired_map_columns()
    with left:
        render_map_panel(panels[0])
    with right:
        render_map_panel(panels[1])


def render_map_panel(panel: MapPanel) -> None:
    st.markdown(
        f"""
        <div class="cri-section">
            <div style="font-weight:700; margin-bottom:0.35rem;">{panel.title}</div>
            <div class="cri-muted">{panel.body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_map_card(title: str, body: str) -> None:
    render_map_panel(MapPanel(title=title, body=body))
