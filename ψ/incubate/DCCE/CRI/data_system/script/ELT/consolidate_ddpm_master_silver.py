#!/usr/bin/env python3
r"""
CRI Data System v4.3 - Step 1: Consolidate Raw Bronze DDPM Files to Silver
Ingests raw Bronze DDPM village disaster statistics (2557–2567),
applies strict parse_clean_numeric() comma sanitization, standardizes admin codes,
and outputs clean master file: `data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv`
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Path definitions
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_SYSTEM_DIR = SCRIPT_DIR.parents[1]

BRONZE_DIR = DATA_SYSTEM_DIR / "data" / "0_bronze" / "ddpm"
BRONZE_EXTRACTS_DIR = DATA_SYSTEM_DIR / "data" / "0_bronze" / "2026-06-12_cri_proj_data" / "ddpm_extracts"
SILVER_DIR = DATA_SYSTEM_DIR / "data" / "1_silver" / "ddpm"
OUTPUT_SILVER_MASTER = SILVER_DIR / "master_village_disaster_stat_2557_2567.csv"

def parse_clean_numeric(series: pd.Series) -> pd.Series:
    """Strips thousand-separator commas, whitespace, and invalid characters before numeric coercion."""
    return pd.to_numeric(
        series.astype(str).str.replace(",", "", regex=False).str.strip(),
        errors="coerce"
    ).fillna(0.0)

def clean_admin_code(series: pd.Series, digits: int) -> pd.Series:
    """Formats administrative codes to clean zero-padded strings of exact length."""
    cleaned = (
        series.astype(str)
        .str.replace(r"\.0$", "", regex=True)
        .str.strip()
    )
    # Extract leading digits
    cleaned = cleaned.str.extract(r"(\d+)", expand=False).fillna("")
    return cleaned.str.zfill(digits)

def consolidate_silver_master():
    print("=" * 80)
    print("🚀 CRI Data System v4.3: Starting Step 1 - Rebuilding Silver DDPM Master Stats")
    print("   Ingesting Bronze raw files with mandatory parse_clean_numeric() comma sanitization")
    print("=" * 80)

    SILVER_DIR.mkdir(parents=True, exist_ok=True)

    # Collect all available Bronze CSV files (2557-2567)
    bronze_files = []
    for p in sorted(BRONZE_DIR.glob("*.csv")):
        m = re.search(r"(\d{4})", p.name)
        year = int(m.group(1)) if m else None
        bronze_files.append((year, p))

    # Also check extra extracts directory if present
    if BRONZE_EXTRACTS_DIR.exists():
        for p in BRONZE_EXTRACTS_DIR.glob("*.csv"):
            m = re.search(r"(\d{4})", p.name)
            year = int(m.group(1)) if m else None
            bronze_files.append((year, p))


    if not bronze_files:
        print(f"❌ Error: No raw Bronze DDPM files found in {BRONZE_DIR}")
        sys.exit(1)

    print(f"📦 Discovered {len(bronze_files)} Bronze raw CSV sources.")

    processed_dfs = []
    
    for year_hint, fpath in bronze_files:
        print(f"   Reading: {fpath.name} (Year hint: {year_hint})")
        try:
            df = pd.read_csv(fpath, encoding="utf-8-sig", low_memory=False)
        except Exception:
            df = pd.read_csv(fpath, encoding="cp874", low_memory=False)

        # Normalize column names
        df.columns = [str(c).strip() for c in df.columns]

        # Ensure year column exists
        if "ปี" not in df.columns and "year_be" not in df.columns:
            if year_hint:
                df["ปี"] = year_hint
            elif "Disaster Date" in df.columns:
                # Extract year from date string (e.g. 21/11/2024 -> 2567)
                dates = pd.to_datetime(df["Disaster Date"], dayfirst=True, errors="coerce")
                df["ปี"] = dates.dt.year + 543

        if "ปี" in df.columns:
            df["ปี"] = pd.to_numeric(df["ปี"], errors="coerce").fillna(year_hint or 2567).astype(int)

        # Mandatory Comma-String Sanitization on all Impact Columns
        numeric_cols = [
            "Affected Households", "Affected People", "Deaths", 
            "Evacuated People", "Evacuated Households", "Missing", "Injured",
            "Housing Damage", "Business Damage", "Agriculture Damage"
        ]
        
        for col in numeric_cols:
            if col in df.columns:
                df[col] = parse_clean_numeric(df[col])
            else:
                df[col] = 0.0

        # Administrative Code Formatting
        if "Subdistrict Code" in df.columns:
            df["Subdistrict Code"] = clean_admin_code(df["Subdistrict Code"], 6)
        if "Province Code" in df.columns:
            df["Province Code"] = clean_admin_code(df["Province Code"], 2)
        if "District Code" in df.columns:
            df["District Code"] = clean_admin_code(df["District Code"], 4)
        if "Village Code" in df.columns:
            df["Village Code"] = clean_admin_code(df["Village Code"], 8)

        processed_dfs.append(df)

    # Combine all historical raw frames
    master_df = pd.concat(processed_dfs, ignore_index=True)

    # Deduplicate exact line duplicates in raw Bronze extracts
    dedup_cols = ["ปี", "Subdistrict Code", "Village Code", "Disaster Date", "Disaster Type"]
    existing_dedup = [c for c in dedup_cols if c in master_df.columns]
    
    initial_rows = len(master_df)
    if existing_dedup:
        master_df = master_df.drop_duplicates(subset=existing_dedup, keep="first")
    
    print(f"✅ Master Silver DF Consolidated: {initial_rows:,} raw rows -> {len(master_df):,} cleaned rows.")
    print(f"   National 2567 Cleaned Flood Household Sum: {master_df[(master_df['ปี'] == 2567) & (master_df['Disaster Type'].astype(str).str.contains('อุทกภัย', na=False))]['Affected Households'].sum():,.0f} HH")

    # Save out to 1_SILVER
    master_df.to_csv(OUTPUT_SILVER_MASTER, index=False, encoding="utf-8-sig")
    print(f"💾 Saved rebuilt Silver master file to: {OUTPUT_SILVER_MASTER}")
    print("=" * 80)

if __name__ == "__main__":
    consolidate_silver_master()
