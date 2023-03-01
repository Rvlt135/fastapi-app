from pydantic import BaseModel, validator, Field
from typing import List, Optional
from typing import Dict
import hashlib


class CategoriesStrain(BaseModel):
    pass


class Effects(BaseModel):

    count: int
    name: str
    tag: dict = {"name": "Anxious", "type": "Negative"}


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
    Один из видов валидации
    @validator('age')
    def check_age(cls, value):
        if value < 18:
            raise ValueError('only over eighteen')
        return value
    """