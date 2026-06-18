"""Shell, header, and navigation primitives for the v2 app."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import streamlit as st


@dataclass(frozen=True)
class NavItem:
    key: str
    label: str


APP_TITLE = "CRI Impact Dashboard"
APP_SUBTITLE = "Climate risk impact views for Thailand"


def apply_shell_style() -> None:
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1.25rem;
            padding-bottom: 2rem;
            max-width: 96rem;
        }
        .cri-shell {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            margin-bottom: 1rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid rgba(49, 51, 63, 0.12);
        }
        .cri-shell h1 {
            font-size: 2rem;
            margin: 0;
            line-height: 1.1;
        }
        .cri-shell p {
            margin: 0;
            color: rgba(49, 51, 63, 0.72);
            font-size: 0.98rem;
        }
        .cri-section {
            background: white;
            border: 1px solid rgba(49, 51, 63, 0.10);
            border-radius: 14px;
            padding: 1rem;
        }
        .cri-muted {
            color: rgba(49, 51, 63, 0.70);
        }
        .cri-metric {
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
            padding: 0.9rem 1rem;
            border: 1px solid rgba(49, 51, 63, 0.10);
            border-radius: 12px;
            background: rgba(250, 250, 252, 0.96);
        }
        .cri-metric__label {
            font-size: 0.82rem;
            color: rgba(49, 51, 63, 0.68);
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }
        .cri-metric__value {
            font-size: 1.4rem;
            font-weight: 700;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_shell(title: str = APP_TITLE, subtitle: str = APP_SUBTITLE) -> None:
    st.markdown(
        f"""
        <div class="cri-shell">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_navigation(items: Sequence[NavItem], active_key: str) -> str:
    labels = [item.label for item in items]
    keys = [item.key for item in items]
    index = keys.index(active_key) if active_key in keys else 0
    selected = st.radio(
        "Navigation",
        labels,
        index=index,
        horizontal=True,
        label_visibility="collapsed",
    )
    return keys[labels.index(selected)]


def render_metric(label: str, value: str) -> None:
    st.markdown(
        f"""
        <div class="cri-metric">
            <div class="cri-metric__label">{label}</div>
            <div class="cri-metric__value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

