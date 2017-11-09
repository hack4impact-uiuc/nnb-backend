from api import app
from flask import Blueprint, request
from api.models import PointsOfInterest
from .. import db
import json
from api.utils import serializeList
from flask import jsonify
import requests
import time
from datetime import date

mod = Blueprint('main', __name__)
my_id = 0
@app.route('/')
def mainpage():
    return '<h1>NNB API Home Page</h1>'

# this doesnt work 
@app.route('/name')
def name():
    print(serializeList(PointsOfInterest.query.all()))
    return jsonify(serializeList(PointsOfInterest.query.all()))

@app.route('/name2/<input>/')
def name2(input):
    result = PointsOfInterest(
            name=input,
            event_date = date(2002, 12, 26),
            event_info = "hi",
            year = 2016,
            x_coord = 13.45,
            y_coord = 47.34,
            id=2
    )
    db.session.add(result)
    db.session.commit()
    return"HI"


@app.route('/getall')
def getall():

    r = (PointsOfInterest.query.all())
    print(r)
    return"HI"
