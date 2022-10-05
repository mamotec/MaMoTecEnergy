"""
File for reading Information on the BUS.
"""
import app.modbus.modbus_management as modbus_management

client = modbus_management.return_client()


def read_holding_registers():
    result = client.read_holding_registers(address=0, count=10, unit=0)
    return result
