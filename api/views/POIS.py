from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest, AdditionalLinks, Content, InvalidUsage
import json
from flask import jsonify
from api.utils import serializeList, serializePOI
from sqlalchemy import func
import time
from datetime import date
import uuid

mod = Blueprint('POIS', __name__)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/poi/<poi_id>', methods=['GET', 'DELETE'])
def poiID(poi_id):
    if request.method == 'GET':
        try:
            year = request.args['year']
            if year:
                return jsonify({'status': 'success', 'data': serializeList((PointsOfInterest.query.filter(PointsOfInterest.year==input)))})
            else:
                poi = PointsOfInterest.query.get(poi_id)
                if poi is None:
                    raise InvalidUsage('Error: <poi ' + poi_id + '> does not exist', status_code=404)
                dict2 = poi.toDict()
                dict2["additional_links"] = serializeList(AdditionalLinks.query.filter(AdditionalLinks.poi_id==poi_id))
                dict2["content"] = serializeList((Content.query.filter(Content.poi_id==poi_id)))
                dict = {'status': 'success', 'data': dict2}
                return jsonify(dict)
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
    elif request.method == 'DELETE':
        # THIS DOESNT WORK - FOREIGN KEY CONSTRAINT
        try:
            obj = PointsOfInterest.query.get(poi_id)
            db.session.delete(obj)
            db.session.commit()
            return jsonify({'status':'success', 'message': 'deleted '+ poi_id + " from database"})
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
    else:
        raise InvalidUsage('Error: Endpoint, /poi/<poi_id, needs a GET request', status_code=404)
        

@app.route('/poi', methods=['GET', 'POST'])
def poi():
    print(request.method == "POST")
    if request.method == "GET":
        try:
            return jsonify({'status': 'success', 'data': serializePOI((PointsOfInterest.query.all()))})
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
    elif request.method == "POST":
        try:
            json_dict = json.loads(request.data)
            result = PointsOfInterest(
                name=json_dict['name'],
                data = date((int)(json_dict['year']), (int)(json_dict['month']), (int)(json_dict['day'])),
                eventinfo = json_dict['info'],
                year = (int)(json_dict['year']),
                x_coord = (int)(json_dict['x_coor']),
                y_coord = (int)(json_dict['y_coor']), 
            )
            db.session.add(result)
            db.session.commit()
            new_poi_id = result.id
            for link in json_dict['content']:
                result = Content(
                    content_url=(link['content_url']),
                    caption=(link['caption']),
                    poi_id=new_poi_id
                )
                db.session.add(result)
                db.session.commit()
            for link in json_dict['additional_links']:
                result = AdditionalLinks(
                    url=(link['url']),
                    poi_id=new_poi_id
                )
                db.session.add(result)
                db.session.commit()

            return jsonify({"status:": "success"})
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
    raise InvalidUsage('Error: Endpoint, /poi, needs a GET or PULL request', status_code=404)
    
