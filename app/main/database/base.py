# Import all the models, so that Base has them before being
# imported by Alembic
from app.main.database.db import Base  # noqa
from app.main.database.models.port import Port  # noqa
