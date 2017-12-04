from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest, AdditionalLinks, Content, Maps, InvalidUsage
import json
from flask import jsonify
from api.utils import serializeList, serializePOI
from sqlalchemy import func
import time
from datetime import date
import uuid
from flask_login import LoginManager, login_required, login_user, logout_user 

mod = Blueprint('maps', __name__)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

#Gets all maps
@app.route('/maps', methods=['GET'])
def getallyears():
    if request.method == 'GET':
        try:
            return jsonify({'status': 'success', 'data': serializeList((Maps.query.all()))})
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
    else:
        return jsonify({"status: ": "failed", "message: ": "Endpoint, /years, needs a GET request"})

#Maps for certain year
@app.route('/maps/years/<year>', methods=['GET'])
def getmapsforyear(year):
    if request.method == 'GET':
        try:
            poi_years = PointsOfInterest.query.filter(PointsOfInterest.map_by_year == year)
            if not poi_years.first():
                raise Exception('year,  <'+ year + "> does not exist")
            arr = serializePOI(poi_years)
            map_obj = Maps.query.filter(Maps.year == poi_years[0].map_by_year)
            ret_rect = {'map': serializeList(map_obj), 'pois': arr}
            dict = {'status': 'success', 'data': ret_rect}
            return jsonify(dict)
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
    else:
        return jsonify({"status: ": "failed", "message: ": "Endpoint, /maps, needs a GET or POST request"})

#Add a map
@app.route('/maps', methods=['POST'])
def addmapforyear():
    if request.method == 'POST':
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
        return jsonify({"status: ": "failed", "message: ": "Endpoint, /maps, needs a GET or POST request"})


# delete maps by id
@app.route('/maps/<id>', methods=['DELETE'])
def delete_map(id):
    try:
        map_to_delete = Maps.query.get(id)
        if map_to_delete is None:
            raise Exception("map" + id + "doesn't exist")
        year = map_to_delete.year
        poi_to_delete = PointsOfInterest.query.filter(PointsOfInterest.map_by_year == year)
        for obj in poi_to_delete:
            for s in obj.stories:
                db.session.delete(s)
                db.session.commit()
            db.session.delete(obj)
            db.session.commit()
        db.session.delete(map_to_delete)
        db.session.commit()
        return jsonify({"status":'success','message':'successfully deleted'})
    except Exception as ex:
        raise InvalidUsage('Error: ' + str(ex), status_code=404)
