#!/usr/bin/python3
""" check class """

from models import Base
from models.core import Core
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class Check(Core, Base):
    """ class for check """
    __tablename__ = 'check'
    tid = Column(String(60), ForeignKey('task.id'), nullable=False)
    case = Column(String(640))
    solution = Column(String(640))
    weight = Column(Integer)

    def get_all_checks(self, tid):
        lst = self.all()
        all = []
        for obj in lst:
            if obj.tid == tid:
                all.append(obj)
        return all
