import folium
import pandas

data = pandas.read_csv("../assets/data/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elv = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles= "Stamen Terrain")  

def color_change(elevation):
    if elevation <= 1000:
        return 'blue'
    elif 1000 <= elevation < 3000:
        return 'red'
    else: 
        return 'green'
fgv = folium.FeatureGroup(name = "volcanoes")

for lt, ln, el in zip(lat,lon,elv):
    fgv.add_child(folium.CircleMarker(location=[lt,ln] ,radius = 10,popup = str(el) + " m",
    fill_color =color_change(el),color = 'grey', fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "population")

fgp.add_child(folium.GeoJson(data=open('../assets/data/world.json', 'r', encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000 
else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("../output/map1.html")
