import psycopg2
from sqlalchemy import Column
from gino import Gino
from config import *

db: Gino = Gino()
Base = db.Model
dsn = database_dsn


class products(db.Model):
    __tablename__ = 'products'

    type_prod = Column(db.string)
    manufacturer = Column(db.character_varying(100))
    name_prod = Column(db.character_varying(100))
    selling_price = Column(db.money)
    purchase_price = Column(db.money)
    value_prod = Column(db.string)

async def init_db(database: str, dsn: str):
    """ Присоединяет gino к циклу событий """
    await db.set_bind(f"{database}://{dsn}")

