import psycopg2
from gino import Gino
from config import *

db: Gino = Gino()
Base = db.Model
database = 'postgresql'
dsn = database_dsn


class products(db.Model):
    __tablename__ = 'products'

    type_prod = db.Column(db.string)
    manufacturer = db.Column(db.character_varying(100))
    name_prod = db.Column(db.character_varying(100))
    selling_price = db.Column(db.money)
    purchase_price = db.Column(db.money)
    value_prod = db.Column(db.string)

async def init_db(database: str, dsn: str):
    """ Присоединяет gino к циклу событий """
    await db.set_bind(f"{database}://{dsn}")

