from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from . import login_manager

ROLE_USER = 0
ROLE_ADMIN = 1

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first() 
    def __repr__(self):
        return '<User %r>' % (self.username)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self, perssion):
        return self.role is not None and (self.role.permissions & perssions) == perssions
    
    def is_administrator(self):
        return self.can(Perssion.ADMINISTER)

class AnonymousUser(AnonymousUserMixin):
    def can(self, perssion):
        return False
    
    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'
    id          = db.Column(db.Integer, primary_key = True)
    name        = db.Column(db.String(64), unique = True)
    default     = db.Column(db.Boolean, default = False, index = True)
    permissions = db.Column(db.Integer)
    users       = db.relationship('User', backref = 'role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User':(permissions.FOLLOW |
                    permissions.COMMENT |
                    permissions.WRITE_ARTICLES, True),
            'Moderator':(permissions.FOLLOW |
                         permissions.COMMENT |
                         permissions.WRITE_ARTICLES |
                         permissions.MODERATE_COMMENTS, False),
            'Administrator':(0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name = r).first()
            if role is None:
                role = Role(name = r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

class permissions:
    FOLLOW            = 0X01
    COMMENT           = 0X02
    WRITE_ARTICLES    = 0X04
    MODERATE_COMMENTS = 0X08
    ADMINISTER        = 0X80

class Camera(db.Model):
    __tablename__ = 'cameras'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    address = db.Column(db.String(140))
    port = db.Column(db.Integer)

    

class VideoFile(db.Model):
    __tablename__ = 'videoFiles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    address = db.Column(db.String(140))

