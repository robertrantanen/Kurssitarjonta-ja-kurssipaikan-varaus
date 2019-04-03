
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi",[validators.Length(min=1, message="Käyttäjänimen pitää olla vähintään 1 merkkiä pitkä")])
    password = PasswordField("Salasana",[validators.Length(min=1, message="Salasanan pitää olla vähintään 1 merkkiä pitkä")])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Käyttäjänimi",[validators.Length(min=1, message="Käyttäjänimen pitää olla vähintään 1 merkkiä pitkä")])
    password = PasswordField("Salasana",[validators.Length(min=1, message="Salasanan pitää olla vähintään 1 merkkiä pitkä"),  validators.EqualTo("confirm", message='Salasanat eivät täsmää')])
    confirm = PasswordField("Vahvista salasana")
  
    class Meta:
        csrf = False

