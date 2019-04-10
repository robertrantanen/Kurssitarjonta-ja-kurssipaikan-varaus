
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi",[validators.Length(min=1, max=144, message="Käyttäjänimen täytyy olla vähintään 1 merkkiä pitkä")])
    password = PasswordField("Salasana",[validators.Length(min=1, max=144, message="Salasanan täytyy olla vähintään 1 merkkiä pitkä")])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Käyttäjänimi",[validators.Length(min=1, max=144, message="Käyttäjänimen täytyy olla vähintään 1 merkkiä pitkä")])
    password = PasswordField("Salasana",[validators.Length(min=1, max=144, message="Salasanan täytyy olla vähintään 1 merkkiä pitkä"),  validators.EqualTo("confirm", message='Salasanat eivät täsmää')])
    confirm = PasswordField("Vahvista salasana")
    admin = BooleanField("Admin")
  
    class Meta:
        csrf = False

