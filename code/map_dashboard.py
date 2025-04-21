'''
map_dashboard.py
'''
import streamlit as st
import streamlit_folium as sf
import folium
import pandas as pd
import geopandas as gpd
# these constants should help you get the map to look better
# you need to figure out where to use them
CUSE = (43.0481, -76.1474)  # center of map
ZOOM = 14                   # zoom level
VMIN = 1000                 # min value for color scale
VMAX = 5000                 # max value for color scale

map = pd.read_csv('/Users/jack/Downloads/IST 356/assignment-08-JackVsyr/cache/top_locations_mappable.csv')
st.title('Top Locations for Parking Tickets in Syracuse')
st.caption('This dashboard shows the tickets that were issued in the top locations with $1,000 or more in total violation amounts.')

geo = gpd.GeoDataFrame(map, geometry=gpd.points_from_xy(map.lon, map.lat))
map2 = folium.Map(location=CUSE, zoom_start=ZOOM)
syr_map = geo.explore(geo['amount'], m=map2, 
                       cmap="magma",vmin=VMIN, vmax=VMAX, 
                       legend=True, legend_name='Amount',
                       marker_type = "circle",
                       marker_kwds = {"radius": 10, "fill": True},
)
sf.folium_static(syr_map, width=800, height=600)