from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class CharacterCreation(FlaskForm):
    character_name= StringField('Character Name', validators=[DataRequired()])
    race = StringField('Character Race')
    character_class = StringField('Character Class')
    submit = SubmitField('Submit')


class UserSearch(FlaskForm):
    search_name = StringField('User Search', validators=[DataRequired()])
    submit = SubmitField('Search')