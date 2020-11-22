import pandas
import folium


df = pandas.read_csv('FastFoodRestaurants.csv')
rest_names = df['name']
rest_cities = df["city"]
rest_lats = df['latitude']
rest_lons = df["longitude"]

rest_map = folium.Map([30, -30], zoom_start=3)
fg = folium.FeatureGroup('Restaurants')

html = """
<h4>{name}</h4>
<p>City: {city}.</p>
"""

for name, city, lat, lon in zip(rest_names, rest_cities, rest_lats, rest_lons):
    iframe = folium.IFrame(html=html.format(name=name, city=city), width=130, height=80)
    fg.add_child(folium.CircleMarker(location=[lat, lon], popup=folium.Popup(iframe),
                                     color='grey',
                                     fill_opacity=100,
                                     fill_color='yellow' if name.lower() == "mcdonald's"
                                            else "red" if name.lower() in ("wendy's", "pizza hut", "burger king", "dairy queen")
                                            else "blue" if name.lower() == "domino's pizza"
                                            else "violet" if name.lower() == "taco bell"
                                            else "green" if name.lower() == "subway"
                                            else "grey"))


rest_map.add_child(fg)

rest_map.save("rest_map.html")




