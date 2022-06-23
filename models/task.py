from models import Base
from models.core import Core
from sqlalchemy import Column, Integer, String, ForeignKey


class Task(Core, Base):
    """ class for task """
    __tablename__ = 'task'
    pid = Column(String(60), ForeignKey('project.id'), nullable=False)
    name = Column(String(128), nullable=False)
    weight = Column(Integer)
    no_checks = Column(Integer)

    def get_all_tasks(self, pid):
        lst = self.all()
        all = []
        for obj in lst:
            if obj.pid == pid:
                all.append(obj)
        return all
