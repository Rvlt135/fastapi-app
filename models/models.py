import datetime

from sqlalchemy import MetaData, Integer, Column, String, TIMESTAMP, ForeignKey, Table, JSON

metadata = MetaData()

roles = Table("roles",
              metadata,
              Column("id", Integer, primary_key=True),
              Column("name", String, nullable=False),
              Column("permissions", JSON)
              )

user = Table(
    "strains",
    Column("id", Integer, primary_key=True),
    Column("user_mane", String, nullable=False,),
    Column("password", String, nullable=False,),
    Column("email", String, nullable=False,),
    Column("registred_data", TIMESTAMP, default=datetime.utcnow()),
    Column("role_id", Integer, ForeignKey("roles.id")),

)

categories_list = Table(
    "categories",
    Column("id", Integer, primary_key=True),
    Column("category", String, nullable=False, )

)

strains = Table(
    "strains",
    Column("id", Integer, primary_key=True),
    Column("slug_name", String, nullable=False,),
    Column("name", String, nullable=False,),
    # Column("created_strains", TIMESTAMP, default=datetime.utcnow()),
    Column("category", String, nullable=False, ),
    Column("hash_id", String, ForeignKey("categories.category"), nullable=False, ),

)