from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

class Pitch(db.model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))

def __repr__(self):
        return f'User {self.username}'
