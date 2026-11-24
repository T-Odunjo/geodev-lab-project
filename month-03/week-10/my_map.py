import geopandas as gpd
import matplotlib.pyplot as plt

NB_Buildings = gpd.read_file("data_folder/processed/NB_Buildings.gpkg", layer="NB_Buildings")
Population = gpd.read_file("data_folder/processed/Population.gpkg", layer="Population")

fig, ax = plt.subplots(figsize=(7, 8))
NB_Buildings.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
Population.plot(
    ax=ax, 
    column="Population",
    cmap="Greens",
    markersize=18,
    legend=True,
    legend_kwds={"label": "Population Density", "shrink": 0.6}
)

ax.set_title("Population Distribution in New Bussa")
ax.set_axis_off()

fig.savefig("month-3/week-10/Population_map.png", dpi=150, bbox_inches="tight")
print("Map saved")