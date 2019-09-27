from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_babel import Babel, lazy_gettext as _l


# app = Flask(__name__)
#
# # On spécifie à flask, au moment de l'instanciation du projet, de lire et
# # d'appliquer le fichier de configuration config.py
# app.config.from_object(Config)
#
# # Objet représentant la base de données
# db = SQLAlchemy(app)
# # Objet représentant le moteur de migration
# migrate = Migrate(app, db)
#
# login = LoginManager(app)
# login.login_view = 'login'
#
# # Initialisation du module mail
# mail = Mail(app)

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')
mail = Mail()
babel = Babel()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    babel.init_app(app)
    from webapp.main import mn as mn_bp
    app.register_blueprint(mn_bp)
    from webapp.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    return app

from webapp import models
