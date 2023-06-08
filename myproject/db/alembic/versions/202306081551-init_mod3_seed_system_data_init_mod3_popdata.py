"""Init mod3 seed system data

Revision ID: init_mod3_popdata
Revises: init_mod3_funcproc
Create Date: 2023-06-08 15:51:17.574280+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.mod3.model import DBModule3Base


# revision identifiers, used by Alembic.
revision = 'init_mod3_popdata'
down_revision = 'init_mod3_funcproc'
branch_labels = None
depends_on = None

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    log.info("Populate Module 3 tables with seed data.")


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.

    log.info("UnPopulate Module 3 tables with seed data.")
