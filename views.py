from main import app
from flask import render_template

# Rota da página principal
@app.route("/")
def homepage():
    return render_template("homepage.html")

# Rota do blog
@app.route("/blog")
def blog():
    return "Bem vindo ao blog"
