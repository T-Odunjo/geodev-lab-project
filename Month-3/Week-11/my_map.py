from pathlib import Path
import geopandas as gpd
import matplotlib.pyplot as plt

week_dir = Path("Month-3/Week-11")
week_dir.mkdir(parents=True, exist_ok=True)

reach = gpd.read_file(
    "data_folder/processed/NB_Buildings_Reach.gpkg",
    layer="NB_Buildings_Reach",
)

uncovered = reach[reach["distance_km"] > 0.2].copy()

base_layer = gpd.read_file(
    "data_folder/processed/NB_Buildings.gpkg",
    layer="NB_Buildings",
)

if base_layer.crs != reach.crs:
  base_layer = base_layer.to_crs(reach.crs)

fig, ax = plt.subplots(figsize=(9, 9))

base_layer.plot(
    ax=ax,
    color="#e5e7eb",
    edgecolor="#9ca3af",
    linewidth=0.4,
    label="Base Layer",
)

uncovered.plot(
    ax=ax,
    color="#d90429",
    markersize=8,
    alpha=0.9,
    label="Uncovered (> 0.2 km / 200 m)",
)

ax.set_title("New Bussa: Uncovered Buildings (> 0.2 km from Road)")
ax.set_xlabel("Easting (m, EPSG:32631)")
ax.set_ylabel("Northing (m, EPSG:32631)")
ax.legend(loc="best")
plt.tight_layout()

output_png = week_dir / "NB_Uncovered_Buildings_Map.png"
plt.savefig(output_png, dpi=300)
plt.close()

print(f"Map saved to {output_png} ({len(uncovered)} uncovered features)")