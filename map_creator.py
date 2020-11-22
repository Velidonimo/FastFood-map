import pandas
import folium


def create_fg(df, name, color):
    """Create a featuregroup for restaurant"""
    rest_names = df['name']
    rest_cities = df["city"]
    rest_lats = df['latitude']
    rest_lons = df["longitude"]

    html = """
    <h4>{name}</h4>
    <p>City: {city}.</p>
    """

    fg = folium.FeatureGroup(name)
    for name, city, lat, lon in zip(rest_names, rest_cities, rest_lats, rest_lons):
        iframe = folium.IFrame(html=html.format(name=name, city=city), width=170, height=100)
        fg.add_child(folium.CircleMarker(location=[lat, lon], popup=folium.Popup(iframe),
                                         color=None,
                                         fill_opacity=100,
                                         fill_color=color))
    return fg


df = pandas.read_csv('FastFoodRestaurants.csv')
feature_groups = []

chosen = {"McDonald's": "yellow", "Wendy's": "red", "Taco Bell": "violet", "Burger King": "darkred"}


for name in chosen:
    df_concrete = df.loc[df["name"] == name]
    fg_concrete = create_fg(df_concrete, name, chosen[name])
    # enable only a pair of restaurants
    if name not in ("McDonald's", "Wendy's"): fg_concrete.show = False
    feature_groups.append(fg_concrete)

df_others = df.loc[~df["name"].isin(chosen)]
fg_others = create_fg(df_others, "Others", "grey")
fg_others.show = False
feature_groups.append(fg_others)

rest_map = folium.Map([30, -30], zoom_start=3, tiles=None)
folium.TileLayer(name="Restaurants").add_to(rest_map)


for fg in feature_groups:
    rest_map.add_child(fg)
rest_map.add_child(folium.LayerControl(collapsed=False))

rest_map.save("rest_map.html")




