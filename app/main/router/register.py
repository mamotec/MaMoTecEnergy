from typing import Optional

from fastapi import APIRouter, Depends

from app.main.database.models.register import Register
from app.main.schemas.register import RegisterBase
from app.main.services import get_registers_service
from app.main.services.register_service import RegisterService

router = APIRouter(prefix="/registers")


@router.get("/{register_id}", response_model=RegisterBase)
async def get_register(register_id: int, register_service: RegisterService = Depends(get_registers_service)) -> \
        Optional[Register]:
    return register_service.get(register_id)
