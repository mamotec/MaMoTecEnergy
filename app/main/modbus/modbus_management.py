"""
File for serving the communication with the Modbus TCP Protocol
"""
from pymodbus.client.sync import ModbusTcpClient

client: ModbusTcpClient = ModbusTcpClient()


def connect_to_bus():
    client.connect()
    if not client.is_socket_open():
        raise BaseException("Modbus socket is not open.")

def disconnect_from_bus():
    """ Disconnects to the Bus """
    client.close()


def return_client():
    """ Returns the Modbus TCP Client """
    connect_to_bus()
    return client
