#!usr/bin/python

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
 
from base import Base

class ContentType(Base):
    """Contains the different content types (web page, file)"""
    __tablename__ = 'content_type'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), unique=True)
    contentratings = relationship('ContentRating',backref='contentType',lazy='dynamic')

    def serialize(self):
        return {        
            'id': self.id, 
            'title': self.title      
        }

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self):
        return '<ContentType: Type: %s>' % (self.title)
