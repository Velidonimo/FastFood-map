"""
Create a file map.html with a word map and some volcanoes
"""

import folium


map = folium.Map([40., -110], zoom_start=6)



map.save('templates/map.html')





