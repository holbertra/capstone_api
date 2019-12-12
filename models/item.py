##########################
#  ITEM.PY  Capstone API
##########################
from . import db
from  datetime import datetime

from marshmallow import Schema, fields

class Item(db.Model):
    __tablename__ = 'items' 

    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(50), nullable=False)         
    model_type = db.Column(db.String(50), nullable=False)         
    model_num = db.Column(db.String(25), nullable=False) 
    color = db.Column(db.String(25), nullable=False)              
    price =  db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))    #Foreign Key
    date_created = db.Column(db.DateTime)
    last_modified = db.Column(db.DateTime)

    def __init__(self, model_name, model_type, model_num, color, price, user_id, date_created, last_modified):
        self.model_name = model_name
        self.model_type = model_type
        self.model_num = model_num
        self.color = color
        self.price = price
        self.user_id = user_id
        self.date_created = date_created
        self.last_modified = last_modified 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_one_item(item_id):
        print(f'*****Enter get_one_item::item.py ')
        return Item.query.filter_by(id=item_id).first() 

    @staticmethod
    def get_items_by_user_id(user_id):
        print(f'*****get_items_by_user_id::item.py ')
        # print(len(Item.query.filter_by(user_id=user_id)))
        return Item.query.filter_by(user_id=user_id)

    @staticmethod
    def get_all_items():
        return Item.query.all()  

class ItemSchema(Schema):
    id = fields.Int(dump_only=True)  
    model_name = fields.Str(required=True)
    model_type = fields.Str(required=True)
    color = fields.Str(required=True)
    price = fields.Int(dump_only=True) 
    user_id = fields.Str(required=True)      # Foreign Key field
    date_created = fields.DateTime(dum_only=True)
    last_modified = fields.DateTime(dump_only=True)


