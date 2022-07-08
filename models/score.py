from models import Base
import models
from models.core import Core
from sqlalchemy import Column, Float, ForeignKey, String, Boolean


class Score(Core, Base):
    """ class for score """
    __tablename__ = 'score'
    sid = Column(String(60), ForeignKey('student.id'))
    pid = Column(String(60), ForeignKey('project.id'))
    tid = Column(String(60), ForeignKey('task.id'))
    cid = Column(String(60), ForeignKey('check.id'))
    pscore = Column(Float)
    tscore = Column(Float)
    ccheck = Column(Boolean)

    def save(self):
        """ saves the current object to database """
        models.db.add(self)
        models.db.commit()

    @classmethod
    def task_by_sid(cls, sid, tid):
        """ method to fetch task score by student """
        all = Score.all()
        for s in all:
            if s.sid == sid and s.tid == tid:
                return s
        return None

    @classmethod
    def all_tasks(cls, sid):
        """ method to fetch all task scores by student """
        all = Score.all()
        dct = {}
        for s in all:
            if s.sid == sid and s.tid is not None:
                dct[s.tid] = s.tscore
        return dct

    @classmethod
    def project_by_sid(cls, sid, pid):
        """ method to fetch project score by student """
        all = Score.all()
        lst = []
        for s in all:
            if s.sid == sid and s.pid == pid:
                lst.append(s)
        return lst
