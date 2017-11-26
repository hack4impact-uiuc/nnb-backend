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
from flask_login import LoginManager, login_required, login_user, logout_user
from passlib.apps import custom_app_context as pwd_context
from api.models import PointsOfInterest, AdditionalLinks, Content, User

mod = Blueprint('auth', __name__)

@app.route('/login', methods = ['POST'])
def new_user():
    json_dict = json.loads(request.data)
    username = json_dict['username']
    if User.query.filter_by(username = username).first() is not None:
        if User.query.filter(User.username==json_dict['username']).first().verify_password(json_dict['password']):
            user = User.query.filter(User.username==json_dict['username']).first()
            login_user(user)
            db.session.commit()
            return jsonify({'status':'success', 'username': json_dict['username']})
        else:
            return jsonify({'status':'failed', 'username': json_dict['username']})
    user = User(username = username, password_hash=pwd_context.encrypt(json_dict['password']))
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return jsonify({'status':'success', 'username': user.username})

@login_required
@app.route('/logout', methods = ['POST'])
def logout():
    logout_user()
    db.session.commit()
    return jsonify({'status':'suceeded', 'message': "logged out"})
