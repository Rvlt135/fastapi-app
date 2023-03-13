from fastapi import APIRouter
from .shemas import CategoriesStrain, CategoriesList
import hashlib
from typing import List
from .models import fake_categories_by_strain, categories_list
from .service import get_categories_list
categories_router = APIRouter(
    prefix='/categories',
    tags=['categories'],

)


@categories_router.get("/api/categories")
def get_categories():
    return get_categories_list


@categories_router.get('/api/categories/byStrain', response_model=CategoriesStrain)
def get_categories_by_strains(get_id: int):
    """Принимает get_id возвращает несколько вариантов strains old and new"""

    for category_id in fake_categories_by_strain:
        if category_id.get("id") == get_id:
            return category_id
