import pandas
import folium


def create_fg(df, name, color):
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
                                         color='grey',
                                         fill_opacity=100,
                                         fill_color=color))
    return fg

                                         # 'yellow' if name.lower() == "mcdonald's"
                                         # else "red" if name.lower() in (
                                         # "wendy's", "pizza hut", "burger king", "dairy queen")
                                         # else "blue" if name.lower() == "domino's pizza"
                                         # else "violet" if name.lower() == Taco Bell
                                         # else "green" if name.lower() == "subway"
                                         # else "grey"))


df = pandas.read_csv('FastFoodRestaurants.csv')
feature_groups = []

df_mc = df.loc[df["name"] == "McDonald's"]
feature_groups.add(create_fg(df_mc, "McDonald's", 'yellow'))

df_w = df.loc[df["name"] == "Wendy's"]
feature_groups.add(create_fg(df_w, "Wendy's", "red"))

df_tb = df.loc[df["name"] == "Taco Bell"]
feature_groups.add(create_fg(df_tb, "Taco Bell", "violet"))

df_bk = df.loc[df["name"] == "Burger King"]
feature_groups.add(create_fg(df_bk, "Burger King", "darkred"))

chose = ("McDonald's", "Wendy's", "Taco Bell", "Burger King")
df_others = df.loc[~df["name"].isin(chose)]
feature_groups.add(create_fg(df_others, "Others", "grey"))


for fg in feature_groups:
    rest_map.add_child(fg)


rest_map.save("rest_map.html")




