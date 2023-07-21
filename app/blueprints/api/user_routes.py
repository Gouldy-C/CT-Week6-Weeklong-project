from . import bp as api
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models import Characters, User


@api.post('/create-character')
@jwt_required()
def create_character():
    try:
        character_name, race, character_class = request.json.get('character_name').title(),request.json.get('race').title(),request.json.get('character_class').title()
    except:
        return jsonify({'error': 'Did not recive keys needed to create character. character_name, race, character_class'}), 400
    user = get_jwt_identity()
    user = User.query.filter_by(username=user).first()
    try:
        c = Characters(character_name=character_name, race=race, character_class=character_class, user_id=user.user_id)
        c.commit()
    except:
        return jsonify({'error': 'Invalid character creation, try again'}), 400
    return jsonify({'message': 'Character created successfully',
                    'loged in as' : user.username}), 200


@api.get('/user-characters/<username>')
@jwt_required()
def get_user_characters(username):
    user = User.query.filter_by(username=username).first()
    if user:
        characters = user.characters
        return jsonify({
            'message': 'Success',
            'characters' : [{'character_id': character.character_id,
                            'character_name': character.character_name,
                            'race' : character.race,
                            'character_class': character.character_class} for character in characters]
        }),200
    return jsonify({'error' : 'Not a valid username'}),400



@api.delete('/delete-characters/<character_id>')
@jwt_required()
def delete_post(character_id):
    character = Characters.query.filter_by(character_id=character_id).first()
    if not character:
        return jsonify(message = 'Invalid character id'),401
    if character.maker.username != get_jwt_identity():
        return jsonify(message = 'You are not allowed to delete this Character'),401
    character.delete()
    return jsonify(message = 'Character deleted'),200


@api.get('/user-profile/<username>')
@jwt_required()
def user_profile(username):
    user = User.query.filter_by(username= username).first()
    if user:
        return jsonify(user = user.to_dict()),200
    return jsonify(error = 'Invalid username')

