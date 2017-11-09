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

mod = Blueprint('POIS', __name__)

@app.route('/poi/<poi_id>', methods=['GET', 'POST'])
def poiID(poi_id):
    return jsonify(serializeList((PointsOfInterest.query.filter(PointsOfInterest.id==poi_id)))
    + serializeList(AdditionalLinks.query.filter(AdditionalLinks.poi_id==poi_id))
    + serializeList((Content.query.filter(AdditionalLinks.poi_id==poi_id))))

@app.route('/poi/', methods=['GET', 'POST'])
def poi():
    if request.method == "GET":
        return jsonify(serializeList((PointsOfInterest.query.all())))
    if request.method == "POST":
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
        return "SUCEEDED"
    
