from sqlalchemy import Column, Integer, Boolean, String
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,autoincrement=True)
    nombre = Column(String)
    username = Column(String)
    password = Column(String)