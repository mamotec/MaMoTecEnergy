"""
Start of the MaMoTecEnergy Backend
"""
from fastapi import FastAPI

import app.main.modbus.modbus_management as mod_management
from app.main.router import register

app = FastAPI()


@app.on_event("startup")
def startup():
    # Modbus Connection
    mod_management.connect_to_bus()


app.include_router(register.router)
