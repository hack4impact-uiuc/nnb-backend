from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest

mod = Blueprint('years', __name__)

@app.route('/years', methods=['GET'])
def years():
    return "All years and corresponding map urls"

@app.route('/years/<input>/poi', methods=['GET'])
def years2(input):
    return "All POIs for " + input

@app.route('/years/<input>/maps', methods=['GET', 'POST'])
def years3(input):
    return "Map url for " + input
