from sqlalchemy import select, insert
from src.database import async_session
from .models import CategoryList


@async_session
async def get_categories_list(asyc_session):
    stmt = select(CategoryList).filter()
    result = await asyc_session.execute(stmt)
    return result.scalars().all()


@async_session
async def get_category_name(asyc_session):
    query = select(CategoryList.category_name)
    result = await asyc_session.execute(query)
    return result.scalars().all()
