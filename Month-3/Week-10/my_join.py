import pandas as pd
import geopandas as gpd

NB_Buildings = gpd.read_file("data_folder/processed/NB_Buildings.gpkg", layer="NB_Buildings")
Population = pd.read_csv("data_folder/raw/WorldPop_Population.csv")

first_try = NB_Buildings.merge(Population, left_on="Building_name", right_on="NB_Buildings", how="left")
matched = first_try["Population"].notna().sum()
print("Matched on first try:", matched, "of", len(NB_Buildings))


def clean_name(name):
    return name.strip().upper().replace("-", " ")

NB_Buildings["join_key"] = NB_Buildings["Building_name"].apply(clean_name)
Population["join_key"] = Population["NB_Buildings"].apply(clean_name)

joined = NB_Buildings.merge(Population, on="join_key", how="left")
matched = joined["population_2024"].notna().sum()
print("Matched after cleaning:", matched, "of", len(NB_Buildings))
print(joined[["Building_name", "Population"]])