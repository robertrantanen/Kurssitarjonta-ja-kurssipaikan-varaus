from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.varaus.models import Varaus
from application.kurssit.models import Kurssi
from application.auth.models import User

@app.route("/varaukset", methods=["GET"])
@login_required
def varaus_index():
    return render_template("varaus/list.html", kurssit = Varaus.loyda_kayttajan_kurssit())

@app.route("/varaukset/delete/<kurssi_id>/", methods=["POST"])
@login_required
def varaus_delete(kurssi_id):
    v = Varaus.query.filter_by(account_id=current_user.id, kurssi_id=kurssi_id)

    db.session().delete(v)
    db.session().commit()
  
    return redirect(url_for("varaus_index"))