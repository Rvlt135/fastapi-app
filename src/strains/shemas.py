from pydantic import BaseModel, Field
from typing import Optional
from src.categories.shemas import CategoriesType


class Strain(BaseModel):
    id: int = Field(ge=1, default=1)
    slug_name: str = Field(min_length=6)
    name: str = Field(min_length=6)
    # created_strains: Optional[datetime]
    category: CategoriesType  # field from CategoriesStrain
    hash_id: str


class StrainDetails(BaseModel):
    id: Optional[int] = None
    slug_name: Optional[str] = None
    name: Optional[str] = None
    category: Optional[CategoriesType] = None
    # created_strains: Optional[datetime]  = None
    hash_id: Optional[str] = None
