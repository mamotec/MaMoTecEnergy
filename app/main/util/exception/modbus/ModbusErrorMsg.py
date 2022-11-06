from enum import Enum
from fastapi import status


class ModbusErrorMsg(Enum):
    CONNECTION_TIMEOUT = (status.HTTP_408_REQUEST_TIMEOUT, "Modbus TCP connection not established.")

    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail
