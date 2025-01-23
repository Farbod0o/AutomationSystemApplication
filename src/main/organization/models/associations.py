from sqlalchemy import Table, Column, Integer, String,ForeignKey
from src.main.database.da import Base

organization_permission_table = Table(
    'organization_permissions',
    Base.metadata,
    Column('organization_id', Integer, ForeignKey('organizations.id')),
    Column('permission_id', Integer, ForeignKey('permissions.id'))
)

