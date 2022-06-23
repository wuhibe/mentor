from models import Base
from models.core import Core
from sqlalchemy import Column, Float, ForeignKey, String, Boolean


class Score(Core, Base):
    """ class for score """
    __tablename__ = 'score'
    sid = Column(String(60), ForeignKey('student.id'), nullable=False)
    pid = Column(String(60), ForeignKey('project.id'))
    tid = Column(String(60), ForeignKey('task.id'))
    cid = Column(String(60), ForeignKey('check.id'))
    pscore = Column(Float)
    tscore = Column(Float)
    ccheck = Column(Boolean)
