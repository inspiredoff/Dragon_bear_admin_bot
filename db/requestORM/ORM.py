import asyncpg
import asyncio
from sqlalchemy.ext.asyncio import async_session, AsyncSession, async_sessionmaker
from ..models import TypeGoods, Manufacturer, Products
from ..database import async_session_factory, async_engine, Base


class AsyncORM:
    @staticmethod
    async def create_table():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_data_type_goods(
        # добавляем в базу данных новый тип продукта или производителя
        async_session: async_sessionmaker[AsyncSession], goods: str
    ) -> None:
        data = TypeGoods(type_goods=goods)
        async with async_session() as session:
            session.add(data)
            await session.commit()

    @staticmethod
   async def select_products(async_session: async_sessionmaker[AsyncSession]) ->type_goods, manufacturer:
       async with async_session() as session:
           query = select(TypeGoods.type_goods)
           result = await session.execute(query)
       return result.scalar().all()
