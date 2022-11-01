import sqlalchemy.sql.functions as func
from sqlalchemy import Column, Integer, DateTime

from app.main.database.db import Base


class BaseModel(Base):
    """
    Base Model for general Information which every model should inherit.
    """

    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.current_timestamp)
