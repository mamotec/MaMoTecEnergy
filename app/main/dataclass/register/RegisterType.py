from enum import Enum


class RegisterType(Enum):
    """
    Type of Modbus Object Types
    """
    COIL = ("1", "9999")
    DISCRETE_INPUT = ("10001", "19999")
    INPUT_REGISTER = ("30001 ", "39999")
    HOLDING_REGISTER = ("40001", "49999")

    def __init__(self, start_address, end_address):
        self.start_address = start_address
        self.end_address = end_address

    def get_start_address(self):
        return int(self.start_address)

    def get_end_address(self):
        return int(self.end_address)

    def is_in_between(self, address: int):
        start = self.get_start_address()
        end = self.get_end_address()

        return start < address < end
