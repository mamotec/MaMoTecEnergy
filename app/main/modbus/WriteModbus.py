"""
File for writing Modbus register.
"""

import app.main.modbus.ModbusManagement as modbus_management


def write_register(address: int, payload: float, unit: int):
    """
        Write´s a Register to specific Slave with given Payload.

    :param address: Address which the register should be written.
    :param payload: Value that should be written.
    :param unit: Slave ID where to write the value.
    """
    client = modbus_management.return_client()

    client.write_register(address, payload, unit=unit)
