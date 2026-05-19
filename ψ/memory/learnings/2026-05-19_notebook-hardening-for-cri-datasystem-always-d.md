---
title: Notebook hardening for CRI data_system:
tags: [jupyter, windows, matplotlib, thai, reproducibility, paths, cri, gis]
created: 2026-05-19
source: rrr: Arun_Creagy
project: github.com/sitth/arun_creagy
---

# Notebook hardening for CRI data_system:

Notebook hardening for CRI data_system:
- Always derive a stable base path by walking upward until the `data_system` directory is found, rather than assuming `Path.cwd()`.
- For Thai-language maps on Windows/Jupyter, explicitly pin a Thai-capable Matplotlib font early (e.g., `plt.rcParams['font.family'] = 'Tahoma'`) and set `plt.rcParams['axes.unicode_minus']=False`.
- When the deliverable is a map notebook, implement notebook-first (load → transform → join → plot), and only factor out scripts if asked.

Reference implementation: `ψ/incubate/DCCE/CRI/data_system/script/analysis_notebooks/ddpm_national_province_score_2560_2567.ipynb`

---
*Added via Oracle Learn*
