from api import app
from flask import Blueprint, request
from api.models import User
from .. import db
import json
from api.utils import serializeList
from flask import jsonify
import requests
import time
from datetime import date
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user 
from passlib.apps import custom_app_context as pwd_context

mod = Blueprint('auth', __name__)

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


@app.route('/new_user', methods = ['POST'])
def new_user():
    json_dict = json.loads(request.data)
    username = json_dict['username']
    if User.query.filter_by(username = username).first() is not None:
        return jsonify({'status':'failed', 'username': json_dict['username']})
    user = User(username = username, password_hash=pwd_context.encrypt(json_dict['password']))
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return jsonify({'status':'success', 'username': user.username})

@app.route('/user', methods = ['POST'])
def user():
    json_dict = json.loads(request.data)
    if username in User.query.all():
        if User.query.filter(User.username==json_dict['username']).first().verify_password(json_dict['password']):
            # login_user(user)
            return jsonify({'status':'success', 'username': json_dict['username']})
    return jsonify({'status':'failed', 'username': json_dict['username']})

@app.route('/user', methods = ['GET'])
def users():
    return str(len(User.query.all()))
    return "HI"
