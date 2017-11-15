from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest, AdditionalLinks, Content,Maps
import json
from flask import jsonify
from api.utils import serializeList
from sqlalchemy import func
import time
from datetime import date
import uuid

mod = Blueprint('years', __name__)

@app.route('/years', methods=['GET'])
def getallyears():
    if request.method == 'GET':
        try:
            return jsonify({'status': 'success', 'data': serializeList((Maps.query.all()))})
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})
    else:
        return jsonify({"status: ": "failed", "message: ": "Endpoint, /years, needs a GET request"})

@app.route('/years/<input>/poi', methods=['GET'])
def getpoiforyear(input):
    if request.method == 'GET':
        try:
            return jsonify({'status': 'success', 'data': serializeList((PointsOfInterest.query.filter(PointsOfInterest.year==input)))})
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})
    else:
        return jsonify({"status: ": "failed", "message: ": "Endpoint, /years/<input>/poi, needs a GET request"})

@app.route('/maps', methods=['GET', 'POST'])
def getmapsforyear():
    if request.method == 'GET':
        try:
            return jsonify({'status': 'success', 'data': serializeList((Maps.query.all()))})
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})

    elif request.method == 'POST':
        try:
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
            return jsonify({"status:": "success", "message": "successfully added maps and year"})
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})
    else:
        return jsonify({"status: ": "failed", "message: ": "Endpoint, /maps, needs a GET or POST request"})
     
@app.route('/maps/<input>', methods=['GET'])
def years4(input):
    if request.method == 'GET':
        try:
            return jsonify({'status': 'success', 'data': serializeList((Maps.query.filter(Maps.year==input)))})
            #return jsonify(serializeList((Maps.query.filter(Maps.year==input))))
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})
    else:
        return jsonify({"status: ": "failed", "message: ": "Endpoint, /maps/<input>, needs a GET request"})