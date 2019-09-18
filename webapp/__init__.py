from flask import Flask
from config import Config

app = Flask(__name__)

# On spécifie à flask, au moment de l'instanciation du projet, de lire et
# d'appliquer le fichier de configuration config.py
app.config.from_object(Config)

from webapp import routes
