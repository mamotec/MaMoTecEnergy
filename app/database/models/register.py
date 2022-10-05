"""
Model for holding register´s
"""
from sqlalchemy import Column, Integer, String

from app.database.db import Base


class Register(Base):
    __tablename__ = "register"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(Integer, index=True, nullable=False)
    translation = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
