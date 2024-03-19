from sqlalchemy.ext.asyncio import async_session, AsyncSession
from ..models import TypeGoods, Manufacturer, Products
from ..database import async_session_factory


async def insert_data_type_goods(
    async_session: async_session_factory[AsyncSession], goods: str
) -> None:
    type_goods = TypeGoods(type_goods=goods)
    async with async_session() as session:
        await session.add(type_goods)
        await session.commit()
