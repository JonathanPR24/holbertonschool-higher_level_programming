#!/usr/bin/python3
"""Contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

class City(Base):
    """Class definition of a City"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __str__(self):
        """Return a string representation of the City object"""
        return "({}) {}".format(self.id, self.name)
