from aiogram.fsm.state import StatesGroup, State


class MainMenu(StatesGroup):
    menu = State()


class post(StatesGroup):
    button_back_menu = State()
    create_post = State()
    sending_post = State()
    sending_post_photo = State()

class goods(StatesGroup):
    selection_goods = State()
