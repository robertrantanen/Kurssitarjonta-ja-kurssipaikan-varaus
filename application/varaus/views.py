from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.varaus.models import Varaus
from application.kurssit.models import Kurssi
from application.auth.models import User

@app.route("/varaukset", methods=["GET"])
@login_required()
def varaus_index():
    if current_user.admin == False:
        return render_template("varaus/list.html", kurssit = Varaus.loyda_kayttajan_kurssit())
    else:
        return render_template("varaus/varaukset.html", varaukset = Varaus.loyda_kaikki_varaukset())


@app.route("/varaukset/delete/<kurssi_id>/", methods=["POST"])
@login_required(role="NORMAL")
def varaus_delete(kurssi_id):
    v = Varaus.query.filter_by(account_id=current_user.id, kurssi_id=kurssi_id).first()

    db.session().delete(v)
    db.session().commit()
  
    return redirect(url_for("varaus_index"))

@app.route("/varaukset/delete/<account_id><kurssi_id>/", methods=["POST"])
@login_required(role="ADMIN")
def varaus_delete2(account_id, kurssi_id):
    v = Varaus.query.filter_by(account_id=account_id, kurssi_id=kurssi_id).first()

    db.session().delete(v)
    db.session().commit()
  
    return redirect(url_for("varaus_index"))

@app.route("/varaukset/<kurssi_id>/", methods=["POST"])
@login_required(role="NORMAL")
def varaus_maksa(kurssi_id):
    v = Varaus.query.filter_by(account_id=current_user.id, kurssi_id=kurssi_id).first()

    v.maksettu = "Kyllä"
    db.session().commit()
  
    return redirect(url_for("varaus_index"))

