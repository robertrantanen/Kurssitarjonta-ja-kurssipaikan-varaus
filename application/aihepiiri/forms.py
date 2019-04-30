from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class AihepiiriForm(FlaskForm):
    nimi = StringField("Aihepiirin nimi", [validators.Length(min=1, max=144, message="Aihepiirin nimen täytyy olla vähintään 1 merkkiä pitkä")])
 
    class Meta:
        csrf = False