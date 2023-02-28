from pydantic import BaseModel
from typing import List
from typing import Dict


class Categories(BaseModel):
    list_with_catories = { 1: 'Sativa', 2: "Indica", 3: 'Hybrid'}
    id: int
    categories: list = list_with_catories


class Effects(BaseModel):
    count: int
    name: str
    tag: dict = {"name": "Anxious", "type": "Negative"}


class Strain(BaseModel):
    id: int
    name: str
    slug_name: str
    description: str
    reviewsCount: int
    rating: int
    category: str
    countByEffects: List[Effects]
