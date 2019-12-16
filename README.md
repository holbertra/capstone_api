CAPSTONE API

A Shopping API to compare items by model, description and price

DATABASE SETUP: 
Set these environment variables for the WINDOWS OS:
$ENV:DATABASE_URL="postgresql://postgres:password123@localhost/capstone_db"
$ENV:SECRET_KEY="qwertyuiop1234567890"

Run:
py manage.py db init
py manage.py db migrate
py manage.py db upgrade

ROUTES:

AUTH ROUTES:  prefix = 'auth/'

1. @auth_blueprint.route('/login', methods=['POST']) 
2. @auth_blueprint.route('/register', methods=['POST'])
3. @auth_blueprint.route('/logout', methods=['GET'])

ITEM ROUTES:  prefix = 'item/'

4. @item_blueprint.route('/new', methods=['POST'])
5. @item_blueprint.route('/view/<int:item_id>', methods=['GET']) 
6. @item_blueprint.route('/view/all/<int:user_id>', methods=['GET'])
7. @item_blueprint.route('/view/all', methods=['GET'])
8. @item_blueprint.route('/delete/<int:item_id>', methods=['DELETE'])  

CART ROUTES:  prefix = 'cart/'

9.  @cart_blueprint.route('/add/<int:item_id>', methods=['GET', 'POST' ])
10. @cart_blueprint.route('/delete/<int:user_id>', methods=['GET', 'PUT', 'DELETE']) 
11. @cart_blueprint.route('/checkout', methods=['GET', 'POST']) 


TESTING DATA:   
USER & ITEM data to be copied into body of POSTMAN.


-- User Test Cases: --  
{  
     "email": "elevenfifty@gmail.com",  
     "password": "a_very_secure_password123",  
     "f_name": "Saint",  
     "l_name": "Nick"  
}  

{  
     "email": "bogus@gmail.com", 
     "password": "hacked_password", 
     "f_name": "Mister",  
     "l_name": "Robot"  
}  

{  
     "email": "cracker@msn.com",  
     "password": "iamaviolentdude",  
     "f_name": "John",  
      "l_name": "Wick"  
}  

-- Item Test Cases: --  
{  
     "model_name": "Gibson Les Paul",  
     "model_type": "Electric",  
     "model_num": "AX245-34",  
     "color": "Black",  
     "price": 7500,  
     "user_id": 0  
}  

{  
     "model_name": "Fender Stratocaster",  
     "model_type": "Electric",  
     "model_num": "JYC-28SX",  
     "color": "Sunbrust",  
     "price": 3750,  
     "user_id": 0  
}  

{  
     "model_name": "Martin Dreadnought",  
     "model_type": "Acoustic",  
     "model_num": "D-28",  
     "color": "Spruce Top/Rosewood Sides",  
     "price": 4500,  
     "user_id": 0  
}  

{  
     "model_name": "Gretsch ",  
     "model_type": "Electromatic Hollow Body",  
     "model_num": "G5420T",  
     "color": "Cobalt Blue",  
     "price": 3000,  
     "user_id": 0  
}  



