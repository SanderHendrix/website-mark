from flask import render_template, request
from website import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/product')
def product():
    gallery = []
    original, med, thumb = {}, {}, {}
    original["href"] = "http://placehold.it/1200x800"
    original["width"] = 1200
    original["height"] = 800
    original["caption"] = "Caption ware grote"
    med["href"] = "http://placehold.it/600x400"
    med["width"] = 600
    med["height"] = 400
    med["caption"] = "word dit gebruikt?"
    thumb["href"] = "http://placehold.it/300x200"
    thumb["width"] = 300
    thumb["height"] = 200
    thumb["caption"] = "thumb caption"
    thumb = med
    for _ in range(12):
        gallery.append((original, med, thumb))
    return render_template("product.html", gallery=gallery)

@app.route('/portret')
def portret():
    return render_template("portret.html")

@app.route('/les')
def les():
    return render_template("les.html")
