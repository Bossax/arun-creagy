# CRI_England — Data & Usage Snippets

This repo ships **data and a front-end**, not the modelling code. There are no exported functions to call; instead, users load the CSVs into their own tools. Below are practical examples of how to work with the data and what that implies for DCCE/CRI.

## 1. Loading the data (Python example)

```python
import pandas as pd

base = r"C:/Users/sitth/ghq/github.com/Christine-L-Camacho/CRI_England"

# Raw indicators for 42 indicators
indicators = pd.read_csv(f"{base}/indicators.csv")

# Composite index and sub-index scores for 307 local authority districts
index = pd.read_csv(f"{base}/index.csv")

print(indicators.head())
print(index.head())
```

- `indicators` is the **input feature table** for the index (42 indicators).
- `index` contains the **output scores** (overall and sub-indexes).

## 2. Joining indicators and index

Assuming a shared key like `lad_code`:

```python
merged = indicators.merge(index, on="lad_code", how="inner")

cols = ["lad_name", "CRI_overall", "CRI_social", "CRI_economic"]
print(merged[cols].head())
```

This gives a single table where you can inspect how indicator values relate to overall and sub-index scores.

## 3. Understanding indicator metadata

```python
meta = pd.read_excel(f"{base}/indicator_descriptors.xlsx")
print(meta[["indicator_name", "dimension", "description"]].head())
```

- `meta` functions like a **tagging dictionary** for CRI_England.
- Dimensions map indicators to resilience components (social, economic, institutional, infrastructure, etc.).
- Most indicators are **stocks or outcomes**, not process/governance metrics.

## 4. Example: profile for a single local authority

```python
la = merged.loc[merged["lad_name"] == "Manchester"].T
print(la)
```

- Transposing produces a quick **indicator + index profile** for a district.
- Useful for local narrative: which dimensions are strong/weak, how they compare to national distribution (once you compute ranks or quantiles).

## 5. Conceptual contrast vs DCCE/CRI

- **CRI_England**:
  - Uses trait/outcome indicators, aggregated into composite and sub-indices.
  - Provides neat **data packaging** and an interactive front-end.
  - Process or governance behaviour is implicit at best.

- **DCCE/CRI**:
  - Phase 1 impact index (Fiscal Relief) + Phase 2 capacity profiles with explicit **process/governance emphasis**.
  - Tagging dictionary that distinguishes **asset vs process** indicators and attaches **data-richness/confidence** scores.
  - Evidence registry and coverage map for defensibility and audit.

**Takeaway:**
- Use CRI_England for inspiration on **how to structure public data releases and interactive tools**.
- Keep DCCE/CRI’s more demanding stance on **process, governance, and evidence traceability**.

