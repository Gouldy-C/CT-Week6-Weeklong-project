from app import app
from flask import render_template, flash, redirect, request, url_for
from app.forms import SignInForm, SignUpForm
from app.models import User, Characters

loged_user = None

@app.route('/')
def index():
    return render_template('index.jinja')

@app.route('/sign-up', methods=['GET','POST'])
def signup():
    global loged_user
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        try:
            user = User(username=username, email=email)
            user.hash_password(form.password.data)
            user.commit()
            flash(f'Account with username: {username} successfully created.', category='success')
            loged_user = user
            return redirect(url_for('user_home'))
        except:
            flash(f'Email or Username already taken, please try again', category='warning')
    return render_template('signup.jinja', title='Sign Up', form=form)

@app.route('/sign-in', methods=['GET','POST'])
def signin():
    global loged_user
    form = SignInForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(form.password.data):
            flash(f'{user.email} logged in successfully', category='success')
            loged_user = user
            return redirect(url_for('user_home'))
        else:
            flash('Incorrect login information, please try again', category='warning')
    return render_template('signin.jinja', title='Sign In', form=form)

@app.route('/user')
def user_home():
    global loged_user
    username = loged_user.username
    return render_template('user_homepage.jinja', username=username)