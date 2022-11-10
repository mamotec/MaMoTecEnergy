import warnings

from app.main.dataclass.register.RegisterType import RegisterType


def get_register_type_from_address(address: int) -> RegisterType:
    if RegisterType.COIL.get_start_address() < address < RegisterType.COIL.get_end_address():
        return RegisterType.COIL
    elif RegisterType.DISCRETE_INPUT.get_start_address() < address < RegisterType.DISCRETE_INPUT.get_end_address():
        return RegisterType.DISCRETE_INPUT
    elif RegisterType.INPUT_REGISTER.get_start_address() < address < RegisterType.INPUT_REGISTER.get_end_address():
        return RegisterType.INPUT_REGISTER
    elif RegisterType.HOLDING_REGISTER.get_start_address() < address < RegisterType.HOLDING_REGISTER.get_end_address():
        return RegisterType.HOLDING_REGISTER
    else:
        warnings.warn("No Mapping found for address: " + str(address))
