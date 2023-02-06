from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    team = db.relationship('Team', backref='user', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    ability = db.Column(db.String(45), nullable=False)
    base_xp = db.Column(db.Integer, nullable=False)
    front_shiny = db.Column(db.String(145), nullable=False)
    base_atk = db.Column(db.Integer, nullable=False)
    base_hp = db.Column(db.Integer, nullable=False)
    base_def = db.Column(db.Integer, nullable=False)
    team = db.relationship('Team', backref='pokemon', lazy=True)

    def __init__(self, name, ability, base_xp, front_shiny, base_atk, base_hp, base_def):
        self.name = name
        self.ability = ability
        self.base_xp = base_xp
        self.front_shiny = front_shiny
        self.base_atk = base_atk
        self.base_hp = base_hp
        self.base_def = base_def
        
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    poke_name = db.Column(db.String(45), db.ForeignKey('pokemon.name'), nullable=False, unique=True)

    def __init__(self, user_id, poke_name):
        self.user_id = user_id
        self.poke_name = poke_name
    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    def countTeam(self):
        db.session.query(self).count()
        