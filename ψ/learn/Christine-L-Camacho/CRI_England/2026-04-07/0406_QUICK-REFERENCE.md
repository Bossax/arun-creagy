# CRI_England — Quick Reference

## What this project is

- A **data repository and interactive tool** for the **Community Resilience Index for England**, an adaptation of the Baseline Resilience Indicators for Communities (BRIC) framework.
- Key artefacts:
  - `indicators.csv` — values for 42 resilience indicators across 307 local authority districts.
  - `index.csv` — overall index and sub-index scores.
  - `indicator_descriptors.xlsx` — metadata for all 44 indicators (2 not in the public indicator CSV due to licensing).
  - `interactive_tool/` — static site for exploring the index.
- Methodology lives in the paper:
  - Camacho et al. (2024) *"Adapting the Baseline Resilience Indicators for Communities (BRIC) Framework for England"* (IJERPH 21(1012)).

## Where it lives locally

- ghq clone: `C:/Users/sitth/ghq/github.com/Christine-L-Camacho/CRI_England`

## How to use it — data side

1. Load `indicators.csv` and `index.csv` into R/Python/Stata.
2. Use `indicator_descriptors.xlsx` as the data dictionary:
   - Understand indicator meaning, units, and dimension mapping.
   - See which indicators are omitted from the public CSV and why.
3. Combine indicators and index scores to build custom analyses (e.g., comparisons with Thai CRI designs, scenario testing).

## How to use it — interactive tool

1. In `interactive_tool/`, relevant HTML files include:
   - `index.html` — main landing page.
   - `local_authority_view.html`, `localauthority.html` — local authority views.
   - `geographygroup.html`, `groupview.html` — grouped geography views.
   - `indicators.html` — indicator-focused view.
   - `largemap.html`, `map_embed.html` — full map and embeddable maps.
2. To view locally:
   - Serve the `interactive_tool` directory with a simple static server (e.g., `python -m http.server` from `interactive_tool/`).
   - Open `index.html` in a browser.

## Notable patterns to track for DCCE/CRI

- **Data packaging**
  - Clear separation between input indicators (`indicators.csv`), outputs (`index.csv`), and metadata (`indicator_descriptors.xlsx`).
  - This is a good template for how DCCE/CRI might publish Phase 1/Phase 2 results.

- **Index design stance**
  - Focuses on trait/asset/outcome-based indicators.
  - Produces a single composite index plus sub-indices for each local authority (ranking-friendly).

- **Spatial resolution**
  - Uses local authority districts as the analysis unit.
  - Excludes very small units (City of London, Isles of Scilly) for robustness.

## Contrast with DCCE/CRI

- CRI_England:
  - Trait/outcome indicators, composite scores, strong packaging and communication.

- DCCE/CRI:
  - Phase 1: Fiscal Relief impact index.
  - Phase 2: capacity profiles with explicit Coping/Adaptive/Transformative tiers, asset vs process structure, evidence registry, and data-richness overlay.

**Takeaway:**
- Use CRI_England as a **publishing and communication benchmark**, not as a one-to-one methodological template.

