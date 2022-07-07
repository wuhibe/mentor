from models import Base
import models
from models.core import Core
from sqlalchemy import Column, Integer, String, ForeignKey, Text


class Task(Core, Base):
    """ class for task """
    __tablename__ = 'task'
    pid = Column(String(60), ForeignKey('project.id'))
    name = Column(String(128))
    description = Column(Text)
    weight = Column(Integer)
    avg_denom = Column(Integer)
    output = Column(String(128))

    @classmethod
    def get_all_tasks(cls, pid):
        lst = models.db.all('Task')
        all = []
        for obj in lst:
            if obj.pid == pid:
                all.append(obj)
        return all
