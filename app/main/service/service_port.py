import serial.tools.list_ports


def get_available_ports():
    print(list(serial.tools.list_ports.comports()))
    return serial.tools.list_ports.comports()
