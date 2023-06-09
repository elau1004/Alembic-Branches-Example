"""Init mod3 create tables

Revision ID: init_mod3_newtable
Revises: 
Create Date: 2023-06-08 15:51:16.272467+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.alembic import exist_table
from myproject.db.core.model import SystemUser
from myproject.db.mod3.model import DBModule3Base, Module3_Table


# revision identifiers, used by Alembic.
revision = 'init_mod3_newtable'
down_revision = None
branch_labels = ('INITMOD3',)
depends_on = 'init_core_newtable'

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    # NOTE: Keep schema DDL changes seperate from data DML chanegs in different migration script.
    #
    # NOTE: Following is an example on how to use the SQLAlchemy model definition in Alembic.
    engine = op.get_context().connection.engine
    DBModule3Base.metadata.create_all(engine)

    if exist_table(SystemUser.__tablename__):
    #     op.create_foreign_key(
    #         f"{Module3_Table.__tablename__}_created_by_FK",
    #         f"{Module3_Table.__tablename__}",
    #         f"{SystemUser.__tablename__}",
    #         [f"{Module3_Table.updated_by.name}"],
    #         [f"{SystemUser.ID.name}"],
    #     )
        pass

def downgrade() -> None:
    # Alembic downgrade migration entrypoint.
    
    # NOTE: Keep schema DDL changes seperate from data DML chanegs in different migration script.
    #
    # NOTE: Following is an example on how to use the SQLAlchemy model definition in Alembic.
    engine = op.get_context().connection.engine
    DBModule3Base.metadata.drop_all(engine)
