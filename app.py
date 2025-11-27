from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "clave-segura"

# ---- BASE DE DATOS DE DISCOS ----
albums = [
    {"id": 0, "img": "unmechon.jpg", "title": "UN MECHON DE PELO"},
    {"id": 1, "img": "tinitini.jpg", "title": "TINI TINI TINI"},
    {"id": 2, "img": "tini1.jpg", "title": "TINI MARTINA STOESSEL"},
    {"id": 3, "img": "cupido.jpg", "title": "CUPIDO"},
    {"id": 4, "img": "cuartoazul.jpg", "title": "CUARTO AZUL"},
    {"id": 5, "img": "lanacion.jpg", "title": "LA NACION"},
    {"id": 6, "img": "secretus.jpg", "title": "THE SECRET OF US"},
    {"id": 7, "img": "showgirl.jpg", "title": "THE LIFE OF A SHOWGIRL"},
    {"id": 8, "img": "reputation.jpg", "title": "REPUTATION"},
    {"id": 9, "img": "1989.jpg", "title": "1989"},
    {"id": 10, "img": "balasperdidas.jpg", "title": "BALAS PERDIDAS"},
    {"id": 11, "img": "siayrhoy.jpg", "title": "SI AYR FUERA HOY"},
    {"id": 12, "img": "vida.jpg", "title": "LA VIDA ERA MAS CORTA"},
    {"id": 13, "img": "111.jpg", "title": "111"},
    {"id": 14, "img": "sour.jpg", "title": "SOUR"},
    {"id": 15, "img": "debifotos.jpg", "title": "DEBI TIRAR MAS FOTOS"},
    {"id": 16, "img": "verano.jpg", "title": "UN VERANO SIN TI"},
    {"id": 17, "img": "30.jpg", "title": "30"},
]


# ---- RUTAS ----

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/discos")
def discos():
    return render_template(
        "discos.html",
        albums=albums,
        cart_count=len(session.get("cart", []))
    )

@app.route("/historia")
def historia():
    return render_template("historia.html")


# ---- AGREGAR AL CARRITO ----
@app.route("/agregar", methods=["POST"])
def agregar():
    album_id = int(request.form["album_id"])

    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(album_id)
    session.modified = True

    return redirect("/discos")


# ---- MOSTRAR CARRITO ----
@app.route("/carrito")
def carrito():
    cart_ids = session.get("cart", [])
    items = [a for a in albums if a["id"] in cart_ids]
    return render_template("carrito.html", items=items)


# ---- ELIMINAR DEL CARRITO ----
@app.route("/eliminar", methods=["POST"])
def eliminar():
    album_id = int(request.form["album_id"])

    if "cart" in session and album_id in session["cart"]:
        session["cart"].remove(album_id)
        session.modified = True

    return redirect("/carrito")


# ---- RUN ----
if __name__ == "__main__":
    app.run(debug=True)
