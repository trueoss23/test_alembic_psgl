from sqlalchemy import MetaData, String, ForeignKey, Integer
from sqlalchemy import Column, Table


metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
)

assignees = Table(
    'assignees',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('email', String, nullable=False),
    Column('role_id', Integer, ForeignKey('roles.id')),
)
