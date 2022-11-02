#!/usr/bin/python3
""" project class """

from models import Base
from models.core import Core
from sqlalchemy import Column, Integer, String, DateTime, Text


class Project(Core, Base):
    """ class for project """
    __tablename__ = 'project'
    name = Column(String(60))
    description = Column(Text)
    start_date = Column(DateTime)
    duration = Column(Integer)
    weight = Column(Integer)
    parent = Column(String(60))
