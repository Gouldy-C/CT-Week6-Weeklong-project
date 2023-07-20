from . import bp as main
from flask import render_template


@main.route('/')
def home():
    return render_template('index.jinja')