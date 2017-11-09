from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy import func

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
    stories = db.relationship('Stories', backref='poi', lazy=True)
    # years = db.relationship('Maps', backref='poi', lazy=True)
    # content = db.relationship('Content', backref='poi', lazy=True)

    def __repr__(self):
        return '<name {}>'.format(self.name)

    def toDict(self):
        return {'id': self.id, 'name': self.name, 'data': self.data}



class Maps(db.Model):
    __tablename__ = "maps"
    
    id = db.Column(db.Integer, unique=True, primary_key=True)
    image_url = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, db.ForeignKey('poi.id'), nullable=False)


    def __repr__(self):
        return '<map {}>'.format(self.year)

    def toDict(self):
        return {'year': self.year, 'image_url': self.image_url}


class Content(db.Model):
    __tablename__ = "content"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    content_url = db.Column(db.String, nullable=True)
    caption = db.Column(db.String, nullable=True)
    poi_id = db.Column(db.Integer, db.ForeignKey('poi.id'), nullable=False)

    
    def __repr__(self):
        return '<content {}>'.format(self.caption)

    def toDict(self):
        return {'id': self.id, 'poi-link': self.poi_id, 'content_url':
                self.content_url, 'caption': self.caption}


class StoryNames(db.Model):
    __tablename__ = 'story_names'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    story_name = db.Column(db.String, nullable=0)
    story_id = db.relationship('Stories', backref='story_name')

    def __repr__(self):
        return '<story_names {}>'.format(self.story_name)

    def toDict(self):
        return {'id': self.id, 'story_name': self.story_name}


class Stories(db.Model):
    __tablename__ = 'stories'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    story_names_id = db.Column(db.Integer, db.ForeignKey("story_names.id"), nullable=True)
    poi_id = db.Column(db.Integer, db.ForeignKey('poi.id'), nullable=True)
    
    def __repr__(self):
        return '<stories {}>'.format(self.id)

    def toDict(self):
        # return {'story_uuid': self.story_uuid, 'poi_id': self.poi_id}
        return {'id':self.id}


class AdditionalLinks(db.Model):
    __tablename__ = 'additional_links'

    id = db.Column (db.Integer, unique=True, primary_key=True)
    url = db.Column(db.String)
    poi_id = db.Column(db.Integer, db.ForeignKey('poi.id'), nullable=False)

    def __repr__(self):
        return '<additional_links poi_id = {}>'.format(self.poi_id)

    def toDict(self):
        return {'url': self.url, 'poi_id': self.poi_id}


with app.app_context():
    db.create_all()