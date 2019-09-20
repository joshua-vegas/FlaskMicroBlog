from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , BooleanField , SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from webapp.models import User

class LoginForm(FlaskForm):
    username = StringField(' Utilisateur', validators = [DataRequired()])
    password = PasswordField('Mot de passe', validators = [DataRequired()])
    remember_me = BooleanField('Se rappeler de moi')
    submit = SubmitField('Me connecter')

class CreateAccountForm(FlaskForm):
    username = StringField(' Utilisateur', validators = [DataRequired()])
    email = StringField(' Courriel', validators = [DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators = [DataRequired()])
    password2 = PasswordField(
                                 'Mot de passe',
                                 validators = [DataRequired(), EqualTo('password')]
                             )
    submit = SubmitField('Créer mon compte')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError('Username déjà utilisé, veuillez en choisir un nouveau.')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError('Email déjà utilisé, veuillez en choisir un nouveau.')
