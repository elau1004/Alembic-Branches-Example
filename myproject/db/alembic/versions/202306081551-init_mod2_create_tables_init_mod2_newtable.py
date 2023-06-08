"""Init mod2 create tables

Revision ID: init_mod2_newtable
Revises: 
Create Date: 2023-06-08 15:51:13.758480+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.alembic import exist_table
from myproject.db.core.model import SystemUser
from myproject.db.mod2.model import DBModule2Base, Module2_Table


# revision identifiers, used by Alembic.
revision = 'init_mod2_newtable'
down_revision = None
branch_labels = ('INITMOD2',)
depends_on = 'init_core_newtable'

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    # NOTE: Keep schema DDL changes seperate from data DML chanegs in different migration script.
    #
    # NOTE: Following is an example on how to use the SQLAlchemy model definition in Alembic.
    engine = op.get_context().connection.engine
    DBModule2Base.metadata.create_all(engine)

    if exist_table(SystemUser.__tablename__):
    #     op.create_foreign_key(
    #         constraint_name=f"{Module2_Table.__tablename__}_created_by_FK",
    #         source_table=f"{Module2_Table.__tablename__}",
    #         referent_table=f"{SystemUser.__tablename__}",
    #         local_cols=[f"{Module2_Table.updated_by.name}"],
    #         remote_cols=[f"{SystemUser.ID.name}"],
    #     )
        pass


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.
    
    # NOTE: Keep schema DDL changes seperate from data DML chanegs in different migration script.
    #
    # NOTE: Following is an example on how to use the SQLAlchemy model definition in Alembic.
    engine = op.get_context().connection.engine
    DBModule2Base.metadata.drop_all(engine)
