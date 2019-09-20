from flask import Flask, render_template, escape, url_for, flash, redirect
from webapp import app, db
from bdd.connector import connect
from flask_login import current_user, login_user, logout_user, login_required
from webapp.models import User
from webapp.forms import LoginForm, CreateAccountForm
from format_date import formater_date

@app.route('/')
@app.route('/index')

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
                              'index.html',
                              title="Page d'accueil",
                              posts = posts
                          )


@app.route('/employees')
@login_required
def employees():

    # Ici je met dans la variable result la valeur retourné par la fonction
    # connect. Donc la liste de du select
    result = connect()
    return render_template(
                              'employees.html',
                              result = result,
                              content_type = 'application/json'
                          )


# référence tutoriel : https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
@app.route('/inscription', methods = ['GET', 'POST'])
def inscription():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = CreateAccountForm()

    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Félicitation vous avez créer un nouveau compte.')
        return redirect(url_for('login'))

    return render_template(
                              'inscription.html',
                              title = 'Création de compte',
                              form = form
                          )


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    # Par défaut au chargement de la page, validate_on_submit est à false
    # du coup la condition n'est pas remplie et il n'y a pas de redirection.
    # On passera cette méthode à true en cliquant sur le bouton d'envoi du formulaire.
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Login ou mot de passe invalide')
            return redirect(url_for('login'))
        login_user(user, remember = form.remember_me.data)
        return redirect(url_for('index'))
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).nextloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title = 'Authentification', form = form)


    '''
        # La fonction flash permet de facilement envoyer un message à l'utilisateur
        # s'il a réussi à se connecter par exemple.
        flash('Login obligatoire pour {}, se_rappeler_de_moi = {}'.format(
            form.username.data, form.remember_me.data
        ))
        # Fonction redirect qui permet de rediriger l'utilisateur sur la page index
        return redirect('/index')
    '''

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

# Ecriture de print dans la console.
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next = '/'))
    print(url_for('profile', username = 'John Doe'))
