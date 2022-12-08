#!/usr/bin/python3
"""This module instantiates an object
 of class File OR DB storage"""
from os import environ

storage_type = environ.get('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

__all__ = ['place', 'city', 'amenity', 'state', 'review', 'user']
