from shapely.geometry import Polygon
from shapely.validation import explain_validity
import geopandas as gpd

NB_Buildings = gpd.read_file("data_folder/processed/NB_Buildings.gpkg", layer="NB_Buildings")
if invalid_before := (~NB_Buildings.geometry.is_valid).sum():
    print(f"Invalid geometries before fix: {invalid_before}")

if invalid_before == 0:
    print("There were no invalid geometries found in the layer.")
else:
    NB_Buildings["geometry"] = NB_Buildings.geometry.make_valid()
    invalid_after = (~NB_Buildings.geometry.is_valid).sum()
    print(f"Invalid geometries after fix: {invalid_after}")