from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from texts.text_MainMenu import *
from texts.text_quantity_of_goods import *
from keyboards.kb_quantity_of_goods import *
from states.states import *
from db.requestORM.addGoods import insert_data_type_goods
from db.database import async_session_factory

route = Router()


@route.message(F.text == quantity_of_goods)
async def views_goods(message: Message, state: FSMContext):
    await insert_data_type_goods(async_session_factory, "пиво")
    await message.answer(goods_selection)
    await state.set_state(goods.selection_goods)
