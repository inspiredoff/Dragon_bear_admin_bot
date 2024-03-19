import asyncpg
from sqlalchemy.ext.asyncio import async_session, AsyncSession, async_sessionmaker
from db.models import TypeGoods, Manufacturer, Products
from db.database import async_session_factory


async def insert_data_type_goods(
    async_session: async_sessionmaker[AsyncSession], goods: str
) -> None:
    type_goods = TypeGoods(type_goods=goods)
    async with async_session() as session:
        session.add(type_goods)
        await session.commit()
