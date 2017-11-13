from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest, AdditionalLinks, Content
import json
from flask import jsonify
from api.utils import serializeList, serializePOI
from sqlalchemy import func
import time
from datetime import date
import uuid

mod = Blueprint('POIS', __name__)

@app.route('/poi/<poi_id>', methods=['GET'])
def poiID(poi_id):
    if request.method == 'GET':
        try:
            dict2 = PointsOfInterest.query.get(poi_id).toDict()
            dict2["additional_links"] = serializeList(AdditionalLinks.query.filter(AdditionalLinks.poi_id==poi_id))
            dict2["content"] = serializeList((Content.query.filter(Content.poi_id==poi_id)))
            dict = {'status': 'success', 'data': dict2}
            return jsonify(dict)
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})
    else:
        return jsonify({"status: ": "failed", "message: ": "Endpoint, /poi/<poi_id, needs a GET request"})
        

@app.route('/poi', methods=['GET', 'POST'])
def poi():
    print(request.method == "POST")
    if request.method == "GET":
        try:
            return jsonify({'status':'success', 'data': serializePOI((PointsOfInterest.query.all()))})
        except Exception as ex:
            return jsonify({"Status: ": "Failed", "Message:": str(ex)})
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

            for link in json_dict['content']:
                result = Content(
                    content_url = (link['content_url']),
                    caption = (link['caption']),
                    poi_id=result.id
                )
                db.session.add(result)
                db.session.commit()
                for link in json_dict['additional_links']:
                    result = AdditionalLinks(
                        url = (link['link']),
                        poi_id=result.id
                    )
                    db.session.add(result)
                    db.session.commit()
                for link in json_dict['content']:
                    result = Content(
                        content_url = (link['content_url']),
                        caption = (link['caption']),
                        poi_id=result.id
                    )
                    db.session.add(result)
                    db.session.commit()
            return jsonify({"Status:": "Succeeded"})
        except Exception as ex:
            return jsonify({"Status: ": "Failed", "Message:": str(ex)})            
    return jsonify({"Status: ": "Failed", "Message: ": "Endpoint, /poi, needs a GET or PULL request"})
    
