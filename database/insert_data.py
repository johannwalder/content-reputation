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

# add default items to content type table
session.add_all([
    ContentType(id=1, contentType='Web Page'),
    ContentType(id=2, contentType='File')])

# add default items to rating table
session.add_all([
    Rating(id=1, level='Rating Level 1', terms='hello,world'),
    Rating(id=2, level='Rating Level 2', terms='12345,test1,test2'),
    Rating(id=3, level='Rating Level 3', terms='abc')])

session.commit()
