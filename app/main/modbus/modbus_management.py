"""
File for serving the communication with the Modbus TCP Protocol
"""
from pymodbus.client.sync import ModbusTcpClient
import warnings

client: ModbusTcpClient = ModbusTcpClient()


def connect_to_bus():
    client.connect()
    if not client.is_socket_open():
        warnings.warn("Warning: Socket not open")

def disconnect_from_bus():
    """ Disconnects to the Bus """
    client.close()


def return_client():
    """ Returns the Modbus TCP Client """
    connect_to_bus()
    return client
