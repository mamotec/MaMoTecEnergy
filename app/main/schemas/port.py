import datetime
from typing import Optional

from pydantic import BaseModel


class PortBase(BaseModel):
    port_name: Optional[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime


class PortCreate(PortBase):
    pass


class PortUpdate(PortBase):
    ...
