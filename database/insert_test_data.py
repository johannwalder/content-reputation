#!usr/bin/python

import sys
import os
sys.path.append(os.path.abspath('../models'))

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
import dev_settings
from base import Base
from rating import Rating
from content_type import ContentType
from content_rating import ContentRating

engine = create_engine(URL(**dev_settings.DATABASE))
Session = sessionmaker(bind=engine)

session = Session()

# add test items to rating table
session.add_all([
    ContentRating(location='http://some-url/test1.html', ratingId=1, contentTypeId=1),
    ContentRating(location='http://some-url/test2.html', ratingId=2, contentTypeId=1),
    ContentRating(location='http://some-url/test3.html', ratingId=1, contentTypeId=1),
    ContentRating(location='/home/user1/documents/test.foo', ratingId=1, contentTypeId=2),
    ContentRating(location='/home/user1/documents/hello.foo', ratingId=1, contentTypeId=2)])

session.commit()
