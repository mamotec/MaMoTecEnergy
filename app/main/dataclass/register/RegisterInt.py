from dataclasses import dataclass

from app.main.dataclass.register.RegisterBase import RegisterBase


@dataclass
class RegisterInt(RegisterBase):
    value: int
