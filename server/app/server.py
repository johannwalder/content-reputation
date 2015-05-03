#!flask/bin/python

from flask import Flask, jsonify, abort, make_response
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.sqlalchemy import SQLAlchemy

import sys
import os
sys.path.append(os.path.abspath('../models'))
sys.path.append(os.path.abspath('../database'))

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from base import Base
from rating import Rating
from content_type import ContentType
from content_rating import ContentRating
import dev_settings

engine = create_engine(URL(**dev_settings.DATABASE))
Session = sessionmaker(bind=engine)

session = Session()

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()

rating_fields = {
    'id': fields.Integer,
    'level': fields.String,
    'terms': fields.String
}

class RatingListAPI(Resource):
    def __init__(self):
        super(RatingListAPI, self).__init__()

    def get(self):
        ratings = session.query(Rating).all()
        return {'ratings': [marshal(rating, rating_fields) for rating in ratings]}

api.add_resource(RatingListAPI, '/api/v1.0/ratings', endpoint='ratings')
