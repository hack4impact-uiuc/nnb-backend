from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest, AdditionalLinks, Content
import json
from flask import jsonify
from api.utils import serializeList
from sqlalchemy import func
import time
from datetime import date
import uuid

mod = Blueprint('years', __name__)

@app.route('/years', methods=['GET'])
def years():
    return jsonify(serializeList((Maps.query.all())))

@app.route('/years/<input>/poi', methods=['GET'])
def years2(input):
    return jsonify(serializeList((PointsOfInterest.query.filter(poi.year==input))))

@app.route('/years/<input>/maps', methods=['GET', 'POST'])
def years3(input):
    if request.method == 'GET':
        return jsonify(serializeList((Maps.query.filter(maps.year==input))))
    if request.method == 'POST':
        json_dict = json.loads(request.data)
        result = Maps(
            image_url = json_dict['image_url'],
            year = (int)(json_dict['year'])
        )
        if Maps.query.filter(Maps.year == json_dict['year']).count():
            Maps.query.filter(Maps.year == json_dict['year']).delete()
            db.session.commit()
        db.session.add(result)
        db.session.commit()
        return "SUCEEDED"
     
