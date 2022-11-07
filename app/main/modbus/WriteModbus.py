"""
File for writing Modbus register.
"""

import app.main.modbus.ModbusManagement as modbus_management


def write_register(address: int, payload: float, unit: int):
    client = modbus_management.return_client()

    client.write_register(address, payload, unit=unit)
