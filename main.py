"""
Start of the MaMoTecEnergy Backend
"""
from fastapi import FastAPI

import app.main.modbus.ModbusManagement as mod_management
from app.main.dataclass.register.RegisterType import RegisterType
from app.main.modbus.ReadModbus import read_holding_registers
import app.main.crud as crud

app = FastAPI()


@app.on_event("startup")
def startup():
    # Modbus Connection
    mod_management.connect_to_bus_on_startup()


@app.get("/read")
def root():
    holding = read_holding_registers(RegisterType.COIL.get_start_address(), 125, 1)
    return {tuple(holding)}

@app.get("/port")
def root():
    result = crud.port.get_available_ports()
    return result
