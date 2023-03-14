
from sqlalchemy import select
from src.database import async_session, session_db
from .models import CategoryList


@async_session
async def get_categories_list(asyc_session):
    stmt = select(CategoryList).filter()
    result = await asyc_session.execute(stmt)
    return result.scalars().all()

"""@async_session
async def get_categories_list(asyc_session):
    stmt = select(CategoryList).filter()
    result = await asyc_session.execute(stmt)
    return result.scalars().all()"""