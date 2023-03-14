from fastapi import APIRouter
from .shemas import CategoriesStrain, CategoriesListName
from typing import List
from src.categories.models import fake_categories_by_strain, CategoryList
from .service import get_categories_list, get_category_name

categories_router = APIRouter(
    prefix='/api/categories',
    tags=['categories'],

)


@categories_router.get("/list")
async def get_categories():
    return await get_categories_list()


@categories_router.get("/category_name")
async def get_categories_name():
    return await get_category_name()

@categories_router.get('/api/categories/byStrain', response_model=CategoriesStrain)
def get_categories_by_strains(get_id: int):
    """Принимает get_id возвращает несколько вариантов strains old and new"""

    for category_id in fake_categories_by_strain:
        if category_id.get("id") == get_id:
            return category_id
