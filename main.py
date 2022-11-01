"""
Start of the MaMoTecEnergy Backend
"""
from fastapi import FastAPI

import app.main.modbus.modbus_management as mod_management
from app.main.modbus.read_modbus import read_holding_registers
from app.main.router import register

app = FastAPI()


@app.on_event("startup")
def startup():
    # Modbus Connection
    mod_management.connect_to_bus()


app.include_router(register.router)


@app.get("/")
def root():
    result = read_holding_registers().registers
    print(result)
    return {tuple(result)}
