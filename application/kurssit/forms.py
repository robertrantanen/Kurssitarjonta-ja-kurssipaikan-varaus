from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class TaskForm(FlaskForm):
    nimi = StringField("Kurssin nimi")
    aika = StringField("Kurssin ajankohta")
    paikka = StringField("Kurssin paikka")
    maksimikoko = IntegerField("Osallistujien maksimimäärä")
 
    class Meta:
        csrf = False