#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')

    @property
    def cities(self):
        """getter attribute to show FileStorge relationship
        between city and state"""
        if type(storage).__name__ == 'FileStorage':
            from models import storage
            from models.city import City
            cities = storage.all(City)
            state_city = {}
            for k, v in cities.items():
                if self.id == v.state_id:
                    state_city[k] = v
            return state_city
        else:
            return State.cities
