from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
db.create_all()

# import and register blueprints
from api.views import main
app.register_blueprint(main.mod)

from api.views import years
app.register_blueprint(years.mod)

from api.views import stories
app.register_blueprint(stories.mod)

from api.views import POIS
app.register_blueprint(POIS.mod)
