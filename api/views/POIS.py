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

#Get POI given a year or POI ID
@app.route('/pois', methods=['GET']) 
def poi_get():
    year = request.args.get('year')
    poi_id = request.args.get('poi_id')
    if request.method == 'GET':
        try:
            if year:
                poi_years = PointsOfInterest.query.filter(PointsOfInterest.map_by_year == year)
                arr = []
                if not poi_years:
                    return jsonify({'status': 'failed', 'message': 'year '+ year + "> does not exist"})
                for poi_year in poi_years:
                    dict3 = poi_year.toDict()
                    poi_year_id = dict3['id']
                    dict3["additional_links"] = serializeList(AdditionalLinks.query.filter(AdditionalLinks.poi_id==poi_year_id))
                    dict3["content"] = serializeList((Content.query.filter(Content.poi_id==poi_year_id)))
                    arr.append(dict3)
                dict = {'status': 'success', 'data': arr}
                return jsonify(dict)
            elif poi_id:
                poi = PointsOfInterest.query.get(poi_id)
                if poi is None:
                    return jsonify({'status': 'failed', 'message': '<poi '+ poi_id + "> does not exist"})
                dict2 = poi.toDict()
                dict2["additional_links"] = serializeList(AdditionalLinks.query.filter(AdditionalLinks.poi_id==poi_id))
                dict2["content"] = serializeList((Content.query.filter(Content.poi_id==poi_id)))
                dict = {'status': 'success', 'data': dict2}
                return jsonify(dict)
            else:
                return jsonify({'status': 'success', 'data': serializePOI((PointsOfInterest.query.all()))})
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})
    return jsonify({"status: ": "failed", "message: ": "Endpoint, /pois, needs a GET or POST request"})

#Add POI
# @login_required
@app.route('/pois', methods=['POST'])
def poi():
    if request.method == "POST":
        try:
            json_dict = json.loads(request.data)
            result = PointsOfInterest(
                name=json_dict['name'],
                date = date((int)(json_dict['year']), (int)(json_dict['month']), (int)(json_dict['day'])),
                eventinfo = json_dict['info'],
                map_by_year = (int)(json_dict['map_by_year']),
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
            return jsonify({"status:": "success", "message":"Successfully added POI with id " +str(result.id) })
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})            
    return jsonify({"status: ": "failed", "message: ": "Endpoint, /pois, needs a gGET or POST request"})

#Returns all POIs
@app.route('/pois/<poi_id>', methods=['GET']) 
def poi_get_with_id(poi_id):
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

#Delete POI given POI ID
# @login_required
@app.route('/pois/<poi_id>', methods=['DELETE','PUT']) 
def poi_delete(poi_id):
    if request.method == 'DELETE':
        try:
            obj = PointsOfInterest.query.get(poi_id)
            for s in obj.stories:
                db.session.delete(s)
                db.session.commit()
            db.session.delete(obj)
            db.session.commit()
            return jsonify({'status':'success', 'message': 'deleted '+ poi_id + " from database"})
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})
    if request.method == "PUT":
        try:
            obj = PointsOfInterest.query.filter(PointsOfInterest.id==poi_id).first()
            if (obj):
                for s in obj.stories:
                    db.session.delete(s)
                    db.session.commit()
                db.session.delete(obj)
                db.session.commit()
            json_dict = json.loads(request.data)
            result = PointsOfInterest(
                name=json_dict['name'],
                date = date((int)(json_dict['year']), (int)(json_dict['month']), (int)(json_dict['day'])),
                eventinfo = json_dict['info'],
                map_by_year = (int)(json_dict['map_by_year']),
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
            # db.session.commit()
            return jsonify({"status:": "success"})
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})            
    else:
        return jsonify({"status: ": "failed", "message: ": "Endpoint, /pois/<poi_id, needs the correct request method"})
    

#Add POI
# @login_required
@app.route('/pois/<poi_id>', methods=['PUT'])
def poi_put(poi_id):
    if request.method == "PUT":
        try:
            obj = PointsOfInterest.query.filter(PointsOfInterest.id==poi_id).first()
            if (obj):
                for s in obj.stories:
                    db.session.delete(s)
                    db.session.commit()
                db.session.delete(obj)
                db.session.commit()
            json_dict = json.loads(request.data)
            result = PointsOfInterest(
                name=json_dict['name'],
                date = date((int)(json_dict['year']), (int)(json_dict['month']), (int)(json_dict['day'])),
                eventinfo = json_dict['info'],
                map_by_year = (int)(json_dict['map_by_year']),
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
            # db.session.commit()
            return jsonify({"status:": "success"})
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})            
    return jsonify({"status: ": "failed", "message: ": "Endpoint, /poi, needs a PUT request"})

#Returns all POIs
@app.route('/pois/year/<year>', methods=['GET']) 
def poi_get_with_year(year):
    try:
        poi_years = PointsOfInterest.query.filter(PointsOfInterest.map_by_year == year)
        arr = []
        if not poi_years:
            return jsonify({'status': 'failed', 'message': 'year '+ year + "> does not exist"})
        for poi_year in poi_years:
            dict3 = poi_year.toDict()
            poi_year_id = dict3['id']
            dict3["additional_links"] = serializeList(AdditionalLinks.query.filter(AdditionalLinks.poi_id==poi_year_id))
            dict3["content"] = serializeList((Content.query.filter(Content.poi_id==poi_year_id)))
            arr.append(dict3)
        map_obj = Maps.query.filter(Maps.year == poi_year.map_by_year)
        ret_rect = {'map':map_obj.toDict(),'pois':arr}
        dict = {'status': 'success', 'data': ret_rect}
        return jsonify(dict)
    except Exception as ex:
        return jsonify({"status: ": "failed", "message:": str(ex)})

@app.route('/pois/<name>', methods=['GET']) 
def poi_search_name(name):
    if request.method == "GET":
        try:
            return jsonify({'status': 'success', 'data': serializePOI(PointsOfInterest.query.filter(PointsOfInterest.name==name).first())})
        except Exception as ex:
            return jsonify({"status: ": "failed", "message:": str(ex)})
    return jsonify({"status: ": "failed", "message: ": "Endpoint, /poi, needs a GET request"})

