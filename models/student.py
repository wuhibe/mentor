#!/usr/bin/python3
""" student class """

from models import Base
import models
from models.core import Core
from sqlalchemy import Column, String, DateTime
from app import login, db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Student(Core, Base, UserMixin, db.Model):
    """ class for student """
    __tablename__ = 'student'
    start_date = Column(DateTime)
    email = Column(String(128), unique=True)
    github = Column(String(128), unique=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    def set_password(self, password):
        """ set student password """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """ check student password """
        return check_password_hash(self.password, password)

    @classmethod
    def get_by_email(cls, email):
        ''' fetch an object from its classname and its id '''
        all = models.db.all('Student')
        for obj in all:
            if (obj.email == email):
                return obj
        return None

    def save(self):
        """ saves the current object to database """
        models.db.add(self)
        models.db.commit()


@login.user_loader
def load_user(id):
    """ method to load student id """
    return Student.query.get(id)
