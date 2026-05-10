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

    search = request.args.get("search", "").lower()
    planet_type = request.args.get("type", "")
    order = request.args.get("order", "asc")

    planet_types = sorted(set(planet["type"] for planet in all_planets))

    if search:
        planets = [
            planet for planet in planets
            if search in planet["name"].lower()
        ]

    if planet_type:
        planets = [
            planet for planet in planets
            if planet["type"] == planet_type
        ]

    if order == "desc":
        planets = sorted(planets, key=lambda planet: planet["name"], reverse=True)
    else:
        planets = sorted(planets, key=lambda planet: planet["name"])

    return render_template(
        "planets.html",
        planets=planets,
        search=search,
        selected_type=planet_type,
        planet_types=planet_types,
        order=order
    )

@app.route("/planet/<position>")
def planet_detail(position):
    planets = load_planets()

if __name__ == "__main__":
    app.run(debug=True)