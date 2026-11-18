import geopandas as gpd
import pandas as pd

NB_Buildings = gpd.read_file("data_folder/processed/NB_Buildings.gpkg", layer="NB_Buildings")

NB_Buildings['X'] = NB_Buildings.geometry.centroid.x
NB_Buildings['Y'] = NB_Buildings.geometry.centroid.y

print(NB_Buildings[['X', 'Y']].head())

import pandas as pd
import geopandas as gpd

NB_Buildings = gpd.read_file("data_folder/processed/NB_Buildings.gpkg", layer="NB_Buildings")
worldpop_df = pd.read_csv("data_folder/raw/WorldPop_Population.csv")

first_try = NB_Buildings.merge(worldpop_df, on=["X", "Y"], how="left")
matched_first = first_try["population"].notna().sum()
print("Matched on first try (exact coordinates):", matched_first, "of", len(NB_Buildings))


def clean_name(name):
    return name.strip().upper().replace("-", " ")

wards["join_key"] = wards["ward_name"].apply(clean_name)
pop["join_key"] = pop["ward"].apply(clean_name)

joined = wards.merge(pop, on="join_key", how="left")
matched = joined["population_2024"].notna().sum()
print("Matched after cleaning:", matched, "of", len(wards))
print(joined[["ward_name", ""]])