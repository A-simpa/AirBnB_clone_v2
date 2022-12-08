#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Table, String, Column
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
    	name = Column(String(128), nullable=False)
    else:
	name = ""
