"""Init core seed system data

Revision ID: init_core_popdata
Revises: init_core_funcproc
Create Date: 2023-06-08 15:51:09.834771+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.core.model import DBCoreBase   # Optional.


# revision identifiers, used by Alembic.
revision = 'init_core_popdata'
down_revision = 'init_core_funcproc'
branch_labels = None
depends_on = None

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    log.info("Populate seed data into the Core tables.")


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.

    log.info("Delete seed data from the Core tables.")
