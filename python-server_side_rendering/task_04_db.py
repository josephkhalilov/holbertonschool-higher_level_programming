from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# ---------- JSON oxu ----------
def read_json():
    file_path = os.path.join(os.path.dirname(__file__), "products.json")
    with open(file_path, "r") as file:
        return json.load(file)

# ---------- CSV oxu ----------
def read_csv():
    file_path = os.path.join(os.path.dirname(__file__), "products.csv")
    products = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

# ---------- SQLite oxu ----------
def read_sql():
    db_path = os.path.join(os.path.dirname(__file__), "products.db")
    products = []

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        rows = cursor.execute("SELECT id, name, category, price FROM Products").fetchall()

        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": float(row[3])
            })

        conn.close()
        return products

    except Exception:
        return None  # error vəziyyətində None qaytarırıq


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # ---------- Mənbə düzgün deyil ----------
    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html", error="Wrong source", products=None)

    # ---------- Düzgün mənbəyə əsasən oxu ----------
    if source == "json":
        data = read_json()

    elif source == "csv":
        data = read_csv()

    elif source == "sql":
        data = read_sql()
        if data is None:
            return render_template("product_display.html", error="Database error", products=None)

    # ---------- ID ilə filter ----------
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in data if p["id"] == product_id]

            if not filtered:
                return render_template("product_display.html", error="Product not found", products=None)

            return render_template("product_display.html", products=filtered, error=None)

        except ValueError:
            return render_template("product_display.html", error="Invalid ID format", products=None)

    # ---------- Bütün məhsulları göstər ----------
    return render_template("product_display.html", products=data, error=None)


if __name__ == "__main__":
    app.run(debug=True)
