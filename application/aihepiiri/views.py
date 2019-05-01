from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.aihepiiri.models import Aihepiiri
from application.aihepiiri.forms import AihepiiriForm
from application.kurssit.models import Kurssi
from flask_login import current_user


@app.route("/aihepiiri", methods=["GET"])
def aihepiiri_index():
    return render_template("aihepiiri/list.html", aihepiirit = Aihepiiri.loyda_aihepiirit())

@app.route("/aihepiiri/<aihepiiri_id>/", methods=["GET"])
def aihepiirin_kurssit(aihepiiri_id):
    return render_template("kurssit/list.html", kurssit = Kurssi.loyda_aihepiirin_kurssit(aihepiiri_id))

@app.route("/aihepiiri/new/")
@login_required(role="ADMIN")
def aihepiiri_form():
    return render_template("aihepiiri/new.html", form = AihepiiriForm())


@app.route("/aihepiiri/", methods=["POST"])
@login_required(role="ADMIN")
def aihepiiri_create():
    form = AihepiiriForm(request.form)

    if not form.validate():
        return render_template("aihepiiri/new.html", form = form)

    a = Aihepiiri(request.form.get("nimi"))

    db.session().add(a)
    db.session().commit()
  
    return redirect(url_for("aihepiiri_index"))


@app.route("/aihepiiri/muokkaa/<aihepiiri_id>/", methods=["POST"])
@login_required(role="ADMIN")
def aihepiiri_muokkaa(aihepiiri_id):
    a = Aihepiiri.query.get(aihepiiri_id)

    form = AihepiiriForm(request.form)

    if not form.validate():
        return render_template("aihepiiri/muokkaa.html", a = a, form = form)

    form.populate_obj(a)

    db.session().commit()
  
    return redirect(url_for("aihepiiri_index")) 

@app.route("/aihepiiri/delete/<aihepiiri_id>/", methods=["POST"])
@login_required(role="ADMIN")
def aihepiiri_poista(aihepiiri_id):

    a = Aihepiiri.query.get(aihepiiri_id)
    
    db.session().delete(a)
    db.session().commit()
  
    return redirect(url_for("aihepiiri_index"))

