#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


s = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')

    if s != 'db':
        @property
        def cities(self):
            """getter attribute to show FileStorge relationship
            between city and state"""
            from models import storage
            from models.city import City
            cities = storage.all(City)
            state_city = []
            for k, v in cities.items():
                if self.id == v.state_id:
                    state_city.append(v)
            return state_city
