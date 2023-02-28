from pydantic import BaseModel
from typing import List
from typing import Dict


class CategoriesStrain(BaseModel):
    id: int
    categories = {1: 'Sativa', 2: "Indica", 3: 'Hybrid'}


class Effects(BaseModel):
    count: int
    name: str
    tag: dict = {"name": "Anxious", "type": "Negative"}


class Strain(BaseModel):
    strain_id: int
    name: str
    slug_name: str
    description: str
    reviewsCount: int
    rating: int
    categories: CategoriesStrain
    countByEffects: List[Effects]


class User(BaseModel):
    name: str
    email: str
    user_name: str
