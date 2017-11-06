from api import app
from flask import Blueprint, request
from api.models import PointsOfInterest
from .. import db
import json
from api.utils import serializeList
from flask import jsonify


mod = Blueprint('main', __name__)

@app.route('/')
def mainpage():
    return '<h1>NNB API Home Page</h1>'

# this doesnt work 
@app.route('/name')
def name():
    print(serializeList(PointsOfInterest.query.all()))
    return jsonify(serializeList(PointsOfInterest.query.all()))

@app.route('/name2/<input>')
def name2(input):
    result = PointsOfInterest(
            name=input
    )
    db.session.add(result)
    db.session.commit()
    return"HI"


@app.route('/getall')
def getall():

    r = (PointsOfInterest.query.all())
    print(r)
    return"HI"
