from typing import Any

from sqlalchemy.orm import Session

from app.main.database.models.register import Register
from app.main.services.base import BaseService
from app.main.schemas.register import RegisterCreate


class RegisterService(BaseService[Register, RegisterCreate, Any]):
    def __init__(self, db_session: Session):
        super(RegisterService, self).__init__(Register, db_session)

    def create(self, obj: RegisterCreate) -> Register:
        register = Register()
        self.db_session.add(register)
        self.db_session.flush()
        self.db_session.commit()
        return register
