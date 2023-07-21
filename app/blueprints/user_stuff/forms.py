from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class CharacterCreation(FlaskForm):
    races = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']
    classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard', 'Artificer', 'Blood Hunter']
    character_name= StringField('Character Name', validators=[DataRequired()])
    race = SelectField('Character Race', choices=races)
    character_class = SelectField('Character Class', choices=classes)
    submit = SubmitField('Submit')


class UserSearch(FlaskForm):
    search_name = StringField('User Search', validators=[DataRequired()])
    submit = SubmitField('Search')