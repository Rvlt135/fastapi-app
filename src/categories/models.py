from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Boolean
from src.database import Base
from database import async_engine

metadata = MetaData()


categories_list = Table(
    "categories",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("category_name", String, nullable=False),
)


class CategoryList(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    category_name = Column(String, nullable=False)

# metadata.create_all(async_engine) нужно ли здесь это?

fake_categories_by_strain = [
    {"id": 1, "category_name": "Indica", "strain_id": "5be017ac85e474c239bb0ad5", "strain_slug": "purple-punch"},
    {"id": 2, "category_name": "Sativa", "strain_id": "5be0181985e474c239bb0def", "strain_slug": "jack-herer"},
    {"id": 3, "category_name": "Hybrid", "strains":
        [{"strain_id": "5be0181985e474c239bb01244", "strain_slug": "blue-dream"}, ]},
]

