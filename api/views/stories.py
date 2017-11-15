from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest, StoryNames, Stories
import json
from flask import jsonify
from api.utils import serializeList
from sqlalchemy import func
mod = Blueprint('stories', __name__)

# Returns all story names aka stories
@app.route('/stories', methods=['GET', 'POST'])
def stories():
    if request.method == 'GET':
        try:
            return jsonify({'status': 'success', 'data': serializeList(StoryNames.query.all())})
        except Exception as ex:
            return jsonify({'status': 'failed', 'message': str(ex)})
    elif request.method == 'POST':
        try:
            json_dict = json.loads(request.data)
            story_added = StoryNames(
                story_name=json_dict['story_name'],
            )
            db.session.add(story_added)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Added new Story'})
        except Exception as ex:
            return jsonify({'status': 'failed', 'message': str(ex)})
    else:
        return jsonify({"status: ": "failed", "message: ": "Endpoint, /maps, needs a GET or POST request"})

# Returns all POIS for a specific Story Name aka story
@app.route('/stories/<id>', methods=['GET'])
def stories_get(id):
    try:
        arry = []
        stories = StoryNames.query.get(id).story_id
        if stories is None:
            return jsonify({'status':'failed','message':'Story Name with ' + id + " doesn't exist"})
        for story in stories:
            arry.append(PointsOfInterest.query.get(story.poi_id))
        ret_dict = {'story_name_id': id, 'story_name': StoryNames.query.get(id).story_name, 'pois': serializeList(arry)}
        return jsonify(ret_dict)
        # return jsonify({'status': 'success', 'data': serializeList((Stories.query.filter(func.lower(StoryNames.story_name)==func.lower(inputStoryName))))})
    except Exception as ex:
        return jsonify({'status': 'failed', 'message': str(ex)})

# adds a POI to an existing story name aka story, POI must exist!!!!
@app.route('/story_poi', methods=['POST'])
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
            return jsonify({"status": "failed", "message": str(ex)})
        return jsonify({"status": "success", "message": "new story poi added to existing story"})
    else:
        return jsonify({"status": "failed", "message": "POST request only"})


#Added this functionality to the /stories endpoint
#adds a new story name aka story
@app.route('/story', methods=["POST"])
def new_story():
    try:
        json_dict = json.loads(request.data)
        story_added = StoryNames(
            story_name=json_dict['story_name'],
        )
        db.session.add(story_added)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Added new Story'})
    except Exception as ex:
        return jsonify({'status': 'failed', 'message': str(ex)})
