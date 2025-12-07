from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Home page is working!"

@app.route("/items")
def items():
    # JSON faylının yolu
    file_path = os.path.join(os.path.dirname(__file__), "items.json")

    # JSON-dan məlumatı oxu
    with open(file_path, "r") as file:
        data = json.load(file)

    items_list = data.get("items", [])

    return render_template("items.html", items=items_list)

if __name__ == "__main__":
    app.run(debug=True)
