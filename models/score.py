from models import Base
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

    @classmethod
    def task_by_sid(sid, tid):
        """ method to fetch task score by student """
        all = Score.all()
        lst = []
        for s in all:
            if s.sid == sid and s.tid == tid:
                lst.append(s)
        return lst

    @classmethod
    def project_by_sid(sid, pid):
        """ method to fetch project score by student """
        all = Score.all()
        lst = []
        for s in all:
            if s.sid == sid and s.pid == pid:
                lst.append(s)
        return lst
