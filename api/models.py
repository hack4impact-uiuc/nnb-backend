from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import json
from sqlalchemy import func
from api import db
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):
    """Points of Interest"""
    __tablename__ = "users"
    id = db.Column(db.Integer, unique=True,  primary_key = True)
    username = db.Column(db.String(32), index = True)
    password_hash = db.Column(db.String(128))
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def is_authenticated(self):
        return True

class PointsOfInterest(db.Model):
    """Points of Interest"""
    __tablename__ = "poi"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    eventinfo = db.Column(db.String, nullable=False)
    map_by_year = db.Column(db.Integer, nullable=False)
    x_coord = db.Column(db.Float, nullable=False)
    y_coord = db.Column(db.Float, nullable=False)
    stories = db.relationship('Stories', backref='poi', lazy=True)
    # years = db.relationship('Maps', backref='poi', lazy=True)
    # content = db.relationship('Content', backref='poi', lazy=True)

    def __repr__(self):
        return '<name {}>'.format(self.name)

    def toDict(self):
        return {'id': self.id, 'name': self.name, 'date': self.date, 'event_info': self.eventinfo, 'map_by_year': self.map_by_year, 'x_coord': self.x_coord, 'y_coord': self.y_coord}


class Maps(db.Model):
    __tablename__ = "maps"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    image_url = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer,  nullable=False)


    def __repr__(self):
        return '<map {}>'.format(self.year)

    def toDict(self):
        return {'id':self.id,'year': self.year, 'image_url': self.image_url}


class Content(db.Model):
    __tablename__ = "content"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    content_url = db.Column(db.String, nullable=True)
    caption = db.Column(db.String, nullable=True)
    poi_id = db.Column(db.Integer, db.ForeignKey('poi.id', ondelete='SET NULL'), nullable=True)

    def __repr__(self):
        return '<content {}>'.format(self.caption)

    def toDict(self):
        return {'id': self.id, 'poi_link': self.poi_id, 'content_url':
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
    story_names_id = db.Column(db.Integer, db.ForeignKey("story_names.id", ondelete='SET NULL'), nullable=True)
    poi_id = db.Column(db.Integer, db.ForeignKey('poi.id', ondelete='SET NULL'), nullable=True)
    
    def __repr__(self):
        return '<stories {}>'.format(self.id)

    def toDict(self):
        # return {'story_uuid': self.story_uuid, 'poi_id': self.poi_id}
        return {'id':self.id,'story_names_id': self.story_names_id, 'poi_id': self.poi_id}


class AdditionalLinks(db.Model):
    __tablename__ = 'additional_links'

    id = db.Column (db.Integer, unique=True, primary_key=True)
    url = db.Column(db.String)
    poi_id = db.Column(db.Integer, db.ForeignKey('poi.id', ondelete='SET NULL'), nullable=True)

    def __repr__(self):
        return '<additional_links poi_id = {}>'.format(self.poi_id)

    def toDict(self):
        return {'id':self.id,'url': self.url, 'poi_id': self.poi_id}


# with app.app_context():
#     db.create_all()