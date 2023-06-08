"""Init modules

Revision ID: init_all_modules
Revises: 
Create Date: 2023-06-08 15:51:18.907621+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.core.model import DBCoreBase   # Optional.


# revision identifiers, used by Alembic.
revision = 'init_all_modules'
down_revision = None
branch_labels = ('INITALL',)
depends_on = ['init_core_popdata', 'init_mod1_popdata', 'init_mod2_popdata', 'init_mod3_popdata']

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    log.info("Development shortcut branch to install all modules.")


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.

    log.info("Development shortcut branch to uninstall all modules.")
