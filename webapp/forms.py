from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , BooleanField , SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(' Utilisateur', validators = [DataRequired()])
    password = PasswordField('Mot de passe', validators = [DataRequired()])
    remember_me = BooleanField('Se rappeler de moi')
    submit = SubmitField('Me connecter')
