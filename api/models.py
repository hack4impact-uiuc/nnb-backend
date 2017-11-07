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
    __tablename__ = "poi"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    data = db.Column(db.Date, nullable=False)
    eventinfo = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    x_coord = db.Column(db.Float, nullable=False)
    y_coord = db.Column(db.Float, nullable=False)
    years = db.relationship('Maps', backref='poi', lazy=True)
    content = db.relationship('Content', backref='poi', lazy=True)

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
    
    id = db.Column(db.Integer, unique=True, primary_key=True)
    image_url = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, db.ForeignKey('poi.id'), nullable=False)

    # Not sure if I did the foreign key stuff correctly ^^^

    def __init__(self, image_url, year):
        self.id = id
        self.image_url = image_url
        self.year = year

    def __repr__(self):
        return '<map {}>'.format(self.year)

    def toDict(self):
        return {'year': self.year, 'image_url': self.image_url}


class content(db.Model):
    __tablename__ = "content"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    content_url = db.Column(db.String, nullable=True)
    caption = db.Column(db.String, nullable=True)
    poi_id = db.Column(db.Integer, db.ForeignKey('poi.id'), nullable=False)

    def __init__(self, id, content_url, caption, poi_id):
        self.id = id
        self.content_url = content_url
        self.caption = caption
        self.poi_id = poi_id
    
    def __repr__(self):
        return '<content {}>'.format(self.caption)

    def toDict(self):
        return {'id': self.id, 'poi-link': self.poi_id, 'content_url':
                self.content_url, 'caption': self.caption}


class story_names(db.Model):
    __tablename__ = 'story_names'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    story_name = db.Column(db.String, nullable=0)
    story_id = db.relationship('Stories', backref='story_name', lazy=True)

    def __init__(self, story_name, story_id):
        self.id = id
        self.story_name = story_name
        self.story_id = story_id

    def __repr__(self):
        return '<story_names {}>'.format(self.story_name)

    def toDict(self):
        return {'id': self.id, 'story_name': self.story_name, 
                'story_id': self.story_id}


class stories(db.Model):
    __tablename__ = 'stories'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    story_uuid = db.Column(db.Integer, db.ForeignKey("story_names.id"), nullable=False)
    poi_id = db.Column(db.Integer, db.ForeignKey('poi.id'), nullable=False)

    def __init__(self, story_uuid, poi_id):
        self.id = id
        self.story_uuid = story_uuid
        self.poi_id = poi_id
    
    def __repr__(self):
        return '<stories {}>'.format(self.story_uuid)

    def toDict(self):
        return {'story_uuid': self.story_uuid, 'poi_id': self.poi_id}


class additional_links(db.Model):
    __tablename__ = 'additional_links'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    url = db.Column(db.String)
    poi_id = db.Column(db.Integer, db.ForeignKey('poi.id'), nullable=False)

    def __init__(self, url, poi_id):
        self.id = id
        self.url = url
        self.poi_id = poi_id

    def __repr__(self):
        return '<additional_links poi_id = {}>'.format(self.poi_id)

    def toDict(self):
        return {'url': self.url, 'poi_id': self.poi_id}


with app.app_context():
    db.create_all()