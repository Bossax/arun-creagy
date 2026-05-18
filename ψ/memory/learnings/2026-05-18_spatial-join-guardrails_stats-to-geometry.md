# Learning — Spatial join guardrails for DDPM disaster stats × tambon geometries (CRI)

## Pattern
When joining disaster statistics to administrative boundary geometries at tambon level:

1) **Define the integrity test as “stats → geometry coverage.”**
   - Accept that many geometries will have *no recorded disasters* in a window.
   - Treat as failure only when a tambon appears in stats but has no geometry.

2) **Use code-only join keys; never use name fallback.**
   - Name matching (Thai spellings, tone marks, renames, district shifts) introduces silent misassignment risk.

3) **Normalize and validate the join key before aggregation.**
   - Convert source “Subdistrict Code” to strict 6-digit DOPA tambon code.
   - Filter/validate province prefix (e.g., Chiang Rai = `57xxxx`).
   - Report counts of dropped invalid-code rows.

4) **For YoY mapping, normalize and enforce non-computability rules.**
   - Prefer percent change: `(HH_t - HH_{t-1}) / HH_{t-1}`.
   - Set YoY to NaN when baseline is missing or 0.

## Why it matters
These guardrails prevent two high-impact failure modes:
- False failures (misclassifying “no disasters recorded” as a mismatch)
- False correctness (silent wrong matches caused by fallback-by-name or dirty codes)

