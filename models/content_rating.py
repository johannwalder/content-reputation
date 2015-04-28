#!usr/bin/python

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base import Base
from rating import Rating
from content_type import ContentType

class ContentRating(Base):
    """Contains the different results of rated content"""
    __tablename__ = 'content_rating'
    id = Column(Integer, primary_key=True)
    # location saves the URL or path of the content based on the ContentType
    location = Column(String(2048), unique=False)
    rating_id = Column(Integer, ForeignKey('rating.id'))
    content_type_id = Column(Integer, ForeignKey('content_type.id'))
    rating = relationship("Rating")
    contentType = relationship("ContentType")

    def serialize(self):
        return {        
            'id': self.id, 
            'location': self.location,
            'rating_id': self.rating_id,
            'content_type_id': self.content_type_id   
        }

    def __init__(self, location, ratingId, contentTypeId):
        self.location = location
        self.rating_id = ratingId
        self.content_type_id = contentTypeId

    def __repr__(self):
        return '<Content Rating: Location: %s - Rating Id: %d - Content Type Id: %d >' % (self.location, self.rating_id, self.content_type_id)


