from flask import Flask, render_template, request, abort
import json

app = Flask(__name__)

def load_planets():
    with open("data/planets_info.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
@app.route("/")
def index():
    planets = load_planets()
    return render_template("index.html", planets=planets)

@app.route("/planets")
def planets():
    all_planets = load_planets()
    planets = all_planets.copy()


if __name__ == "__main__":
    app.run(debug=True)