from application import app
from flask import render_template, request

@app.route("/kurssit/new/")
def kurssit_form():
    return render_template("kurssit/new.html")

@app.route("/kurssit/", methods=["POST"])
def kurssit_create():
    print(request.form.get("nimi"))
  
    return "hello world!"

