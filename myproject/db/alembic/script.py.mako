"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.alembic import has_table  # Optional
from myproject.db.core.model import DBCoreBase   # Optional.
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    # NOTE: Keep schema DDL changes seperate from data DML chanegs in different migration script.
    #
    # NOTE: Following is an example on how to use the SQLAlchemy model definition in Alembic.
    # engine = op.get_context().connection.engine
    # DBCoreBase.metadata.create_all(engine)
    #
    # In order to apply incremental upgrade, you MUST explicitly request for it via the CLI parameter "-x REVISE=".
    # Example: alembic -X REVISE=  upgrade  CORE@head
    #
    # if op.get_context().environment_context.get_x_argument(as_dictionary=True).get('REVISE', None) is None:
    #     log.warn("Skiping upgrade but update the alembic version in DB.  Use CLI: '-X REVISE=' to enable.")
    # else:
    #     pass
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.

    # NOTE: Keep schema DDL changes seperate from data DML chanegs in different migration script.
    #
    # NOTE: Following is an example on how to use the SQLAlchemy model definition in Alembic.
    # engine = op.get_context().connection.engine
    # DBCoreBase.metadata.drop_all(engine)
    #
    # In order to apply incremental downgrade, you MUST explicitly request for it via the CLI parameter "-x REVISE=".
    # Example: alembic -X REVISE=  upgrade  CORE@head
    #
    # if op.get_context().environment_context.get_x_argument(as_dictionary=True).get('REVISE', None) is None:
    #     log.warn("Skiping downgrade but update the alembic version in DB.  Use CLI: '-X REVISE=' to enable.")
    # else:
    #     pass
    ${downgrades if downgrades else "pass"}
