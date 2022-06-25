#!/usr/bin/python3
""" core class """
from datetime import datetime
from uuid import uuid4
import models
from sqlalchemy import Column, String
Base = models.Base


class Core:
    """ core class to allow inheritance """
    id = Column(String(60), primary_key=True)

    def __init__(self, *args, **kwargs):
        """Initialization of core"""
        self.__db = models.db
        if kwargs:
            if 'id' not in kwargs.keys():
                id = str(uuid4())
                setattr(self, 'id', id)
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """ saves the current object to database """
        self.__db.commit()

    def delete(self):
        """delete the current instance from the storage"""
        self.__db.delete(self)

    @classmethod
    def get(cls, id):
        ''' fetch an object using its id '''
        return models.db.get(cls.__name__, id)

    @classmethod
    def all(cls):
        ''' return all instances of the class as list '''
        return models.db.all(cls.__name__)
