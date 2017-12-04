 
import os
import unittest
from flask import jsonify
from api import app, db
from flask import Flask, request

import requests
from flask import jsonify

r = requests.get('http://127.0.0.1:5000/pois')
print(r.json)
r = requests.post('http://127.0.0.1:5000/pois',json="")




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
 

# if __name__ == "__main__":
#     unittest.main()
