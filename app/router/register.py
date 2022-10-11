from fastapi import APIRouter
from app.database.models import register
from app.database.db import SessionLocal

router = APIRouter()
session = SessionLocal()


@router.get("/register")
def get_registers():
    registers = session.query(register.Register).all()
    session.close()
    return registers
