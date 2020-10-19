"""Server for a small site on flask"""

from flask import Flask, render_template
import map_creator

app = Flask(__name__)
map_creator.volcano_map_creator()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/map")
def map_page():
    return render_template("map.html")



app.run(debug=True)

