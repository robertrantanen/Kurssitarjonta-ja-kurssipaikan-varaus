from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.kurssit.models import Kurssi
from application.kurssit.forms import KurssiForm
from flask_login import current_user
from application.varaus.models import Varaus

@app.route("/kurssit", methods=["GET"])
def kurssit_index():
    return render_template("kurssit/list.html", kurssit = Kurssi.loyda_kaikki_kurssit())

@app.route("/kurssit/new/")
@login_required(role="ADMIN")
def kurssit_form():
    return render_template("kurssit/new.html", form = KurssiForm())

@app.route("/kurssit/<kurssi_id>/", methods=["POST"])
@login_required()
def kurssit_varaa_tai_muuta(kurssi_id):

    k = Kurssi.query.get(kurssi_id)

    if current_user.admin == False:
        varaukset = Varaus.loyda_onko_varaus_jo_olemassa(kurssi=kurssi_id)
        if len(varaukset) == 0:
            if k.taynna == "Ei":
                v = Varaus(account_id=current_user.id, kurssi_id=kurssi_id) 
                db.session().add(v)
                db.session().commit()
            else:
                return redirect(url_for("kurssit_index", errorMessage = "Kurssi on täynnä")) 
        else:
            return redirect(url_for("kurssit_index", errorMessage = "Olet jo varannut kurssin")) 
    
    else:
        if k.taynna == "Kyllä":
            k.taynna = "Ei"
        else:
            k.taynna = "Kyllä"
        db.session().commit()
  
    return redirect(url_for("kurssit_index", errorMessage = ""))  
  

#@app.route("/kurssit/muokkaa/<kurssi_id>/", methods=["POST"])
#@login_required
#def kurssit_muokkaa(kurssi_id):
#    form = KurssiForm(request.form)

#    if not form.validate():
#        return render_template("kurssit/list.html", form = form)

#    k = Kurssi.query.get(kurssi_id)


#    k.nimi = form.nimi.data


#    db.session().commit()
  
#    return redirect(url_for("kurssit_index")) 

@app.route("/kurssit/", methods=["POST"])
@login_required(role="ADMIN")
def kurssit_create():
    form = KurssiForm(request.form)

    if not form.validate():
        return render_template("kurssit/new.html", form = form)

    k = Kurssi(request.form.get("nimi"))
    k.aika = form.aika.data
    k.paikka = form.paikka.data
    k.maksimikoko = form.maksimikoko.data

    db.session().add(k)
    db.session().commit()
  
    return redirect(url_for("kurssit_index"))

@app.route("/kurssit/delete/<kurssi_id>/", methods=["POST"])
@login_required(role="ADMIN")
def kurssit_delete(kurssi_id):

    varaukset = Varaus.loyda_kurssin_varaukset(kurssi_id)

    for v in varaukset:
        varaus = Varaus.query.filter_by(kurssi_id=kurssi_id).first()
        db.session().delete(varaus)
        db.session().commit()

    k = Kurssi.query.get(kurssi_id)
    
    db.session().delete(k)
    db.session().commit()
  
    return redirect(url_for("kurssit_index"))


