from todo import db , login
from flask_login import UserMixin  
from werkzeug.security import generate_password_hash , check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    missions = db.relationship('Mission', backref='author', lazy='dynamic')
     
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)



@login.user_loader
def loader(id):
    return User.query.get(int(id))
