from . import bp as auth
from flask import render_template, flash, redirect, url_for
from app.blueprints.auth.forms import SignInForm, SignUpForm
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user
from app import login_manager
from datetime import timedelta


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@auth.route('/sign-up', methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('user_stuff.home'))
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        try:
            user = User(username=username, email=email.lower())
            user.hash_password(form.password.data)
            user.commit()
            flash(f'Account with username: {username} successfully created.', category='success')
            login_user(user)
            return redirect(url_for('user_stuff.home'))
        except:
            flash(f'Email or Username already taken, please try again', category='warning')
    return render_template('signup.jinja', title='Sign Up', form=form)

@auth.route('/sign-in', methods=['GET','POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('user_stuff.home'))
    form = SignInForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email.lower()).first()
        if user and user.check_password(form.password.data):
            flash(f'{user.email} logged in successfully', category='success')
            login_user(user, remember=form.remember_me.data, duration=timedelta(days=60))
            return redirect(url_for('user_stuff.home'))
        else:
            flash('Incorrect login information, please try again', category='warning')
    return render_template('signin.jinja', title='Sign In', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))