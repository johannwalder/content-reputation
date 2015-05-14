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
    'terms': fields.String,
    'uri': fields.Url('rating')
}

class RatingListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('level', type = str, required = True,
             help = 'No rating level provided', location = 'json')
        self.reqparse.add_argument('terms', type = str, required = True,
             help = 'No rating terms provided', location = 'json')
        super(RatingListAPI, self).__init__()

    def get(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('limit', type = int, default=10,
             location = 'args')
        self.reqparse.add_argument('offset', type = int, default=0,
             location = 'args')

        args = self.reqparse.parse_args()

        limit = args.get('limit')
        offset = args.get('offset')
        ratings = session.query(Rating).limit(limit).offset(offset).all()
        return {'ratings': [marshal(rating, rating_fields) for rating in ratings]}


class RatingAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('level', type = str, required = True,
             help = 'No rating level provided', location = 'json')
        self.reqparse.add_argument('terms', type = str, required = True,
             help = 'No rating terms provided', location = 'json')
        super(RatingAPI, self).__init__()

    def get(self, id):
        rating = session.query(Rating).filter(Rating.id == id).all()
        if len(rating) == 0: 
            abort(404) 
        return {'rating': marshal(rating[0], rating_fields)} 

api.add_resource(RatingListAPI, '/api/v1.0/ratings', endpoint='ratings')
api.add_resource(RatingAPI, '/api/v1.0/ratings/<int:id>', endpoint = 'rating')
