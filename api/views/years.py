from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest, AdditionalLinks, Content, Maps, InvalidUsage
import json
from flask import jsonify
from api.utils import serializeList
from sqlalchemy import func
import time
from datetime import date
import uuid

mod = Blueprint('years', __name__)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/years', methods=['GET'])
def getallyears():
    if request.method == 'GET':
        try:
            return jsonify({'status': 'success', 'data': serializeList((Maps.query.all()))})
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
    else:
        raise InvalidUsage('Error: Endpoint, /years, needs a GET request' + str(ex), status_code=404)

@app.route('/years/<input>/poi', methods=['GET'])
def getpoiforyear(input):
    if request.method == 'GET':
        try:
            return jsonify({'status': 'success', 'data': serializeList((PointsOfInterest.query.filter(PointsOfInterest.year==input)))})
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
    else:
        raise InvalidUsage('Error: Endpoint, /years/<input>/poi, needs a GET request' + str(ex), status_code=404)

@app.route('/maps', methods=['GET', 'POST'])
def getmapsforyear():
    if request.method == 'GET':
        try:
            return jsonify({'status': 'success', 'data': serializeList((Maps.query.all()))})
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)

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
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
    else:
        raise InvalidUsage('Error: Endpoint, /maps, needs a GET or POST request' + str(ex), status_code=404)

     
@app.route('/maps/<input>', methods=['GET'])
def years4(input):
    if request.method == 'GET':
        try:
            return jsonify({'status': 'success', 'data': serializeList((Maps.query.filter(Maps.year==input)))})
            #return jsonify(serializeList((Maps.query.filter(Maps.year==input))))
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
    else:
        raise InvalidUsage('Error: Endpoint, /maps/<input>, needs a GET request', status_code=404)