import geopandas as gpd

print(gpd.list_layers("data_folder/processed/NB_Buildings.gpkg"))

NB_Buildings = gpd.read_file("data_folder/processed/NB_Buildings.gpkg", layer="NB_Buildings")

print(NB_Buildings.head())
print("Rows and columns:", NB_Buildings.shape)
print(NB_Buildings.geom_type.value_counts())
print("CRS:", NB_Buildings.crs)
print("Bounds:", NB_Buildings.total_bounds)