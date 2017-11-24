from api import app
from flask import Blueprint, request
from api.models import PointsOfInterest
from .. import db
import json
from api.utils import serializeList
from flask import jsonify
import requests
import time
from datetime import date

mod = Blueprint('auth', __name__)

# sign up and get token
@app.route('/signup', methods=['POST'])
def register():
    return jsonify({'status':'success', 'token':'136458476182639'})

# login and get token
@app.route('/auth', methods=['POST'])
def auth():
    return jsonify({'status':'success','token':'136458476182639'})

# logout provided account info with token
@app.route('/logout',methods=['POST'])
def logout():    
    return jsonify({'status':'success','message':'successfully logged out'})
