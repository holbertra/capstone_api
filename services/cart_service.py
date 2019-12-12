from models.cart import Cart, CartSchema
from datetime import datetime

cart_schema = CartSchema()

def create_cart(item, user):
    new_cart = Cart(
        user_id=item['user_id'],
        item_id=item['id'],
        date_created=datetime.utcnow(),
        last_modified=datetime.utcnow()     
    )
    try:
        new_cart.save()
        message = 'Cart saved successfully'
        return message, 200    
    except Exception as e:
        return str(e), 400

    return 'Cart created and items added'    # Test code - remove later

def fetch_one_cart(user_id):
    print(f'*******Enter fetch_one_cart::cart_service.py')
    x = Cart.get_one_cart(user_id)     # get_one_cart() defined in cart.py
    cart_list = cart_schema.dump(x)
    return cart_list


def remove_cart(user_id):
    print(f'*******Enter delete_cart::cart_service.py ')    
    x = Cart.get_one_cart(user_id)   # get_one_cart() defined in cart.py
    x.delete()
    return 'Cart Successfully Deleted'
