from flask import Flask, render_template, escape, url_for
from webapp import app
from bdd.connector import connect

@app.route('/')
@app.route('/index')

def index():
    # Return le h1 avec css instyle
    # return "<h1 style='color:red;'>Hello, World</h1>"
    user = {'username' : 'Moez'}
    posts = [
        {
            'author' : {'username': 'Josh'},
            'body' : 'Pas sympa le git avec Pycharm.'
        },
        {
            'author' : {'username': 'Mélanie'},
            'body' : 'Mais non il suffit de bien le configurer.'
        }
    ]
    # Mauvaise pratique, test le retour de contenu dans le fichier routes au lieu de templates
    # return '''
    #     <!DOCTYPE html>
    #     <html lang="fr" dir="ltr">
    #         <head>
    #             <meta charset="utf-8">
    #             <title>Microblog - Page d'accueil</title>
    #         </head>
    #         <body>
    #             <h1>Bonjour, '''+ user['username'] +'''</h1>
    #         </body>
    #     </html>
    # '''

    return render_template(
                              'index.html',
                              title="Page d'accueil",
                              user = user,
                              posts = posts
                          )

@app.route('/employees')

def employees():

    # Ici je met dans la variable result la valeur retourné par la fonction
    # connect. Donc la liste de du select
    result = connect()
    return render_template(
                              'employees.html',
                              result = result,
                              content_type = 'application/json'
                          )


from webapp.forms import LoginForm
from flask import render_template, flash, redirect
from format_date import formater_date
@app.route('/login', methods = ['GET', 'POST'])

def login():
    form = LoginForm()

    # Par défaut au chargement de la page, validate_on_submit est à false
    # du coup la condition n'est pas remplie et il n'y a pas de redirection.
    # On passera cette méthode à tru en cliquant sur le bouton d'envoi du formulaire.
    if form.validate_on_submit():
        # La fonction flash permet de facilement envoyer un message à l'utilisateur
        # s'il a réussi à se connecter par exemple.
        flash('Login obligatoire pour {}, se_rappeler_de_moi = {}'.format(
            form.username.data, form.remember_me.data
        ))
        # Fonction redirect qui permet de rediriger l'utilisateur sur la page index
        return redirect('/index')

    return render_template('login.html', title = 'Authentification', form = form)


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next = '/'))
    print(url_for('profile', username = 'John Doe'))
