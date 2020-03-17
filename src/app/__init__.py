from flask import Flask

from app.config import Config
from app.models import db, Participant, EventType, EventCategory, Event, Location, Enrollment
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

admin = Admin(app)

db.init_app(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)

from app.views.v1.participants import *
from app.views.v1.locations import *
from app.views.v1.events import *
from app.views.v1.event_types import *
from app.views.v1.event_categories import *
from app.views.v1.enrollments import *

admin.add_view(ModelView(Location, db.session))
admin.add_view(ModelView(Participant, db.session))
admin.add_view(ModelView(EventType, db.session))
admin.add_view(ModelView(EventCategory, db.session))
admin.add_view(ModelView(Event, db.session))
admin.add_view(ModelView(Enrollment, db.session))
