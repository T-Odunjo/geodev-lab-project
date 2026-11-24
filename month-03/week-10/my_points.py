import pandas as pd
import geopandas as gpd
table = pd.read_csv("data_folder/raw/WorldPop_Population.csv")
print(table.head(3))

Population = gpd.GeoDataFrame(
    table, 
    geometry=gpd.points_from_xy(table["X"], table["Y"]),
    crs="EPSG:4326",
)
print(Population.head(3))
print(Population.crs)

Population.to_file("data_folder/processed/Population.gpkg", layer="Population")
print("Saved", len(Population), "Population")