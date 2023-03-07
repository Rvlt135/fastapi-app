from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from old_database import Base


class Strain(Base):
    __tablename__ = "strain"

    id = Column(String, primary_key=True, unique=True, index=True)
    name = Column(String)
    slug_name = Column(String, unique=True, index=True)
    category_name = relationship("CategoriesStrain", back_populates="id")
    items = relationship("CategoriesStrain", back_populates="category")


class CategoriesStrain(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    category_strain_name = Column(String, unique=True, index=True)
    strain_id = Column(String, ForeignKey("strain.id"))
    strain_slug = Column(String, ForeignKey("strain.slug_name"))
    strain_name = relationship("Strain", back_populates="items")


class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    category_name = Column(String, unique=True, index=True)
    strain_id = Column(Strain, ForeignKey("strain.id"))
    strain_name = relationship("CategoriesStrain", back_populates="strain_name")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")