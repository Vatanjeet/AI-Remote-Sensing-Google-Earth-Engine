// Define an area of interest (AOI)
var aoi = ee.Geometry.Point([77.2090, 28.6139]); // New Delhi

// Load Sentinel-2 Image Collection
var s2 = ee.ImageCollection("COPERNICUS/S2")
  .filterBounds(aoi)
  .filterDate("2024-01-01", "2024-03-01") // Adjust date range
  .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 10)) // Remove cloudy images
  .median(); // Take median composite

// Compute NDVI: (NIR - RED) / (NIR + RED)
var ndvi = s2.normalizedDifference(["B8", "B4"]).rename("NDVI");

// Add layers to the map
Map.centerObject(aoi, 10);
Map.addLayer(ndvi, {min: -1, max: 1, palette: ["blue", "white", "green"]}, "NDVI");
