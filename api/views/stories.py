from api import app
from flask import Blueprint, request
from .. import db
from api.models import PointsOfInterest,StoryNames, Stories
import json
from flask import jsonify
from api.utils import serializeList
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

#adds a POI to an existing story, POI must exist!!!!
@app.route('/story_poi/', methods=['POST'])
def story_point():
    if request.method == "POST":
        json_dict = json.loads(request.data)
        try:
            storynames = StoryNames.query.get(json_dict["input_story_name_id"]) #check if it is empty later
            storynames.story_id.append(Stories()) #add new Stories() to storynames
            
            db.session.commit()
            #get poi and add the same story to it
            poi = PointsOfInterest.query.filter(PointsOfInterest.id==json_dict["input_poi_id"])[0]
            poi.stories.append(storynames.story_id[-1]) #gets last index, which is the Stories() that was just added
            db.session.commit()
        except Exception as ex:
            return jsonify({"status": "failed", "message": str(ex)})
        return "new story poi added to existing story"
    else:
        return jsonify({"status": "failed", "message": "POST request only"})

#adds a new story
@app.route('/story', methods=["POST"])
def new_story():
    json_dict = json.loads(request.data)
    story_added = StoryNames(
        story_name = json_dict['story_name'],
    )
    db.session.add(story_added)
    db.session.commit()
    return "new story added" 
