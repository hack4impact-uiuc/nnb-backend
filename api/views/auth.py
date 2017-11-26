from api import app
from flask import Blueprint, request
from api.models import Users
from .. import db
import json
from api.utils import serializeList
from flask import jsonify
import requests
import time
from datetime import date

mod = Blueprint('auth', __name__)

# sign up and get token - might be redundant
@app.route('/signup', methods=['POST'])
def register():
    if request.method == 'POST':
        try:
            json_dict = json.loads(request.data)
            #TODO: check whether email is legit
            #TODO: randomly generate a token, and make password private
            created_user = Users(email=json_dict["email"],
                password=json_dict["password"], token="randomtoken")
            db.session.add(created_user)
            db.session.commit()
        except Exception as ex:
            return jsonify({'status': 'failed', 'message': str(ex)})
    return jsonify({'status':'success', 'token':'136458476182639'})

# login and get token
@app.route('/auth', methods=['POST'])
def auth():
    if request.method == 'POST':
        try:
            json_dict = json.loads(request.data)
            #TODO: check whether email is legit
            filter_array = Users.query.filter(Users.email==json_dict["email"])
            if len(filter_array) != 0:
                user = filter_array[0]
                if json_dict["password"] == user.password:
                    # TODO : NEED A BETTER WAY TO DO THIS
                    return jsonify({'status':'success','token':'randomtoken'}) 
                else:
                    return jsonify({'status':'failed','message':'incorrect email/password combination'})
            else:
                # creates a new user if user doesn't exist
                #TODO: randomly generate a token, and make password private
                created_user = Users(email=json_dict["email"],
                    password=json_dict["password"], token="randomtoken")
                db.session.add(created_user)
                db.session.commit()
                return jsonify({'status':'success','token':created_user.token}) # change how to get token
        except Exception as ex:
            return jsonify({'status': 'failed', 'message': str(ex)})
    return jsonify({'status':'failed','message':"couldn't create/get user"})

# logout provided account info with token
@app.route('/logout',methods=['POST'])
def logout():    
    return jsonify({'status':'success','message':'successfully logged out'})
