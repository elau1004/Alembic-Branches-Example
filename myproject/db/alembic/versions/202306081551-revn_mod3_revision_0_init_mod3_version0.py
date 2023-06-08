"""Revn mod3 revision 0

Revision ID: init_mod3_version0
Revises: 
Create Date: 2023-06-08 15:51:18.238290+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.core.model import DBCoreBase   # Optional.


# revision identifiers, used by Alembic.
revision = 'init_mod3_version0'
down_revision = None
branch_labels = ('MOD3',)
depends_on = 'init_mod3_popdata'

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    log.info("Base down revision branch MOD3 to point to as scripts are deleted from the repo.")


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.

    log.info("Base down revision branch MOD3 to point to as scripts are deleted from the repo.")
