from hashlib import md5
from models import Base
from models.core import Core
from sqlalchemy import Column, String, DateTime


class Student(Core, Base):
    """ class for student """
    __tablename__ = 'student'
    start_date = Column(DateTime, nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    github = Column(String(128), unique=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    def __setattr__(self, name, value) -> None:
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
