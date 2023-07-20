from . import bp as user_stuff
from flask_login import current_user, login_required
from flask import render_template, g, flash, redirect, url_for
from app import app
from app.blueprints.user_stuff.forms import UserSearch, CharacterCreation
from app.models import Characters


@app.before_request
def before_request():
    g.search_form = UserSearch()


@user_stuff.route('/user')
@login_required
def home():
    characters = current_user.characters
    return render_template('user_homepage.jinja', username=current_user.username, characters=characters)


@user_stuff.route('/user/character-creator', methods=['GET','POST'])
def character_creator():
    form = CharacterCreation()
    if form.validate_on_submit():
        character = Characters(user_id=current_user.user_id,
                                    character_name=form.character_name.data,
                                    race=form.race.data,
                                    character_class=form.character_class.data)
        character.commit()
        flash(f'{character.character_name.title()} was successfully created.', category='success')
        return redirect(url_for('user_stuff.home'))
    return render_template('character_maker.jinja', form=form)

