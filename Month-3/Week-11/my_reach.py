import geopandas as gpd

NB_Buildings = gpd.read_file("data_folder/processed/NB_Buildings.gpkg", layer="NB_Buildings").to_crs(epsg=32631)
NB_Roads = gpd.read_file(
    "data_folder/processed/NB_Roads.gpkg", layer="NB_Roads"
).to_crs(epsg=32631)

centres = NB_Buildings[["osm_id", "geometry"]].copy()
centres["geometry"] = NB_Buildings.centroid

nearest = gpd.sjoin_nearest(
    centres, NB_Roads[["highway", "geometry"]], how="left", distance_col="distance_m"
    )
nearest["distance_km"] = (nearest["distance_m"] / 1_000).round(2)
print(nearest[["osm_id", "highway", "distance_km"]])