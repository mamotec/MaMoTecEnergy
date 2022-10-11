"""
Schema for register´s
"""
from pydantic import BaseModel

class RegisterGet(BaseModel):
    """
    This is the description of the GET Model of Register
    """

    address: str
    translation: str
    value: int
