"""
Schema for register´s
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RegisterBase(BaseModel):
    """
    This is the description of the GET Model of Register
    """
    id: int
    address: str
    translation: str
    value: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class RegisterCreate(RegisterBase):
    pass


class RegisterUpdate(RegisterBase):
    pass
