# Engineering Design Document: CRI Impact Visualization Dashboard

**Project**: Climate Resilience Index (CRI) - DCCE  
**Release Version**: 1.0.0 (Hardened Standalone)  
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

### 3.4 The Bootstrap Launcher
`launcher.py` serves as the compiled entry point. It performs two concurrent tasks:
1.  **Server Start**: Invokes `streamlit.web.cli` in the background.
2.  **Browser Trigger**: Uses a `threading.Timer` to wait 3 seconds (allowing the server to warm up) before calling `webbrowser.open()`.

## 4. Build & Reproducibility
### 4.1 Dependency Installation
```bash
pip install streamlit pandas geopandas plotly matplotlib pyarrow pyinstaller
```

### 4.2 Packaging Workflow
We use `bundle_windows.py` which executes PyInstaller with specific "Hardening" flags:
*   `--collect-all streamlit`: Essential for bundling Streamlit's static web components.
*   `--collect-all plotly`: Ensures Mapbox templates and JS assets are included.
*   `--copy-metadata`: Preserves package identity required by some C-extensions at runtime.

### 4.3 Build Command
To reproduce the `.exe` (folder-based distribution), run:
```bash
python bundle_windows.py
```
The output will reside in `dist/CRI_Impact_Dashboard/`.

---
*Status: FINALIZED. This document serves as the authoritative blueprint for the CRI Digital Interface.*
