from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, validators

class KurssiForm(FlaskForm):
    nimi = StringField("Kurssin nimi", [validators.Length(min=1, max=144, message="Kurssin nimen täytyy olla vähintään 1 merkkiä pitkä")])
    aihepiiri_id = SelectField("Aihepiiri", coerce=int)
    aika = StringField("Kurssin ajankohta", [validators.Length(min=1, max=144, message="Kurssin ajan täytyy olla vähintään 1 merkkiä pitkä")])
    paikka = StringField("Kurssin paikka", [validators.Length(min=1, max=144, message="Kurssin paikan täytyy olla vähintään 1 merkkiä pitkä")])
    maksimikoko = IntegerField("Osallistujien maksimimäärä", [validators.DataRequired(message="Osallistujien maksimimäärän täytyy olla kokonaisluku")])
 
    class Meta:
        csrf = False