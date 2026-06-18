"""Lean ranking table helpers."""
from __future__ import annotations

from typing import Iterable, Mapping

import pandas as pd
import streamlit as st


def as_rank_frame(rows: Iterable[Mapping[str, object]]) -> pd.DataFrame:
    frame = pd.DataFrame(rows)
    if frame.empty:
        return pd.DataFrame(columns=["rank", "thai_name", "value"])
    frame = frame.loc[:, ~frame.columns.duplicated()].copy()
    columns = [c for c in ["rank", "thai_name", "value"] if c in frame.columns]
    return frame.loc[:, columns].copy()


def render_rank_table(rows: Iterable[Mapping[str, object]], empty_text: str = "No data") -> None:
    frame = as_rank_frame(rows)
    if frame.empty:
        st.info(empty_text)
        return
    for column in ("rank", "thai_name", "value"):
        if column not in frame.columns:
            frame[column] = "-"
    frame = frame[["rank", "thai_name", "value"]]
    frame["rank"] = frame["rank"].fillna("-")
    frame["thai_name"] = frame["thai_name"].fillna("-")
    frame["value"] = frame["value"].fillna("-")
    st.dataframe(
        frame,
        hide_index=True,
        use_container_width=True,
        column_config={
            "rank": st.column_config.TextColumn("Rank", width="small"),
            "thai_name": st.column_config.TextColumn("Thai name", width="large"),
            "value": st.column_config.TextColumn("Value", width="medium"),
        },
    )

