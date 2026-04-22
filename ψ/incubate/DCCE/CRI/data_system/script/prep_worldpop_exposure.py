import pandas as pd
import geopandas as gpd
import rasterio
from rasterio.features import rasterize
from rasterstats import zonal_stats
from pathlib import Path

def main():
    base_path = Path(__file__).resolve().parent.parent
    shp_path = base_path / "data/1_silver/dopa/tambon_boundaries_enriched.shp"
    raster_path = base_path / "data/0_bronze/worldpop/tha_pop_2020_CN_100m_R2025A_v1.tif"
    out_csv = base_path / "data/1_silver/worldpop/tambon_population_count_worldpop.csv"
    out_tif = base_path / "data/1_silver/worldpop/tambon_population_count_worldpop.tif"
    
    out_csv.parent.mkdir(parents=True, exist_ok=True)

    print(f"Loading enriched boundaries from {shp_path}...")
    gdf = gpd.read_file(shp_path)
    
    # We explicitly named these in prep_dopa_boundaries
    join_key = 'subdist_cd'
    prov_key = 'prov_code'

    print(f"Calculating zonal statistics using {raster_path}...")
    stats = zonal_stats(gdf, str(raster_path), stats="sum", nodata=-999)
    gdf['pop_sum'] = [s['sum'] if s['sum'] is not None else 0 for s in stats]

    print(f"Saving tabular results to {out_csv}...")
    # Preserve both keys
    cols_to_keep = [join_key, prov_key, 'pop_sum']
    gdf[cols_to_keep].to_csv(out_csv, index=False, encoding='utf-8-sig')

    print(f"Creating rasterized population map: {out_tif}...")
    with rasterio.open(raster_path) as src:
        meta = src.meta.copy()
        meta.update(dtype=rasterio.float32, nodata=-999)
        shapes = ((geom, value) for geom, value in zip(gdf.geometry, gdf.pop_sum))
        rasterized = rasterize(
            shapes=shapes, out_shape=src.shape, transform=src.transform,
            fill=-999, all_touched=True, dtype=rasterio.float32
        )
        with rasterio.open(out_tif, 'w', **meta) as dst:
            dst.write(rasterized, 1)

    print("SUCCESS: WorldPop Exposure Prepared.")

if __name__ == "__main__":
    main()
