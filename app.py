#Autor: Rodrigo Olmos
from flask import Flask, jsonify, render_template
from requests import get

app = Flask(__name__)

#Configura rutas html
@app.route("/")
def index():
    return render_template("index.html")


#Se almacena datos de API entregada y se envian al HTML
@app.route("/seguro")
def show_seguro():

    seguro = get("https://dn8mlk7hdujby.cloudfront.net/interview/insurance/58").json()
    #return seguro["insurance"]
    return render_template("seguro.html", seguro=seguro)

if __name__ == "__main__":
    app.run(debug=True, port=4000)
