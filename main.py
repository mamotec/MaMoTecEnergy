"""
Start of the MaMoTecEnergy Backend
"""
from fastapi import FastAPI

import app.main.modbus.ModbusManagement as mod_management
from app.main.modbus.ReadModbus import read_holding_registers

app = FastAPI()


@app.on_event("startup")
def startup():
    # Modbus Connection
    mod_management.connect_to_bus_on_startup()


@app.get("/read")
def root():
    result = read_holding_registers(0, 20, 1)
    print(result)
    return {tuple(result)}
