from flask import Flask, render_template, url_for, request, redirect
from deployment_model.seq_model import SeqModel
from utils.preprocessing_helper import *
from nltk.tokenize import word_tokenize
from wordcloud import STOPWORDS
import folium
import geopy
from geopy import Nominatim

import pickle
import os
import nltk

# from flask_bootstrap import Bootstrap
nltk.download("stopwords")
nltk.download("punkt")

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEMPLATE_DIR = os.path.abspath("templates")
STATIC_DIR = os.path.abspath("static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/resultspage", methods=["POST", "GET"])
def resultspage():
    address = request.form["search"]
    address = preprocess(address)
    
    prediction = None
    with open("./models/model3.pkl", "rb") as f:
        model = pickle.load(f)
        prediction = model.predict([[address.latitude, address.longitude]])
    
    folium_map = folium.Map(location=[address.latitude, address.longitude], zoom_start=12, tiles="Stamen Terrain")

    tooltip = "Click me!"

    folium.Marker(
        [41.92369842529297, -87.64631652832031], popup=f"Prediction here!", tooltip=tooltip
    ).add_to(folium_map)

    return folium_map._repr_html_()


def preprocess(address):
    locator = Nominatim(user_agent="myGeocoder")
    address = locator.geocode(address)
    return address


# def predicted_val(lst):
#     predicted1= clf1.predict(lst)
#     lp=list(predicted1)
#     return lp 


if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)