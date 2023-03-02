from enum import Enum

from pydantic import BaseModel, validator, Field
from typing import List, Optional, Union
from typing import Dict
import hashlib


class CategoriesType(Enum):
    category_sativa = "Sativa"
    category_indica = "Indica"
    category_hybrid = "Hybrid"


class CategoriesTypeList(BaseModel):
    id: int
    categories_list: List[CategoriesType]


class CategoriesList(BaseModel):
    id: int
    category: CategoriesType


class StrainsByCategories(BaseModel):
    strain_id: str
    strain_slug: str


class CategoriesStrain(BaseModel):
    id: int
    category_name: CategoriesType
    strain_id: Optional[str]  # hash_id
    strain_slug: Optional[str]
    strains: Optional[List[StrainsByCategories]]


class Strain(BaseModel):
    id: int = Field(ge=1, default=1)
    slug_name: str = Field(min_length=6)
    name: str = Field(min_length=6)
    category: CategoriesType  # field from CategoriesStrain
    hash_id: str


class StrainDetails(BaseModel):
    id: int
    slug_name: str
    name: str
    category: CategoriesType
    hash_id: str
"""
class EffectStrain(CategoriesStrain):
    pass


class Effects(BaseModel):

    count: int
    name: str
    tag: dict


class StrainOutBySlugName(BaseModel):

    categories = {1: 'Sativa', 2: "Indica", 3: 'Hybrid'}
    # strain_id: int
    name: str
    slug_name: str
    rating: Optional[int] = None
    categories: dict = categories
    countByEffects: List[Effects]
    description: Optional[str] = None
    strain_id: str


class StrainInBySlugName(BaseModel):

    categories = {1: 'Sativa', 2: "Indica", 3: 'Hybrid'}
    # strain_id: int
    name: str
    slug_name: str
    description: Optional[str] = None
    reviewsCount: int
    rating: Optional[int] = None
    categories: dict
    countByEffects: List[Effects]


class StrainResult(StrainInBySlugName):

    result: int = 2


class User(BaseModel):

    name: str = Field(max_length=25)
    email: str
    user_name: str
    age: int = Field(..., gt=18, lt=70)
"""