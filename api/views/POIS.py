from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest

mod = Blueprint('POIS', __name__)

#Returns all POIS and information for each
@app.route('/poi', methods=['GET', 'POST'])
def poi():
    return "All the POIS"

@app.route('/poi/<poiuuid>', methods=['GET', 'POST'])
def poiID(poiuuid):
    return "Return POI corresponding to ID: " + poiuuid + " And all its information"