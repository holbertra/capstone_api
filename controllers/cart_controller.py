from flask import Blueprint, request, Response, json, jsonify
from services.item_service import fetch_one_item
from services.user_service import fetch_user
from services.cart_service import create_cart, fetch_one_cart, remove_cart
from flask_jwt_extended import jwt_required, get_jwt_identity

cart_blueprint = Blueprint('cart_api', __name__)

#Add individual item to cart route  - WORKS!
@cart_blueprint.route('/add/<int:item_id>', methods=['GET', 'POST' ])
@jwt_required
def add_to_cart(item_id): 
    print(f'Enter cart/add/<item_id> route')
    if request.method == 'POST':
        item = fetch_one_item(item_id)            #Defined in item_service.py
        if item:
            user = get_jwt_identity()
            print(f'item:{item} user:{user}')
            return create_cart(item, user)        #Create Cart and add item to it
        else:
            return 'Failed to add to cart'

#Delete cart based in user_id
@cart_blueprint.route('/delete/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required
def delete_cart(user_id):
    print(f'!!************ Enter cart/delete/<int:user> route - user_id:{user_id} ****************!! ') 
    if request.method == 'DELETE':
 #        user_id = get_jwt_identity()
        cart_entry = fetch_one_cart(user_id)   #Defined in cart_service.py
        print(f'cart_entry:{cart_entry}')
        if str(user_id) == cart_entry['user_id']: #user_id is a column in items table
            print(f'user_id) == cart_entry[user_id] is good')
            return remove_cart(cart_entry['user_id'])
        else:
            return 'delete_cart() - cart not found'

# The Checkout/Pay for order
@cart_blueprint.route('/checkout', methods=['GET', 'POST'])
@jwt_required
def purchase_items(): 
    user_id = get_jwt_identity() 
    print(f'user_id:{user_id}')
    #Get user name, email from user table
    current_user = fetch_user(user_id)
#    print(f'current_user:{current_user}')
    email = current_user['email']
    f_name = current_user['first_name']
    l_name = current_user['last_name']

    #Get item info: item #, model, num & price 
    # First go to cart table and get item number
    cart_entry = fetch_one_cart(user_id)
    if not cart_entry:
        return 'No selected item(s) in cart'
    else:
#        print(f'cart_entry:{cart_entry}')
        item_id = cart_entry['item_id']
        order_num = cart_entry['id']
        item = fetch_one_item(item_id)
        price = item['price']
        model_name = item['model_name']
        
        #delete record from cart table
        ret = remove_cart(cart_entry['user_id'])
        print(f'ret:{ret}')

        return {
            'message':'THANK YOU FOR YOUR PURCHASE!',
            'Order #': order_num,
            'ID': user_id,
            'Item': model_name,
            'Amount PAID': price,
            'First': f_name,
            'Last': l_name,
            'Email': email
        } 

def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )