import os
from sqlalchemy import engine
from sqlalchemy.orm import scoped_session, sessionmaker
import models
from models.check import Check
from models.project import Project
from models.score import Score
from models.student import Student
from models.task import Task

Base = models.Base

classes = {'Student': Student, 'Task': Task, 'Project': Project,
           'Check': Check, 'Score': Score}


class Database:
    def __init__(self):
        host = os.getenv('HOST_USR')
        pwd = os.getenv('HOST_PWD')
        self.__engine = engine.create_engine(
                        'mysql+mysqldb://{}:{}@localhost/mentor'
                        .format(host, pwd))
        self.reload()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def add(self, obj):
        ''' add object to current session '''
        self.__session.add(obj)

    def all(self, clas):
        ''' all objects of type clas '''
        lst = []
        objs = self.__session.query(classes[clas]).all()
        for obj in objs:
            lst.append(obj)
        return lst

    def get(self, cls, id):
        ''' fetch an object from its classname and its id '''
        if cls not in classes.keys():
            return None
        all = self.all(cls)
        for obj in all:
            if (obj.id == id):
                return obj
        return None

    def commit(self):
        ''' commit session data to database '''
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
        self.commit()
