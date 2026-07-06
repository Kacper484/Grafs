# Paris Metro Network Analysis 🚇🗼

## 📖 Overview
This project performs a comprehensive structural analysis of the Paris Metro network. The research translates spatial station data and line connections into a graph model to understand network topology, centrality, and connectivity patterns. 

## 🚀 Key Objectives
* **Data Integration:** Cleaning and merging station metadata (GPS coordinates, traffic volume) with liaison connectivity data.
* **Graph Modeling:** Building a `MultiDiGraph` representation where nodes are stations and edges represent metro lines.
* **Network Analysis:** Identifying key transit hubs based on traffic volume and centrality measures.
* **Spatial Visualization:** Leveraging the `folium` library to map the metro network onto real-world geographical coordinates (WGS84) using local projection transformations.

## 🛠️ Tech Stack
* **Language:** Python 3 (Google Colab)
* **Graph Engine:** `NetworkX` (MultiDiGraph implementation)
* **Geospatial Processing:** `folium`, `pyproj` (EPSG:2154 to WGS84 projection)
* **Data Analysis:** `pandas`, `NumPy`
* **Visualization:** `matplotlib`

## 📊 Key Findings & Visualizations
* **Network Topology:** The visualization reveals the dense connectivity of central Paris versus the hub-and-spoke configuration of the outskirts.
* **Traffic Intensity:** Used `CircleMarker` radius and color-coding to highlight high-traffic transit nodes, effectively pinpointing systemic stress points.
* **Geographic Mapping:** The `paris_metro_map_Kaszuba.html` provides an interactive layer where each line is color-coded, and nodes are interactively discoverable.

## 📂 Source Material
* Data provided for the laboratory exercise: `stations.csv`, `liaisons.csv`.