##########################
#  CART.PY  Capstone API
##########################
from . import db
from  datetime import datetime

from marshmallow import Schema, fields

class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))    #Foreign Key
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))    #Foreign Key
    date_created = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)

    def __init__(self, user_id, item_id, date_created, last_modified):
        self.user_id = user_id
        self.item_id = item_id
        self.date_created = date_created
        self.last_modified = last_modified 

    @staticmethod
    def get_one_cart(user_id):
        print(f'*****Enter get_one_cart::cart.py user_id:{user_id}')
        return Cart.query.filter_by(user_id=user_id).first() 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class CartSchema(Schema):
    id = fields.Int(dump_only=True)  
    user_id = fields.Str(required=True)      # Foreign Key field
    item_id = fields.Str(required=True)      # Foreign Key field  
    date_created = fields.DateTime(dum_only=True)
    last_modified = fields.DateTime(dump_only=True)     

