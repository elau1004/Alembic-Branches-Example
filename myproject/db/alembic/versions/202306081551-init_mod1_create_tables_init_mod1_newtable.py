"""Init mod1 create tables

Revision ID: init_mod1_newtable
Revises: 
Create Date: 2023-06-08 15:51:11.169378+00:00

"""

import logging
import sqlalchemy as sa
from alembic import op
from myproject.db.alembic import exist_table
from myproject.db.core.model import SystemUser
from myproject.db.mod1.model import DBModule1Base, Module1_Table


# revision identifiers, used by Alembic.
revision = 'init_mod1_newtable'
down_revision = None
branch_labels = ('INITMOD1',)
depends_on = 'init_core_newtable'

log = logging.getLogger("alembic.runtime.migration")


def upgrade() -> None:
    # Alembic upgrade migration entrypoint.

    # NOTE: Keep schema DDL changes seperate from data DML chanegs in different migration script.
    #
    # NOTE: Following is an example on how to use the SQLAlchemy model definition in Alembic.
    engine = op.get_context().connection.engine
    DBModule1Base.metadata.create_all(engine)

    if exist_table(SystemUser.__tablename__):
    #         f"{Module1_Table.__tablename__}_created_by_FK",
    #         f"{Module1_Table.__tablename__}",
    #         f"{SystemUser.__tablename__}",
    #         [f"{Module1_Table.updated_by.name}"],
    #         [f"{SystemUser.ID.name}"],
    #     )
        pass


def downgrade() -> None:
    # Alembic downgrade migration entrypoint.
    
    # NOTE: Keep schema DDL changes seperate from data DML chanegs in different migration script.
    #
    # NOTE: Following is an example on how to use the SQLAlchemy model definition in Alembic.
    engine = op.get_context().connection.engine
    DBModule1Base.metadata.drop_all(engine)
