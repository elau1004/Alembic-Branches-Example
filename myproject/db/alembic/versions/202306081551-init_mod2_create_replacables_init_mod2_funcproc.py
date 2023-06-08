"""Init mod2 create replacables

Revision ID: init_mod2_funcproc
Revises: init_mod2_newtable
Create Date: 2023-06-08 15:51:14.396482+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.mod2.model import DBModule2Base


# revision identifiers, used by Alembic.
revision = 'init_mod2_funcproc'
down_revision = 'init_mod2_newtable'
branch_labels = None
depends_on = None

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    log.info("Create Module 2 replacables (views/functions/procedures).")


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.

    log.info("Drop Module 2 replacables (views/functions/procedures).")
