"""Time-period control primitives."""
from __future__ import annotations

from dataclasses import dataclass

import streamlit as st


@dataclass(frozen=True)
class PeriodOption:
    key: str
    label: str


DEFAULT_PERIODS = [
    PeriodOption("cumulative", "Cumulative"),
    PeriodOption("specific_year", "Specific year"),
]


def plot_period_toggle(plot_key: str, options: list[PeriodOption] | None = None, default_key: str = "cumulative") -> str:
    options = options or DEFAULT_PERIODS
    labels = [option.label for option in options]
    keys = [option.key for option in options]
    index = keys.index(default_key) if default_key in keys else 0
    selected = st.radio(
        f"Period for {plot_key}",
        labels,
        index=index,
        horizontal=True,
        key=f"period_toggle_{plot_key}",
    )
    return keys[labels.index(selected)]


def plot_period_control(plot_key: str, options: list[PeriodOption] | None = None, default_key: str = "cumulative") -> str:
    """Preferred per-plot control used by plot-heavy screens."""
    return plot_period_toggle(plot_key, options=options, default_key=default_key)


def tab_period_toggle(tab_key: str, options: list[PeriodOption] | None = None, default_key: str = "cumulative") -> str:
    return tab_period_fallback(tab_key, options=options, default_key=default_key)


def plot_period_caption(plot_key: str, period_label: str) -> None:
    st.caption(f"{plot_key}: {period_label}")


def tab_period_fallback(tab_key: str, options: list[PeriodOption] | None = None, default_key: str = "cumulative") -> str:
    options = options or DEFAULT_PERIODS
    labels = [option.label for option in options]
    keys = [option.key for option in options]
    index = keys.index(default_key) if default_key in keys else 0
    selected = st.selectbox(
        f"Period for {tab_key}",
        labels,
        index=index,
        key=f"period_fallback_{tab_key}",
    )
    return keys[labels.index(selected)]

