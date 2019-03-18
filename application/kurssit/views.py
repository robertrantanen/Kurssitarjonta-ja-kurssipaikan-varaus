from application import app, db
from flask import render_template, request
from application.kurssit.models import Kurssi

@app.route("/kurssit/new/")
def kurssit_form():
    return render_template("kurssit/new.html")

@app.route("/kurssit/", methods=["POST"])
def kurssit_create():
    k = Kurssi(request.form.get("nimi"))

    db.session().add(k)
    db.session().commit()
  
    return "hello world!"

