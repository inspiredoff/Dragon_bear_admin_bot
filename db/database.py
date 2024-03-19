from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.orm import declarative_base
import asyncpg
from ..config import dsn

async_engine = create_async_engine(url=dsn, echo=True, pool_size=5, max_owerflow=10)
async_session_factory = async_sessionmaker(async_engine)


class Base(declarative_base):
    pass
