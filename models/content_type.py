#!usr/bin/python

from sqlalchemy import Column, String, Integer
 
from base import Base

class ContentType(Base):
    """Contains the different content types (web page, file)"""
    __tablename__ = 'content_type'
    id = Column(Integer, primary_key=True)
    content_type = Column(String(80), unique=True)

    def serialize(self):
        return {        
            'id': self.id, 
            'content_type': self.content_type      
        }

    def __init__(self, contentType):
        self.content_type = contentType

    def __repr__(self):
        return '<ContentType: Type: %s>' % (self.content_type)
