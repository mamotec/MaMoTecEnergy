"""
File for serving the communication with the Modbus TCP Protocol
"""
from fastapi import HTTPException
from pymodbus.client.sync import ModbusTcpClient

from app.main.util.exception.modbus.ModbusErrorMsg import ModbusErrorMsg

import warnings

client: ModbusTcpClient = ModbusTcpClient()


def connect_to_bus_on_startup():
    client.connect()
    if not client.is_socket_open():
        warnings.warn(ModbusErrorMsg.CONNECTION_TIMEOUT.detail)


def connect_to_bus():
    client.connect()
    if not client.is_socket_open():
        raise HTTPException(status_code=ModbusErrorMsg.CONNECTION_TIMEOUT.status_code,
                            detail=ModbusErrorMsg.CONNECTION_TIMEOUT.detail)


def disconnect_from_bus():
    """ Disconnects to the Bus """
    client.close()


def return_client():
    """ Returns the Modbus TCP Client """
    connect_to_bus()
    return client
