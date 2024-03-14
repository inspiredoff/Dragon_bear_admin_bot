from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from texts.text_MainMenu import *
from texts.text_quantity_of_goods import *
from keyboards.kb_quantity_of_goods import *
from states.states import *

route = Router()
@route.message(F.text == quantity_of_goods)
async def views_goods(message:Message, state: FSMContext) -> Rep:
    await message.answer(goods_selection, reply_markup=GoodsKeyboard.view_keyboard())
    await state.set_state(goods.selection_goods)

