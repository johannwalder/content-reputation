#!usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import sys
import os
sys.path.append(os.path.abspath('../models'))

import dev_settings
from base import Base
from rating import Rating
from content_type import ContentType
from content_rating import ContentRating
 
#engine = create_engine('postgresql://username:password@localhost/databasename')
#engine = create_engine(URL(**settings.DATABASE))
engine = create_engine(URL(**dev_settings.DATABASE))
 
Base.metadata.create_all(engine)
