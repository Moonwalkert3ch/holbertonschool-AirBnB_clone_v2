#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade='delete')

    @property
    def cities(self):
            """Retrieve list of related cities"""
            related_city = []
            for cities in list(models.storage.all(City).values()):
                if cities.state_id == self.id:
                    related_city.append(cities)
            return related_city