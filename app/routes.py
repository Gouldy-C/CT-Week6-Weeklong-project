from app import app
from flask import render_template
from app.forms import SignInForm, SignUpForm


@app.route('/')
def index():
    return render_template('index.jinja')

@app.route('/sign-up', methods=['GET','POST'])
def signup():
    form = SignUpForm()
    return render_template('signup.jinja', title='Sign Up', form=form)

@app.route('/sign-in', methods=['GET','POST'])
def signin():
    form = SignInForm()
    return render_template('signin.jinja', title='Sign In', form=form)

@app.route('/<username>')
def user_home():
    return render_template('user_homepage.jinja')