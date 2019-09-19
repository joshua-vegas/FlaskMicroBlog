from datetime import datetime
from webapp import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Cette class User, qui hérite de db.Model, va permettre d'instancier des colonnes
# pour la bdd.
# Toutes le colonnes de la bdd sont instanciés grâce aux champs db.Column.
# On peut aussi passer des paramètres supplémentaire comme unique, index, etc.

# Par defaut Flask-SQLAlchemy formatera le nom de la table en snake case.
# ex : Class UserClient = user_client
# Pour changer ça on peut définir la méthode __table_name__ à la classe
# pour changer le manuellement le nom de la table.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    # La méthode __repr__ permet d'afficher du texte dans l'interpréteur python.
    # Pratique pour débugger.
    def __repr__(self):
        return '<Utilisateur {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(40), index = True)
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))