"""Init mod2 seed system data

Revision ID: init_mod2_popdata
Revises: init_mod2_funcproc
Create Date: 2023-06-08 15:51:15.012523+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.mod2.model import DBModule2Base


# revision identifiers, used by Alembic.
revision = 'init_mod2_popdata'
down_revision = 'init_mod2_funcproc'
branch_labels = None
depends_on = None

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    log.info("Populate seed data into the Module 2 tables.")


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.

    log.info("Delete seed data from the Module 2 tables.")
