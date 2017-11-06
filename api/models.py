from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)



class PointsOfInterest(db.Model):
    """Points of Interest"""
    __tablename__ = "points_of_interests"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    data = db.Column(db.Date, nullable=False)
    eventinfo = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    x_coord = db.Column(db.Float, nullable=False)
    y_coord = db.Column(db.Float, nullable=False)
    years = db.relationship('Maps', backref='poi', Lazy=True)

    def __init__(self, id, name, data, eventinfo, year, x_coord, y_coord):
        self.id = id
        self.name = name
        self.data = data
        self.eventinfo = eventinfo
        self.year = year
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __repr__(self):
        return '<name {}>'.format(self.name)

    def toDict(self):
        return {'id': self.id, 'name': self.name}

class maps(db.Model):
    __tablename__ = "maps"

    image_url = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, db.ForeignKey('poi.id'), nullable=False)

    # Not sure if I did the foreign key stuff correctly ^^^

    def __init__(self, image_url, year):
        self.image_url = image_url
        self.year = year



with app.app_context():
    db.create_all()