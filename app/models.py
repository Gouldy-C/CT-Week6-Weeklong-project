from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    created_date= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    username = db.Column(db.String(75), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    characters = db.relationship('Characters', backref='maker', lazy=True)
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return str(self.user_id)
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
    
    def from_dict(self, user_dict):
        for k, v in user_dict.items():
            if k == 'email':
                setattr(self, k, v.lower())
            else:
                setattr(self, k, v)
    
    def to_dict(self):
        return {
            'username' : self.username,
            'email' : self.email,
            'characters' : [{'character_id': character.character_id,
                        'character_name': character.character_name,
                        'race' : character.race,
                        'character_class': character.character_class} for character in self.characters]
        }


class Characters(db.Model):
    
    character_id = db.Column(db.Integer, primary_key=True)
    created_date= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    character_name = db.Column(db.String(75), nullable=False)
    race = db.Column(db.String(75))
    character_class = db.Column(db.String(75))
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()