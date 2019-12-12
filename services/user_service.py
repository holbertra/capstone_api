from models.user import User, UserSchema
from datetime import datetime

user_schema = UserSchema()

def create_user(email, password, f_name, l_name):         #Called from auth_controller.py in the register route
    new_user = User(email, password, f_name, l_name)
    return new_user.save()

def fetch_user(user_id):
    print(f'Enter fetch_user::user_id:{user_id}')
    x = User.get_user_rec(user_id)
    user_data = user_schema.dump(x)
#    print(f'user_data:{user_data}')
    return user_data
