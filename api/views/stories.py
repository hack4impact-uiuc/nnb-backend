from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest
import json
from flask import jsonify
from api.utils import serializeList
from api.models import StoryNames, Stories
from sqlalchemy import func
mod = Blueprint('stories', __name__)

#Returns all story names
@app.route('/stories', methods=['GET'])
def stories():
    return jsonify(serializeList(StoryNames.query.all()))

#Returns all POIS for a specific Story
@app.route('/stories/<inputStoryName>', methods=['GET'])
def stories_get(inputStoryName):
    return jsonify(serializeList((Stories.query.filter(func.lower(StoryNames.story_name)==func.lower(inputStoryName)))))

#adds a POI to an existing story
@app.route('/story_poi/', methods=['POST'])
def story_point():
    if request.method == 'POST':
        json_dict = json.loads(request.data)
        story_added = Stories(
            story_uuid = input_story_uuid,
            poi_id = input_poi_id
        )
        db.session.add(story_added)
        db.session.commit()
        return "new story poi added to existing story"

#adds a new story

@app.route('/story', methods=["POST"])
def new_story():
    json_dict = json.loads(request.data)
    story_added = StoryNames(
        id = 1,
        story_name =  json_dict['story_name'],
        story_id = json_dict['story_id'],
    )
    db.session.add(story_added)
    db.session.commit()
    return "new story added"