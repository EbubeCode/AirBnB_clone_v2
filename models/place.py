#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False,)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref='place', cascade='delete')
    amenity_ids = []

    @property
    def reviews(self):
        """getter attribute to show FileStorge relationship
        between place and reviews"""
        if type(storage).__name__ == 'FileStorage':
            from models import storage
            from models.review import Review
            reviews = storage.all(Review)
            p_revs = []
            for k, v in reviews.items():
                if self.id == v.place_id:
                    p_revs.append(v)
            return p_revs
        else:
            return Place.reviews
