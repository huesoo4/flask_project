from flask import Flask, render_template, request, abort
import json

app = Flask(__name__)

def load_planets():
    with open("data/planets_info.json", "r", encoding="utf-8") as file:
        return json.load(file)

if __name__ == "__main__":
    app.run(debug=True)