from dataclasses import dataclass

from app.main.dataclass.register.RegisterType import RegisterType


@dataclass
class RegisterBase:
    register_name: str
    type: RegisterType
    address: int
    unit: int
