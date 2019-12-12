from models.item import Item, ItemSchema
from datetime import datetime

item_schema = ItemSchema()

def create_item(data, new_user):   #Called from item_controller.py
    print(f'Enter create_item:new_user:{new_user}')
    new_item = Item(
        model_name=data['model_name'],
        model_type=data['model_type'],
        model_num=data['model_num'],        
        color=data['color'],
        price=data['price'],
        user_id=new_user,
        date_created=datetime.utcnow(),
        last_modified=datetime.utcnow() 
    )
    try:
        new_item.save()
        message = 'Item saved successfully'
        return message, 200
    except Exception as e:
        return str(e), 400
#    return "Created new item"    

def fetch_one_item(item_id):
    print(f'*******Enter fetch_one_item::item_service.py')
    x = Item.get_one_item(item_id)     # get_one_item() defined in item.py
    print(f'x:{x}')
    item_posts = item_schema.dump(x)
#    print(f'item_posts:{item_posts}')
    return item_posts

def fetch_items_by_user_id(user_id):
    print(f'*******Enter fetch_items_by_user_id::item_service.py')
    x = Item.get_items_by_user_id(user_id)  #get_items_by_user_id() defined in item.py
    item_posts = item_schema.dump(x, many=True)
#    print(f'item_posts: {item_posts}')
    return item_posts

def fetch_items():
    x = Item.get_all_items() # defined as static method in Class Item
    all_items = item_schema.dump(x, many=True)
    return all_items

def delete_item(item):
    print(f'*******Enter delete_item::item_service.py ')    
    x = Item.get_one_item(item)   # get_one_item() defined in item.py
    x.delete()
    return 'Item Successfully Deleted'
