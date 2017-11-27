from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager, login_required

app = Flask(__name__)
app.config.from_object('config')
CORS(app)

db = SQLAlchemy(app)
db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from api.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id = user_id).first()

# import and register blueprints
from api.views import main
app.register_blueprint(main.mod)

from api.views import maps
app.register_blueprint(maps.mod)

from api.views import stories
app.register_blueprint(stories.mod)

from api.views import POIS
app.register_blueprint(POIS.mod)

from api.views import auth
app.register_blueprint(auth.mod)
