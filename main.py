"""
Start of the MaMoTecEnergy Backend
"""
from fastapi import FastAPI

import app.modbus.modbus_management as mod_management
from app.database.db import SessionLocal
from app.modbus.read_modbus import read_holding_registers

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup():
    # Modbus Connection
    mod_management.connect_to_bus()
    get_db()


@app.get("/")
def root():
    result = read_holding_registers().registers
    print(result)
    return {tuple(result)}
