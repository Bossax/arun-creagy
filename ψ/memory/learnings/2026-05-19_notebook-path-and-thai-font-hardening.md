# Learning: Notebook hardening for data_system paths + Thai plot titles (Windows)

## Problem
Notebooks executed in different contexts (interactive vs `nbconvert`) can have different working directories, causing broken relative paths (e.g., expecting `data_system/data/...`). Additionally, Thai titles/labels in Matplotlib can render as garbled text or tofu (□) on Windows if font is not pinned.

## Pattern
1) **Anchor-root discovery**: in the first cell, derive a stable project root by walking upward until a known directory name exists (here: `data_system`). Avoid assuming `Path.cwd()` already equals the root.

2) **Thai rendering**: explicitly set a Thai-capable font early:
- `plt.rcParams['font.family'] = 'Tahoma'` (fallback; replace with a known installed Thai font if needed)
- `plt.rcParams['axes.unicode_minus'] = False`

## Why it matters
- Prevents “works on my machine” breakage when notebooks are run from different folders or via automation.
- Treats Thai-language output as a first-class requirement (presentation artifact), not a cosmetic afterthought.

## Implementation example
See: [`ddpm_national_province_score_2560_2567.ipynb`](ψ/incubate/DCCE/CRI/data_system/script/analysis_notebooks/ddpm_national_province_score_2560_2567.ipynb:1)

