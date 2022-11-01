from fastapi import Depends
from sqlalchemy.orm import Session

from .register_service import RegisterService
from .. import get_session


def get_registers_service(db_session: Session = Depends(get_session)) -> RegisterService:
    return RegisterService(db_session)


__all__ = ("get_registers_service",)
