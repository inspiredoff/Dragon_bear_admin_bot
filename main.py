import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from config import *
from states.states import *
from handlers import start_MainMenu, create_post
from handlers.quantity_of_goods import quantity_of_goods


async def main():
    logging.basicConfig(level=logging.INFO)
    dp = Dispatcher(storage=STORAGE)
    dp.include_router(start_MainMenu.route)
    dp.include_router(create_post.route)
    dp.include_router(quantity_of_goods.route)
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
