from flask import Flask, render_template, escape, url_for, flash, redirect
from webapp import db
from bdd.connector import connect
from flask_login import login_required
from webapp.models import User
from flask import current_app
from webapp.main import mn


@mn.route('/')
@mn.route('/index')

def index():
    # Return le h1 avec css instyle
    # return "<h1 style='color:red;'>Hello, World</h1>"
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
                              'main/index.html',
                              title="Page d'accueil",
                              posts = posts
                          )


@mn.route('/employees')
@login_required
def employees():

    # Ici je met dans la variable result la valeur retourné par la fonction
    # connect. Donc la liste de du select
    result = connect()
    return render_template(
                              'main/employees.html',
                              result = result,
                              content_type = 'application/json'
                          )


@mn.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

# Ecriture de print dans la console.
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next = '/'))
#     print(url_for('profile', username = 'John Doe'))
