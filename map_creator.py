def volcano_map_creator():
    """
    Create a file map.html with a world map and some volcanoes
    """
    import folium
    import pandas

    df = pandas.read_csv('Volcanoes.csv')
    volc_names = df['NAME']
    volc_heights = df["ELEV"]
    volc_lats = df['LAT']
    volc_lons = df["LON"]

    volc_map = folium.Map([41, -120], zoom_start=3)
    fg = folium.FeatureGroup('Volcanoes')

    html = """
    <h4>{name}</h4>
    <p>Height: {height}m.</p>
    """

    for name, ht, lat, lon in zip(volc_names, volc_heights, volc_lats, volc_lons):
        iframe = folium.IFrame(html=html.format(name=name, height=ht), width=200, height=150)
        fg.add_child(folium.CircleMarker(location=[lat, lon], popup=folium.Popup(iframe),
                                         color='grey',
                                         fill_opacity=100,
                                         fill_color='red' if ht>3000 else "yellow" if ht>1000 else "green"))


    volc_map.add_child(fg)

    volc_map.save("templates/map.html")




