from webapp import db

# Cette class User, qui hérite de db.Model, va permettre d'instancier des colonnes
# pour la bdd.
# Toutes le colonnes de la bdd sont instanciés grâce aux champs db.Column.
# On peut aussi passer des paramètres supplémentaire comme unique, index, etc.
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(40), index = True, unique = True)
    email = db.Column(db.String(40), index = True, unique = True)
    password = db.Column(db.String(50))

    # La méthode __repr__ permet d'afficher du texte dans l'interpréteur python.
    # Pratique pour débugger.
    def __repr__(self):
        return '<Utilisateur {}>'.format(self.username)
