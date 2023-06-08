# MIT License
#
# Copyright (c) 2023 Edward Lau

from alembic import op
# om sqlalchemy import engine_from_config
# om sqlalchemy.engine import reflection
from sqlalchemy.engine.reflection import Inspector

# Utility functions to be accesable from the mirgation scripts.


def exist_table(table_name: str) -> bool:
    # SEE: https://stackoverflow.com/questions/31299709/alembic-create-table-check-if-table-exists
    # config = op.get_context().config
    # engine = engine_from_config(
    #     config.get_section(config.config_ini_section), prefix="sqlalchemy."
    # )
    # inspector = Inspector.from_engine(engine)
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    return table_name in tables
