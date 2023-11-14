#!/usr/bin/python3
"""Defines the State class"""
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ Represents State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Retrieve list of related cities"""
            related_city = []
            for cities in list(models.storage.all(City).values()):
                if cities.state_id == self.id:
                    related_city.append(cities)
            return related_city