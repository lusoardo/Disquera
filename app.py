from flask import Flask, render_template

app = Flask(__name__)

albums = [
    {"img": "unmechon.jpg", "title": "UN MECHON DE PELO"},
    {"img": "tinitini.jpg", "title": "TINI TINI TINI"},
    {"img": "tini1.jpg", "title": "TINI MARTINA STOESSEL"},
    {"img": "cupido.jpg", "title": "CUPIDO"},
    {"img": "cuartoazul.jpg", "title": "CUARTO AZUL"},
    {"img": "lanacion.jpg", "title": "LA NACION"},
    {"img": "secretus.jpg", "title": "THE SECRET OF US"},
    {"img": "showgirl.jpg", "title": "THE LIFE OF A SHOWGIRL"},
    {"img": "reputation.jpg", "title": "REPUTATION"},
    {"img": "1989.jpg", "title": "1989"},
    {"img": "balasperdidas.jpg", "title": "BALAS PERDIDAS"},
    {"img": "siayrhoy.jpg", "title": "SI AYR FUERA HOY"},
    {"img": "vida.jpg", "title": "LA VIDA ERA MAS CORTA"},
    {"img": "111.jpg", "title": "111"},
    {"img": "sour.jpg", "title": "SOUR"},
    {"img": "debifotos.jpg", "title": "DEBI TIRAR MAS FOTOS"},
    {"img": "verano.jpg", "title": "UN VERANO SIN TI"},
    {"img": "30.jpg", "title": "30"},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/discos")
def discos():
 return render_template("discos.html", albums=albums, cart_count=len(session.get("cart", [])))

@app.route("/historia")
def historia():
    return render_template("historia.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
@app.route("/agregar", methods=["POST"])
def agregar():
    album_id = int(request.form["album_id"])

    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(album_id)
    session.modified = True

    return redirect("/")

@app.route("/carrito")
def carrito():
    cart_ids = session.get("cart", [])
    items = [a for a in albums if a["id"] in cart_ids]
    return render_template("carrito.html", items=items)