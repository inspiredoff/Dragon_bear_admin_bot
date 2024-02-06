from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.kb_MainMenu import *
from states import states
from states.states import *
from text.text_MainMenu import *

route = Router()


@route.message(Command('start'))
@route.message(F.text == back)
async def view_main_menu(message: Message, state: FSMContext):
    await state.set_state(MainMenu.menu)
    await message.answer(mm, reply_markup=MainMenuKeyboards.view_main_menu())


@route.message(F.text == send_post)
async def back_main_menu(message: Message, state: FSMContext):
    await state.set_state(ToMainMenu.button)
    await message.answer(post, reply_markup=MainMenuKeyboards.back_main_menu())

@route.message(F.text)
async def back_main_menu(message: Message, state: FSMContext):
    await state.set_state(ToMainMenu.button)
    await message.answer(post, reply_markup=MainMenuKeyboards.back_main_menu())
