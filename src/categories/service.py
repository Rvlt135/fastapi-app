from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.database import get_async_session
from .models import categories_list


async def get_categories_list(session: AsyncSession = Depends(get_async_session)):
    query = select(categories_list)
    result = await session.execute(query)
    return result.all()


