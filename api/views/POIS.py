from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest, AdditionalLinks, Content, User
import json
from flask import jsonify
from api.utils import serializeList, serializePOI
from sqlalchemy import func
import time
from datetime import date
import uuid
from flask_httpauth import HTTPBasicAuth
from flask_login import LoginManager, login_required, login_user, logout_user 

mod = Blueprint('POIS', __name__)

@app.route('/poi/<poi_id>', methods=['GET']) 
def poiID(poi_id):
    if request.method == 'GET':
        try:
            poi = PointsOfInterest.query.get(poi_id)
            if poi is None:
                return jsonify({'status': 'failed', 'message': '<poi '+ poi_id + "> does not exist"})
            dict2 = poi.toDict()
            dict2["additional_links"] = serializeList(AdditionalLinks.query.filter(AdditionalLinks.poi_id==poi_id))
            dict2["content"] = serializeList((Content.query.filter(Content.poi_id==poi_id)))
            dict = {'status': 'success', 'data': dict2}
            return jsonify(dict)
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})
    else:
        return jsonify({"status: ": "failed", "message: ": "Endpoint, /poi/<poi_id, needs a GET or POST request"})


@login_required
@app.route('/poi/<poi_id>', methods=['DELETE']) 
def poi_delete(poi_id):
    if request.method == 'DELETE':
        try:
            obj = PointsOfInterest.query.get(poi_id)
            db.session.delete(obj)
            db.session.commit()
            return jsonify({'status':'success', 'message': 'deleted '+ poi_id + " from database"})
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})
    else:
        return jsonify({"status: ": "failed", "message: ": "Endpoint, /poi/<poi_id, needs a GET or POST request"})


@app.route('/poi', methods=['GET']) 
def poi_get():
    if request.method == "GET":
        try:
            return jsonify({'status': 'success', 'data': serializePOI((PointsOfInterest.query.all()))})
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})

@login_required
@app.route('/poi', methods=['POST'])
def poi():
    if request.method == "POST":
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
            new_poi_id = result.id
            for link in json_dict['content']:
                result = Content(
                    content_url=(link['content_url']),
                    caption=(link['caption']),
                    poi_id=new_poi_id
                )
                db.session.add(result)
            for link in json_dict['additional_links']:
                result = AdditionalLinks(
                    url=(link['url']),
                    poi_id=new_poi_id
                )
                db.session.add(result)
            db.session.commit()
            return jsonify({"status:": "success"})
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})            
    return jsonify({"status: ": "failed", "message: ": "Endpoint, /poi, needs a gGET or POST request"})
