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
    return '<h1>HI THERE</h1>'
