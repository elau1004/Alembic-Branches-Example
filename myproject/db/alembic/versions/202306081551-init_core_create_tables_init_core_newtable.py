"""Init core create tables

Revision ID: init_core_newtable
Revises: 
Create Date: 2023-06-08 15:51:08.476797+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.core.model import DBCoreBase


# revision identifiers, used by Alembic.
revision = 'init_core_newtable'
down_revision = None
branch_labels = ('INITCORE',)
depends_on = None

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    # NOTE: Keep schema DDL changes seperate from data DML chanegs in different migration script.
    #
    # NOTE: Following is an example on how to use the SQLAlchemy model definition in Alembic.
    engine = op.get_context().connection.engine
    DBCoreBase.metadata.create_all(engine)
    

def downgrade() -> None:
    # Alembic downgrade migration entrypoint.

    # NOTE: Keep schema DDL changes seperate from data DML chanegs in different migration script.
    #
    # NOTE: Following is an example on how to use the SQLAlchemy model definition in Alembic.
    engine = op.get_context().connection.engine
    DBCoreBase.metadata.drop_all(engine)
