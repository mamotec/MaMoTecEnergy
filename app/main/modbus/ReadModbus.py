"""
File for reading Information on the BUS.
"""

import app.main.modbus.ModbusManagement as modbus_management


def read_coil(address: int, count: int, unit: int):
    """
        Read´s coils - address area is 00001 - 09999.

    :param address: Start of the address range.
    :param count: Count of to register to read.
    :param unit: Represents the Slave ID, which will be requested
    :return: Register of the request.
    """
    client = modbus_management.return_client()

    result = client.read_coils(address=address, count=count, unit=unit)
    return result.registers


def read_discrete_input(address: int, count: int, unit: int):
    """
        Read´s Discrete Inputs - address area is 10001 - 19999.

    :param address: Start of the address range.
    :param count: Count of to register to read.
    :param unit: Represents the Slave ID, which will be requested
    :return: Register of the request.
    """
    client = modbus_management.return_client()

    result = client.read_discrete_inputs(address=address, count=count, unit=unit)
    return result.registers


def read_input_register(address: int, count: int, unit: int):
    """
        Read´s Input Registers - address area is 30001 - 39999.

    :param address: Start of the address range.
    :param count: Count of to register to read.
    :param unit: Represents the Slave ID, which will be requested
    :return: Register of the request.
    """
    client = modbus_management.return_client()

    result = client.read_input_registers(address=address, count=count, unit=unit)
    return result.registers


def read_holding_registers(address: int, count: int, unit: int):
    """
        Read´s Holding Registers - address area is 40001 - 49999.

    :param address: Start of the address range.
    :param count: Count of to register to read.
    :param unit: Represents the Slave ID, which will be requested
    :return: Register of the request.
    """
    client = modbus_management.return_client()

    result = client.read_holding_registers(address=address, count=count, unit=unit)
    return result.registers
