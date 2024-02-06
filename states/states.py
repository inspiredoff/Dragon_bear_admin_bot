from aiogram.fsm.state import StatesGroup, State


class ToMainMenu(StatesGroup):
    button = State()


class MainMenu(StatesGroup):
    menu = State()
