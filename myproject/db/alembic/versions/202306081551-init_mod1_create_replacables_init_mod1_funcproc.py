"""Init mod1 create replacables

Revision ID: init_mod1_funcproc
Revises: init_mod1_newtable
Create Date: 2023-06-08 15:51:11.808339+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.mod1.model import DBModule1Base


# revision identifiers, used by Alembic.
revision = 'init_mod1_funcproc'
down_revision = 'init_mod1_newtable'
branch_labels = None
depends_on = None

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    log.info("Create Module 1 replacables (views/functions/procedures).")


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.

    log.info("Drop Module 1 replacables (views/functions/procedures).")
