 
import os
import unittest
from flask import jsonify
from api import app, db
from flask import Flask, request
from api.models import PointsOfInterest, AdditionalLinks, Content, User, Maps, InvalidUsage, StoryNames, Stories
from datetime import date
import requests
from flask import jsonify
import json

poi_add_json_1 = {
  "name": "Aria Bot 1",
  "map_by_year": "2017",
  "year": "2016",
  "month": "1",
  "day": "1",
  "info": "Test info",
  "x_coor": "25",
  "y_coor": "25",
  "additional_links": [
    {
        "url": "test1.url.com"
    },
    {
        "url": "test2.url.com"
    }
  ],
  "content": [
    {
        "content_url": "test3.url.com",
        "caption": "test caption"
    }
]}

poi_add_json_2 = {
  "name": "Aria Bot 2",
  "map_by_year": "2016",
  "year": "2016",
  "month": "1",
  "day": "1",
  "info": "Test info",
  "x_coor": "25",
  "y_coor": "25",
  "additional_links": [
    {
        "url": "test1.url.com"
    },
    {
        "url": "test2.url.com"
    }
  ],
  "content": [
    {
        "content_url": "test3.url.com",
        "caption": "test caption"
    }
]}


def clear_database():
        PointsOfInterest.query.delete()
        Content.query.delete()
        AdditionalLinks.query.delete()
        StoryNames.query.delete()
        Stories.query.delete()
        Maps.query.delete()
        db.session.commit()


class PointsOfInterestsTests(unittest.TestCase):

    def test_story(self):
        clear_database()
        requests.post('http://127.0.0.1:5000/pois', data=json.dumps(poi_add_json_1))
        data = requests.get('http://127.0.0.1:5000/pois')
        self.assertEqual(len(data.json()['data']),1)
        self.assertEqual(data.json()['data'][0]['name'],"Aria Bot 1")
        self.assertEqual(data.json()['data'][0]['map_by_year'],2017)
        self.assertEqual(data.json()['data'][0]['event_info'],"Test info")
        self.assertEqual(data.json()['data'][0]['date'],'Fri, 01 Jan 2016 00:00:00 GMT')
        self.assertEqual(data.json()['data'][0]['x_coord'],25)
        self.assertEqual(data.json()['data'][0]['y_coord'],25)
        self.assertEqual(data.json()['data'][0]['additional_links'][0]['url'],"test1.url.com")
        self.assertEqual(data.json()['data'][0]['additional_links'][1]['url'],"test2.url.com")
        self.assertEqual(data.json()['data'][0]['content'][0]['content_url'],"test3.url.com")
        self.assertEqual(data.json()['data'][0]['content'][0]['caption'],"test caption")

        requests.post('http://127.0.0.1:5000/pois', data=json.dumps(poi_add_json_2))
        data2 = requests.get('http://127.0.0.1:5000/pois')
        self.assertEqual(len(data2.json()['data']),2)
        self.assertEqual(data2.json()['data'][1]['name'],"Aria Bot 2")
        self.assertEqual(data2.json()['data'][1]['map_by_year'],2016)
        self.assertEqual(data2.json()['data'][1]['event_info'],"Test info")
        self.assertEqual(data2.json()['data'][1]['date'],'Fri, 01 Jan 2016 00:00:00 GMT')
        self.assertEqual(data2.json()['data'][1]['x_coord'],25)
        self.assertEqual(data2.json()['data'][1]['y_coord'],25)
        self.assertEqual(data2.json()['data'][1]['additional_links'][0]['url'],"test1.url.com")
        self.assertEqual(data2.json()['data'][1]['additional_links'][1]['url'],"test2.url.com")
        self.assertEqual(data2.json()['data'][1]['content'][0]['content_url'],"test3.url.com")
        self.assertEqual(data2.json()['data'][1]['content'][0]['caption'],"test caption")

        story = {
        "story_name": "Arias"
        }

        requests.post('http://127.0.0.1:5000/stories', data=json.dumps(story))
        story_data = requests.get('http://127.0.0.1:5000/stories')
        self.assertEqual(len(data.json()['data']),1)
        self.assertEqual(story_data.json()['data'][0]['story_name'],"Arias")

        story_id = story_data.json()['data'][0]['id']
        poi = data2.json()['data'][0]['id']

        add_poi_json = {
            "input_story_name_id": str(story_id),
            "input_poi_id": str(poi)
        }

        requests.post('http://127.0.0.1:5000/stories/add', data=json.dumps(add_poi_json))
        stories = requests.get('http://127.0.0.1:5000/stories/' + str(story_id) )
        self.assertEqual(stories.status_code,200)
        self.assertEqual(stories.json()['story_name'],"Arias")
        self.assertEqual(stories.json()['pois'][0]['name'],"Aria Bot 1")

        poi = data2.json()['data'][1]['id']

        add_poi_json = {
            "input_story_name_id": str(story_id),
            "input_poi_id": str(poi)
        }

        requests.post('http://127.0.0.1:5000/stories/add', data=json.dumps(add_poi_json))
        stories = requests.get('http://127.0.0.1:5000/stories/' + str(story_id) )
        self.assertEqual(stories.status_code,200)
        self.assertEqual(stories.json()['story_name'],"Arias")
        self.assertEqual(stories.json()['pois'][1]['name'],"Aria Bot 2")

        new_story = {
            "story_name": "More Arias"
        }
        story_id = story_data.json()['data'][0]['id']

        r = requests.put('http://127.0.0.1:5000/stories/' + str(story_id),data=json.dumps(new_story)  )
        # self.assertEqual(r.status_code,200)
        # stories = requests.get('http://127.0.0.1:5000/stories/' + str(story_id) )
        # self.assertEqual(stories.status_code,200)
        # self.assertEqual(stories.json()['story_name'],"More Arias")

# /stories/<story_id>

        


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PointsOfInterestsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
