from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from models.database import Database
db = Database()
