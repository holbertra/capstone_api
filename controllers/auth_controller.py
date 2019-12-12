from flask import Blueprint, Flask, request, jsonify, render_template, url_for
from services.user_service import create_user
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_raw_jwt
from . import jwt
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_blueprint = Blueprint('auth_api', __name__)
blacklist = set()

# from flask_jwt_extended import (
#     JWTManager, create_access_token, create_refresh_token, get_jti,
#     jwt_refresh_token_required, get_jwt_identity, jwt_required, get_raw_jwt
# )

from services import bcrypt
from models.user import User

# # Function to check if a token has been blacklisted.
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

# see https://flask-jwt-extended.readthedocs.io/en/stable/blacklist_and_token_revoking/

#index route
@auth_blueprint.route('/index')
def index():
    user = {'username': 'Capstone API'}
    return render_template('index.html', title='Home', user=user)

#login route
@auth_blueprint.route('/login', methods=['POST'])
def login():
    print('Enter login route')
    # To log user in and return an authentication token
    # Body: {email, password}
    # Return {auth_token}    
    body = request.json
    first_nam = request.json.get('username', None)

    to_check = User.query.filter_by(email=body['email']).first()
    if to_check == None:
        return 'No user record found in db'

    if bcrypt.check_password_hash(to_check.password, body['password']):
         # Create JWT token and return it
        print(f'bcrypt.check_password_hash(  passed!')     
        access_token = create_access_token(to_check.id)
        print(f'create_access_token(to_check.id) passed!')
        return{
            'message': 'Hey you logged in fine',
            'access_token'  :  access_token                   #This appears in Postman
        }
    else:
        return {
            'message': 'Incorrect password'
        }  

#logout route
@auth_blueprint.route('/logout', methods=['GET'])
@jwt_required
def logout():
    print('Enter logout route')
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)    
    return 'Logging out. Goodbye!'


#register route
@auth_blueprint.route('/register', methods=['POST'])
def register():
    print('Enter /register route')
    body = request.json
    message = create_user(     # create_user() defined in user_service.py
        body['email'], 
        bcrypt.generate_password_hash(body['password']).decode('utf-8'), 
        body['f_name'], 
        body['l_name'],
    )    
    return {
        'message': message
    }

