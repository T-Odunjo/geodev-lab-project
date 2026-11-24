# My GeoDev Lab Africa Project
Which locations in New Bussa, Niger State, are suitable for permanent and temporary waste disposal facilities, and how can the existing road network support access to and connectivity between these locations?
Built over twelve months with GeoDev Lab Africa, Cohort One.
See project-brief.md for the full brief.

# Month 2: Development Environment and Early Python
Week 5: Set up Python, VS Code, and the terminal. hello.py runs
Week 6: Set up the project with uv and add pandas. check.py prints the pandas version.
Week 7: analyse.py reads wards.csv, converts each area, and classifies each ward.
Week 8: inspect_data.py summarises "X" and "Population" in my WorldPop_Population data.
Week 9: summary.py refactored inspect_data.py and still produced the same outputs.
# Month 2 reflection
I now know there are cleaner ways to shape codes while still producing the desired output.
I still can't properly interpret the codes line by line
The outputs of summary.py tell me the average population per 100m by 100m square km of the study area
# Month 3: Geospatial Python and Automation 
Week 10: Geopandas. Loaded, checked, joined and mapped Population Distribution in New Bussa in code
Week 11: CRS and spatial operations. Reprojected to EPSG: 32631 and measured km2. 
- I used this UTM zone because New Bussa falls within it. My justification for using ('sjoin_nearest') is due to the absence of existing waste disposal facility data, traditional coverage gap analysiswas unfeasible. 
- The workflow was instead structured around infrastructure proximity and accessibility. NB_Building.gpkg has no invalid geometries. 
Week 12: Rasters. Computed NDVI for Ibadan North wards. 
- For my_index.py and my_zonal.py, i used the teaching data because the Earthexplorer site was under maintenance when i wanted to download the data and had to use the teaching one because of time. 
- For my_inspect.py, the worldpop file is in crs EPSG:4326 making the values in degrees even though i reprojected the file from QGIS. The width times resolution is equal to right minus left.