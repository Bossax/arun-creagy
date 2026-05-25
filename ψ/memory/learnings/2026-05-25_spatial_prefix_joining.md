# Learning: Prefer Administrative Code Prefixes for Spatial Joins

**Date**: 2026-05-25
**Category**: Data Engineering / Spatial Analysis
**Context**: Fixing missing Bangkok and Central Region plots in the CRI Impact Dashboard.

## The Pattern
When joining tabular impact data to spatial geometries (Shapefiles/GeoJSON), avoid filtering or joining based on province/district names. Thai administrative datasets frequently have corrupted, missing, or inconsistent naming conventions (e.g., Bangkok might be "กรุงเทพมหานคร", "กทม", or even "<NA>").

### Robust Alternative
Use the standardized DOPA administrative code prefixes:
1.  **Province Level**: Use the first 2 digits (e.g., `10` for Bangkok).
2.  **District Level**: Use the first 4 digits.
3.  **Subdistrict Level**: Use the full 6 digits.

## Implementation Example (Python/GeoPandas)
```python
# Robust Filtering: Use 2-digit province code prefix to isolate geometry
prov_sample = impact_df[impact_df['province_name_th'] == selected_prov]
if not prov_sample.empty:
    # Extract prefix from the standardized subdistrict code
    prov_prefix = prov_sample['subdistrict_code'].iloc[0][:2]
    
    # Filter SHP by prefix - bypasses missing name fields
    gdf_target = gdf_tambon[gdf_tambon['subdist_cd'].str.startswith(prov_prefix)].copy()
    
    # Left join to ensure full province boundaries are preserved
    map_data = gdf_target.merge(prov_sample, left_on='subdist_cd', right_on='subdistrict_code', how='left')
```

## Benefits
*   **Resilience**: Immune to corrupted name fields in the Shapefile.
*   **Precision**: Prevents "holes" in the map by allowing all geometries in a region to render even if some lack impact data (when using `left` join).
*   **Standardization**: Aligns with official DCCE/DOPA administrative standards.
