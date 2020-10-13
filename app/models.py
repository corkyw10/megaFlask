from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Association table, an auxiliary table that is not holding any data except
# foriegn keys and therefore doesn't need a model class
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def follow(self, user):
        # Allows a user to follow another user
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        # Allows a user to unfollow another user
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        # Checks if user is already following another user
        # The result of this query will be either 1 or 0
        return self.followed.filter(
            followers.c.followed_id == user.id
        ).count() > 0

    def __repr__(self):
        return '<User {}>'.format(self.username)

    #todo
    #add avatar to registration process
    def avatar(self):
        avatar = "avatars/{}.jpeg".format(self.username)
        return avatar


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

