from sqlalchemy import Column, Integer, String

from app.main.database.models.BaseModel import BaseModel


class Register(BaseModel):
    """
    Model for holding register´s
    """

    __tablename__ = "register"

    address = Column(String, index=True, nullable=False)
    translation = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
