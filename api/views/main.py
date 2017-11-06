from api import app
from flask import Blueprint, request
from api.models import PointsOfInterest
from .. import db
import json

mod = Blueprint('main', __name__)

@app.route('/')
def mainpage():
    return '<h1>NNB API Home Page</h1>'

# this doesnt work 
@app.route('/name')
def name():
    print(PointsOfInterest.query.all()[0].toJSON())
    return"HI"

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
