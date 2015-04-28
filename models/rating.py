#!usr/bin/python

from sqlalchemy import Column, String, Integer
 
from base import Base

class Rating(Base):
    """Contains the different rating levels of content"""
    __tablename__ = 'rating'
    id = Column(Integer, primary_key=True)
    level = Column(String(80), unique=True)
    terms = Column(String(2048), unique=True)

    def serialize(self):
        return {        
            'id': self.id, 
            'level': self.level,
            'terms': self.terms        
        }

    def __init__(self, id, level, terms):
        self.id = id
        self.level = level
        self.terms = terms

    def __repr__(self):
        return '<Rating: Level: %s - Terms: %s>' % (self.level, self.terms)
