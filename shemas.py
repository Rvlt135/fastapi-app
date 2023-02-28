from pydantic import BaseModel
from typing import List


class Effects(BaseModel):
    count: int
    name: str
class Strain(BaseModel):
    id: int
    name: str
    slug_name: str
    description: str
    rating: int
    category: str
    countByEffects: List[Effects]
