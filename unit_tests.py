 
import os
import unittest
from flask import jsonify
from api import app, db
from flask import Flask, request

import requests
from flask import jsonify
import json

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
dict2 = poi_add_json.copy()
dict3 = poi_add_json.copy()
dict2["name"] = "Endpoint test2"
dict3["name"] = "Endpoint test3"


r = requests.get('http://127.0.0.1:5000/pois')

class PointsOfInterestsTests(unittest.TestCase):

    def test_add_poi(self):
        r = requests.post('http://127.0.0.1:5000/pois', data=json.dumps(poi_add_json))
        self.assertEqual(r.status_code,200)
        json_dict = r.json()
    def test_add_multiple_poi(self):
        
        r = requests.post('http://127.0.0.1:5000/pois', data=json.dumps(poi_add_json))
        r = requests.post('http://127.0.0.1:5000/pois', data=json.dumps(poi_add_json))
    # def get_poi_with_id(self):
      

# app = Flask(__name__)
# with app.app_context():
#     r = requests.post(url = "http://127.0.0.1:5000/",params=jsonify({'username':'admin', 'password': 'admin'}))
 
# class BasicTests(unittest.TestCase):
#     def setUp(self):
#         app.config['TESTING'] = True
#         app.config['WTF_CSRF_ENABLED'] = False
#         app.config['DEBUG'] = False
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nbb:password@127.0.0.1:5432/nbb_db'
#         self.app = app.test_client()
       
#         db.drop_all()
#         db.create_all()
 
#         # Disable sending emails during unit testing
#         # mail.init_app(app)
#         self.assertEqual(app.debug, False)
 
#     # executed after each test
#     def tearDown(self):
#         pass
 

 
#     def test_main_page(self):
#         response = self.app.get('/', follow_redirects=True)
#         self.assertEqual(response.status_code, 200)
#         result = self.app.get('/pois')
#         client = app.test_client()
#         # client.post('/signup', 
#         #     jsonify({'username':'admin', 'password': 'admin'})
#         # )
#         # client.post('/signup', data=dict(
#         #     username="admin",
#         #     password="admin"
#         # ), follow_redirects=True)

#     def register(self, username, password):
#         return "HI"
#         return self.app.post(
#         '/signup',
#         data=dict(username=username, password=password),
#         follow_redirects=True
#     )

#     def login(self, username, password):
#         return self.app.post(
#             '/login',
#             data=dict(username=username, password=password),
#             follow_redirects=True
#         )
 
#     def logout(self):
#         return self.app.get(
#             '/logout',
#             follow_redirects=True
#         )

#     def test_valid_user_registration(self):
#         response = self.register("patkennedy79@gmail.com", "FlaskIsAwesome")
#         # self.assertEqual(response.status_code, 200)
#         # self.assertIn(b'Thanks for registering!', response.data)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PointsOfInterestsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
