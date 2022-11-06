"""
File for reading Information on the BUS.
"""
import app.main.modbus.ModbusManagement as modbus_management


def read_holding_registers():
    client = modbus_management.return_client()

    result = client.read_holding_registers(address=0, count=10, unit=1)
    return result.registers
