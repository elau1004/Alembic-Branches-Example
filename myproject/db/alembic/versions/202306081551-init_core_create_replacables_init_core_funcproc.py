"""Init core create replacables

Revision ID: init_core_funcproc
Revises: init_core_newtable
Create Date: 2023-06-08 15:51:09.203941+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.core.model import DBCoreBase


# revision identifiers, used by Alembic.
revision = 'init_core_funcproc'
down_revision = 'init_core_newtable'
branch_labels = None
depends_on = None

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    log.info("Create Core replacables (views/functions/procedures).")


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.

    log.info("Create Core replacables (views/functions/procedures).")
