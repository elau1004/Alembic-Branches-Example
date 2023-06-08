# MIT License
#
# Copyright (c) 2023 Edward Lau

# SEE:  https://www.databasestar.com/database-table-naming-conventions/
#       https://medium.com/@fbnlsr/the-table-naming-dilemma-singular-vs-plural-dc260d90aaff
# SEE:  https://docs.sqlalchemy.org/en/20/index.html

from sqlalchemy import ForeignKey, schema
from sqlalchemy.types import Boolean, DateTime, Float, Integer, SmallInteger, String
from sqlalchemy.sql import expression, func
from typing import List
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

# DB::Module3 model.

# NOTE: The following is the version 2.0 way of declaring the objects (ORM Mapped Classes).
#
# SEE:  https://docs.sqlalchemy.org/en/20/tutorial/metadata.html#declaring-mapped-classes
#       https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html#whatsnew-20-orm-declarative-typing
#
class DBModule3Base(DeclarativeBase):
    pass


class Module3_Table(DBModule3Base):
    __tablename__ = "module3_table"

    ID: Mapped[SmallInteger] = mapped_column(SmallInteger, primary_key=True, nullable=False, comment="The unique ID to identify a row in this table.")
    updated_on: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.now(), comment="The date/time this row was last updated on.")
    updated_by: Mapped[SmallInteger] = mapped_column(SmallInteger, nullable=True, comment="The foreign key to the system user table.")


# SEE:  https://dbdiagram.io/home/
#       https://dbml.dbdiagram.io/home/
