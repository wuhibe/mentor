from models import Base
from models.core import Core
from sqlalchemy import Column, Integer, String, DateTime


class Project(Core, Base):
    """ class for project """
    __tablename__ = 'project'
    name = Column(String(60), nullable=False)
    start_date = Column(DateTime, nullable=False)
    duration = Column(Integer)
    weight = Column(Integer)
