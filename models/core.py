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
            id = str(uuid4())
            setattr(self, 'id', id)
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        self.__db.add(self)
        self.__db.commit()

    def get(self, id):
        ''' fetch an object using its id '''
        return self.__db.get(self.__class__.__name__, id)

    def delete(self):
        """delete the current instance from the storage"""
        self.__db.delete(self)

    def all(self):
        ''' return all objects as s'''
        return self.__db.all(self.__class__.__name__)
