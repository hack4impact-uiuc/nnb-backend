from api import app
from flask import Blueprint, request
from api.models import PointsOfInterest
from .. import db

mod = Blueprint('main', __name__)

@app.route('/')
def mainpage():
    return '<h1>NNB Home Page</h1>'

# this doesnt work 
@app.route('/name')
def name():
    PointsOfInterest.query.all()
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
