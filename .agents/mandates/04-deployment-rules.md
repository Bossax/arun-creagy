# Mandate: Standalone Cloud Deployment Guardrails

These rules govern the development and deployment pipelines for the Climate Resilience Index (CRI) dashboards.

## 1. Minimal Dependency Isolation
*   **Minimized Requirements**: Standalone cloud deployment targets (such as `ψ/outbox/cri_deploy/`) must use a minimized `requirements.txt` containing only essential runtime libraries (e.g., `streamlit`, `pandas`, `pydeck`, `numpy`, `watchdog`, `uvicorn`). Never include heavy C-dependent geospatial libraries (e.g., `geopandas`, `fiona`, `gdal`, `shapely`, `pyogrio`, `rasterio`) in the deployment directory to avoid compile-time build failures on serverless host systems.

## 2. Payload/Resolution Integrity
*   **Asset Configuration Consistency**: Exporter scripts (such as `script/tmp_stage1_export.py`) generating manifest metadata must explicitly reference downsampled, simplified spatial files (e.g., `*_simple.geojson` instead of full `.geojson`) in manifest JSON files, ensuring payload reduction optimizations are not reverted during subsequent data exports or synchronization runs.
