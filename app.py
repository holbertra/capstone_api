from flask import Flask
from models import db
from services import bcrypt
from controllers import jwt, auth_blueprint, item_blueprint, cart_blueprint

app = Flask(__name__)

app.config.from_object('config.Development') 

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Add blueprints here
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(item_blueprint, url_prefix="/item")
app.register_blueprint(cart_blueprint, url_prefix="/cart")

if __name__ == "__main__":
    app.run()
