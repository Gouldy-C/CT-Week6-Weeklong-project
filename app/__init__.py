from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from flask_jwt_extended import JWTManager


from ConfigModule import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
CORS(app)

jwt = JWTManager(app)



from app.blueprints.auth import bp as auth
app.register_blueprint(auth)
from app.blueprints.main import bp as main
app.register_blueprint(main)
from app.blueprints.user_stuff import bp as user_stuff
app.register_blueprint(user_stuff)


from app import models