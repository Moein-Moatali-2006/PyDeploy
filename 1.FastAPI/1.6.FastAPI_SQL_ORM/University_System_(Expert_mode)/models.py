from sqlalchemy import Column, Integer, String
from .database import Base

class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True, nullable=True)
    secret_name = Column(String, nullable=False)
