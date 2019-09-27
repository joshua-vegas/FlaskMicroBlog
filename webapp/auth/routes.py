from flask import Flask, render_template, escape, url_for, flash, redirect
from bdd.connector import connect
from flask_login import current_user, login_user, logout_user, login_required
from webapp.auth.forms import LoginForm, CreateAccountForm, ResetPasswordRequestForm, ResetPasswordForm
from webapp.auth import bp
from webapp.models import User, Post
from webapp.email import send_password_reset_email


@bp.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    # Par défaut au chargement de la page, validate_on_submit est à false
    # du coup la condition n'est pas remplie et il n'y a pas de redirection.
    # On passera cette méthode à true en cliquant sur le bouton d'envoi du formulaire.
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Login ou mot de passe invalide')
            return redirect(url_for('auth.login'))
        login_user(user, remember = form.remember_me.data)
        return redirect(url_for('main.index'))
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).nextloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)

    return render_template('auth/login.html', title = 'Authentification', form = form)


    '''
        # La fonction flash permet de facilement envoyer un message à l'utilisateur
        # s'il a réussi à se connecter par exemple.
        flash('Login obligatoire pour {}, se_rappeler_de_moi = {}'.format(
            form.username.data, form.remember_me.data
        ))
        # Fonction redirect qui permet de rediriger l'utilisateur sur la page index
        return redirect('/index')
    '''

# référence tutoriel : https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
@bp.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = CreateAccountForm()

    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Félicitation vous avez créer un nouveau compte.')
        return redirect(url_for('auth.login'))

    return render_template(
                              'auth/register.html',
                              title = 'Création de compte',
                              form = form
                          )

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# Route pour accéder au formulaire permettatn de recréer son mot de passe en cas d'oublie
@bp.route('/reset_password_request', methods = ['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Consultez votre email pour et suiver les instructions')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html', form = form)

# Route pour créer son nouveau de passe grâce au token envoyé par mail
@bp.route('/reset_password/<token>', methods = ['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Votre mot de passe à été réinitialisé.')
        return redirect(url_for('auth.login'))
    return render_template('main/reset_password.html', form = form)

# Ecriture de print dans la console.
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next = '/'))
#     print(url_for('profile', username = 'John Doe'))
