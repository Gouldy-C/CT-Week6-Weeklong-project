from flask import request, jsonify
from flask_jwt_extended import create_access_token, unset_jwt_cookies, jwt_required, get_jwt
import re

from app.models import User
from . import bp as api


@api.post('/sign-up')
def sign_up():
    pass_pat = re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
    content, response = request.json, {}
    if User.query.filter_by(email=content['email'].lower()).first():
        response['email error'] = f'{content["email"]} email is already taken. Try again.'
        
    if User.query.filter_by(username=content['username']).first():
        response['username error'] = f'{content["username"]} username is already taken. Try again.'
        
    if 'password' not in content or not bool(re.fullmatch(pass_pat, content['password'])):
        response['password error'] = 'Password must contain at least one of each of the following and be at least 8 characters long. A-Z, a-z, 0-9, #?!@$%^&*-'
    if response:
        return jsonify(response),400
    
    user = User()
    user.from_dict(content)
    
    try:
        user.hash_password(user.password)
        user.commit()
        return jsonify({'Success': f'{user.username} is signed up.'}),200
    except:
        return jsonify({'creation error': 'The user could not be created'}),400


@api.post('/sign-in')
def sign_in():
    email, password = request.json.get('email').lower(), request.json.get('password')
    user = User.query.filter_by(email=email).first()
    
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.username)
        return jsonify({'access_token': access_token}),200
    else:
        return jsonify({'message': 'Invalid email or password. Try again.'}),400


@api.post('/logout')
@jwt_required()
def logout():
    response = jsonify({ 'message' : 'Successfully logged out.'})
    unset_jwt_cookies(response)
    return response