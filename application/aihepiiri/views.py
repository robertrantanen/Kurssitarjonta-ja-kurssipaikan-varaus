from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.aihepiiri.models import Aihepiiri
from application.aihepiiri.forms import AihepiiriForm
from flask_login import current_user


@app.route("/aihepiiri", methods=["GET"])
def aihepiiri_index():
    return render_template("aihepiiri/list.html", aihepiirit = Aihepiiri.loyda_aihepiirit())

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

