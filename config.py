import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.flaskenv'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ma_cle_secrete'

    # Création d'une variable de configuration de connecter le package sqlAlchemy
    # à notre base de données (DATABASE_URL).
    # Si il n'y a pas de bdd, il créer une bdd sqlite qui se nomme app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # password = ''
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:'+password+'@localhost/micro_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # mysql://scott:tiger@localhost/mydatabase

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = os.environ.get('ADMINS')
