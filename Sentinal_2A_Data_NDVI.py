import ee
import geemap

# Initialize GEE
ee.Initialize()

# Define an area of interest (AOI)
aoi = ee.Geometry.Point([77.2090, 28.6139])  # New Delhi

# Load Sentinel-2 Image Collection
s2 = (
    ee.ImageCollection("COPERNICUS/S2")
    .filterBounds(aoi)
    .filterDate("2024-01-01", "2024-03-01")  # Adjust date range
    .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 10))  # Remove cloudy images
    .median()  # Take median composite
)

# Compute NDVI: (NIR - RED) / (NIR + RED)
ndvi = s2.normalizedDifference(["B8", "B4"]).rename("NDVI")

# Visualize using geemap
Map = geemap.Map()
Map.centerObject(aoi, 10)
ndvi_vis = {"min": -1, "max": 1, "palette": ["blue", "white", "green"]}
Map.addLayer(ndvi, ndvi_vis, "NDVI")
Map
