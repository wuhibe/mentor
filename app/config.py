#!/usr/bin/python3
""" module for config class """

import os
from uuid import uuid4


class Config(object):
    """ config class """
    host = os.getenv('HOST_USR')
    pwd = os.getenv('HOST_PWD')
    SECRET_KEY = str(uuid4())
    s = 'mysql+mysqldb://{}:{}@localhost/mentor'.format(host, pwd)
    SQLALCHEMY_DATABASE_URI = s
    SQLALCHEMY_TRACK_MODIFICATIONS = False
