# Engineering Design Document: CRI Impact Visualization Dashboard

**Project**: Climate Resilience Index (CRI) - DCCE  
**Release Version**: 1.2.0 (Robust Spatial Hardening)  
**Implementation Date**: May 25, 2026  
**Author**: Arun Creagy, Strategic Climate Knowledge Auditor

---

## 1. Executive Summary
The CRI Impact Dashboard is a high-integrity, standalone digital artifact that transforms official DCCE Gold Layer climate data into a stakeholder-ready interactive interface. It is engineered for "Zero-Discovery" deployment, requiring no local Python installation or internet connectivity.

## 2. System Architecture
### 2.1 Technical Stack
*   **Engine**: Python 3.12.0
*   **Frontend**: Streamlit 1.32.0+ (Web-native local server)
*   **Data Processing**: Pandas (Logic), GeoPandas (Spatial), PyArrow (IO Speed)
*   **Visualization**: Plotly 5.18.0+ (Interactive Maps), Matplotlib (Static/Thai-rendered charts)
*   **Packaging**: PyInstaller 6.4.0+ (Multi-module dependency collection)

### 2.2 Directory Structure (Source & Bundle)
```text
cri_impact_app/
├── app.py                # Main Streamlit logic (Processing + UI)
├── launcher.py           # PyInstaller Entry Point (Bootstraps server + browser)
├── bundle_windows.py     # Automated build script
├── data/                 # Immutable Assets (Gold Fact CSVs + SHP Boundaries)
│   ├── fact_ddpm_tambon_impact_climate_2560_2567.csv
│   └── tambon_boundaries_enriched.shp (+.dbf, .shx, etc.)
└── assets/fonts/         # Thai Typography (.ttf)
    └── KaniGa Bold.ttf
```

## 3. Core Implementation Logic
### 3.1 Portable Path Resolution (The _MEIPASS Pattern)
To ensure the app can find its data whether running as a script or a bundled `.exe`, we use a resource path resolver:
```python
def get_resource_path(relative_path):
    # PyInstaller creates a temporary folder and stores path in _MEIPASS
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return Path(base_path) / relative_path
```

### 3.2 Thai Font Rendering Strategy
Standard Streamlit/Matplotlib environments often fail to render Thai characters. We implement a dual-layer injection:
1.  **Streamlit UI**: We read the `.ttf` file as `base64` and inject a `@font-face` CSS block into the page.
2.  **Matplotlib Charts**: We register the font with `font_manager` and set `plt.rcParams['font.family']` globally.

### 3.3 6-Digit DOPA Code Normalization (Gold Standard)
To prevent join failures between CSV data (often read as floats) and Shapefiles (strings), we enforce a strict 6-digit normalization:
*   Strip `.0` suffixes from float-to-string conversions.
*   `zfill(6)` to ensure leading zeros are preserved.
*   Filter out `nan` or invalid codes to maintain spatial integrity.

## 4. The 7-Stage Data Processing Pipeline
To maintain structural integrity from raw signal to final visualization, the app executes the following sequence:

1.  **Environment Adaptation (Bootstrapping)**: Resolves physical paths using the `_MEIPASS` pattern to handle script-vs-bundled execution modes.
2.  **Ingestion (Multimodal Loading)**: Parallel loading of Tabular Gold Fact CSVs and Spatial Enriched Boundary Shapefiles via `@st.cache_data`.
3.  **Normalization (The 6-Digit DOPA Standard)**: Uses `_clean_code_6()` to enforce a strict 6-digit subdistrict code, stripping decimals and padding leading zeros to ensure join compatibility.
4.  **Spatial Integrity (Precision Geometry)**: Standardizes CRS to EPSG:4326. Note: As of v1.1.0, spatial simplification is disabled to preserve boundary accuracy at high zoom levels.
5.  **Semantic Mapping & Runtime Filtering**: Employs a `METRICS_CONFIG` layer to map user-facing labels to internal fact columns.
6.  **Integrity-First Join**: Performs an `inner` join (for performance) or `left` join (for robustness) on normalized codes to bind impact data to spatial polygons.
7.  **Localization & Visualization Rendering**: Dynamically switches between Matplotlib (Performance/National) and Plotly (Interaction/Province) using injected Thai fonts.

## 5. Build & Reproducibility
### 5.1 Dependency Installation
```bash
pip install streamlit pandas geopandas plotly matplotlib pyarrow pyinstaller
```

### 5.2 Packaging Workflow
We use `bundle_windows.py` which executes PyInstaller with specific "Hardening" flags:
*   `--collect-all streamlit`: Essential for bundling Streamlit's static web components.
*   `--collect-all plotly`: Ensures Mapbox templates and JS assets are included.
*   `--copy-metadata`: Preserves package identity required by some C-extensions at runtime.

### 5.3 Build Command
To reproduce the `.exe` (folder-based distribution), run:
```bash
python bundle_windows.py
```
The output will reside in `dist/CRI_Impact_Dashboard/`.

## 6. Change Log
### v1.2.0 (May 25, 2026)
*   **Bangkok & Central Region Fix**: Switched to 2-digit province code prefixes for filtering Shapefile geometries. This bypasses corrupted or missing province names (e.g., Bangkok labeled as `<NA>` in SHP) and ensures the central region renders correctly.
*   **Hole-Free Province Focus**: Refactored the join logic to use a `left` join from the filtered Shapefile to the Impact CSV. All subdistricts in a province are now rendered, with missing impact data appearing as 0/white instead of empty holes.
*   **Robust DOPA Cleaning**: Hardened the `_clean_code_6` utility to better handle string edge cases.

### v1.1.0 (May 25, 2026)
*   **Precision Hardening**: Removed `simplify(0.005)` from the spatial processing stage. Province-level focus plots now display high-fidelity subdistrict boundaries.
*   **Version Registration**: Added `APP_VERSION` global variable and integrated it into the Sidebar UI and Page Title for traceability.
*   **Pipeline Documentation**: Integrated the 7-stage data processing lifecycle into the official Design Specification.

### v1.0.0 (May 20, 2026)
*   Initial release of the standalone CRI Impact Visualization Dashboard.
*   Implemented "Zero-Discovery" path resolution for bundled deployment.
*   Added Thai font support for both Streamlit and Matplotlib.

---
*Status: FINALIZED. This document serves as the authoritative blueprint for the CRI Digital Interface.*
