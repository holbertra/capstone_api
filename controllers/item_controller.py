from flask import Blueprint, request, Response, json
from services.item_service import create_item, fetch_one_item, fetch_items, fetch_items_by_user_id, delete_item
#from services.event_service import create_event, fetch_one_event, fetch_events
from flask_jwt_extended import jwt_required, get_jwt_identity

item_blueprint = Blueprint('item_api', __name__)

#new item route    - WORKS!
@item_blueprint.route('/new', methods=['POST'])    # /item/new item data is passed in body of postman  
@jwt_required
def new_item():
    print(f'Enter item/new route')
    new_user = get_jwt_identity()
    print(f'new_user:{new_user}') 
    data = request.json 
    print(f'data:{data}')   
    return create_item(data, new_user)   # create_item defined in item_service.py

#view/item/<id> route  view by item ID - WORKS!
@item_blueprint.route('/view/<int:item_id>', methods=['GET'])
@jwt_required
def view_item_id(item_id):
    print(f'     !!************ Enter /view/<int:item_id> route - item_id:{item_id} ****************!! ')
    if request.method == 'GET':
        item = fetch_one_item(item_id)  #Defined in item_service.py
        if item:
            return custom_response(item, 200)    
        else:
            return 'item doesnt exist in db' 

#View all by user_id -  WORKS!
@item_blueprint.route('/view/all/<int:user_id>', methods=['GET'])
@jwt_required
def view_all_items_by_user_id(user_id):
    print(user_id)
    list_items = fetch_items_by_user_id(user_id)   # defined in item_service.py
    return custom_response(list_items, 200)

#View ALL items route  - WORKS!
@item_blueprint.route('/view/all', methods=['GET'])
@jwt_required
def view_all_items():
    print(f'!!************ Enter /view/all route ****************!! ')
    list_items = fetch_items()   # defined in item_service.py
    return custom_response(list_items, 200)
 

#Delete route  - WORKS!
@item_blueprint.route('/delete/<int:item_id>', methods=['DELETE'])
@jwt_required
def delete_item_id(item_id):
    print(f'!!************ Enter /delete/<int:item_id> route - item_id:{item_id} ****************!! ')    
    if request.method == 'DELETE':
        user = get_jwt_identity()
        item = fetch_one_item(item_id)   #Defined in item_service.py
        if str(user) == item['user_id']: #user_id is a column in items table
            return delete_item(item['id'])
        else:
            return 'delete_item_id::item_controller - item not found'

def custom_response(res, status_code):
    print(f'custom_response:res:{res}')
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )

