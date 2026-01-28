from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import os

app = Flask(__name__)
API_KEY = os.getenv("YOUR_API_KEY")  # Replace with your Spoonacular API key

FAV_FILE = "favorites.json"

# Ensure favorites file exists
if not os.path.exists(FAV_FILE):
    with open(FAV_FILE, "w") as f:
        json.dump([], f)

@app.route("/", methods=["GET", "POST"])
def index():
    recipes = []
    ingredients = ""
    cuisine = ""
    if request.method == "POST":
        ingredients = request.form["ingredients"]
        cuisine = request.form.get("cuisine")
        url = f"https://api.spoonacular.com/recipes/complexSearch?query={ingredients}&number=10&apiKey={API_KEY}&addRecipeInformation=true"
        if cuisine:
            url += f"&cuisine={cuisine}"

        response = requests.get(url)
        data = response.json()
        recipes = data.get("results", [])

    # Load favorites
    with open(FAV_FILE, "r") as f:
        favorites = json.load(f)

    return render_template("index.html", recipes=recipes, favorites=favorites, ingredients=ingredients, cuisine=cuisine)

@app.route("/save_favorite", methods=["POST"])
def save_favorite():
    recipe_id = request.form["recipe_id"]
    title = request.form["title"]
    image = request.form["image"]
    link = request.form["link"]

    with open(FAV_FILE, "r") as f:
        favorites = json.load(f)

    # Avoid duplicates
    if not any(fav["id"] == recipe_id for fav in favorites):
        favorites.append({
            "id": recipe_id,
            "title": title,
            "image": image,
            "link": link
        })

    with open(FAV_FILE, "w") as f:
        json.dump(favorites, f)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

