"""
File for serving the communication with the Modbus TCP Protocol
"""
from pymodbus.client.sync import ModbusTcpClient


def __init__():
    global client
    client = ModbusTcpClient()
    client.connect()


def disconnect_from_bus():
    """ Disconnects to the Bus """
    client.close()


def return_client():
    """ Returns the Modbus TCP Client """
    return client
