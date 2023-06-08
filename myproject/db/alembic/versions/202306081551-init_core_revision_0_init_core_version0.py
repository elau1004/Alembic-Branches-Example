"""Init core revision 0

Revision ID: init_core_version0
Revises: 
Create Date: 2023-06-08 15:51:10.488276+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.core.model import DBCoreBase   # Optional.


# revision identifiers, used by Alembic.
revision = 'init_core_version0'
down_revision = None
branch_labels = ('CORE',)
depends_on = 'init_core_popdata'

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
