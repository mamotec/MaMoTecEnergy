from sqlalchemy import Column, String

from app.main.database.models.BaseModel import BaseModel


class Port(BaseModel):
    __tablename__ = "port"

    port_name = Column(String(256), nullable=False)
