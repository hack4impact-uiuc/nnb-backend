 
import os
import unittest
from flask import jsonify
from api import app, db
from flask import Flask, request
from api.models import PointsOfInterest, AdditionalLinks, Content, User, Maps, InvalidUsage, StoryNames, Stories


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

    def test_add_poi(self):
        clear_database()
        requests.post('http://127.0.0.1:5000/pois', data=json.dumps(poi_add_json_1))
        data = requests.get('http://127.0.0.1:5000/pois')
        print(len(data.json()['data']) == 1)
        print(data.json()['data'][0]['name'] == "Aria Bot 1")
        




if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PointsOfInterestsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
