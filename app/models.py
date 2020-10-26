from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):

    """
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    """
    return User.query.get(int(user_id))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')

    # securing passwords
    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(), index = True)

    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    
    def save_pitches(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Title {self.title}'

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))

    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')


    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories





