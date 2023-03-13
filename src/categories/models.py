from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


metadata = MetaData()


categories_list = Table(
    "categories",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("category_name", String, nullable=False),
)

class CategoryList(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, nullable=False)
    category_name = Column(String, nullable=False)


fake_categories_by_strain = [
    {"id": 1, "category_name": "Indica", "strain_id": "5be017ac85e474c239bb0ad5", "strain_slug": "purple-punch"},
    {"id": 2, "category_name": "Sativa", "strain_id": "5be0181985e474c239bb0def", "strain_slug": "jack-herer"},
    {"id": 3, "category_name": "Hybrid", "strains":
        [{"strain_id": "5be0181985e474c239bb01244", "strain_slug": "blue-dream"}, ]},
]

'''fake_categories_list = [
    {"id": 1, "category": "Indica"},
    {"id": 2, "category": "Sativa"},
    {"id": 3, "category": "Hybrid"},
]'''


