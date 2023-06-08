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

# DB::Core model.

# NOTE: The following is the version 2.0 way of declaring the objects (ORM Mapped Classes).
#
# SEE:  https://docs.sqlalchemy.org/en/20/tutorial/metadata.html#declaring-mapped-classes
#       https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html#whatsnew-20-orm-declarative-typing
#
class DBCoreBase(DeclarativeBase):
    pass


class SystemUser(DBCoreBase):
    __tablename__ = "system_user"

    ID: Mapped[SmallInteger] = mapped_column(SmallInteger, primary_key=True, nullable=False, comment="The unique ID to identify a row in this table.")
    updated_on: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.now(), comment="The date/time this row was last updated on.")
    email: Mapped[String] = mapped_column(String(64), nullable=False, comment="The globally unique email.")
    is_active: Mapped[Boolean] = mapped_column(Boolean, nullable=False, server_default=expression.true(), comment="Set to instruct the application/query to filter this row.")
    first_name: Mapped[String] = mapped_column(String(64), nullable=False, comment="First name")
    last_name: Mapped[String] = mapped_column(String(64), nullable=False, comment="Last name")

    __table_args__ = (
        schema.CheckConstraint(
            'system_user.ID >= 0'
        ),
        schema.CheckConstraint(
            'system_user.ID <= 999'
        )
    )


class QueryCriteria(DBCoreBase):
    __tablename__ = "query_criteria"

    ID: Mapped[SmallInteger] = mapped_column(SmallInteger, primary_key=True, comment="The unique ID to identify a row in this table.")
    updated_on: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.now(), comment="The date/time this row was last updated on.")
    updated_by: Mapped[SmallInteger] = mapped_column(SmallInteger, ForeignKey(f"{SystemUser.__tablename__}.{SystemUser.ID.name}"), nullable=False, comment="The foreign key to the system user table.")
    namespace: Mapped[String] = mapped_column(String(128), nullable=False, comment="A grouping to collect different unique keys.")
    key_value: Mapped[String] = mapped_column(String(64), nullable=False, comment="The unique key in the given namespace.")
    num_value: Mapped[float] = mapped_column(Float, comment="The Integer typed value for the key.")
    str_value: Mapped[String] = mapped_column(String(128), comment="The String typed value for the key.")
    dtm_value: Mapped[DateTime] = mapped_column(DateTime, comment="The DateTime typed value for the key.")
    is_active: Mapped[Boolean] = mapped_column(Boolean, nullable=False, server_default=expression.true(), comment="Set to instruct the application/query to filter this row.")
    to_include: Mapped[Boolean] = mapped_column(Boolean, server_default=expression.true(), comment="Positive filter requesting this value in the dataset." )
    to_exclude: Mapped[Boolean] = mapped_column(Boolean, server_default=expression.false(), comment="Negative filter disgarding this value in the dataset." )
    health_system: Mapped[String] = mapped_column(String(8))
    tag0: Mapped[String] = mapped_column(String(32))
    tag1: Mapped[String] = mapped_column(String(32))
    tag2: Mapped[String] = mapped_column(String(32))
    tag3: Mapped[String] = mapped_column(String(32))
    tag4: Mapped[String] = mapped_column(String(32))
    tag5: Mapped[String] = mapped_column(String(32))

    #   system_users: Mapped[SystemUser] = relationship(back_populates="query_filter")


# SEE:  https://dbdiagram.io/home/
#       https://dbml.dbdiagram.io/home/
