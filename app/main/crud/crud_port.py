from app.main.crud.base import CRUDBase
from app.main.database.models.port import Port
from app.main.schemas.port import PortCreate, PortUpdate
import app.main.service.service_port as port_service


class CRUDPort(CRUDBase[Port, PortCreate, PortUpdate]):

    def get_available_ports(self):
        return port_service.get_available_ports()


port = CRUDPort(Port)
