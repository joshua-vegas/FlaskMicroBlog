import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ma_cle_secrete'

    # Création d'une variable de configuration de connecter le package sqlAlchemy
    # à notre base de données (DATABASE_URL).
    # Si il n'y a pas de bdd, il créer une bdd sqlite qui se nomme app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
