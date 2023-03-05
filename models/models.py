import datetime
from sqlalchemy import MetaData, Column, Integer, String, ForeignKey, Table, JSON, TIMESTAMP
import sqlalchemy as sa
from alembic import op

metadata = MetaData()

roles = Table("roles",
              metadata,
              Column("id", Integer, primary_key=True),
              Column("name", String, nullable=False),
              Column("permissions", JSON),
              )

user = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_mane", String, nullable=False,),
    Column("password", String, nullable=False,),
    Column("email", String, nullable=False,),
    Column("registred_data", TIMESTAMP),
    Column("role_id", Integer, ForeignKey("roles.id")),

)


"""
categories_list = Table(
    "categories",
    sa.Column("id", Integer, primary_key=True),
    sa.Column("category", String, nullable=False, )

)

strains = Table(
    "strains",
    sa.Column("id", Integer, primary_key=True),
    sa.Column("slug_name", String, nullable=False,),
    sa.Column("name", String, nullable=False,),
    # Column("created_strains", TIMESTAMP, default=datetime.utcnow()),
    sa.Column("category", String, nullable=False, ),
    sa.Column("hash_id", String, sa.Text(), ForeignKey("categories.category"), nullable=False, ),
)
"""