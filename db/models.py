from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm.properties import ForeignKey
from db.database import Base


class TypeGoods(Base):
    __tablename__ = "typ"

    id: Mapped[int] = mapped_column(primary_key=True)
    type_goods: Mapped[str] = mapped_column()


class Manufacturer(Base):
    __tablename__ = "manufacturer"

    id: Mapped[int] = mapped_column(primary_key=True)
    manufacturer: Mapped[str] = mapped_column()
    type_goods: Mapped[str] = mapped_column(ForeignKey("typ.id"))


class Products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_type_goods: Mapped[int] = mapped_column(ForeignKey("typ.id"))
    id_manufacturer: Mapped[int] = mapped_column(ForeignKey("manufacturer.id"))
    name_prod: Mapped[str] = mapped_column()
    selling_price: Mapped[int] = mapped_column()
    purchase_price: Mapped[int] = mapped_column()
    value_prod: Mapped[int] = mapped_column()
