#!usr/bin/python

from sqlalchemy import Column, String, Integer, ForeignKey

from base import Base
from rating import Rating
from content_type import ContentType

class ContentRating(Base):
    """Contains the different results of rated content"""
    __tablename__ = 'content_rating'
    # location saves the URL or path of the content based on the ContentType
    location = Column(String(2048), unique=False)
    rating_id = Column(Integer, ForeignKey('rating.id'))
    content_type_id = Column(Integer, ForeignKey('content_type.id'))

    def serialize(self):
        return {        
            'id': self.id, 
            'location': self.location,
            'rating': self.rating.level,
            'contenttype': self.contenttype.title   
        }

    def __init__(self, location, rating, contentType):
        self.location = location
        self.rating = rating
        self.contentType = contentType

    def __repr__(self):
        return '<Content Rating: Location: %s - Rating Id: %d - Content Type Id: %d >' % (self.location, self.rating.level, self.contentType.Title)


