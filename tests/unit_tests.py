import os
import unittest
from flask import jsonify
from api import app, db
from flask import Flask, request

import requests
from flask import jsonify
import json
from api.models import 

poi_add_json = {
  "name": "Endpoint test",
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

map_add_json = {
    'image_url': 'url1.com',
    'year': '2016'
}
map_add_json2 = {
    'image_url': 'url2.com',
    'year': '2016'
}
dict2 = poi_add_json.copy()
dict3 = poi_add_json.copy()
dict2["name"] = "Endpoint test2"
dict3["name"] = "Endpoint test3"


def post_with_json_body(url, j):
    r = requests.post('http://127.0.0.1:5000' + url, data=j)
    return r

class PointsOfInterestsTests(unittest.TestCase):

    def test_add_poi(self):
        r = requests.post('http://127.0.0.1:5000/pois', data=json.dumps(poi_add_json))
        self.assertEqual(r.status_code,200)
        json_dict = r.json()
        print(json_dict)
        self.assertEqual(json_dict["status"], "success")
    def test_add_multiple_poi(self):
        
        r = requests.post('http://127.0.0.1:5000/pois', data=json.dumps(poi_add_json))
        r2 = requests.post('http://127.0.0.1:5000/pois', data=json.dumps(poi_add_json))
        self.assertEqual(r.status_code,200)
        self.assertEqual(r2.status_code,200)
    # def get_poi_with_id(self):


class Maps(unittest.TestCase):

    def test_add_map(self):
        r = post_with_json_body('/maps', map_add_json)
        r2 = post_with_json_body('/maps', map_add_json2)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r2.status_code,200)
        json_dict = r.json()
        json_dict2 = r2.json()
        self.assertEqual(json_dict["message"], 'successfully added maps and year')
        self.assertEqual(json_dict2["message"], 'successfully added maps and year')
        

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PointsOfInterestsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
