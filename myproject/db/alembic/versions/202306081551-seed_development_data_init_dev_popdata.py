"""Seed development data

Revision ID: init_dev_popdata
Revises: 
Create Date: 2023-06-08 15:51:19.531893+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.core.model import DBCoreBase   # Optional.


# revision identifiers, used by Alembic.
revision = 'init_dev_popdata'
down_revision = None
branch_labels = ('INITDEV',)
depends_on = 'init_all_modules'

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    log.info("Populate all table tables with DEVELOPMENT test data.")


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.

    log.info("Delete all table tables with DEVELOPMENT test data.")

