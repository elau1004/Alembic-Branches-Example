"""MOD3 Rev3

Revision ID: mod3_rev3
Revises: mod3_rev2
Create Date: 2023-06-08 15:51:27.161498+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.core.model import DBCoreBase   # Optional.


# revision identifiers, used by Alembic.
revision = 'mod3_rev3'
down_revision = 'mod3_rev2'
branch_labels = None
depends_on = None

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    # In order to apply incremental upgrade, you MUST explicitly request for it via the CLI parameter "-x REVISE=".
    # Example: alembic -X REVISE=  upgrade  BRANCH@head
    #
    if op.get_context().environment_context.get_x_argument(as_dictionary=True).get('REVISE', None) is None:
        log.warn("Skiping upgrade but update the alembic version in DB.  Use CLI: '-X REVISE=' to enable.")
    else:
        # You should check for existance before your add new DB objects.
        pass


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.

    # In order to apply incremental downgrade, you MUST explicitly request for it via the CLI parameter "-x REVISE=".
    # Example: alembic -X REVISE=  downgrade  BRANCH@base
    #
    if op.get_context().environment_context.get_x_argument(as_dictionary=True).get('REVISE', None) is None:
        log.warn("Skiping downgrade but update the alembic version in DB.  Use CLI: '-X REVISE=' to enable.")
    else:
        # You should check for existance before your drop new DB objects.
        pass
