import os
import unittest
from flask import jsonify
from api import app, db
from flask import Flask, request

import requests
from flask import jsonify
import json
from api.models import PointsOfInterest, AdditionalLinks, Content, User, Maps, InvalidUsage, StoryNames, Stories

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
    r = requests.post('http://127.0.0.1:5000' + url, data=json.dumps(j))
    return r

def assert_status_good(obj, req):
    obj.assertEqual(req.status_code,200)

class MapsTest(unittest.TestCase):

    def test_add_map(self):
        # r = requests.post('http://127.0.0.1:5000/maps',data=json.dumps(map_add_json))
        r = post_with_json_body('/maps', map_add_json)
        r2 = post_with_json_body('/maps', map_add_json2)
        assert_status_good(self,r)
        assert_status_good(self,r2)
        json_dict = r.json()
        json_dict2 = r2.json()
        self.assertEqual(json_dict["message"], 'successfully added maps and year')
        self.assertEqual(json_dict2["message"], 'successfully added maps and year')
        elm2 = Maps.query.all()[-1]
        self.assertEqual(elm2.image_url,map_add_json2["image_url"])
        self.assertEqual(elm2.year,2016)

    def test_poi_in_map(self):
        r = post_with_json_body('/maps', map_add_json)
        r2 = post_with_json_body('/maps', map_add_json2)
        poi_r = post_with_json_body('/pois', poi_add_json)
        assert_status_good(self,r)
        assert_status_good(self,r2)
        assert_status_good(self,poi_r)
        year_req = requests.get('http://127.0.0.1:5000/maps/years/2016')
        assert_status_good(self,year_req)
        json_dict = year_req.json()
        self.assertTrue(json_dict["data"])
        self.assertTrue(len(json_dict["data"]["map"]) == 1)
        self.assertIsNotNone(json_dict["data"]["pois"])

    def test_delete_map(self):
        r = post_with_json_body('/maps', map_add_json)
        assert_status_good(self, r)
        elm = Maps.query.all()[-1]
        print('http://127.0.0.1:5000/maps/' +str(elm.id))
        r = requests.delete('http://127.0.0.1:5000/maps/' +str(elm.id))
        assert_status_good(self, r)
        json_dict = r.json()
        self.assertEqual(json_dict["message"], 'successfully deleted')
        r2 = requests.delete('http://127.0.0.1:5000/maps/' + str(elm.id))
        self.assertEqual(r2.status_code, 404)
        



if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(MapsTest)
    unittest.TextTestRunner(verbosity=3).run(suite)
