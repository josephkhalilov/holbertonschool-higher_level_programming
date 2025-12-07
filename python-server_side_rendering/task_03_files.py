from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

# ---------- JSON oxuma funksiyası ----------
def read_json():
    file_path = os.path.join(os.path.dirname(__file__), "products.json")
    with open(file_path, "r") as file:
        return json.load(file)

# ---------- CSV oxuma funksiyası ----------
def read_csv():
    file_path = os.path.join(os.path.dirname(__file__), "products.csv")
    products = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # CSV-də hər şey stringdir → id və price-ı çevirmək lazımdır
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })

    return products

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # ---------- Mənbə düzgün deyil ---------
    if source not in ["json", "csv"]:
        return render_template("product_display.html", error="Wrong source", products=None)

    # ---------- Mənbəyə görə oxu ----------
    if source == "json":
        data = read_json()
    else:
        data = read_csv()

    # ---------- Əgər id verilmişdirsə filter et ----------
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in data if p["id"] == product_id]

            if not filtered:
                return render_template("product_display.html", error="Product not found", products=None)

            return render_template("product_display.html", products=filtered, error=None)

        except ValueError:
            return render_template("product_display.html", error="Invalid ID format", products=None)

    # ---------- id verilməyibsə bütün məhsulları göstər ----------
    return render_template("product_display.html", products=data, error=None)

if __name__ == "__main__":
    app.run(debug=True)
