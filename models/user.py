from . import db
import datetime

from marshmallow import Schema, fields

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)

    def __init__(self, email, password, first_name, last_name=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.date_created = datetime.datetime.now()
        self.last_modified = datetime.datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return f'User {self.first_name} {self.last_name} successfully created'

    @staticmethod
    def get_user_rec(user_id):
        print(f'***Enter item.py::get_user_rec::user_id:{user_id}')
        return User.query.filter_by(id=user_id).first() 

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    date_created = fields.DateTime(dum_only=True)
    last_modified = fields.DateTime(dump_only=True)
    
