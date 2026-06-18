---
title: Slimming down runtime requirements by removing heavy geospatial libraries (e.g.,
tags: [deployment, streamlit, dependency-management, performance]
created: 2026-06-18
source: Oracle Learn
project: github.com/dcce/cri
---

# Slimming down runtime requirements by removing heavy geospatial libraries (e.g.,

Slimming down runtime requirements by removing heavy geospatial libraries (e.g., geopandas, fiona) in Streamlit Cloud environments is a critical optimization when data processing is shifted to a pre-deployment Stage 1 (JSON export). This avoids GDAL compilation errors and significantly reduces container cold-start times.

---
*Added via Oracle Learn*
