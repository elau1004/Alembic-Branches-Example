"""Init mod3 create replacables

Revision ID: init_mod3_funcproc
Revises: init_mod3_newtable
Create Date: 2023-06-08 15:51:16.932285+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.mod3.model import DBModule3Base


# revision identifiers, used by Alembic.
revision = 'init_mod3_funcproc'
down_revision = 'init_mod3_newtable'
branch_labels = None
depends_on = None

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    log.info("Create Module 3 replacables (views/functions/procedures).")


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.

    log.info("Drop Module 3 replacables (views/functions/procedures).")
