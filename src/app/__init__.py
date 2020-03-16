from flask import Flask

from app.config import Config
from app.models import db
from flask_migrate import Migrate
from flask_admin import Admin
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

admin = Admin(app)

db.init_app(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)

from app.views_v1 import *