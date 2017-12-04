from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest, StoryNames, Stories, InvalidUsage
import json
from flask import jsonify
from api.utils import serializeList
from sqlalchemy import func
from flask_login import LoginManager, login_required, login_user, logout_user 

mod = Blueprint('stories', __name__)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# Returns all story names aka stories
@app.route('/stories', methods=['GET'])
def stories():
    if request.method == 'GET':
        try:
            return jsonify({'status': 'success', 'data': serializeList(StoryNames.query.all())})
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
    else:
        return jsonify({"status": "failed", "message": "Endpoint, /maps, needs a GET or POST request"})

# Add story
@app.route('/stories', methods=['POST'])
# @login_required
def stories_post():
    if request.method == 'POST':
        try:
            json_dict = json.loads(request.data)
            story_added = StoryNames(
                story_name=json_dict['story_name'],
            )
            db.session.add(story_added)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Added new Story'})
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
    else:
        return jsonify({"status": "failed", "message": "Endpoint, /maps, needs a GET or POST request"})

# Returns all POIS for a specific Story Name aka story
@app.route('/stories/<id>', methods=['GET'])
def stories_get(id):
    if request.method == 'GET':
        try:
            arry = []
            storyname = StoryNames.query.get(id)
            if storyname is None:
                raise Exception('Story with ID: ' + id + ' does not exist')
            stories = storyname.story_id
            if stories is None:
                raise Exception('Storyname ' + id + '> does not exist')
            
            for story in stories:
                if story.poi_id is None:
                    db.session.delete(story)
                    db.session.commit()
                    continue
                arry.append(PointsOfInterest.query.get(story.poi_id))
            ret_dict = {'story_name_id': id, 'story_name': StoryNames.query.get(id).story_name, 'pois': serializeList(arry)}
            return jsonify(ret_dict)
            # return jsonify({'status': 'success', 'data': serializeList((Stories.query.filter(func.lower(StoryNames.story_name)==func.lower(inputStoryName))))})
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
    else:
        return jsonify({'status': 'failed', 'message': 'You can only GET or DELETE'})

@app.route('/stories/<id>', methods=['DELETE'])
# @login_required
def stories_delete(id):
    try:
        storyname = StoryNames.query.get(id)
        if storyname:
            stories = storyname.story_id
            for s in stories:
                db.session.delete(s)
                db.session.commit()
            db.session.delete(storyname)
            db.session.commit()
            return jsonify({'status':'success','message':'Successfully deleted Story ' + id})
        else:
            raise InvalidUsage('Error: <Story ' + id + '> does not exist', status_code=404)
    except Exception as ex:
        raise InvalidUsage('Error: ' + str(ex), status_code=404)

# adds a POI to an existing story name aka story, POI must exist!!!!
@app.route('/stories/add', methods=['POST'])
# @login_required  
def story_point():
    if request.method == "POST":
        try:
            json_dict = json.loads(request.data)
            storynames = StoryNames.query.get(json_dict["input_story_name_id"]) #check if it is empty later
            storynames.story_id.append(Stories()) #add new Stories() to storynames
            db.session.commit()
            # get poi and add the same story to it
            poi = PointsOfInterest.query.get(json_dict["input_poi_id"])
            poi.stories.append(storynames.story_id[-1]) # gets last index, which is the Stories() that was just added
            db.session.commit()
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
        return jsonify({"status": "success", "message": "new story poi added to existing story"})
    else:
        return jsonify({"status": "failed", "message": "POST request only"})

# Adds POI to multiple stories, not sure what to call it
@app.route('/stories/add/multiple', methods=['POST'])
# @login_required
def addtomultiplestory():
    if request.method == "POST":
        try:
            json_dict = json.loads(request.data)
            if len(json_dict["input_story_name_id"]) == 1:
                storynames = StoryNames.query.get(json_dict["input_story_name_id"]) #check if it is empty later
                storynames.story_id.append(Stories()) #add new Stories() to storynames
                db.session.commit()
                # get poi and add the same story to it
                poi = PointsOfInterest.query.get(json_dict["input_poi_id"])
                poi.stories.append(storynames.story_id[-1]) # gets last index, which is the Stories() that was just added
                db.session.commit()
            else:
                for i in range(len(json_dict["input_story_name_id"])):
                    storynames = StoryNames.query.get(json_dict["input_story_name_id"][i]) #check if it is empty later
                    storynames.story_id.append(Stories()) #add new Stories() to storynames
                    db.session.commit()
                    # get poi and add the same story to it
                    poi = PointsOfInterest.query.get(json_dict["input_poi_id"])
                    poi.stories.append(storynames.story_id[-1]) # gets last index, which is the Stories() that was just added
                    db.session.commit()
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
        return jsonify({"status": "success", "message": "new story poi added to existing story"})
    else:
        return jsonify({"status": "failed", "message": "POST request only"})
#Added this functionality to the /stories endpoint, so no need for it
#adds a new story name aka stor

@app.route('/stories/<story_id>', methods=['PUT'])
# @login_required  
def story_name_edit(id):
    if request.method == "PUT":
        try:
            s = StoryNames.query.get(id)
            if s:
                json_dict = json.loads(request.data)
                s.story_name = json_dict["story_name"]
                db.session.commit()
        except Exception as ex:
            raise InvalidUsage('Error: ' + str(ex), status_code=404)
            return jsonify({"status": "success", "message": "editted story name"})
    else:
        return jsonify({"status": "failed", "message": "POST request only"})

