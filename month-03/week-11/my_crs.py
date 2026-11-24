import geopandas as gpd

NB_Buildings = gpd.read_file("data_folder/processed/NB_Buildings.gpkg", layer="NB_Buildings")
print("CRS:", NB_Buildings.crs)

NB_Buildings["area_wrong"] = NB_Buildings.area
print(NB_Buildings[["Name", "area_wrong"]].head(3))

print("Suggested UTM:", NB_Buildings.estimate_utm_crs())
NB_Buildings_utm = NB_Buildings.to_crs(epsg=32631)
NB_Buildings_utm["area_km2"] = NB_Buildings_utm.area / 1_000_000
print(NB_Buildings_utm[["Name", "area_km2"]].head(3))
print("New Bussa total:", round(NB_Buildings_utm["area_km2"].sum(), 1), "km2")