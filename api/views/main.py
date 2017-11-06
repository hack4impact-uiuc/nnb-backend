from api import app
from flask import Blueprint, request
from api.models import PointsOfInterest

mod = Blueprint('main', __name__)

# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# import os

# uri = os.environ.get('DATABASE_URL', 'postgresql://nbb:password@127.0.0.1:5432/nbb_db')
# engine = create_enggine(uri, convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
# 					 autoflush=False,
# 					 bind=engine))
# Base = declarative_base()
# Base.query = db_session.query_property()

# def init_db():
# #   import Flasktest.models

#   Base.metadata.create_all(bind=engine)


@app.route('/')
def mainpage():
    return '<h1>NNB Home Page</h1>'

# this doesnt work 
@app.route('/name')
def name():
    # result = PointsOfInterest(
    #     name="aria"
    # )
    # init_db()
    PointsOfInterest.query.all()
    return"HI"

@app.route('/name3')
def name3():
    # result = PointsOfInterest(
    #     name="aria"
    # )
    # PointsOfInterest.query.all()
    return"HI"
