import geopandas as gpd

NB_Buildings = gpd.read_file("data_folder/processed/NB_Buildings.gpkg", layer="NB_Buildings").to_crs(epsg=32631)
Population = gpd.read_file(
    "data_folder/processed/Population.gpkg", layer="Population"
).to_crs(epsg=32631)

# buffer
reach = Population.copy()
reach["geometry"] = Population.buffer(2000)
print("Buffered", len(reach), "population")

# count facilities per ward
joined = gpd.sjoin(
    Population, NB_Buildings[["osm_id", "geometry"]], how="inner", predicate="within"
)
counts = joined.groupby("osm_id").size().rename("population_count").reset_index()
NB_Buildings = NB_Buildings.merge(counts, on="osm_id", how="left")
NB_Buildings["population_count"] = NB_Buildings["population_count"].fillna(0).astype(int)
print(NB_Buildings[["osm_id", "population_count"]])
print("Total counted:", NB_Buildings["population_count"].sum(), "of", len(Population))