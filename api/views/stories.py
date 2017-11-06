from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest

mod = Blueprint('stories', __name__)

#Returns all story names
@app.route('/stories', methods=['GET'])
def stories():
    return "All story names"

#Returns all POIS for a specific Story
@app.route('/stories/<input>', methods=['GET', 'POST'])
def stories2(input):
    return "All POIs for story: " + input