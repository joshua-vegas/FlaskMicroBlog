from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
# Objet représentant la base de données
db = SQLAlchemy(app)
# Objet représentant le moteur de migration
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

# On spécifie à flask, au moment de l'instanciation du projet, de lire et
# d'appliquer le fichier de configuration config.py
app.config.from_object(Config)

from webapp import routes, models
