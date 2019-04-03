from application import app, db
from flask import redirect, render_template, request, url_for
from application.kurssit.models import Kurssi
from application.kurssit.forms import KurssiForm
from flask_login import login_required

@app.route("/kurssit", methods=["GET"])
def kurssit_index():
    return render_template("kurssit/list.html", kurssit = Kurssi.query.all())

@app.route("/kurssit/new/")
@login_required
def kurssit_form():
    return render_template("kurssit/new.html", form = KurssiForm())

@app.route("/kurssit/<kurssi_id>/", methods=["POST"])
@login_required
def kurssit_set_varattu(kurssi_id):

    k = Kurssi.query.get(kurssi_id)
    k.varattu = True
    db.session().commit()
  
    return redirect(url_for("kurssit_index"))    

@app.route("/kurssit/", methods=["POST"])
@login_required
def kurssit_create():
    form = KurssiForm(request.form)
    k = Kurssi(request.form.get("nimi"))
    k.aika = form.aika.data
    k.paikka = form.paikka.data
    k.maksimikoko = form.maksimikoko.data

    db.session().add(k)
    db.session().commit()
  
    return redirect(url_for("kurssit_index"))

@app.route("/kurssit/delete/<kurssi_id>/", methods=["POST"])
@login_required
def kurssit_delete(kurssi_id):
    k = Kurssi.query.get(kurssi_id)

    if k:
        db.session().delete(k)
        db.session().commit()
  
    return redirect(url_for("kurssit_index"))
