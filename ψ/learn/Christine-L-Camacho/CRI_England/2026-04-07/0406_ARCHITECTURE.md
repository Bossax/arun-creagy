# CRI_England — Architecture Notes

Source inspected via ghq clone at:
`C:/Users/sitth/ghq/github.com/Christine-L-Camacho/CRI_England`

## 1. Top-level structure

From `ls` and `README.md`:

- Data + metadata files at repo root:
  - `indicators.csv` — raw data for **42** of the indicators used in the Community Resilience Index.
    - Two additional indicators are excluded from this public repo because they are under license (retail vacancies from the Consumer Data Research Centre, and assets of community value from Plunkett UK).
  - `index.csv` — **index and sub-index results** for **307 local authority districts** in England.
    - City of London and Isles of Scilly are excluded due to very small populations.
  - `indicator_descriptors.xlsx` (README refers to `indicator_description.xlsx`) — metadata for all **44 indicators**.
    - Descriptions, units, and notes; highlighted rows mark indicators that are not present in `indicators.csv`.
  - `README.md` — documentation and citation.

- Interactive visualization / web front-end under `interactive_tool/`:
  - `_file/`, `_import/`, `_npm/`, `_observablehq/` — ObservableHQ/JavaScript build artifacts and dependency bundles.
  - `dist/` — compiled JS/CSS assets for the interactive site.
  - `images/` — static image assets.
  - HTML entrypoints:
    - `index.html` — main landing page.
    - `local_authority_view.html`, `localauthority.html` — local authority views.
    - `geographygroup.html`, `groupview.html` — grouped geography views.
    - `indicators.html` — indicator-focused view.
    - `largemap.html`, `map_embed.html` — map visualizations and embeddable maps.
  - `Readme.md` — documentation for the interactive tool.

## 2. Implied data architecture

The repo does **not** ship the computational pipeline; it ships the **data outputs** and the **presentation layer**. The structure is:

- **Indicator layer (`indicators.csv`)**
  - Each row: a local authority district.
  - Columns: values for ~42 indicators.
  - Indicators are largely **asset/trait/outcome-based** measures of community conditions (consistent with BRIC).

- **Index layer (`index.csv`)**
  - Each row: a local authority district (307 units).
  - Columns: overall Community Resilience Index plus sub-index scores (dimensions inherited from BRIC, e.g., social, economic, institutional, infrastructure, community capital).
  - This is the **post-aggregation output** for mapping and comparison.

- **Metadata layer (`indicator_descriptors.xlsx`)**
  - Defines the indicator catalog: names, definitions, sources, notes.
  - Encodes the conceptual mapping between raw variables and resilience dimensions.

- **Presentation layer (`interactive_tool/`)**
  - Consumes `index.csv` and possibly indicator metadata to drive an interactive UI:
    - Map views of overall and sub-index scores.
    - Local authority views with indicator breakdowns.
    - Group/geography views and indicator-focused exploration.
  - Implemented via HTML + JS bundles built from ObservableHQ notebooks.

This is a classic **data package + front-end** pattern: the modelling code is described in the paper, not exposed here.

## 3. Entry points and typical usage

Two main entry points are implied:

1. **Data analysis entrypoint**
   - Users load `indicators.csv` and `index.csv` into R/Python/Stata/etc. to:
     - Reproduce descriptive statistics and plots.
     - Perform secondary analyses (e.g., regressions, clustering, comparisons with other indices).
   - `indicator_descriptors.xlsx` acts as the data dictionary.

2. **Interactive visualization entrypoint**
   - Users host or open `interactive_tool/index.html` (e.g., via a static server) to:
     - Explore resilience scores on a map.
     - Drill down to local authorities.
     - Inspect underlying indicator profiles.

The computational pipeline (normalization, weighting, aggregation) is in the **paper**, not in this repository.

## 4. Conceptual alignment vs DCCE/CRI

- CRI_England:
  - Composite, **trait/outcome-based** resilience index for local authorities.
  - Clear separation between indicator table, index results, and metadata.
  - Visual front-end for exploration and communication.

- DCCE/CRI (design intent):
  - Phase 1: **impact index** (Fiscal Relief) rather than a general resilience index.
  - Phase 2: **capacity profiles** with explicit **Coping / Adaptive / Transformative** tiers.
  - Indicators structured as **asset vs process**, with data-richness/confidence overlay and explicit evidence registry.

**Implication for us:**
- Reuse CRI_England’s **data packaging and publication pattern** (input table, output table, descriptor sheet, interactive tool).
- Do **not** copy its trait-only indicator mix; instead maintain our process/governance emphasis via the CRI tagging dictionary and evidence spine.

