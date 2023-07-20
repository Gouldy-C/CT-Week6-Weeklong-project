from flask import Blueprint

bp = Blueprint('user_stuff', __name__)

from . import routes