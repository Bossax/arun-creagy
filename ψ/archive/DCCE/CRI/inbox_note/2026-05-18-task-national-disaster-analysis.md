# Task: National Disaster Statistics Analysis & Visualization
**Date**: 2026-05-18
**Project**: DCCE Climate Resilience Index (CRI)
**Status**: Pending

## Context
Following the successful prototype for Chiang Rai using DDPM disaster statistics, we are scaling this analysis to the entire country. This provides the empirical "Impact" layer for the CRI.

## Action Items
1. **National Scaling**: Apply the visualization logic and analysis code from the Chiang Rai notebook to all 77 provinces.
2. **Tambon-Level Analysis**: Perform the data analysis for every tambon in the country once shapefiles are cleaned.
3. **Web App Storage**: Design the data storage schema (e.g., Parquet or optimized JSON) to support fast visualization in a web application.
4. **Provincial Export**: Implement an export feature to generate province-specific Excel/CSV workbooks with Thai area names.

## Goal
Create a national disaster impact baseline to support CRI's resilience assessments.

## Lessons learned from the Chiang Rai prototype (what must be true to scale nationally)

1) **Integrity test direction matters (stats → geometry, not geometry → stats).**
   - A province’s boundary layer will often contain tambons with **no recorded disasters** in the analysis window.
   - That is not a mismatch.
   - The only mismatch that matters is: **a tambon appears in disaster statistics but has no matching geometry**.

2) **Name-based fallback creates “false correctness”.**
   - Joining by Thai names (ตำบล/อำเภอ) is brittle (spelling, tone marks, renames, district shifts).
   - A fallback-by-name can silently attach the wrong stats to the wrong tambon.
   - Scaling nationally amplifies that risk.

3) **Subdistrict Code hygiene is non-negotiable.**
   - Disaster-stat files can contain invalid or malformed `Subdistrict Code` values (blank/NaN/short codes).
   - These must be filtered/normalized before any join; otherwise you get “phantom missing geometries” (e.g., `match_id=123`).

4) **Fail fast with explicit diagnostics, then fix upstream.**
   - When a stats tambon can’t find geometry, the pipeline must stop and produce a short diagnostic table.
   - The fix should be: correct code cleaning / source mapping — not “patch by name”.

## Guardrails (mandatory rules for national scaling)

### A) Join keys and matching
- **Primary join key is a 6-digit DOPA tambon code only** (e.g., `570101`).
- **No name fallback** (no join by `T_NAME_T`, `Subdistrict`, etc.).
- **Normalize codes** from the disaster stats into a strict 6-digit string before aggregating.
  - Province filter must match the first 2 digits (e.g., Chiang Rai = `57xxxx`).

### B) Integrity checks (must run before any map/export)
- **Stats → geometry coverage** check is required for each province:
  - build the set of tambon codes present in stats (after cleaning)
  - verify every one exists in the province geometry layer
  - if not, **stop** and output diagnostics (top 50 rows is fine)

### C) Treatment of “no disaster recorded”
- When building the mapping table (geometry-left join), missing stats values are allowed and must be filled as **0** for visualization.
- Do not treat “no record” as a join failure.

### D) Auditable handling of invalid codes
- Any row dropped due to invalid code must be counted and reported (warning-level) per province.
- Keep a per-province “dropped-invalid-code rows” count in outputs (either console log or a small QA CSV).

### E) Export contract (for every province)
- Exports must be Excel-friendly Thai encoding (`utf-8-sig`).
- Minimum outputs per province:
  - aggregated tambon stats table
  - joined flat table (no geometry)
  - missing-geometry diagnostics table (should be empty when clean)
  - **map metric CSVs** (one per mapped metric) for: Affected Households, Affected People, Deaths, Avg YoY Change

### F) Reproducibility expectation
- The run must be deterministic: same inputs → same outputs.
- Any exceptions (e.g., province-specific anomalies) must be recorded as explicit QA outputs, not hidden in ad-hoc code edits.
