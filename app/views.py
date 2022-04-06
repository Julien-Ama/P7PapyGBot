from flask import Flask, request, render_template

from app import app
from app import Parser
from app import GeoWrapper
from app import WikiWrapper

# Pour lancer l'app : export FLASK_APP=hello + flask run
@app.route('/')
@app.route('/accueil')
def hello_world():
    return render_template("index.html", title="p7 PapyGBot")

@app.route("/question", methods=['GET', 'POST'])
def question():
    if request.method == 'GET':
        return "Désolé, cette route n'est pas faite pour être GET."
    elif request.method == 'POST':
        question = request.form["question"]

        parser = Parser(question)
        myGeoWrapper = GeoWrapper(parser.question)
        myWikiWrapper = WikiWrapper(myGeoWrapper.latitude, myGeoWrapper.longitude)
        return {
            "basicQuestion" : question,
            "parsedContent": parser.question,
            "geocode" : {
                "latitude" : myGeoWrapper.latitude,
                "longitude" : myGeoWrapper.longitude
            },
            "wikipedia" : myWikiWrapper.content
        }
    else:
        return "Cette méthode n'est pas autorisée"
