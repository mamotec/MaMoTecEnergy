from fastapi import Depends
from sqlalchemy.orm import Session

from app.main.database.db import get_session
from app.main.services import RegisterService


def get_registers_service(db_session: Session = Depends(get_session)) -> RegisterService:
    return RegisterService(db_session)


__all__ = ("get_registers_service",)
